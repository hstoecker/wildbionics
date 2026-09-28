# cat_interference.py – From “Schrödinger's Cat: The Thought Experiment Explained”
# https://wildbionics.com/articles/schroedingers-cat/ · Code: MIT licence
# Needs: python3 -m pip install numpy matplotlib
# Run: python3 cat_interference.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt

BOXES = 1000        # boxes opened per point in time (repetitions of the experiment)
TAU = 1.0           # decoherence time – the unit of time on the x axis
rng = np.random.default_rng(1)


def density_matrix(t):
    """State after time t: the equal superposition (|alive⟩ + |dead⟩)/√2,
    whose coherence – the off-diagonal entry – decays as the environment 'watches'."""
    coherence = 0.5 * np.exp(-t / TAU)
    return np.array([[0.5, coherence],
                     [coherence, 0.5]])


def probabilities(rho):
    """Born rule for two measurements on the same state.
    'Alive or dead?' asks for |alive⟩; the interference test asks for (|alive⟩ + |dead⟩)/√2."""
    p_alive = rho[0, 0]
    p_interference = 0.5 * (rho[0, 0] + rho[1, 1]) + rho[0, 1]
    return p_alive, p_interference


def open_boxes(p):
    """Each box gives one yes/no answer; return the fraction of 'yes' among BOXES boxes."""
    return rng.binomial(BOXES, p) / BOXES


print("time/τ   alive: theory  measured   interference: theory  measured")
for t in [0, 0.5, 1, 2, 5]:
    p_alive, p_int = probabilities(density_matrix(t))
    print(f"{t:6.1f}   {p_alive:13.3f}  {open_boxes(p_alive):8.3f}   {p_int:20.3f}  {open_boxes(p_int):8.3f}")
p_mix = probabilities(np.diag([0.5, 0.5]))[1]
print(f"a box that is simply alive or dead (no superposition): interference {p_mix:.3f}")

times = np.linspace(0, 5, 26)
exact = np.array([probabilities(density_matrix(t)) for t in times])
measured = np.array([[open_boxes(p) for p in row] for row in exact])
plt.rcParams["font.size"] = 13      # large type: the chart stays readable on a phone
fig, ax = plt.subplots(figsize=(6.4, 5.2), layout="constrained")
ax.plot(times, exact[:, 1], lw=2.5, label="interference test (theory)")
ax.plot(times, measured[:, 1], "o", ms=5, label=f"interference test ({BOXES} boxes)")
ax.plot(times, exact[:, 0], "--", lw=2, label="alive or dead? (theory)")
ax.plot(times, measured[:, 0], "s", ms=4, mfc="none", label=f"alive or dead? ({BOXES} boxes)")
ax.axhline(0.5, color="gray", lw=1, ls=":")
ax.text(3.1, 0.54, "no superposition left", color="dimgray", fontsize=11)
ax.set_xlabel("time (in units of the decoherence time τ)")
ax.set_ylabel("fraction of 'yes' answers")
ax.set_title("Only interference reveals the superposition")
ax.set_ylim(0.3, 1.05)
ax.legend(loc="upper right", fontsize=10)
plt.show()
