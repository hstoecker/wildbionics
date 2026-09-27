# rayleigh_plesset.py – Aus „Der Knallkrebs und die Physik der Kavitation“
# https://wildbionics.com/de/artikel/knallkrebs-kavitation/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy scipy matplotlib
# Starten: python3 rayleigh_plesset.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Wasser bei 20 °C
RHO, P_INF, P_V = 998.0, 101_325.0, 2_339.0   # Dichte (kg/m³), Umgebungs- und Dampfdruck (Pa)
SIGMA, MU = 0.0728, 1.0e-3                    # Oberflächenspannung (N/m), Viskosität (Pa·s)
T0 = 293.0                                    # Temperatur des Wassers (K)

R_MAX = 3.0e-3        # größter Blasenradius (m)
GAMMA = 1.4           # Polytropenexponent des Gases

def collapse(p_gas):
    """Simuliert den Kollaps ab R_MAX; p_gas = Gasdruck in der Blase bei R_MAX (Pa)."""
    def rayleigh_plesset(t, y):
        R, dR = y
        p_wall = p_gas * (R_MAX / R) ** (3 * GAMMA) + P_V - 2 * SIGMA / R - 4 * MU * dR / R
        ddR = ((p_wall - P_INF) / RHO - 1.5 * dR**2) / R
        return [dR, ddR]

    def turnaround(t, y):    # Ereignis: Die Blasenwand bleibt stehen und kehrt um
        return y[1]
    turnaround.terminal, turnaround.direction = True, 1

    return solve_ivp(rayleigh_plesset, (0, 2e-3), [R_MAX, 0.0], method="LSODA",
                     events=turnaround, rtol=1e-10, atol=1e-13, max_step=1e-6)

rayleigh = 0.915 * R_MAX * np.sqrt(RHO / (P_INF - P_V))
print(f"Rayleigh-Formel (leere Blase): {rayleigh * 1e6:.0f} µs\n")
print("Gas (Pa)   Kollaps (µs)   R_min (µm)   max. Geschw. (m/s)   T_max (K)")

fig, (whole, end) = plt.subplots(1, 2, figsize=(10, 4), layout="constrained")
for p_gas in [10, 100, 1000]:     # wie viel Gas die Blase des Krebses enthält, hat niemand gemessen
    sol = collapse(p_gas)
    r_min, speed = sol.y[0, -1], np.abs(sol.y[1]).max()
    t_max = T0 * (R_MAX / r_min) ** (3 * (GAMMA - 1))    # adiabatische Erwärmung (Physik-Linse)
    print(f"{p_gas:8}   {sol.t[-1] * 1e6:12.0f}   {r_min * 1e6:10.1f}   {speed:18.0f}   {t_max:9.0f}")
    for ax in (whole, end):
        ax.plot(sol.t * 1e6, sol.y[0] * 1e6, label=f"{p_gas} Pa Gas")

for ax in (whole, end):
    ax.axvline(rayleigh * 1e6, color="grey", linestyle="--", label="Rayleigh-Formel")
    ax.set_xlabel("Zeit (µs)")
whole.set(ylabel="Blasenradius (µm)", title="Ganzer Kollaps: Die Kurven decken sich")
end.set(ylabel="Blasenradius (µm, logarithmisch)", xlim=(rayleigh * 1e6 - 4, rayleigh * 1e6 + 4),
        yscale="log", title="Letzte µs: Das Gas bestimmt, wie klein")
end.yaxis.set_major_formatter("{x:g}")
end.legend()
plt.show()
