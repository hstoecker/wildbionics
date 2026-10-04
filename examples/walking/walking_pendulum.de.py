# walking_pendulum.py – Aus „Wie wir gehen: Pendel, Federn und humanoide Roboter“
# https://wildbionics.com/de/artikel/gehen/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy matplotlib
# Starten: python3 walking_pendulum.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt

# Ein gehender Mensch als inverses Pendel: Der Körper (eine Punktmasse an der Hüfte) schwingt über ein steifes Bein.
G = 9.81                 # Schwerebeschleunigung (m/s²)
LEG = 0.90               # Beinlänge L, Hüftgelenk bis Boden (m) – angenommen für Erwachsene
STEP = 0.70              # Schrittlänge (m) – angenommen
WALK = 1.1               # Gehgeschwindigkeit in der Mitte der Standphase (m/s), nahe der sparsamsten
FR_SWITCH = 0.5          # Froude-Zahl, bei der Menschen vom Gehen ins Laufen wechseln (gemessen)
SWITCH_SPEEDS = {"bevorzugter Wechsel": 2.06, "energetisch günstigster Wechsel": 2.24}   # gemessen (m/s)


def froude(speed, leg=LEG, g=G):
    """Froude-Zahl Fr = v²/(g·L): Zentripetal- im Verhältnis zur Schwerebeschleunigung."""
    return speed**2 / (g * leg)


def max_walking_speed(leg=LEG, g=G):
    """Am höchsten Punkt bewegt sich der Körper auf einem Kreis mit Radius L. Nur die Schwerkraft
    kann ihn auf der Kurve halten, also v²/L ≤ g, d. h. Fr ≤ 1 und v ≤ √(g·L) – schneller, und er hebt ab."""
    return np.sqrt(g * leg)


# Ein Schritt: Das Bein schwingt von −θ0 bis +θ0 um die Senkrechte, ohne Verluste (Energieerhaltung)
theta0 = np.arcsin(STEP / 2 / LEG)
theta = np.linspace(-theta0, theta0, 201)
x = LEG * np.sin(theta)                                   # Position der Hüfte über dem Fuß (m)
height = LEG * np.cos(theta)                              # Höhe der Hüfte (m)
speed = np.sqrt(WALK**2 + 2 * G * (LEG - height))         # oben am langsamsten, an den Enden am schnellsten
potential = G * (height - height.min())                   # Energie pro kg Körpermasse (J/kg)
kinetic = 0.5 * (speed**2 - speed.min()**2)
total = potential + kinetic

v_max = max_walking_speed()
print(f"ein Pendelschritt: Die Hüfte steigt um {100 * (height.max() - height.min()):.1f} cm, "
      f"Geschwindigkeit oben {speed.min():.2f} m/s, an den Enden {speed.max():.2f} m/s")
print(f"kinetische und potenzielle Energie tauschen die Rollen; ihre Summe ändert sich um {np.ptp(total):.1f} J/kg")
print(f"schnellstmögliches Gehen (Fr = 1): v = √(g·L) = {v_max:.2f} m/s = {3.6 * v_max:.1f} km/h")
print(f"vorhergesagter Wechsel ins Laufen bei Fr = {FR_SWITCH}: {np.sqrt(FR_SWITCH * G * LEG):.2f} m/s")
for name, v in SWITCH_SPEEDS.items():
    print(f"gemessen, {name}: {v:.2f} m/s → Fr = {froude(v):.2f}, "
          f"Beinkraft oben = {1 - froude(v):.2f} × Körpergewicht")

plt.rcParams["font.size"] = 13      # große Schrift: Das Diagramm bleibt auf dem Handy lesbar
fig, (top, bottom) = plt.subplots(2, 1, figsize=(6.4, 8.4), layout="constrained")
cm = 100 * x
top.plot(cm, potential, lw=2.5, color="#1f6f8b")
top.plot(cm, kinetic, lw=2.5, ls="--", color="#c0392b")
top.plot(cm, total, lw=1.5, ls=":", color="black")
top.text(0, potential.max() - 0.12, "potenziell", ha="center", va="top", color="#1f6f8b")
top.annotate("kinetisch", xy=(cm[20], kinetic[20]), xytext=(cm[0], 0.98), color="#c0392b",
             arrowprops=dict(arrowstyle="-", color="#c0392b"))
top.text(0, total[0] + 0.05, "Summe: konstant", ha="center", va="bottom")
top.set_xlabel("Position der Hüfte über dem Fuß (cm)")
top.set_ylabel("Energie (J pro kg)")
top.set_ylim(0, total[0] + 0.45)
top.set_title(f"Ein Pendelschritt bei {WALK} m/s: Energien tauschen")

v = np.linspace(0, 3.4, 400)
force = 1 - froude(v)                                     # Beinkraft oben, in Körpergewichten
valid = v <= v_max
bottom.plot(v[valid], force[valid], lw=2.5, color="black", label="Pendelmodell")
bottom.plot(v[~valid], force[~valid], lw=2, ls=":", color="grey", label="Modell ungültig: Körper hebt ab")
bottom.axhline(0, color="grey", lw=0.8)
bottom.axvline(v_max, color="grey", lw=0.8)
bottom.text(v_max + 0.05, 0.85, "Fr = 1", va="top")
for (name, s), marker in zip(SWITCH_SPEEDS.items(), ("o", "s")):
    bottom.plot(s, 1 - froude(s), marker, ms=9, color="#c98a1b", label=f"gemessen: {name}")
bottom.set_xlabel("Gehgeschwindigkeit (m/s)")
bottom.set_ylabel("Beinkraft oben (× Gewicht)")
bottom.set_ylim(-0.45, 1.1)
bottom.set_title("Wir laufen lange, bevor das Bein entlastet")
bottom.legend(loc="lower left", fontsize=11)
plt.show()
