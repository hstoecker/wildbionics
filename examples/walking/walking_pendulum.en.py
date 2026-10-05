# walking_pendulum.py – From “How We Walk: Pendulums, Springs and Humanoid Robots”
# https://wildbionics.com/articles/walking/ · Code: MIT licence
# Needs: python3 -m pip install numpy matplotlib
# Run: python3 walking_pendulum.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt

# A walking person as an inverted pendulum: the body (a point mass at the hip) vaults over a stiff leg.
G = 9.81                 # acceleration of gravity (m/s²)
LEG = 0.90               # leg length L, hip joint to ground (m) – assumed for an adult
STEP = 0.70              # step length (m) – assumed
WALK = 1.1               # walking speed at midstance (m/s), close to the most economical speed
FR_SWITCH = 0.5          # Froude number at which people switch from walking to running (measured)
SWITCH_SPEEDS = {"preferred switch": 2.06, "energetically best switch": 2.24}   # measured (m/s)


def froude(speed, leg=LEG, g=G):
    """Froude number Fr = v²/(g·L): centripetal over gravitational acceleration."""
    return speed**2 / (g * leg)


def max_walking_speed(leg=LEG, g=G):
    """At the top of its arc the body moves on a circle of radius L. Only gravity can pull it
    round the curve, so v²/L ≤ g, i.e. Fr ≤ 1 and v ≤ √(g·L) – faster, and the body takes off."""
    return np.sqrt(g * leg)


# One step: the leg swings from −θ0 to +θ0 about the vertical, with no losses (energy is conserved)
theta0 = np.arcsin(STEP / 2 / LEG)
theta = np.linspace(-theta0, theta0, 201)
x = LEG * np.sin(theta)                                   # position of the hip over the foot (m)
height = LEG * np.cos(theta)                              # height of the hip (m)
speed = np.sqrt(WALK**2 + 2 * G * (LEG - height))         # slowest at the top, fastest at the ends
potential = G * (height - height.min())                   # energy per kg body mass (J/kg)
kinetic = 0.5 * (speed**2 - speed.min()**2)
total = potential + kinetic

v_max = max_walking_speed()
print(f"one pendulum step: the hip rises {100 * (height.max() - height.min()):.1f} cm, "
      f"speed {speed.min():.2f} m/s at the top, {speed.max():.2f} m/s at the ends")
print(f"kinetic and potential energy trade places; their sum changes by {np.ptp(total):.1f} J/kg")
print(f"fastest possible walk (Fr = 1): v = √(g·L) = {v_max:.2f} m/s = {3.6 * v_max:.1f} km/h")
print(f"predicted switch to running at Fr = {FR_SWITCH}: {np.sqrt(FR_SWITCH * G * LEG):.2f} m/s")
for name, v in SWITCH_SPEEDS.items():
    print(f"measured {name}: {v:.2f} m/s → Fr = {froude(v):.2f}, "
          f"leg force at the top = {1 - froude(v):.2f} × body weight")

plt.rcParams["font.size"] = 13      # large type: the chart stays readable on a phone
fig, (top, bottom) = plt.subplots(2, 1, figsize=(6.4, 8.4), layout="constrained")
cm = 100 * x
top.plot(cm, potential, lw=2.5, color="#1f6f8b")
top.plot(cm, kinetic, lw=2.5, ls="--", color="#c0392b")
top.plot(cm, total, lw=1.5, ls=":", color="black")
top.text(0, potential.max() - 0.12, "potential", ha="center", va="top", color="#1f6f8b")
top.annotate("kinetic", xy=(cm[20], kinetic[20]), xytext=(cm[0], 0.98), color="#c0392b",
             arrowprops=dict(arrowstyle="-", color="#c0392b"))
top.text(0, total[0] + 0.05, "sum: constant", ha="center", va="bottom")
top.set_xlabel("hip position over the foot (cm)")
top.set_ylabel("energy (J per kg)")
top.set_ylim(0, total[0] + 0.45)
top.set_title(f"A pendulum step at {WALK} m/s: energies swap")

v = np.linspace(0, 3.4, 400)
force = 1 - froude(v)                                     # leg force at the top, in body weights
valid = v <= v_max
bottom.plot(v[valid], force[valid], lw=2.5, color="black", label="pendulum model")
bottom.plot(v[~valid], force[~valid], lw=2, ls=":", color="grey", label="model invalid: body lifts off")
bottom.axhline(0, color="grey", lw=0.8)
bottom.axvline(v_max, color="grey", lw=0.8)
bottom.text(v_max + 0.05, 0.85, "Fr = 1", va="top")
for (name, s), marker in zip(SWITCH_SPEEDS.items(), ("o", "s")):
    bottom.plot(s, 1 - froude(s), marker, ms=9, color="#c98a1b", label=f"measured {name}")
bottom.set_xlabel("walking speed (m/s)")
bottom.set_ylabel("leg force at the top (× weight)")
bottom.set_ylim(-0.45, 1.1)
bottom.set_title("People run long before the leg unloads")
bottom.legend(loc="lower left", fontsize=11)
plt.show()
