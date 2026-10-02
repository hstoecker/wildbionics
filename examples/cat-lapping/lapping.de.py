# lapping.py – Aus „Wie Katzen trinken: Trägheit gegen Schwerkraft“
# https://wildbionics.com/de/artikel/wie-katzen-trinken/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy matplotlib
# Starten: python3 lapping.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt

# Typische Körpermassen (kg) – grobe Werte zur Veranschaulichung, keine Messungen
CATS = {"Hauskatze": 4, "Ozelot": 11, "Gepard": 45, "Jaguar": 80, "Löwe": 190, "Tiger": 220}
EXPONENT = -1 / 6     # Frequenz ∝ Masse^EXPONENT: Trägheit im Gleichgewicht mit der Schwerkraft (siehe Mathematik-Linse)


def relative_frequency(mass, reference=CATS["Hauskatze"]):
    """Leckfrequenz relativ zur Hauskatze.

    Trägheit und Schwerkraft halten sich die Waage, wenn die Zungengeschwindigkeit U etwa √(g·R) ist
    (Froude-Zahl ≈ 1); ein Zug dauert also etwa R/U = √(R/g). Der Zungenradius R wächst bei Tieren
    ähnlicher Gestalt wie Masse^(1/3), also Frequenz ∝ √(g/R) ∝ Masse^(−1/6).
    """
    return (mass / reference) ** EXPONENT


print("Tier            Masse   Züge relativ zur Hauskatze")
for name, mass in CATS.items():
    print(f"{name:13s} {mass:5d} kg   {relative_frequency(mass):5.2f}")
lion = relative_frequency(CATS["Löwe"])
print(f"ein Löwe ist {CATS['Löwe'] / CATS['Hauskatze']:.1f}-mal schwerer, "
      f"leckt aber nur {1 / lion:.1f}-mal langsamer")

masses = np.logspace(0, 2.6, 100)
plt.rcParams["font.size"] = 13      # große Schrift: Das Diagramm bleibt auf dem Handy lesbar
fig, ax = plt.subplots(figsize=(6.4, 5.2), layout="constrained")
ax.loglog(masses, relative_frequency(masses), lw=2.5, label="Trägheit gegen Schwerkraft: Masse^(−1/6)")
ax.loglog(masses, (masses / CATS["Hauskatze"]) ** (-1 / 3), "--", lw=1.8,
          label="bei gleicher Geschwindigkeit: Masse^(−1/3)")
for name, mass in CATS.items():
    below = name == "Tiger"             # Löwe und Tiger liegen nah beieinander: eine Beschriftung oben, eine unten
    ax.plot(mass, relative_frequency(mass), "o", ms=7, color="black")
    ax.annotate(name, (mass, relative_frequency(mass)), textcoords="offset points",
                xytext=(-10, -20) if below else (6, 6), fontsize=11)
ax.set_xlabel("Körpermasse (kg)")
ax.set_ylabel("Züge pro Sekunde (Hauskatze = 1)")
ax.set_title("Große Katzen lecken nur wenig langsamer")
ax.set_ylim(0.15, 2.5)
ax.set_yticks([0.2, 0.3, 0.5, 1, 2])
ax.xaxis.set_major_formatter("{x:g}")   # einfache Zahlen: 1, 10, 100
ax.yaxis.set_major_formatter("{x:g}")
ax.legend(loc="lower left")
plt.show()
