# squirrel_glide.py – Aus „Gleithörnchen: Der Gleitflug, der bergauf endet“
# https://wildbionics.com/de/artikel/gleithoernchen/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy scipy matplotlib
# Starten: python3 squirrel_glide.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Wie viel Höhe kostet ein Gleithörnchen ein 18-m-Gleitflug, und was bringt es, die Haltung zu ändern?
# Werte aus Bahlman et al. 2013 (Nördliches Gleithörnchen, 23 Gleitflüge über 18 m).
MASS = 0.0927            # Körpermasse (kg), aus einer anderen Population: diese Tiere wurden nicht gewogen
AREA = 0.0154            # Flügelfläche (m²), aus der Masse und einer veröffentlichten Flächenbelastung von 59 N/m²
RHO = 1.204              # Luftdichte (kg/m³)
G = 9.81                 # Schwerebeschleunigung (m/s²)
LAUNCH = 5.37            # horizontale Startgeschwindigkeit (m/s), beste Simulation des Papers
TREE = 18.0              # horizontale Entfernung zum Landebaum (m)
DIVE_CL = 0.01           # Auftriebsbeiwert auf den ersten 3 m (das Paper nennt auch 0.05)
END_CL = 5.6             # Auftriebsbeiwert bei der Ankunft: 1.4 plus etwa 300 %, sehr unsicher

# Äquivalente Kraftbeiwerte entlang des Gleitflugs, unsere Lesart des Paper-Texts
X_NODES = [0.0, 3.0, 3.6, 12.0, 18.0]             # horizontale Strecke (m)
CL_NODES = [DIVE_CL, DIVE_CL, 1.4, 2.1, END_CL]   # 1.4 beim Eintritt ins Kamerabild, +50 % bis 12 m
CD_NODES = [0.05, 0.05, 0.78, 0.975, 0.0]         # 0.78 beim Eintritt, +25 %, dann gegen 0


def changing_pose(x):
    return np.interp(x, X_NODES, CL_NODES), np.interp(x, X_NODES, CD_NODES)


def frozen_pose(x):
    return 1.75, 0.88    # Mitte der für die Gleitphase abgeleiteten Werte, vom Absprung bis zur Landung gehalten


def no_wing(x):
    return 0.0, 0.0      # ein geworfener Stein: gar keine Luftkraft


def forces(t, state, pose):
    """Zweites Newtonsches Gesetz. Auftrieb wirkt quer zur Bewegungsrichtung, Widerstand entgegen."""
    x, z, vx, vz = state
    speed = np.hypot(vx, vz)
    cl, cd = pose(x)
    k = 0.5 * RHO * speed**2 * AREA / MASS       # Staudruck × Fläche / Masse
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
    print(f"{name}: Höhenverlust {drop:.1f} m, Gleitverhältnis {TREE / drop:.2f}, "
          f"mittleres Tempo {np.trapezoid(speed, t) / t[-1]:.1f} m/s, "
          f"Spitze {speed.max():.1f} m/s bei {x[speed.argmax()]:.1f} m, Ankunft {speed[-1]:.1f} m/s, "
          f"Bahnwinkel am Ende {np.degrees(np.arctan2(vz[-1], vx[-1])):+.0f}°")
    return x, z, speed


print("Gemessen (18-m-Flüge): Höhenverlust 7.6 ± 0.5 m, Gleitverhältnis 2.4, mittleres Tempo 7.2 m/s, Spitze etwa 8.5 m/s bei 5-6 m")
curves = [(report("wechselnde Haltung", changing_pose), "wechselnde Haltung", "-", "#1f6f8b"),
          (report("starre Haltung", frozen_pose), "starre Haltung", "--", "#c0392b")]
report("ganz ohne Flügel", no_wing)

plt.rcParams["font.size"] = 13
fig, (top, bottom) = plt.subplots(2, 1, figsize=(6.4, 8.4), layout="constrained", sharex=True)
for (x, z, speed), label, style, colour in curves:
    top.plot(x, z, ls=style, lw=2.5, color=colour, label=label)
    bottom.plot(x, speed, ls=style, lw=2.5, color=colour, label=label)
top.errorbar(TREE, -7.6, yerr=0.5, fmt="s", ms=7, color="black", capsize=4, label="gemessen (Mittel ± SD)")
top.set_ylabel("Höhe (m)")
top.set_ylim(-12, 1)
top.set_title("Wechselnde Haltung: weniger Verlust, schneller")
top.legend(loc="lower left", fontsize=11)
bottom.plot(5.5, 8.5, "s", ms=7, color="black", label="gemessene Spitze (ca.)")
bottom.set_xlabel("horizontale Strecke (m)")
bottom.set_ylabel("Tempo (m/s)")
bottom.set_ylim(0, 10)
bottom.legend(loc="lower left", fontsize=11)
plt.show()
