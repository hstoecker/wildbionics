# young_sun.py – Aus „Wie Einzeller den Himmel veränderten: die Uratmosphäre“
# https://wildbionics.com/de/artikel/uratmosphaere/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy matplotlib
# Starten: python3 young_sun.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt

SOLAR_CONSTANT = 1361.0   # Sonnenlicht, das heute die Erde erreicht (W/m²)
ALBEDO = 0.30             # Anteil des zurückgeworfenen Sonnenlichts, als konstant angenommen
SIGMA = 5.670e-8          # Stefan-Boltzmann-Konstante (W/m²/K⁴)
SUN_AGE = 4.57            # Alter der Sonne (Milliarden Jahre)
T_TODAY = 288.0           # heutige mittlere Oberflächentemperatur der Erde (K)
FREEZING = 273.15         # Gefrierpunkt von Wasser (K)


def luminosity(ago):
    """Helligkeit der Sonne relativ zu heute, vor 'ago' Milliarden Jahren (Goughs Formel)."""
    t = SUN_AGE - ago
    return 1 / (1 + 0.4 * (1 - t / SUN_AGE))


def bare_temperature(ago):
    """Temperatur (K) einer Erde ohne Treibhauseffekt: aufgenommenes Sonnenlicht = abgestrahlte Wärme."""
    absorbed = SOLAR_CONSTANT * luminosity(ago) * (1 - ALBEDO) / 4
    return (absorbed / SIGMA) ** 0.25


def surface_temperature(ago, emissivity):
    """Ein-Schicht-Atmosphäre ('grau'): Sie nimmt den Anteil 'emissivity' der Wärmestrahlung des Bodens
    auf und schickt die Hälfte davon zurück, also T_Boden = T_ohne · (2 / (2 − ε))^(1/4)."""
    return bare_temperature(ago) * (2 / (2 - emissivity)) ** 0.25


# Atmosphäre so abstimmen, dass sie die heutigen 288 K ergibt, dann unverändert lassen.
emissivity_today = 2 - 2 * (bare_temperature(0) / T_TODAY) ** 4
print(f"heute: {bare_temperature(0):.0f} K ohne Treibhauseffekt, "
      f"{T_TODAY:.0f} K mit ihm (Emissivität {emissivity_today:.2f})")
print("vor Mrd. Jahren   Sonne   mit heutiger Atmosphäre")
for ago in [4.0, 3.0, 2.4, 2.0, 1.0, 0.0]:
    surface = surface_temperature(ago, emissivity_today)
    print(f"{ago:15.1f}   {luminosity(ago) * 100:5.0f} %   {surface - 273.15:6.1f} °C")

ages = np.linspace(4.0, 0, 401)
surface = surface_temperature(ages, emissivity_today)
if (surface < FREEZING).any():
    print(f"mit heutiger Atmosphäre wären die Ozeane bis vor "
          f"{ages[surface < FREEZING].min():.1f} Milliarden Jahren gefroren")
else:
    print("mit heutiger Atmosphäre wären die Ozeane nie gefroren")
needed = 2 - 2 * (bare_temperature(4.0) / FREEZING) ** 4
more_or_fewer = "mehr" if needed > emissivity_today else "weniger"
print(f"vor 4,0 Milliarden Jahren brauchte flüssiges Wasser eine Emissivität von {needed:.2f} statt "
      f"{emissivity_today:.2f} – {more_or_fewer} Treibhausgase als heute")

plt.rcParams["font.size"] = 13      # große Schrift: Das Diagramm bleibt auf dem Handy lesbar
fig, ax = plt.subplots(figsize=(6.4, 5.2), layout="constrained")
ax.axhspan(-60, 0, color="#dbe9f4")
ax.plot(ages, surface - 273.15, lw=2.5, label="heutige Atmosphäre")
ax.plot(ages, bare_temperature(ages) - 273.15, "--", lw=1.8, label="ohne Treibhauseffekt")
ax.axvspan(2.4, 2.3, color="0.85")
ax.text(2.33, 22, "Sauerstoff\nsteigt", color="dimgray", fontsize=11, ha="right")
ax.text(3.95, -16, "gefrorene Ozeane", color="steelblue", fontsize=11)
ax.set_xlim(4.0, 0)
ax.set_ylim(-60, 30)
ax.set_xlabel("vor Milliarden Jahren")
ax.set_ylabel("mittlere Oberflächentemperatur (°C)")
ax.set_title("Eine schwächere Sonne hätte die Erde vereist")
ax.legend(loc="lower right")
plt.show()
