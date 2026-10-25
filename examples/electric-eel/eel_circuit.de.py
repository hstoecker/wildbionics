# eel_circuit.py – Aus „Zitteraal: 860 Volt aus lebenden Batterien“
# https://wildbionics.com/de/artikel/zitteraal/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy matplotlib
# Starten: python3 eel_circuit.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt

# Wie viel Leistung treibt ein springender Zitteraal durch einen Angreifer? Ein Ersatzschaltbild.
CELL_EMF = 0.150         # Spannung eines feuernden Elektrozyten (V), Schroeder et al. 2017
# Gemessen an einem kleinen Aal durch Catania (zusammengefasst in Catania 2019, Abb. 12):
EMF, R_INTERNAL = 198.0, 960.0   # Quellenspannung (V) und Innenwiderstand (Ω)
R_WATER = 400.0          # Widerstand des Wasserwegs zurück zum Schwanz (Ω)
RETURN_PATH = 2400.0     # Rückweg vom Kopf am Aal entlang ins Wasser, am höchsten Punkt des Sprungs (Ω)
R_ARM = 2100.0           # ein menschlicher Arm, das Ziel (Ω)
ROWS = 1                 # wie viele Kopien des Organs parallel arbeiten (1 = der echte Aal)


def thevenin(emf, r_source, r_return):
    """Vom Ziel aus gesehen wirken Aal, Wasser und Rückweg wie eine einzige Batterie:
    Der Rückweg teilt die Spannung und liegt parallel zum Ziel."""
    r_loop = r_source + R_WATER
    v_th = emf * r_return / (r_loop + r_return)
    r_th = r_loop * r_return / (r_loop + r_return)
    return v_th, r_th


def target_power(r_target, v_th, r_th):
    """Strom und Leistung in einem Ziel mit Widerstand R: I = V/(R_th + R), P = I²·R."""
    current = v_th / (r_th + r_target)
    return current, current**2 * r_target


r_eel = R_INTERNAL / ROWS                 # parallele Reihen teilen den Innenwiderstand
for volts in (EMF, 600.0, 860.0):
    print(f"{volts:.0f} V brauchen etwa {volts / CELL_EMF:.0f} Elektrozyten in Reihe")

v_th, r_th = thevenin(EMF, r_eel, RETURN_PATH)
print(f"vom Ziel aus gesehen: {v_th:.0f} V hinter {r_th:.0f} Ω")
i_arm, p_arm = target_power(R_ARM, v_th, r_th)
i_eel = EMF / (r_eel + R_WATER + RETURN_PATH * R_ARM / (RETURN_PATH + R_ARM))
print(f"Strom aus dem Aal: {1e3 * i_eel:.0f} mA")
print(f"Arm ({R_ARM:.0f} Ω): {1e3 * i_arm:.0f} mA, {p_arm:.1f} W")
print(f"bestes Ziel: {r_th:.0f} Ω erhält {target_power(r_th, v_th, r_th)[1]:.1f} W (Leistungsanpassung)")
for r_return, name in ((600.0, "niedriger Sprung"), (RETURN_PATH, "höchster Punkt"), (1e9, "ohne Rückweg")):
    i, p = target_power(R_ARM, *thevenin(EMF, r_eel, r_return))
    print(f"{name}: Strom im Arm {1e3 * i:.0f} mA, {p:.1f} W")

plt.rcParams["font.size"] = 13      # große Schrift: Diagramm bleibt auf dem Handy lesbar
fig, ax = plt.subplots(figsize=(6.4, 6.0), layout="constrained")
r_target = np.logspace(2, 5, 400)
for r_return, label, style in ((600.0, "niedriger Sprung (600 Ω, angen.)", ":"),
                               (RETURN_PATH, "höchster Punkt (2400 Ω)", "-"),
                               (1e9, "Grenzfall: ohne Rückweg", "--")):
    v, r = thevenin(EMF, r_eel, r_return)
    ax.plot(r_target, target_power(r_target, v, r)[1], ls=style, lw=2.5, color="#1f6f8b", label=label)
    ax.plot(r, target_power(r, v, r)[1], "o", ms=8, mfc="white", color="#1f6f8b")
ax.axvline(R_ARM, ymax=0.8, color="#c0392b", lw=1.5, ls="-.")
ax.text(R_ARM * 1.15, 5.0, "Arm", color="#c0392b", fontsize=12)
ax.text(115, 9.7, "Kreise: Maximum, Ziel =\nInnenwiderstand", fontsize=11, color="dimgrey", va="top")
ax.set_xscale("log")
ax.xaxis.set_major_formatter("{x:g}")
ax.set_xlabel("Widerstand des Ziels (Ω)")
ax.set_ylabel("Leistung im Ziel (W)")
ax.set_ylim(0, 10)
ax.set_title("Je höher der Sprung, desto mehr Leistung")
ax.legend(loc="upper right", fontsize=11)
plt.show()
