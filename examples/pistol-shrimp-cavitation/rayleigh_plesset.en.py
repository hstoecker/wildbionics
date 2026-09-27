# rayleigh_plesset.py – From “The Pistol Shrimp and the Physics of Cavitation”
# https://wildbionics.com/articles/pistol-shrimp-cavitation/ · Code: MIT licence
# Needs: python3 -m pip install numpy scipy matplotlib
# Run: python3 rayleigh_plesset.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Water at 20 °C
RHO, P_INF, P_V = 998.0, 101_325.0, 2_339.0   # density (kg/m³), ambient and vapour pressure (Pa)
SIGMA, MU = 0.0728, 1.0e-3                    # surface tension (N/m), viscosity (Pa·s)
T0 = 293.0                                    # temperature of the water (K)

R_MAX = 3.0e-3        # bubble radius at its largest (m)
GAMMA = 1.4           # polytropic exponent of the gas
C_WATER = 1482.0      # speed of sound in water (m/s)

def collapse(p_gas):
    """Simulate the collapse from R_MAX; p_gas = gas pressure in the bubble at R_MAX (Pa)."""
    def rayleigh_plesset(t, y):
        R, dR = y
        p_wall = p_gas * (R_MAX / R) ** (3 * GAMMA) + P_V - 2 * SIGMA / R - 4 * MU * dR / R
        ddR = ((p_wall - P_INF) / RHO - 1.5 * dR**2) / R
        return [dR, ddR]

    def turnaround(t, y):    # event: the bubble wall stops and turns around
        return y[1]
    turnaround.terminal, turnaround.direction = True, 1

    return solve_ivp(rayleigh_plesset, (0, 2e-3), [R_MAX, 0.0], method="LSODA",
                     events=turnaround, rtol=1e-10, atol=1e-13, max_step=1e-6)

rayleigh = 0.915 * R_MAX * np.sqrt(RHO / (P_INF - P_V))
print(f"Rayleigh's formula (empty bubble): {rayleigh * 1e6:.0f} µs\n")
print("gas (Pa)   collapse (µs)   R_min (µm)   max. speed (km/s)   T_max (1000 K)")

fig, (whole, end) = plt.subplots(1, 2, figsize=(10, 4), layout="constrained")
for p_gas in [10, 100, 1000]:     # nobody has measured how much gas the shrimp's bubble holds
    sol = collapse(p_gas)
    r_min, speed = sol.y[0, -1], np.abs(sol.y[1]).max()
    t_max = T0 * (R_MAX / r_min) ** (3 * (GAMMA - 1))    # adiabatic heating (physics lens)
    print(f"{p_gas:8}   {sol.t[-1] * 1e6:13.0f}   {r_min * 1e6:10.1f}   {speed / 1e3:17.1f}   {t_max / 1e3:14,.1f}")
    t_us, r_um = sol.t * 1e6, sol.y[0] * 1e6
    fast = np.abs(sol.y[1]) > C_WATER         # wall faster than sound: the model no longer holds
    i = np.argmax(fast) if fast.any() else len(fast)
    for ax in (whole, end):
        line, = ax.plot(t_us[:i + 1], r_um[:i + 1])
        ax.plot(t_us[i:], r_um[i:], ":", color=line.get_color())
    end.annotate(f"{p_gas} Pa", (t_us[-1], r_um[-1]), xytext=(5, 0), textcoords="offset points",
                 va="center", backgroundcolor="white")

for ax in (whole, end):
    ax.axvline(rayleigh * 1e6, color="grey", linestyle="--", label="Rayleigh's formula")
    ax.set_xlabel("time (µs)")
whole.plot([], [], ":", color="grey", label="wall faster than sound: model not valid")
whole.set(ylabel="bubble radius (µm)", title="The whole collapse: the curves overlap")
whole.legend(loc="lower left")
end.set(ylabel="bubble radius (µm, log scale)", xlim=(rayleigh * 1e6 - 4, rayleigh * 1e6 + 5), yscale="log",
        title="Last microseconds: the model reaches its limit")
end.yaxis.set_major_formatter("{x:g}")
plt.show()
