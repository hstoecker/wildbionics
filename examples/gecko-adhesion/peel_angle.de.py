# peel_angle.py – Aus „Wie Geckos an Wänden haften: Van-der-Waals-Kräfte“
# https://wildbionics.com/de/artikel/gecko-haftung/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy scipy matplotlib
# Starten: python3 peel_angle.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# Adhäsionsarbeit aus der Physik-Linse: P = A/(6πD³) vom Kontakt bis unendlich integriert
A_HAMAKER = 1e-19     # Hamaker-Konstante (J), typisch für Festkörper
D_CONTACT = 0.3e-9    # Abstand von Flächen in Kontakt (m), etwa ein Atom
W = A_HAMAKER / (12 * np.pi * D_CONTACT**2)   # Energie, um 1 m² Kontakt zu trennen (J/m²)

# Die Spatula als dünnes elastisches Band
WIDTH = 200e-9        # Breite der Spatula (m), etwa 200 nm
THICKNESS = 10e-9     # Dicke des Spatula-Plättchens (m), angenommen
MODULUS = 1.6e9       # Elastizitätsmodul des Setae-Keratins (Pa), gemessen beim Tokeh


def peel_force(angle_deg):
    """Kraft (N), die das Band unter einem Winkel zur Wand abschält.

    Kendalls Gleichung (F/b)²/(2Eh) + (F/b)(1 − cos θ) = W, nach F aufgelöst.
    So geschrieben, dass keine zwei fast gleichen Zahlen subtrahiert werden –
    das würde Stellen verschenken (1 − cos θ bei kleinem θ, −a + √(a² + ε) bei großem θ).
    """
    one_minus_cos = 2 * np.sin(np.radians(angle_deg) / 2) ** 2
    stretch = 2 * W / (MODULUS * THICKNESS)    # wie stark sich das Band dehnen lässt
    return WIDTH * 2 * W / (one_minus_cos + np.sqrt(one_minus_cos**2 + stretch))


def rigid_tape_force(angle_deg):
    """Dasselbe ohne Dehnung (E → ∞): F = bW / (1 − cos θ)."""
    return WIDTH * W / (2 * np.sin(np.radians(angle_deg) / 2) ** 2)


print(f"Adhäsionsarbeit W = {W * 1e3:.0f} mJ/m²")
print("Winkel   Schälkraft   starres Band")
for angle in [0, 10, 30, 60, 90]:
    rigid = f"{rigid_tape_force(angle) * 1e9:7.1f} nN" if angle else "  unendlich"
    print(f"{angle:5d}°   {peel_force(angle) * 1e9:6.1f} nN   {rigid}")

# Der Schalter: Wie weit muss der Fuß kippen, damit 90 % des Halts verloren gehen?
f_max = peel_force(0)
release = brentq(lambda a: peel_force(a) - 0.1 * f_max, 0, 90)
print(f"Schaltverhältnis F(10°) / F(90°) = {peel_force(10) / peel_force(90):.0f}")
print(f"Halt sinkt bei {release:.0f}° auf 10 % des Höchstwerts")
print("gemessen für eine Spatula: etwa 10 nN (Huber et al. 2005)")

angles = np.linspace(0, 90, 361)
plt.rcParams["font.size"] = 13      # große Schrift: Das Diagramm bleibt auf dem Handy lesbar
fig, ax = plt.subplots(figsize=(6.4, 5.2), layout="constrained")
ax.semilogy(angles, peel_force(angles) * 1e9, lw=2.5, label="elastisches Band (Kendall)")
ax.semilogy(angles[8:], rigid_tape_force(angles[8:]) * 1e9, "--", lw=1.8, label="starres Band (ohne Dehnung)")
ax.plot([90], [10], "ko", ms=7, label="gemessen: etwa 10 nN")
ax.axvline(release, color="gray", lw=1, ls=":")
ax.text(release + 1.5, 300, f"10 % Halt\nbei {release:.0f}°", color="dimgray")
ax.set_xlabel("Schälwinkel θ (Grad)")
ax.set_ylabel("Kraft zum Abschälen einer Spatula (nN)")
ax.set_title("Flach hält, steil löst")
ax.set_xlim(0, 93)
ax.set_ylim(2, 1000)
ax.legend(loc="lower left")
plt.show()
