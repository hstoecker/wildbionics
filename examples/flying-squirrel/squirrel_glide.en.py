# squirrel_glide.py – From “Flying Squirrel: The Glide That Ends Going Up”
# https://wildbionics.com/articles/flying-squirrel/ · Code: MIT licence
# Needs: python3 -m pip install numpy scipy matplotlib
# Run: python3 squirrel_glide.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# How much height does an 18 m glide cost a flying squirrel, and what does changing the pose buy?
# Values from Bahlman et al. 2013 (northern flying squirrel, 23 glides of 18 m).
MASS = 0.0927            # body mass (kg), from another population: these animals were not weighed
AREA = 0.0154            # wing area (m²), from the mass and a published wing loading of 59 N/m²
RHO = 1.204              # air density (kg/m³)
G = 9.81                 # gravity (m/s²)
LAUNCH = 5.37            # horizontal launch speed (m/s), the paper's best-matched simulation
TREE = 18.0              # horizontal distance to the landing tree (m)
DIVE_CL = 0.01           # lift coefficient in the first 3 m (the paper also gives 0.05)
END_CL = 5.6             # lift coefficient on arrival: 1.4 plus about 300 %, very uncertain

# Equivalent force coefficients along the glide, our reading of the text of the paper
X_NODES = [0.0, 3.0, 3.6, 12.0, 18.0]             # horizontal distance (m)
CL_NODES = [DIVE_CL, DIVE_CL, 1.4, 2.1, END_CL]   # 1.4 on entering the camera view, +50 % by 12 m
CD_NODES = [0.05, 0.05, 0.78, 0.975, 0.0]         # 0.78 on entering the view, +25 %, then towards 0


def changing_pose(x):
    return np.interp(x, X_NODES, CL_NODES), np.interp(x, X_NODES, CD_NODES)


def frozen_pose(x):
    return 1.75, 0.88    # midpoint of the values implied for the cruise phase, held from launch to landing


def no_wing(x):
    return 0.0, 0.0      # a thrown stone: no aerodynamic force at all


def forces(t, state, pose):
    """Newton's second law. Lift acts across the direction of travel, drag against it."""
    x, z, vx, vz = state
    speed = np.hypot(vx, vz)
    cl, cd = pose(x)
    k = 0.5 * RHO * speed**2 * AREA / MASS       # dynamic pressure × area / mass
    ax = k * (-cd * vx - cl * vz) / speed
    az = k * (-cd * vz + cl * vx) / speed - G
    return [vx, vz, ax, az]


def glide(pose):
    def reached_tree(t, state, pose):
        return state[0] - TREE
    reached_tree.terminal = True
    sol = solve_ivp(forces, (0, 20), [0, 0, LAUNCH, 0], args=(pose,), events=reached_tree, max_step=0.005)
    return sol.t, *sol.y


def report(name, pose):
    t, x, z, vx, vz = glide(pose)
    speed = np.hypot(vx, vz)
    drop = -z[-1]
    print(f"{name}: drop {drop:.1f} m, glide ratio {TREE / drop:.2f}, "
          f"mean speed {np.trapezoid(speed, t) / t[-1]:.1f} m/s, "
          f"peak {speed.max():.1f} m/s at {x[speed.argmax()]:.1f} m, arrival {speed[-1]:.1f} m/s, "
          f"final path angle {np.degrees(np.arctan2(vz[-1], vx[-1])):+.0f}°")
    return x, z, speed


print("Measured (18 m glides): drop 7.6 ± 0.5 m, glide ratio 2.4, mean speed 7.2 m/s, peak about 8.5 m/s at 5-6 m")
curves = [(report("changing pose", changing_pose), "changing pose", "-", "#1f6f8b"),
          (report("frozen pose", frozen_pose), "frozen pose", "--", "#c0392b")]
report("no wing at all", no_wing)

plt.rcParams["font.size"] = 13
fig, (top, bottom) = plt.subplots(2, 1, figsize=(6.4, 8.4), layout="constrained", sharex=True)
for (x, z, speed), label, style, colour in curves:
    top.plot(x, z, ls=style, lw=2.5, color=colour, label=label)
    bottom.plot(x, speed, ls=style, lw=2.5, color=colour, label=label)
top.errorbar(TREE, -7.6, yerr=0.5, fmt="s", ms=7, color="black", capsize=4, label="measured (mean ± s.d.)")
top.set_ylabel("height (m)")
top.set_ylim(-12, 1)
top.set_title("Changing pose: less height lost, faster")
top.legend(loc="lower left", fontsize=11)
bottom.plot(5.5, 8.5, "s", ms=7, color="black", label="measured peak (approx.)")
bottom.set_xlabel("horizontal distance (m)")
bottom.set_ylabel("speed (m/s)")
bottom.set_ylim(0, 10)
bottom.legend(loc="lower left", fontsize=11)
plt.show()
