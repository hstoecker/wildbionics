# peel_angle.py – From “How Geckos Stick to Walls: van der Waals Forces”
# https://wildbionics.com/articles/gecko-adhesion/ · Code: MIT licence
# Needs: python3 -m pip install numpy scipy matplotlib
# Run: python3 peel_angle.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# Work of adhesion from the physics lens: integrating P = A/(6πD³) from contact to infinity
A_HAMAKER = 1e-19     # Hamaker constant (J), typical for solids
D_CONTACT = 0.3e-9    # distance of surfaces in contact (m), about one atom
W = A_HAMAKER / (12 * np.pi * D_CONTACT**2)   # energy to separate 1 m² of contact (J/m²)

# The spatula as a thin elastic tape
WIDTH = 200e-9        # spatula width (m), about 200 nm
THICKNESS = 10e-9     # thickness of the spatula pad (m), assumed
MODULUS = 1.6e9       # Young's modulus of setal keratin (Pa), measured in tokay geckos


def peel_force(angle_deg):
    """Force (N) that peels the tape off at a given angle to the wall.

    Kendall's equation (F/b)²/(2Eh) + (F/b)(1 − cos θ) = W, solved for F.
    Written so that no two nearly equal numbers are subtracted – that would
    throw away digits (1 − cos θ for small θ, −a + √(a² + ε) for large θ).
    """
    one_minus_cos = 2 * np.sin(np.radians(angle_deg) / 2) ** 2
    stretch = 2 * W / (MODULUS * THICKNESS)    # how much the tape can stretch
    return WIDTH * 2 * W / (one_minus_cos + np.sqrt(one_minus_cos**2 + stretch))


def rigid_tape_force(angle_deg):
    """The same without stretching (E → ∞): F = bW / (1 − cos θ)."""
    return WIDTH * W / (2 * np.sin(np.radians(angle_deg) / 2) ** 2)


print(f"work of adhesion W = {W * 1e3:.0f} mJ/m²")
print("angle   peel force   rigid tape")
for angle in [0, 10, 30, 60, 90]:
    rigid = f"{rigid_tape_force(angle) * 1e9:7.1f} nN" if angle else "   infinite"
    print(f"{angle:4d}°   {peel_force(angle) * 1e9:6.1f} nN   {rigid}")

# The switch: how far must the foot tilt to lose 90 % of the grip?
f_max = peel_force(0)
release = brentq(lambda a: peel_force(a) - 0.1 * f_max, 0, 90)
print(f"switch ratio F(10°) / F(90°) = {peel_force(10) / peel_force(90):.0f}")
print(f"grip falls to 10 % of its maximum at {release:.0f}°")
print("measured for one spatula: about 10 nN (Huber et al. 2005)")

angles = np.linspace(0, 90, 361)
plt.rcParams["font.size"] = 13      # large type: the chart stays readable on a phone
fig, ax = plt.subplots(figsize=(6.4, 5.2), layout="constrained")
ax.semilogy(angles, peel_force(angles) * 1e9, lw=2.5, label="elastic tape (Kendall)")
ax.semilogy(angles[8:], rigid_tape_force(angles[8:]) * 1e9, "--", lw=1.8, label="rigid tape (no stretching)")
ax.plot([90], [10], "ko", ms=7, label="measured: about 10 nN")
ax.axvline(release, color="gray", lw=1, ls=":")
ax.text(release + 1.5, 300, f"10 % grip\nleft at {release:.0f}°", color="dimgray")
ax.set_xlabel("peel angle θ (degrees)")
ax.set_ylabel("force to peel one spatula (nN)")
ax.set_title("Flat angle holds, steep angle lets go")
ax.set_xlim(0, 93)
ax.set_ylim(2, 1000)
ax.legend(loc="lower left")
plt.show()
