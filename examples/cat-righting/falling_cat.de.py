# falling_cat.py – Aus „Wie Katzen auf den Füßen landen: der Drehimpuls erklärt“
# https://wildbionics.com/de/artikel/katzen-stellreflex/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy matplotlib
# Starten: python3 falling_cat.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt

# Zwei Hälften der Katze drehen sich um dieselbe Achse (die Wirbelsäule), Modell „Anziehen und Drehen“.
I_TUCKED = 1.0      # Trägheitsmoment einer Hälfte mit angezogenen Beinen (relative Einheiten)
I_EXTENDED = 3.0    # dieselbe Hälfte mit gestreckten Beinen – angenommen 3-mal größer
TWIST = 180.0       # wie weit sich die vordere gegen die hintere Hälfte pro Schritt verdreht (Grad)
STEP_TIME = 0.1     # Dauer einer Verdrehung (s), angenommen
G = 9.81            # Fallbeschleunigung (m/s²)


def twist(i_front, i_rear, d_relative):
    """Die Hälften um d_relative gegeneinander verdrehen, bei Gesamtdrehimpuls null.
    I_v·Δθ_v + I_h·Δθ_h = 0 und Δθ_v − Δθ_h = d_relative ergeben die Drehung jeder Hälfte."""
    d_front = d_relative * i_rear / (i_front + i_rear)
    d_rear = -d_relative * i_front / (i_front + i_rear)
    return d_front, d_rear


# Ein Zyklus: (1) Vorderbeine angezogen, vordere Hälfte drehen; (2) Hinterbeine angezogen, zurückdrehen.
steps = [(I_TUCKED, I_EXTENDED, +TWIST), (I_EXTENDED, I_TUCKED, -TWIST)]
front, rear, time = [0.0], [0.0], [0.0]
largest_momentum = 0.0
for cycle in range(2):
    for i_front, i_rear, d_relative in steps:
        for _ in range(50):                     # jede Verdrehung in 50 kleinen Schritten
            d_front, d_rear = twist(i_front, i_rear, d_relative / 50)
            rate_front, rate_rear = d_front / (STEP_TIME / 50), d_rear / (STEP_TIME / 50)
            largest_momentum = max(largest_momentum, abs(i_front * rate_front + i_rear * rate_rear))
            front.append(front[-1] + d_front)
            rear.append(rear[-1] + d_rear)
            time.append(time[-1] + STEP_TIME / 50)

per_cycle = front[100]
print(f"größter Gesamtdrehimpuls während der Drehung: {largest_momentum:.3f}")
if abs(per_cycle) < 1e-6:
    print("Drehung pro Zyklus: 0° – ohne Formänderung kann sich die Katze nicht drehen")
else:
    cycles = 180.0 / per_cycle
    fall_time = cycles * 2 * STEP_TIME
    print(f"Drehung pro Zyklus: {per_cycle:.1f}° (vordere und hintere Hälfte gleich)")
    print(f"nötige Zyklen, um auf den Füßen zu landen (180°): {cycles:.1f}")
    print(f"benötigte Zeit: {fall_time:.2f} s  →  sie fällt dabei {0.5 * G * fall_time**2 * 100:.0f} cm")

time = np.array(time)
plt.rcParams["font.size"] = 13      # große Schrift: Das Diagramm bleibt auf dem Handy lesbar
fig, ax = plt.subplots(figsize=(6.4, 5.2), layout="constrained")
for k in range(4):                      # die Schritte mit angezogenen Vorderbeinen grau hinterlegen
    if k % 2 == 0:
        ax.axvspan(k * STEP_TIME, (k + 1) * STEP_TIME, color="0.92")
ax.plot(time, front, lw=2.5, label="vordere Hälfte")
ax.plot(time, rear, "--", lw=2.5, label="hintere Hälfte")
ax.axhline(180, color="gray", lw=1, ls=":")
ax.text(0.005, 186, "Füße unten (180°)", color="dimgray", fontsize=11)
ax.text(0.205, -52, "grau: Vorderbeine\nangezogen", color="dimgray", fontsize=11)
ax.set_xlabel("Zeit (s)")
ax.set_ylabel("Drehung um die Wirbelsäule (Grad)")
ax.set_title("Formänderung dreht die Katze – ohne Drall")
ax.set_ylim(-60, 230)
ax.legend(loc="lower right")
plt.show()
