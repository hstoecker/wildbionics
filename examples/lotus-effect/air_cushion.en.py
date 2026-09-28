# air_cushion.py – From “The Lotus Effect: How Leaves Clean Themselves”
# https://wildbionics.com/articles/lotus-effect/ · Code: MIT licence
# Needs: python3 -m pip install numpy matplotlib
# Run: python3 air_cushion.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt

# Water and lotus wax
SURFACE_TENSION = 0.072   # surface tension of water (N/m), at about 25 °C
WATER_DENSITY = 1000      # density of water (kg/m³)
THETA_FLAT = 119          # contact angle on a flat film of lotus wax (degrees)
THETA_ADVANCING = 148     # angle a water front must reach before it creeps along the wax (degrees)

# The two levels of roughness on the upper side of a lotus leaf
PAPILLA_PITCH = 22.6e-6   # distance between neighbouring papilla tips (m)
TUBULE_DENSITY = 200 / 10e-12   # wax tubules per m² (200 per 10 µm²)
TUBULE_DIAMETER = 100e-9  # diameter of a wax tubule (m), measured 80–120 nm

# Three kinds of water that press on the air cushion
DROP_RADIUS = 1.5e-3      # a drop resting on the leaf (m)
RAIN_SPEED = 8.9          # impact speed of a large raindrop, 4 mm across (m/s)
MIST_RADIUS = 100e-9      # a tiny droplet, e.g. from condensation (m)


def cassie_angle(solid_fraction, theta_flat=THETA_FLAT):
    """Apparent contact angle when water touches only the tips (Cassie–Baxter)."""
    cos_theta = solid_fraction * (np.cos(np.radians(theta_flat)) + 1) - 1
    return np.degrees(np.arccos(cos_theta))


def holding_pressure(gap):
    """Largest pressure (Pa) a water surface spanning a gap can take before it slips in."""
    return 2 * SURFACE_TENSION * -np.cos(np.radians(THETA_ADVANCING)) / gap


# How much solid does a drop touch? Invert Cassie–Baxter for the measured 162°.
cos_flat = np.cos(np.radians(THETA_FLAT))
needed = (np.cos(np.radians(162)) + 1) / (cos_flat + 1)
tubule_tips = TUBULE_DENSITY * np.pi * (TUBULE_DIAMETER / 2) ** 2
print(f"flat wax: {THETA_FLAT}°  →  measured on the leaf: 162°")
print(f"solid fraction needed for 162°: {needed:.3f} (drop touches {needed:.1%} of the area)")
print(f"tips of the wax tubules alone:  {tubule_tips:.3f}  →  {cassie_angle(tubule_tips):.0f}°")
print()

# How much pressure can each level of roughness hold?
tubule_spacing = 1 / np.sqrt(TUBULE_DENSITY)
tubule_gap = tubule_spacing - TUBULE_DIAMETER
levels = {"papillae": PAPILLA_PITCH, "wax tubules": tubule_gap}
threats = {
    "resting drop": 2 * SURFACE_TENSION / DROP_RADIUS,
    "raindrop impact": WATER_DENSITY * RAIN_SPEED**2 / 2,
    "mist droplet": 2 * SURFACE_TENSION / MIST_RADIUS,
}
print("level          gap        holds up to")
for name, gap in levels.items():
    print(f"{name:12s} {gap * 1e6:7.2f} µm   {holding_pressure(gap) / 1e3:7.1f} kPa")
print()
print("pressure from       kPa     papillae   wax tubules")
for name, pressure in threats.items():
    verdict = ["air holds" if holding_pressure(g) > pressure else "water in" for g in levels.values()]
    print(f"{name:16s} {pressure / 1e3:7.1f}   {verdict[0]:10s} {verdict[1]}")
print()
largest_gap = 2 * SURFACE_TENSION * -np.cos(np.radians(THETA_ADVANCING)) / threats["raindrop impact"]
print(f"to resist the raindrop, gaps must be smaller than {largest_gap * 1e6:.1f} µm")
smallest_safe = tubule_gap / -np.cos(np.radians(THETA_ADVANCING))   # where 2γ/r equals the holding pressure
print(f"droplets with a radius below {smallest_safe * 1e6:.2f} µm can slip between the wax tubules")

gaps = np.logspace(-8, -4, 200)        # 10 nm to 100 µm
plt.rcParams["font.size"] = 13      # large type: the chart stays readable on a phone
fig, ax = plt.subplots(figsize=(6.4, 5.2), layout="constrained")
ax.loglog(gaps * 1e6, holding_pressure(gaps) / 1e3, lw=2.5, label="pressure the air cushion holds")
for (name, gap), marker, offset in zip(levels.items(), ["s", "o"], [(10, 6), (-4, -24)]):
    ax.plot(gap * 1e6, holding_pressure(gap) / 1e3, marker, ms=10, color="C0")
    ax.annotate(name, (gap * 1e6, holding_pressure(gap) / 1e3), xytext=offset, textcoords="offset points")
for (name, pressure), style in zip(threats.items(), [":", "--", "-."]):
    ax.axhline(pressure / 1e3, color="C1", ls=style, lw=1.6)
    ax.text(90, pressure / 1e3 * 1.25, name, color="C1", ha="right")
ax.set_xlabel("gap between the structures (µm)")
ax.set_ylabel("pressure (kPa)")
ax.set_title("Only the nano level resists rain")
ax.set_xlim(0.01, 100)
ax.set_ylim(0.03, 1e5)
ax.xaxis.set_major_formatter("{x:g}")   # plain numbers: 0.01, 0.1, 1, 10
ax.yaxis.set_major_formatter("{x:g}")
ax.legend(loc="upper right")
plt.show()
