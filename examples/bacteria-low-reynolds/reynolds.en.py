# reynolds.py – From “Swimming in Honey: the Physics of Bacteria”
# https://wildbionics.com/articles/bacteria-low-reynolds/ · Code: MIT licence
# Needs: python3 -m pip install numpy matplotlib
# Run: python3 reynolds.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt

# Fluids: density (kg/m³) and viscosity (Pa·s)
WATER = (1000, 1.0e-3)       # water: viscosity 1 mPa·s
HONEY = (1400, 6.1)          # runny honey: 6.1 Pa·s (rosemary honey, 30 °C); density assumed
COLI_FLUID = WATER           # the liquid E. coli swims in
# Swimmers: (name, size L in m, speed v in m/s, fluid) – rough typical values, see the text
SWIMMERS = [
    ("human in water", 1.8, 1.0, WATER),
    ("goldfish", 0.05, 0.1, WATER),
    ("human in honey", 1.8, 1.0, HONEY),
    ("human in honey, 1 cm/min", 1.8, 0.01 / 60, HONEY),
    ("E. coli", 2e-6, 30e-6, COLI_FLUID),
]


def reynolds(size, speed, fluid):
    """Re = ρ·v·L/η: inertial forces divided by viscous forces."""
    density, viscosity = fluid
    return density * speed * size / viscosity


for name, size, speed, fluid in SWIMMERS:
    print(f"{name:26s} Re = {reynolds(size, speed, fluid):8.1g}")

# How far does E. coli coast when its motor stops? A sphere of radius a in a viscous fluid
# slows down exponentially with the time constant τ = m / (6πηa) (Stokes drag).
radius, speed, cell_density = 1e-6, 30e-6, 1000      # m, m/s, kg/m³ (cell ≈ water)
mass = cell_density * 4 / 3 * np.pi * radius**3
tau = mass / (6 * np.pi * WATER[1] * radius)
print(f"E. coli stops within {tau * 1e6:.1g} µs and coasts {speed * tau * 1e10:.1g} Å "
      f"(an atom is roughly 1 Å across)")

SUPERSCRIPT = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")


def power_of_ten(value, _pos=None):
    """Tick label 10⁻⁴ as plain text (no mathtext)."""
    return "10" + str(int(round(np.log10(value)))).translate(SUPERSCRIPT)


names = [s[0] for s in SWIMMERS]
values = [reynolds(*s[1:]) for s in SWIMMERS]
plt.rcParams["font.size"] = 13      # large type: the chart stays readable on a phone
fig, ax = plt.subplots(figsize=(6.4, 5.4), layout="constrained")
ax.axvspan(1e-6, 1, color="#c98a1b", alpha=0.12)
ax.axvline(1, color="black", lw=1.5, ls="--")
ax.text(1.6e-6, 4.6, "viscosity wins", fontsize=11)
ax.text(2, 4.6, "inertia wins", fontsize=11)
for row, (name, value) in enumerate(zip(names, values)):
    ax.plot(value, row, "o", ms=9, color="black")
    near_line = 1e-3 < value < 1        # keep this label left of the dashed line
    ax.annotate(name, (value, row), xytext=(8 if near_line else 0, 10), textcoords="offset points",
                ha="right" if near_line else "center", fontsize=11)
ax.set_xscale("log")
ax.set_xlim(1e-6, 1e8)
ax.set_ylim(4.9, -0.7)
ax.set_yticks([])
ax.xaxis.set_major_locator(plt.LogLocator(numticks=8))
ax.xaxis.set_major_formatter(power_of_ten)
ax.set_xlabel("Reynolds number Re = ρvL/η (log scale)")
ax.set_title("Bacteria live far below Re = 1")
plt.show()
