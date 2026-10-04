# radical_pair.py – From “The Robin's Quantum Compass”
# https://wildbionics.com/articles/robin-magnetic-compass/ · Code: MIT licence
# Needs: python3 -m pip install numpy matplotlib
# Run: python3 radical_pair.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt

# Physical constants
GAMMA_E = 1.760859e11     # gyromagnetic ratio of the electron (rad s⁻¹ T⁻¹)
MU_B = 9.2740101e-24      # Bohr magneton (J/T)
K_B = 1.380649e-23        # Boltzmann constant (J/K)
H = 6.62607015e-34        # Planck constant (J s)

# Model – a minimal radical pair (assumptions, see the text)
B_EARTH = 50e-6           # Earth's field (T), about 50 µT
HYPERFINE = 1.0e-3        # axial hyperfine coupling of electron 1 to one nucleus (T)
ANISOTROPY = (0.0, 0.0, 1.0)   # hyperfine tensor diag(x, y, z) in units of HYPERFINE: purely axial
LIFETIME = 1e-6           # radical-pair lifetime (s); recombination rate k = 1/LIFETIME

# Why this is surprising: the magnetic energy of an electron spin in Earth's field vs. heat
zeeman = 2 * MU_B * B_EARTH
print(f"magnetic energy / thermal energy at 37 °C: {zeeman / (K_B * 310):.0e}")
print(f"electron spins precess at {GAMMA_E * B_EARTH / (2 * np.pi) / 1e6:.1f} MHz in Earth's field")

# Spin operators for spin 1/2, combined for electron 1, electron 2 and the nucleus (8 states)
sx, sy, sz = (np.array(m, dtype=complex) / 2 for m in ([[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]))
one = np.eye(2)
def op(a, b, c):
    return np.kron(np.kron(a, b), c)
spin = (sx, sy, sz)
S1 = [op(s, one, one) for s in spin]                     # electron 1
S2 = [op(one, s, one) for s in spin]                     # electron 2
S1_I = [op(s, one, s) for s in spin]                     # products S1x·Ix, S1y·Iy, S1z·Iz
singlet = 0.25 * np.eye(8) - sum(op(s, s, one) for s in spin)     # projector onto the singlet state


def singlet_yield(theta):
    """Fraction of radical pairs that react from the singlet state, field at angle theta to the molecule."""
    b = np.array([np.sin(theta), 0.0, np.cos(theta)])
    w = GAMMA_E * B_EARTH
    zeeman_h = w * sum(bi * (s1 + s2) for bi, s1, s2 in zip(b, S1, S2))
    hyperfine_h = GAMMA_E * HYPERFINE * sum(a * si for a, si in zip(ANISOTROPY, S1_I))
    energies, states = np.linalg.eigh(zeeman_h + hyperfine_h)
    p = np.einsum("im,ij,jn->mn", states.conj(), singlet, states)   # singlet projector in the eigenbasis
    k = 1 / LIFETIME
    omega = energies[:, None] - energies[None, :]
    return float(np.sum(np.abs(p) ** 2 * k**2 / (k**2 + omega**2)).real / 2)   # Tr(singlet) = 2


angles = np.radians(np.linspace(0, 180, 181))
yields = np.array([singlet_yield(a) for a in angles])
print(f"singlet yield: {yields[0]:.4f} along the field axis, {yields[90]:.4f} across it")
print(f"compass signal (max − min): {100 * (yields.max() - yields.min()):.2f} % of all pairs")
print(f"north and south look alike – yield at θ equals yield at 180° − θ to 12 digits: "
      f"{np.allclose(yields, yields[::-1], rtol=0, atol=1e-12)}")

plt.rcParams["font.size"] = 13      # large type: the chart stays readable on a phone
fig, ax = plt.subplots(figsize=(6.4, 5.0), layout="constrained")
ax.plot(np.degrees(angles), 100 * yields, lw=2.5)
ax.axvline(90, color="grey", ls=":", lw=1.5)
ax.set_xlabel("angle between Earth's field and the molecule (°)")
ax.set_ylabel("singlet yield (%)")
ax.set_xticks([0, 45, 90, 135, 180])
ax.set_title("Angle matters – north or south does not")
plt.show()
