# flapping_wing.py – From “How Insects Fly: Vortices, Halteres and RoboBees”
# https://wildbionics.com/articles/insect-flight/ · Code: MIT licence
# Needs: python3 -m pip install numpy matplotlib
# Run: python3 flapping_wing.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt

# Honeybee hovering – measured values, see the article
MASS = 102e-6              # body mass (kg)
WING_LENGTH = 9.7e-3       # wing length R, base to tip (m)
FREQUENCY = 230.0          # wingbeats per second (Hz)
AMPLITUDE = 90.0           # stroke amplitude Φ: the angle one wing sweeps (degrees)
AIR = 1.21                 # density of air (kg/m³)
HELIOX = 0.41              # density of heliox, an oxygen–helium mixture (kg/m³)
# Model assumptions
CHORD = 3.0e-3             # wing width (m): the wing as a rectangle of constant width
SCALE = 1.0                # shrink or grow the whole bee: lengths × SCALE, mass × SCALE³
G = 9.81                   # gravity (m/s²)
VISCOSITY = 1.8e-5         # dynamic viscosity of air (Pa·s)

mass, length, chord = MASS * SCALE**3, WING_LENGTH * SCALE, CHORD * SCALE
weight = mass * G
t = np.linspace(0, 2 / FREQUENCY, 800, endpoint=False)          # two wingbeats


def stroke(amplitude_deg):
    """Sinusoidal stroke φ(t) = Φ/2 · sin(2πft) and its angular speed ω(t) = dφ/dt."""
    phi_max = np.radians(amplitude_deg) / 2
    phase = 2 * np.pi * FREQUENCY * t
    return phi_max * np.sin(phase), phi_max * 2 * np.pi * FREQUENCY * np.cos(phase)


def lift(lift_coefficient, omega, density):
    """Quasi-steady lift of both wings. A strip at distance r moves at u = ω·r and adds
    ½·ρ·C_L·c·u²·dr; summed from base to tip this gives ½·ρ·C_L·ω²·c·R³/3 per wing."""
    return 2 * 0.5 * density * lift_coefficient * omega**2 * chord * length**3 / 3


def needed_cl(amplitude_deg, density):
    """The lift coefficient at which the mean lift over a wingbeat equals the weight."""
    _, omega = stroke(amplitude_deg)
    return weight / lift(1.0, omega, density).mean()


tip_speed = 2 * np.radians(AMPLITUDE) * length * FREQUENCY   # two strokes of Φ·R per wingbeat
reynolds = AIR * tip_speed * chord / VISCOSITY
cl = needed_cl(AMPLITUDE, AIR)
angle, omega = stroke(AMPLITUDE)
force = lift(cl, omega, AIR)
print(f"weight {weight * 1e3:.2f} mN, mean wing-tip speed {tip_speed:.1f} m/s, "
      f"Reynolds number about {round(reynolds, -1):.0f}")
print(f"lift coefficient needed to hover: C_L = {cl:.1f}")
print(f"lift peaks at {force.max() / weight:.1f} × body weight in mid-stroke, 0 at each turn")
print(f"in heliox with the same stroke: C_L = {needed_cl(AMPLITUDE, HELIOX):.1f}; "
      f"with a 50 % wider stroke: C_L = {needed_cl(1.5 * AMPLITUDE, HELIOX):.1f}")

plt.rcParams["font.size"] = 13      # large type: the chart stays readable on a phone
fig, (top, bottom) = plt.subplots(2, 1, figsize=(6.4, 8.4), layout="constrained", sharex=True)
ms = t * 1e3
for ax in (top, bottom):
    for turn in np.arange(0.25, 2, 0.5) / FREQUENCY * 1e3:    # the four turns
        ax.axvline(turn, color="#c98a1b", lw=6, alpha=0.18)
top.plot(ms, np.degrees(angle), lw=2.5, color="black")
top.axhline(0, color="grey", lw=0.8)
top.set_ylabel("stroke angle φ (°)")
top.set_title("The wing sweeps forward and back")
top.text(0.25 / FREQUENCY * 1e3 + 0.07, -40, "turn:\nwing flips", fontsize=11)
bottom.plot(ms, force * 1e3, lw=2.5, label="lift, quasi-steady model")
bottom.axhline(weight * 1e3, color="black", ls="--", lw=1.5, label="body weight")
bottom.set_xlabel("time (ms)")
bottom.set_ylabel("lift (mN)")
bottom.set_ylim(0, 2.6)
bottom.set_title("Lift: peaks mid-stroke, zero at turns")
bottom.legend(loc="upper right", fontsize=11)
plt.show()
