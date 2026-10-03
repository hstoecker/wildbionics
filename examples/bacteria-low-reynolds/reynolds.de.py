# reynolds.py – Aus „Schwimmen in Honig: die Physik der Bakterien“
# https://wildbionics.com/de/artikel/schwimmen-in-honig/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy matplotlib
# Starten: python3 reynolds.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt

# Flüssigkeiten: Dichte (kg/m³) und Viskosität (Pa·s)
WATER = (1000, 1.0e-3)       # Wasser: Viskosität 1 mPa·s
HONEY = (1400, 6.1)          # dünnflüssiger Honig: 6,1 Pa·s (Rosmarinhonig, 30 °C); Dichte angenommen
COLI_FLUID = WATER           # die Flüssigkeit, in der E. coli schwimmt
# Schwimmer: (Name, Größe L in m, Geschwindigkeit v in m/s, Flüssigkeit) – grobe typische Werte, siehe Text
SWIMMERS = [
    ("Mensch in Wasser", 1.8, 1.0, WATER),
    ("Goldfisch", 0.05, 0.1, WATER),
    ("Mensch in Honig", 1.8, 1.0, HONEY),
    ("Mensch in Honig, 1 cm/min", 1.8, 0.01 / 60, HONEY),
    ("E. coli", 2e-6, 30e-6, COLI_FLUID),
]


def reynolds(size, speed, fluid):
    """Re = ρ·v·L/η: Trägheitskräfte geteilt durch Reibungskräfte."""
    density, viscosity = fluid
    return density * speed * size / viscosity


for name, size, speed, fluid in SWIMMERS:
    print(f"{name:27s} Re = {reynolds(size, speed, fluid):8.1g}")

# Wie weit gleitet E. coli, wenn sein Motor stoppt? Eine Kugel mit Radius a wird in einer zähen
# Flüssigkeit exponentiell langsamer, mit der Zeitkonstante τ = m / (6πηa) (Stokes-Reibung).
radius, speed, cell_density = 1e-6, 30e-6, 1000      # m, m/s, kg/m³ (Zelle ≈ Wasser)
mass = cell_density * 4 / 3 * np.pi * radius**3
tau = mass / (6 * np.pi * WATER[1] * radius)
print(f"E. coli steht nach {tau * 1e6:.1g} µs still und gleitet {speed * tau * 1e10:.1g} Å weit "
      f"(ein Atom ist grob 1 Å groß)")

SUPERSCRIPT = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")


def power_of_ten(value, _pos=None):
    """Achsenbeschriftung 10⁻⁴ als einfacher Text (ohne Mathtext)."""
    return "10" + str(int(round(np.log10(value)))).translate(SUPERSCRIPT)


names = [s[0] for s in SWIMMERS]
values = [reynolds(*s[1:]) for s in SWIMMERS]
plt.rcParams["font.size"] = 13      # große Schrift: das Diagramm bleibt auf dem Handy lesbar
fig, ax = plt.subplots(figsize=(6.4, 5.4), layout="constrained")
ax.axvspan(1e-6, 1, color="#c98a1b", alpha=0.12)
ax.axvline(1, color="black", lw=1.5, ls="--")
ax.text(1.6e-6, 4.6, "Zähigkeit gewinnt", fontsize=11)
ax.text(2, 4.6, "Trägheit gewinnt", fontsize=11)
for row, (name, value) in enumerate(zip(names, values)):
    ax.plot(value, row, "o", ms=9, color="black")
    near_line = 1e-3 < value < 1        # diese Beschriftung bleibt links der gestrichelten Linie
    ax.annotate(name, (value, row), xytext=(8 if near_line else 0, 10), textcoords="offset points",
                ha="right" if near_line else "center", fontsize=11)
ax.set_xscale("log")
ax.set_xlim(1e-6, 1e8)
ax.set_ylim(4.9, -0.7)
ax.set_yticks([])
ax.xaxis.set_major_locator(plt.LogLocator(numticks=8))
ax.xaxis.set_major_formatter(power_of_ten)
ax.set_xlabel("Reynolds-Zahl Re = ρvL/η (log. Skala)")
ax.set_title("Bakterien leben weit unter Re = 1")
plt.show()
