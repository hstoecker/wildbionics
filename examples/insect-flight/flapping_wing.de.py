# flapping_wing.py – Aus „Wie Insekten fliegen: Wirbel, Halteren und RoboBees“
# https://wildbionics.com/de/artikel/insektenflug/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy matplotlib
# Starten: python3 flapping_wing.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt

# Schwebende Honigbiene – Messwerte, siehe Artikel
MASS = 102e-6              # Körpermasse (kg)
WING_LENGTH = 9.7e-3       # Flügellänge R, von der Basis zur Spitze (m)
FREQUENCY = 230.0          # Flügelschläge pro Sekunde (Hz)
AMPLITUDE = 90.0           # Schlagamplitude Φ: der Winkel, den ein Flügel überstreicht (Grad)
AIR = 1.21                 # Dichte der Luft (kg/m³)
HELIOX = 0.41              # Dichte von Heliox, einem Sauerstoff-Helium-Gemisch (kg/m³)
# Modellannahmen
CHORD = 3.0e-3             # Flügelbreite (m): der Flügel als Rechteck konstanter Breite
SCALE = 1.0                # die ganze Biene verkleinern oder vergrößern: Längen × SCALE, Masse × SCALE³
G = 9.81                   # Schwerebeschleunigung (m/s²)
VISCOSITY = 1.8e-5         # dynamische Viskosität der Luft (Pa·s)

mass, length, chord = MASS * SCALE**3, WING_LENGTH * SCALE, CHORD * SCALE
weight = mass * G
t = np.linspace(0, 2 / FREQUENCY, 801)           # zwei Flügelschläge


def stroke(amplitude_deg):
    """Sinusförmiger Schlag φ(t) = Φ/2 · sin(2πft) und seine Winkelgeschwindigkeit ω(t) = dφ/dt."""
    phi_max = np.radians(amplitude_deg) / 2
    phase = 2 * np.pi * FREQUENCY * t
    return phi_max * np.sin(phase), phi_max * 2 * np.pi * FREQUENCY * np.cos(phase)


def lift(lift_coefficient, omega, density):
    """Quasistationärer Auftrieb beider Flügel. Ein Streifen im Abstand r bewegt sich mit u = ω·r
    und liefert ½·ρ·C_L·c·u²·dr; von der Basis bis zur Spitze summiert ergibt das ½·ρ·C_L·ω²·c·R³/3 pro Flügel."""
    return 2 * 0.5 * density * lift_coefficient * omega**2 * chord * length**3 / 3


def needed_cl(amplitude_deg, density):
    """Der Auftriebsbeiwert, bei dem der mittlere Auftrieb über einen Flügelschlag das Gewicht trägt."""
    _, omega = stroke(amplitude_deg)
    return weight / lift(1.0, omega, density).mean()


tip_speed = 2 * np.radians(AMPLITUDE) * length * FREQUENCY   # zwei Schläge von Φ·R pro Flügelschlag
reynolds = AIR * tip_speed * chord / VISCOSITY
cl = needed_cl(AMPLITUDE, AIR)
angle, omega = stroke(AMPLITUDE)
force = lift(cl, omega, AIR)
print(f"Gewicht {weight * 1e3:.2f} mN, mittlere Geschwindigkeit der Flügelspitze {tip_speed:.1f} m/s, "
      f"Reynolds-Zahl etwa {round(reynolds, -2):.0f}")
print(f"zum Schweben nötiger Auftriebsbeiwert: C_L = {cl:.1f}")
print(f"Auftrieb in der Schlagmitte bis zum {force.max() / weight:.1f}-Fachen des Gewichts, 0 an jeder Umkehr")
print(f"in Heliox mit gleichem Schlag: C_L = {needed_cl(AMPLITUDE, HELIOX):.1f}; "
      f"mit 50 % weiterem Schlag: C_L = {needed_cl(1.5 * AMPLITUDE, HELIOX):.1f}")

plt.rcParams["font.size"] = 13      # große Schrift: Das Diagramm bleibt auf dem Handy lesbar
fig, (top, bottom) = plt.subplots(2, 1, figsize=(6.4, 8.4), layout="constrained", sharex=True)
ms = t * 1e3
for ax in (top, bottom):
    for turn in np.arange(0.25, 2, 0.5) / FREQUENCY * 1e3:    # die vier Umkehrpunkte
        ax.axvline(turn, color="#c98a1b", lw=6, alpha=0.18)
top.plot(ms, np.degrees(angle), lw=2.5, color="black")
top.axhline(0, color="grey", lw=0.8)
top.set_ylabel("Schlagwinkel φ (°)")
top.set_title("Der Flügel schwingt vor und zurück")
top.text(0.25 / FREQUENCY * 1e3 + 0.07, -40, "Umkehr:\nFlügel dreht", fontsize=11)
bottom.plot(ms, force * 1e3, lw=2.5, label="Auftrieb, quasistationäres Modell")
bottom.axhline(weight * 1e3, color="black", ls="--", lw=1.5, label="Körpergewicht")
bottom.set_xlabel("Zeit (ms)")
bottom.set_ylabel("Auftrieb (mN)")
bottom.set_ylim(0, 2.6)
bottom.set_title("Auftrieb: Spitze mitten im Schlag")
bottom.legend(loc="upper right", fontsize=11)
plt.show()
