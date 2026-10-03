# young_sun.py – From “Early Atmosphere: How Single Cells Changed the Sky”
# https://wildbionics.com/articles/early-atmosphere/ · Code: MIT licence
# Needs: python3 -m pip install numpy matplotlib
# Run: python3 young_sun.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt

SOLAR_CONSTANT = 1361.0   # sunlight reaching Earth today (W/m²)
ALBEDO = 0.30             # fraction of sunlight reflected, assumed constant
SIGMA = 5.670e-8          # Stefan–Boltzmann constant (W/m²/K⁴)
SUN_AGE = 4.57            # age of the Sun (billion years)
T_TODAY = 288.0           # mean surface temperature of Earth today (K)
FREEZING = 273.15         # freezing point of water (K)


def luminosity(ago):
    """Brightness of the Sun relative to today, 'ago' billion years ago (Gough's formula)."""
    t = SUN_AGE - ago
    return 1 / (1 + 0.4 * (1 - t / SUN_AGE))


def bare_temperature(ago):
    """Temperature (K) of an Earth without greenhouse effect: absorbed sunlight = emitted heat."""
    absorbed = SOLAR_CONSTANT * luminosity(ago) * (1 - ALBEDO) / 4
    return (absorbed / SIGMA) ** 0.25


def surface_temperature(ago, emissivity):
    """One-layer 'grey' atmosphere: it absorbs the fraction 'emissivity' of the heat radiation
    from the ground and sends half of it back down, so T_surface = T_bare · (2 / (2 − ε))^(1/4)."""
    return bare_temperature(ago) * (2 / (2 - emissivity)) ** 0.25


# Calibrate the atmosphere so that it gives today's 288 K, then keep it unchanged.
emissivity_today = 2 - 2 * (bare_temperature(0) / T_TODAY) ** 4
print(f"today: {bare_temperature(0):.0f} K without greenhouse effect, "
      f"{T_TODAY:.0f} K with it (emissivity {emissivity_today:.2f})")
print("billion years ago   Sun   with today's atmosphere")
for ago in [4.0, 3.0, 2.4, 2.0, 1.0, 0.0]:
    surface = surface_temperature(ago, emissivity_today)
    print(f"{ago:17.1f}   {luminosity(ago) * 100:3.0f} %   {surface - 273.15:6.1f} °C")

ages = np.linspace(4.0, 0, 401)
surface = surface_temperature(ages, emissivity_today)
if (surface < FREEZING).any():
    print(f"with today's atmosphere the oceans would freeze before "
          f"{ages[surface < FREEZING].min():.1f} billion years ago")
else:
    print("with today's atmosphere the oceans would never freeze")
needed = 2 - 2 * (bare_temperature(4.0) / FREEZING) ** 4
more_or_fewer = "more" if needed > emissivity_today else "fewer"
print(f"4.0 billion years ago, liquid water needed an emissivity of {needed:.2f} instead of "
      f"{emissivity_today:.2f} – {more_or_fewer} greenhouse gases than today")

plt.rcParams["font.size"] = 13      # large type: the chart stays readable on a phone
fig, ax = plt.subplots(figsize=(6.4, 5.2), layout="constrained")
ax.axhspan(-60, 0, color="#dbe9f4")
ax.plot(ages, surface - 273.15, lw=2.5, label="today's atmosphere")
ax.plot(ages, bare_temperature(ages) - 273.15, "--", lw=1.8, label="no greenhouse effect")
ax.axvspan(2.4, 2.3, color="0.85")
ax.text(2.33, 22, "oxygen\nrises", color="dimgray", fontsize=11, ha="right")
ax.text(3.95, -16, "frozen oceans", color="steelblue", fontsize=11)
ax.set_xlim(4.0, 0)
ax.set_ylim(-60, 30)
ax.set_xlabel("billion years ago")
ax.set_ylabel("mean surface temperature (°C)")
ax.set_title("A fainter Sun would have frozen the early Earth")
ax.legend(loc="lower right")
plt.show()
