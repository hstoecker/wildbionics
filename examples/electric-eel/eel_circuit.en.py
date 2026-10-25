# eel_circuit.py – From “How the Electric Eel Shocks: 860 Volts from Living Batteries”
# https://wildbionics.com/articles/electric-eel/ · Code: MIT licence
# Needs: python3 -m pip install numpy matplotlib
# Run: python3 eel_circuit.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt

# How much power does a leaping electric eel push through a threat? An equivalent circuit.
CELL_EMF = 0.150         # voltage of one firing electrocyte (V), Schroeder et al. 2017
# Measured on the smallest of five eels by Catania (summarised in Catania 2019, Fig. 12):
EMF, R_INTERNAL = 198.0, 960.0   # electromotive force (V) and internal resistance (Ω)
R_WATER = 400.0          # resistance of the water path back to the tail (Ω)
RETURN_PATH = 2400.0     # head-to-water path along the eel at the top of the leap (Ω)
R_ARM = 2100.0           # a human arm, the target (Ω)
ROWS = 1                 # how many copies of the eel's organ work in parallel (1 = the real eel)


def thevenin(emf, r_source, r_return):
    """Seen from the target, the eel, the water and the return path act like one battery:
    the return path divides the voltage and sits in parallel with the target."""
    r_loop = r_source + R_WATER
    v_th = emf * r_return / (r_loop + r_return)
    r_th = r_loop * r_return / (r_loop + r_return)
    return v_th, r_th


def target_power(r_target, v_th, r_th):
    """Current and power in a target of resistance R: I = V/(R_th + R), P = I²·R."""
    current = v_th / (r_th + r_target)
    return current, current**2 * r_target


r_eel = R_INTERNAL / ROWS                 # rows in parallel divide the internal resistance
for volts in (EMF, 600.0, 860.0):
    print(f"{volts:.0f} V needs about {volts / CELL_EMF:,.0f} electrocytes in series")

v_th, r_th = thevenin(EMF, r_eel, RETURN_PATH)
print(f"seen from the target: {v_th:.0f} V behind {r_th:.0f} Ω")
i_arm, p_arm = target_power(R_ARM, v_th, r_th)
i_eel = EMF / (r_eel + R_WATER + RETURN_PATH * R_ARM / (RETURN_PATH + R_ARM))
print(f"current leaving the eel: {1e3 * i_eel:.0f} mA")
print(f"arm ({R_ARM:.0f} Ω): {1e3 * i_arm:.0f} mA, {p_arm:.1f} W")
print(f"best target: {r_th:.0f} Ω gets {target_power(r_th, v_th, r_th)[1]:.1f} W (maximum power transfer)")
for r_return, name in ((600.0, "low leap"), (RETURN_PATH, "top of the leap"), (1e9, "no return path")):
    i, p = target_power(R_ARM, *thevenin(EMF, r_eel, r_return))
    print(f"{name}: arm current {1e3 * i:.0f} mA, {p:.1f} W")

plt.rcParams["font.size"] = 13      # large type: the chart stays readable on a phone
fig, ax = plt.subplots(figsize=(6.4, 6.0), layout="constrained")
r_target = np.logspace(2, 5, 400)
for r_return, label, style in ((600.0, "low leap (600 Ω, assumed)", ":"),
                               (RETURN_PATH, "top of the leap (2400 Ω)", "-"),
                               (1e9, "limit: no return path", "--")):
    v, r = thevenin(EMF, r_eel, r_return)
    ax.plot(r_target, target_power(r_target, v, r)[1], ls=style, lw=2.5, color="#1f6f8b", label=label)
    ax.plot(r, target_power(r, v, r)[1], "o", ms=8, mfc="white", color="#1f6f8b")
ax.axvline(R_ARM, ymax=0.8, color="#c0392b", lw=1.5, ls="-.")
ax.text(R_ARM * 1.15, 5.0, "human arm", color="#c0392b", fontsize=12)
ax.text(115, 9.7, "circles: maximum, target =\ninternal resistance", fontsize=11, color="dimgrey", va="top")
ax.set_xscale("log")
ax.xaxis.set_major_formatter("{x:g}")
ax.set_xlabel("resistance of the target (Ω)")
ax.set_ylabel("power in the target (W)")
ax.set_ylim(0, 10)
ax.set_title("The higher the leap, the more power")
ax.legend(loc="upper right", fontsize=11)
plt.show()
