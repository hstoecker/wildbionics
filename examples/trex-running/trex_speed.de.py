# trex_speed.py – Aus „Wie schnell war T. rex? Fährten, Knochen und Physik“
# https://wildbionics.com/de/artikel/t-rex-laufen/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy matplotlib
# Starten: python3 trex_speed.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt

# Wie schnell war der Erzeuger einer fossilen Fährte? Geschwindigkeit aus Doppelschrittlänge und Hüfthöhe.
G = 9.81                 # Fallbeschleunigung (m/s²)
HIP_TREX = 3.10          # Hüfthöhe des ausgewachsenen T. rex „Trix“ (m), wie bei van Bijlert et al.
HIP_HUMAN = 0.90         # Hüfthöhe eines erwachsenen Menschen (m) – angenommen
UNCERTAINTY = 1.5        # Säugetierdaten streuen um die Regel bis zum Faktor 1,5
TRACKWAYS = {            # Name: (Doppelschrittlänge λ in m, Hüfthöhe h in m)
    "Tyrannosauridenfährte, gestrecktes Bein": (3.46, 2.87),
    "Tyrannosauridenfährte, gebeugtes Bein": (3.46, 2.30),
    "dieselbe Fährte, auf T. rex skaliert": (3.88, HIP_TREX),
    "Mensch beim Gehen (angenommen)": (1.40, HIP_HUMAN),
}
SIMULATED_TOP_SPEED = 8.0    # T.-rex-Modell, nur durch Muskeln begrenzt (m/s), Beinlänge 3,089 m


def froude(speed, hip, g=G):
    """Froude-Zahl v²/(g·h): die „Geschwindigkeitszahl“, die bei dynamisch ähnlichen Gangarten gleich ist."""
    return speed**2 / (g * hip)


def speed_from_trackway(stride, hip, g=G):
    """Alexanders Regel für dynamisch ähnliche Tiere, λ/h ≈ 2,3·Fr^0,3, nach v aufgelöst:
    Fr = (λ / 2,3h)^(1/0,3), v = √(Fr·g·h) ≈ 0,25·√g·λ^1,67·h^-1,17."""
    fr = (stride / (2.3 * hip)) ** (1 / 0.3)
    return np.sqrt(fr * g * hip)


def walking_limit(hip, g=G):
    """Bei Fr = 1 kann die Schwerkraft den Körper nicht mehr auf seinem Bogen über dem Fuß halten: v = √(g·h)."""
    return np.sqrt(g * hip)


for name, (stride, hip) in TRACKWAYS.items():
    v = speed_from_trackway(stride, hip)
    print(f"{name}: λ/h = {stride / hip:.2f} → {v:.1f} m/s = {3.6 * v:.1f} km/h (Fr = {froude(v, hip):.2f})")

v_trex = speed_from_trackway(*TRACKWAYS["dieselbe Fährte, auf T. rex skaliert"])
print(f"mit der Streuung der Regel (×/÷ {UNCERTAINTY}) ergibt die skalierte T.-rex-Fährte "
      f"{3.6 * v_trex / UNCERTAINTY:.0f}–{3.6 * v_trex * UNCERTAINTY:.0f} km/h")
v_limit = walking_limit(HIP_TREX)
print(f"Grenze des Gehens für T. rex (Fr = 1): {v_limit:.1f} m/s = {3.6 * v_limit:.0f} km/h")
print(f"reines Muskelmodell: {SIMULATED_TOP_SPEED:.1f} m/s = {3.6 * SIMULATED_TOP_SPEED:.0f} km/h "
      f"(Fr = {froude(SIMULATED_TOP_SPEED, 3.089):.1f}) – eine Gangart des Rennens")

plt.rcParams["font.size"] = 13      # große Schrift: Das Diagramm bleibt auf dem Handy lesbar
fig, ax = plt.subplots(figsize=(6.4, 6.0), layout="constrained")
for hip, label, color, style in ((HIP_TREX, "T. rex, h = 3,1 m", "#1f6f8b", "-"),
                                 (HIP_HUMAN, "Mensch, h = 0,9 m", "#c0392b", "--")):
    stride = np.linspace(0.3, 9.0, 400)
    v = speed_from_trackway(stride, hip)
    walk = v <= walking_limit(hip)
    ax.plot(stride[walk], v[walk], lw=2.5, ls=style, color=color, label=label)
    ax.plot(stride[~walk], v[~walk], lw=1.5, ls=":", color=color)
    i = np.argmax(~walk)
    ax.plot(stride[i], v[i], "o", ms=7, mfc="white", color=color)
ax.text(7.5, 5.0, "Fr = 1:\nEnde des Gehens", va="top", ha="center", fontsize=11, color="#1f6f8b")
ax.text(2.1, 3.6, "Fr = 1", ha="center", fontsize=11, color="#c0392b")
for name, (stride, hip) in list(TRACKWAYS.items())[:3]:
    ax.plot(stride, speed_from_trackway(stride, hip), "s", ms=8, color="#c98a1b")
ax.annotate("Tyrannosauriden-\nfährten", xy=(3.6, 2.2), xytext=(4.3, 0.6), color="#8a5a00",
            arrowprops=dict(arrowstyle="-", color="#8a5a00"))
ax.axhline(SIMULATED_TOP_SPEED, color="grey", lw=1, ls="-.")
ax.text(4.3, SIMULATED_TOP_SPEED + 0.2, "reines Muskelmodell", fontsize=11, color="dimgrey")
ax.set_xlabel("Doppelschrittlänge λ in der Fährte (m)")
ax.set_ylabel("geschätzte Geschwindigkeit (m/s)")
ax.set_xlim(0, 9.2)
ax.set_ylim(0, 10)
ax.set_title("Derselbe Schritt ist für T. rex ein Bummeln")
ax.legend(loc="upper left", fontsize=11)
plt.show()
