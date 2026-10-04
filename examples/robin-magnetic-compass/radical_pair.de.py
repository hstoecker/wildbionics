# radical_pair.py – Aus „Der Quantenkompass des Rotkehlchens“
# https://wildbionics.com/de/artikel/rotkehlchen-magnetkompass/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy matplotlib
# Starten: python3 radical_pair.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt

# Naturkonstanten
GAMMA_E = 1.760859e11     # gyromagnetisches Verhältnis des Elektrons (rad s⁻¹ T⁻¹)
MU_B = 9.2740101e-24      # Bohrsches Magneton (J/T)
K_B = 1.380649e-23        # Boltzmann-Konstante (J/K)
H = 6.62607015e-34        # Planck-Konstante (J s)

# Modell – ein minimales Radikalpaar (Annahmen, siehe Text)
B_EARTH = 50e-6           # Erdmagnetfeld (T), etwa 50 µT
HYPERFINE = 1.0e-3        # axiale Hyperfeinkopplung von Elektron 1 an einen Kern (T)
ANISOTROPY = (0.0, 0.0, 1.0)   # Hyperfeintensor diag(x, y, z) in Einheiten von HYPERFINE: rein axial
LIFETIME = 1e-6           # Lebensdauer des Radikalpaars (s); Reaktionsrate k = 1/LIFETIME

# Warum das erstaunt: magnetische Energie eines Elektronenspins im Erdfeld gegen Wärme
zeeman = 2 * MU_B * B_EARTH
print(f"magnetische Energie / Wärmeenergie bei 37 °C: {zeeman / (K_B * 310):.0e}")
print(f"Elektronenspins präzedieren im Erdfeld mit {GAMMA_E * B_EARTH / (2 * np.pi) / 1e6:.1f} MHz")

# Spinoperatoren für Spin 1/2, kombiniert für Elektron 1, Elektron 2 und den Kern (8 Zustände)
sx, sy, sz = (np.array(m, dtype=complex) / 2 for m in ([[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]))
one = np.eye(2)
def op(a, b, c):
    return np.kron(np.kron(a, b), c)
spin = (sx, sy, sz)
S1 = [op(s, one, one) for s in spin]                     # Elektron 1
S2 = [op(one, s, one) for s in spin]                     # Elektron 2
S1_I = [op(s, one, s) for s in spin]                     # Produkte S1x·Ix, S1y·Iy, S1z·Iz
singlet = 0.25 * np.eye(8) - sum(op(s, s, one) for s in spin)     # Projektor auf den Singulett-Zustand


def singlet_yield(theta):
    """Anteil der Radikalpaare, die aus dem Singulett reagieren; Feld im Winkel theta zum Molekül."""
    b = np.array([np.sin(theta), 0.0, np.cos(theta)])
    w = GAMMA_E * B_EARTH
    zeeman_h = w * sum(bi * (s1 + s2) for bi, s1, s2 in zip(b, S1, S2))
    hyperfine_h = GAMMA_E * HYPERFINE * sum(a * si for a, si in zip(ANISOTROPY, S1_I))
    energies, states = np.linalg.eigh(zeeman_h + hyperfine_h)
    p = np.einsum("im,ij,jn->mn", states.conj(), singlet, states)   # Singulett-Projektor in der Eigenbasis
    k = 1 / LIFETIME
    omega = energies[:, None] - energies[None, :]
    return float(np.sum(np.abs(p) ** 2 * k**2 / (k**2 + omega**2)).real / 2)   # Tr(singlet) = 2


angles = np.radians(np.linspace(0, 180, 181))
yields = np.array([singlet_yield(a) for a in angles])
print(f"Singulett-Ausbeute: {yields[0]:.4f} längs der Feldachse, {yields[90]:.4f} quer dazu")
print(f"Kompass-Signal (max − min): {100 * (yields.max() - yields.min()):.2f} % aller Paare")
print(f"Nord und Süd sehen gleich aus – Ausbeute bei θ gleich der bei 180° − θ auf 12 Stellen: "
      f"{np.allclose(yields, yields[::-1], rtol=0, atol=1e-12)}")

plt.rcParams["font.size"] = 13      # große Schrift: das Diagramm bleibt auf dem Handy lesbar
fig, ax = plt.subplots(figsize=(6.4, 5.0), layout="constrained")
ax.plot(np.degrees(angles), 100 * yields, lw=2.5)
ax.axvline(90, color="grey", ls=":", lw=1.5)
ax.set_xlabel("Winkel zwischen Erdfeld und Molekül (°)")
ax.set_ylabel("Singulett-Ausbeute (%)")
ax.set_xticks([0, 45, 90, 135, 180])
ax.set_title("Der Winkel zählt – Nord oder Süd nicht")
plt.show()
