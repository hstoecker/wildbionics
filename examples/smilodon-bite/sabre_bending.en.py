# sabre_bending.py – From “Sabre-Toothed Cat: Weak Bite, Fragile Sabres”
# https://wildbionics.com/articles/smilodon-bite/ · Code: MIT licence
# Needs: python3 -m pip install numpy matplotlib
# Run: python3 sabre_bending.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt

# How strong is a sabre? The upper canine of Smilodon fatalis as a cantilever beam with an
# elliptical cross-section, measured at the gum line of each stage of a simulated eruption (the adult tooth shifted step by step into the jaw).
# Data: Tseng (2025), Table S1, "morpho" models (article licensed CC BY-NC-ND 4.0; measurement values quoted with citation): (erupted height, front-to-back
# length x, side-to-side width y) in mm.
CANINES = {
    "AMNH FM55576": [(40.62, 21.58, 10.28), (50.23, 24.64, 11.18), (58.62, 26.75, 11.63),
                     (68.15, 28.78, 12.81), (78.31, 30.34, 13.93), (89.28, 31.08, 15.07),
                     (97.68, 31.58, 15.66), (106.83, 32.16, 16.44), (118.43, 32.55, 17.48),
                     (127.78, 31.99, 17.70), (137.76, 32.17, 18.00)],
    "KU S2255": [(20.20, 14.89, 7.73), (31.31, 19.81, 9.67), (42.91, 22.99, 10.58),
                 (54.85, 26.80, 11.96), (65.21, 29.56, 13.25), (75.16, 31.41, 13.94),
                 (85.12, 33.21, 14.94), (95.03, 34.63, 15.65)],
}
SPECIMEN_INDEX = 0          # 0: AMNH FM55576, the longest series in Table S1 (11 stages, 41–138 mm); 1: KU S2255
SPECIMEN = list(CANINES)[SPECIMEN_INDEX]
LOAD_N = 100.0              # force at the tip (N) – an assumed round value for comparison
ROUND = False               # True: same cross-sectional area, but a round tooth


def bending_stress(force, height, x, y):
    """Peak bending stress (MPa) at the base of an elliptical cantilever.
    Semi-axes a = x/2 (front-to-back) and b = y/2 (side-to-side), all in mm.
    Side load bends about the long axis: section modulus π·a·b²/4.
    Front load bends about the short axis: section modulus π·b·a²/4."""
    a, b = x / 2, y / 2
    moment = force * height                      # N·mm
    side = moment / (np.pi * a * b**2 / 4)       # N/mm² = MPa
    front = moment / (np.pi * b * a**2 / 4)
    return side, front


data = np.array(CANINES[SPECIMEN])
height, x, y = data.T
if ROUND:                                        # same area, circular: x = y = √(x·y)
    x = y = np.sqrt(x * y)
side, front = bending_stress(LOAD_N, height, x, y)

print(f"{SPECIMEN}, load {LOAD_N:.0f} N at the tip")
for h, s, f in ((height[0], side[0], front[0]), (height[-1], side[-1], front[-1])):
    print(f"  height {h:.0f} mm: {s:.1f} MPa from the side, {f:.1f} MPa from the front")
print(f"fully erupted, a side load stresses the tooth {side[-1] / front[-1]:.1f} times more than a front load")
print(f"from first to last stage, the side stress changes by a factor of {side[-1] / side[0]:.2f}, "
      f"while the height grows {height[-1] / height[0]:.1f} times")

plt.rcParams["font.size"] = 13      # large type: the chart stays readable on a phone
fig, ax = plt.subplots(figsize=(6.4, 5.6), layout="constrained")
ax.plot(height, side, "o-", lw=2.5, color="#c0392b", label="load from the side")
ax.plot(height, front, "s--", lw=2.5, color="#1f6f8b", label="load from the front")
ax.set_ylim(0, 1.15 * side.max())
ax.axvspan(20, 40, color="grey", alpha=0.15)
ax.text(30, 1.12 * side.max(), "typical\ncat canine", ha="center", va="top", fontsize=11)
ax.set_xlabel("erupted height of the canine (mm)")
ax.set_ylabel(f"bending stress at the base (MPa)\nfor {LOAD_N:.0f} N at the tip")
ax.set_xlim(15, 145)
ax.set_title("Sideways, the sabre is the weak spot")
ax.legend(loc="lower right", fontsize=11)
plt.show()
