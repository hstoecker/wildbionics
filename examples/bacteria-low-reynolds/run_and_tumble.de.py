# run_and_tumble.py – Aus „Schwimmen in Honig: die Physik der Bakterien“
# https://wildbionics.com/de/artikel/schwimmen-in-honig/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy matplotlib
# Starten: python3 run_and_tumble.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt

# Modellparameter – typische Werte, siehe Artikel
SPEED = 20.0       # Schwimmgeschwindigkeit im Lauf (µm/s); Berg maß 20–40 µm/s
RUN_TIME = 1.0     # mittlere Laufdauer (s), wenn nichts besser wird
BOOST = 2.0        # Läufe das Nahrungsgefälle hinauf dauern im Mittel BOOST-mal länger
N_CELLS = 2000     # Bakterien pro Population
T_END = 100.0      # simulierte Zeit (s)
DT = 0.01          # Zeitschritt (s)
rng = np.random.default_rng(1)


def swim(boost):
    """Laufen und Taumeln in 2D. Nach +x gibt es mehr Nahrung, „besser werden“ heißt also: nach +x.

    Ein Taumeln dauert keine Zeit und wählt eine völlig zufällige neue Richtung (eine Vereinfachung).
    In jedem Schritt taumelt eine Zelle mit der Wahrscheinlichkeit DT / mittlere Laufdauer. Bergs
    Regel: Wenn es besser wird, hör nicht so früh auf – Läufe nach +x dauern RUN_TIME × boost.
    """
    steps = int(T_END / DT)
    angle = rng.uniform(0, 2 * np.pi, N_CELLS)
    track = np.zeros((steps + 1, N_CELLS, 2))
    for i in range(steps):
        heading = np.column_stack((np.cos(angle), np.sin(angle)))
        track[i + 1] = track[i] + SPEED * DT * heading
        mean_run = np.where(heading[:, 0] > 0, RUN_TIME * boost, RUN_TIME)
        tumble = rng.random(N_CELLS) < DT / mean_run
        angle = np.where(tumble, rng.uniform(0, 2 * np.pi, N_CELLS), angle)
    return track


t = np.arange(int(T_END / DT) + 1) * DT
late = t > 20                     # Fit nach den ersten Läufen, wenn der Start vergessen ist
plain = swim(boost=1.0)
biased = swim(boost=BOOST)

# 1) Ohne Gefälle: eine Zufallsbewegung. Ausbreitung <r²> = 4 D t mit D = v² τ / 2 in 2D.
msd = (plain ** 2).sum(axis=2).mean(axis=1)
d_sim = np.polyfit(t[late], msd[late], 1)[0] / 4
print(f"Zufallsbewegung: D = {d_sim:.0f} µm²/s (Formel v²τ/2 = {SPEED**2 * RUN_TIME / 2:.0f} µm²/s)")

# 2) Bergs Regel: Die Population driftet das Gefälle hinauf. Formel: v · (2/π) · (b − 1)/(b + 1).
drift_sim = np.polyfit(t[late], biased[late, :, 0].mean(axis=1), 1)[0]
drift_theory = SPEED * 2 / np.pi * (BOOST - 1) / (BOOST + 1)
# round(...) + 0.0 macht aus einem gerundeten „-0.0“ ein „0.0“
print(f"mit der Regel: Drift {round(drift_sim, 1) + 0.0} µm/s (Formel {drift_theory:.1f} µm/s), "
      f"{round(100 * drift_sim / SPEED) + 0} % der Schwimmgeschwindigkeit")
print(f"nach {T_END:.0f} s ist die mittlere Zelle {biased[-1, :, 0].mean():.0f} µm weiter oben im Gefälle")

plt.rcParams["font.size"] = 13      # große Schrift: das Diagramm bleibt auf dem Handy lesbar
fig, (top, bottom) = plt.subplots(2, 1, figsize=(6.4, 8.4), layout="constrained")
for k, style in zip(range(3, 6), ["-", "--", ":"]):   # drei der Zellen, erste 60 s
    path = biased[: int(60 / DT) : 5, k]
    top.plot(path[:, 0], path[:, 1], style, lw=1.6, label=f"Zelle {k}")
top.plot(0, 0, "ko", ms=6)
top.annotate("Start", (0, 0), textcoords="offset points", xytext=(6, -16))
top.set_aspect("equal", adjustable="datalim")
top.set_xlabel("x (µm) – rechts mehr Nahrung →")
top.set_ylabel("y (µm)")
top.set_title("Laufen und Taumeln: drei Zellen, 60 s")
top.legend(loc="upper left", fontsize=11)

bottom.plot(t, biased[..., 0].mean(axis=1), lw=2.5, label="Läufe nach oben dauern länger")
bottom.plot(t, plain[..., 0].mean(axis=1), "--", lw=2, label="ohne Regel: alle Läufe gleich")
bottom.set_xlabel("Zeit (s)")
bottom.set_ylabel("mittlere Position x (µm)")
bottom.set_title("Eine einfache Regel führt bergauf")
bottom.legend(loc="upper left", fontsize=11)
plt.show()
