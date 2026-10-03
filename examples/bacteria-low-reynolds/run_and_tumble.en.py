# run_and_tumble.py – From “Swimming in Honey: the Physics of Bacteria”
# https://wildbionics.com/articles/bacteria-low-reynolds/ · Code: MIT licence
# Needs: python3 -m pip install numpy matplotlib
# Run: python3 run_and_tumble.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt

# Model parameters – typical values, see the article
SPEED = 20.0       # swimming speed during a run (µm/s); Berg measured 20–40 µm/s
RUN_TIME = 1.0     # mean run duration (s) when nothing improves
BOOST = 2.0        # runs up the food gradient last BOOST times longer on average
N_CELLS = 2000     # bacteria per population
T_END = 100.0      # simulated time (s)
DT = 0.01          # time step (s)
rng = np.random.default_rng(1)


def swim(boost):
    """Run and tumble in 2D. Food increases towards +x, so 'getting better' means moving to +x.

    A tumble is instantaneous and picks a completely random new direction (a simplification).
    In each step a cell tumbles with probability DT / mean run time. Berg's rule: if things are
    getting better, don't stop so soon – runs towards +x use RUN_TIME × boost.
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
late = t > 20                     # fit after the first runs, when the walk has lost its start
plain = swim(boost=1.0)
biased = swim(boost=BOOST)

# 1) No gradient: a random walk. Its spreading follows <r²> = 4 D t with D = v² τ / 2 in 2D.
msd = (plain ** 2).sum(axis=2).mean(axis=1)
d_sim = np.polyfit(t[late], msd[late], 1)[0] / 4
print(f"random walk: D = {d_sim:.0f} µm²/s (formula v²τ/2 = {SPEED**2 * RUN_TIME / 2:.0f} µm²/s)")

# 2) Berg's rule: the population drifts up the gradient. Formula: v · (2/π) · (b − 1)/(b + 1).
drift_sim = np.polyfit(t[late], biased[late, :, 0].mean(axis=1), 1)[0]
drift_theory = SPEED * 2 / np.pi * (BOOST - 1) / (BOOST + 1)
# round(...) + 0.0 turns a rounded "-0.0" into "0.0"
print(f"with the rule: drift {round(drift_sim, 1) + 0.0} µm/s (formula {drift_theory:.1f} µm/s), "
      f"{round(100 * drift_sim / SPEED) + 0} % of the swimming speed")
print(f"after {T_END:.0f} s the average cell is {biased[-1, :, 0].mean():.0f} µm further up the gradient")

plt.rcParams["font.size"] = 13      # large type: the chart stays readable on a phone
fig, (top, bottom) = plt.subplots(2, 1, figsize=(6.4, 8.4), layout="constrained")
for k, style in zip(range(3, 6), ["-", "--", ":"]):   # three of the cells, first 60 s
    path = biased[: int(60 / DT) : 5, k]
    top.plot(path[:, 0], path[:, 1], style, lw=1.6, label=f"cell {k}")
top.plot(0, 0, "ko", ms=6)
top.annotate("start", (0, 0), textcoords="offset points", xytext=(6, -16))
top.set_aspect("equal", adjustable="datalim")
top.set_xlabel("x (µm) – more food to the right →")
top.set_ylabel("y (µm)")
top.set_title("Runs and tumbles: three cells, 60 s")
top.legend(loc="upper left", fontsize=11)

bottom.plot(t, biased[..., 0].mean(axis=1), lw=2.5, label="runs up the gradient last longer")
bottom.plot(t, plain[..., 0].mean(axis=1), "--", lw=2, label="no rule: all runs alike")
bottom.set_xlabel("time (s)")
bottom.set_ylabel("average position x (µm)")
bottom.set_title("A simple rule climbs the gradient")
bottom.legend(loc="upper left", fontsize=11)
plt.show()
