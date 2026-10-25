# sabre_bending.py – Aus „Säbelzahnkatze: schwacher Biss, zerbrechliche Säbel“
# https://wildbionics.com/de/artikel/saebelzahnkatze/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy matplotlib
# Starten: python3 sabre_bending.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt

# Wie fest ist ein Säbel? Der obere Eckzahn von Smilodon fatalis als Kragbalken mit
# elliptischem Querschnitt, gemessen am Zahnfleischrand in jedem Stadium seines Durchbruchs.
# Daten: Tseng (2025), Tabelle S1, „morpho“-Modelle (CC BY 4.0): (Durchbruchshöhe, Länge x
# von vorn nach hinten, Breite y von Seite zu Seite) in mm.
CANINES = {
    "AMNH FM55576": [(40.62, 21.58, 10.28), (50.23, 24.64, 11.18), (58.62, 26.75, 11.63),
                     (68.15, 28.78, 12.81), (78.31, 30.34, 13.93), (89.28, 31.08, 15.07),
                     (97.68, 31.58, 15.66), (106.83, 32.16, 16.44), (118.43, 32.55, 17.48),
                     (127.78, 31.99, 17.70), (137.76, 32.17, 18.00)],
    "KU S2255": [(20.20, 14.89, 7.73), (31.31, 19.81, 9.67), (42.91, 22.99, 10.58),
                 (54.85, 26.80, 11.96), (65.21, 29.56, 13.25), (75.16, 31.41, 13.94),
                 (85.12, 33.21, 14.94), (95.03, 34.63, 15.65)],
}
SPECIMEN_INDEX = 0          # 0: AMNH FM55576, die vollständigste Durchbruchsreihe (bis 138 mm); 1: KU S2255
SPECIMEN = list(CANINES)[SPECIMEN_INDEX]
LOAD_N = 100.0              # Kraft an der Spitze (N) – ein angenommener runder Vergleichswert
ROUND = False               # True: gleiche Querschnittsfläche, aber ein runder Zahn


def bending_stress(force, height, x, y):
    """Größte Biegespannung (MPa) an der Basis eines elliptischen Kragbalkens.
    Halbachsen a = x/2 (vorn–hinten) und b = y/2 (seitlich), alle in mm.
    Seitliche Last biegt um die lange Achse: Widerstandsmoment π·a·b²/4.
    Last von vorn biegt um die kurze Achse: Widerstandsmoment π·b·a²/4."""
    a, b = x / 2, y / 2
    moment = force * height                      # N·mm
    side = moment / (np.pi * a * b**2 / 4)       # N/mm² = MPa
    front = moment / (np.pi * b * a**2 / 4)
    return side, front


data = np.array(CANINES[SPECIMEN])
height, x, y = data.T
if ROUND:                                        # gleiche Fläche, kreisförmig: x = y = √(x·y)
    x = y = np.sqrt(x * y)
side, front = bending_stress(LOAD_N, height, x, y)

print(f"{SPECIMEN}, Last {LOAD_N:.0f} N an der Spitze")
for h, s, f in ((height[0], side[0], front[0]), (height[-1], side[-1], front[-1])):
    print(f"  Höhe {h:.0f} mm: {s:.1f} MPa von der Seite, {f:.1f} MPa von vorn")
print(f"voll durchgebrochen belastet eine seitliche Last den Zahn {side[-1] / front[-1]:.1f}-mal stärker als eine Last von vorn")
print(f"vom ersten zum letzten Stadium ändert sich die seitliche Spannung um den Faktor {side[-1] / side[0]:.2f}, "
      f"während die Höhe {height[-1] / height[0]:.1f}-mal zunimmt")

plt.rcParams["font.size"] = 13      # große Schrift: Das Diagramm bleibt auf dem Handy lesbar
fig, ax = plt.subplots(figsize=(6.4, 5.6), layout="constrained")
ax.plot(height, side, "o-", lw=2.5, color="#c0392b", label="Last von der Seite")
ax.plot(height, front, "s--", lw=2.5, color="#1f6f8b", label="Last von vorn")
ax.set_ylim(0, 1.15 * side.max())
ax.axvspan(20, 40, color="grey", alpha=0.15)
ax.text(30, 1.12 * side.max(), "typische\nKatze", ha="center", va="top", fontsize=11)
ax.set_xlabel("Durchbruchshöhe des Eckzahns (mm)")
ax.set_ylabel(f"Biegespannung an der Basis (MPa)\nbei {LOAD_N:.0f} N an der Spitze")
ax.set_xlim(15, 145)
ax.set_title("Seitlich ist der Säbel verwundbar")
ax.legend(loc="lower right", fontsize=11)
plt.show()
