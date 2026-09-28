# cat_interference.py – Aus „Schrödingers Katze: das Gedankenexperiment erklärt“
# https://wildbionics.com/de/artikel/schroedingers-katze/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy matplotlib
# Starten: python3 cat_interference.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt

BOXES = 1000        # pro Zeitpunkt geöffnete Kisten (Wiederholungen des Experiments)
TAU = 1.0           # Dekohärenzzeit – die Zeiteinheit auf der x-Achse
rng = np.random.default_rng(1)


def density_matrix(t):
    """Zustand nach der Zeit t: die gleichgewichtete Überlagerung (|lebendig⟩ + |tot⟩)/√2,
    deren Kohärenz – das Nebendiagonalelement – abklingt, während die Umgebung ‚zusieht‘."""
    coherence = 0.5 * np.exp(-t / TAU)
    return np.array([[0.5, coherence],
                     [coherence, 0.5]])


def probabilities(rho):
    """Bornsche Regel für zwei Messungen am selben Zustand.
    ‚Lebendig oder tot?‘ fragt nach |lebendig⟩; der Interferenztest fragt nach (|lebendig⟩ + |tot⟩)/√2."""
    p_alive = rho[0, 0]
    p_interference = 0.5 * (rho[0, 0] + rho[1, 1]) + rho[0, 1]
    return p_alive, p_interference


def open_boxes(p):
    """Jede Kiste gibt eine Ja/Nein-Antwort; Anteil der ‚Ja‘ unter BOXES Kisten."""
    return rng.binomial(BOXES, p) / BOXES


print("Zeit/τ   lebendig: Theorie  gemessen   Interferenz: Theorie  gemessen")
for t in [0, 0.5, 1, 2, 5]:
    p_alive, p_int = probabilities(density_matrix(t))
    print(f"{t:6.1f}   {p_alive:16.3f}  {open_boxes(p_alive):8.3f}   {p_int:20.3f}  {open_boxes(p_int):8.3f}")
p_mix = probabilities(np.diag([0.5, 0.5]))[1]
print(f"Kiste, deren Katze einfach lebt oder tot ist (keine Überlagerung): Interferenz {p_mix:.3f}")

times = np.linspace(0, 5, 26)
exact = np.array([probabilities(density_matrix(t)) for t in times])
measured = np.array([[open_boxes(p) for p in row] for row in exact])
plt.rcParams["font.size"] = 13      # große Schrift: Das Diagramm bleibt auf dem Handy lesbar
fig, ax = plt.subplots(figsize=(6.4, 5.2), layout="constrained")
ax.plot(times, exact[:, 1], lw=2.5, label="Interferenztest (Theorie)")
ax.plot(times, measured[:, 1], "o", ms=5, label=f"Interferenztest ({BOXES} Kisten)")
ax.plot(times, exact[:, 0], "--", lw=2, label="lebendig oder tot? (Theorie)")
ax.plot(times, measured[:, 0], "s", ms=4, mfc="none", label=f"lebendig oder tot? ({BOXES} Kisten)")
ax.axhline(0.5, color="gray", lw=1, ls=":")
ax.text(3.1, 0.54, "keine Überlagerung mehr", color="dimgray", fontsize=11)
ax.set_xlabel("Zeit (in Einheiten der Dekohärenzzeit τ)")
ax.set_ylabel("Anteil der ‚Ja‘-Antworten")
ax.set_title("Nur Interferenz zeigt die Überlagerung")
ax.set_ylim(0.3, 1.05)
ax.legend(loc="upper right", fontsize=10)
plt.show()
