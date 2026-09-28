# air_cushion.py – Aus „Der Lotuseffekt: Wie sich Blätter selbst reinigen“
# https://wildbionics.com/de/artikel/lotuseffekt/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy matplotlib
# Starten: python3 air_cushion.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt

# Wasser und Lotoswachs
SURFACE_TENSION = 0.072   # Oberflächenspannung von Wasser (N/m), bei etwa 25 °C
WATER_DENSITY = 1000      # Dichte von Wasser (kg/m³)
THETA_FLAT = 119          # Kontaktwinkel auf einem glatten Film aus Lotoswachs (Grad)
THETA_ADVANCING = 148     # Winkel, den eine Wasserfront erreichen muss, bevor sie übers Wachs kriecht (Grad)

# Die zwei Ebenen der Rauheit auf der Oberseite eines Lotosblatts
PAPILLA_PITCH = 22.6e-6   # Abstand benachbarter Papillenspitzen (m)
TUBULE_DENSITY = 200 / 10e-12   # Wachsröhrchen pro m² (200 pro 10 µm²)
TUBULE_DIAMETER = 100e-9  # Durchmesser eines Wachsröhrchens (m), gemessen 80–120 nm

# Drei Arten von Wasser, die auf das Luftpolster drücken
DROP_RADIUS = 1.5e-3      # ein Tropfen, der auf dem Blatt ruht (m)
RAIN_SPEED = 8.9          # Aufprallgeschwindigkeit eines großen Regentropfens, 4 mm Durchmesser (m/s)
MIST_RADIUS = 100e-9      # ein winziges Tröpfchen, z. B. aus Kondensation (m)


def cassie_angle(solid_fraction, theta_flat=THETA_FLAT):
    """Scheinbarer Kontaktwinkel, wenn Wasser nur die Spitzen berührt (Cassie-Baxter)."""
    cos_theta = solid_fraction * (np.cos(np.radians(theta_flat)) + 1) - 1
    return np.degrees(np.arccos(cos_theta))


def holding_pressure(gap):
    """Größter Druck (Pa), den eine Wasseroberfläche über einem Spalt aushält, bevor sie eindringt."""
    return 2 * SURFACE_TENSION * -np.cos(np.radians(THETA_ADVANCING)) / gap


# Wie viel Festkörper berührt ein Tropfen? Cassie-Baxter für die gemessenen 162° umkehren.
cos_flat = np.cos(np.radians(THETA_FLAT))
needed = (np.cos(np.radians(162)) + 1) / (cos_flat + 1)
tubule_tips = TUBULE_DENSITY * np.pi * (TUBULE_DIAMETER / 2) ** 2
print(f"glattes Wachs: {THETA_FLAT}°  →  gemessen auf dem Blatt: 162°")
print(f"nötiger Festkörperanteil für 162°: {needed:.3f} (Tropfen berührt {needed:.1%} der Fläche)")
print(f"nur die Spitzen der Wachsröhrchen:  {tubule_tips:.3f}  →  {cassie_angle(tubule_tips):.0f}°")
print()

# Wie viel Druck hält jede Ebene der Rauheit aus?
tubule_spacing = 1 / np.sqrt(TUBULE_DENSITY)
tubule_gap = tubule_spacing - TUBULE_DIAMETER
levels = {"Papillen": PAPILLA_PITCH, "Wachsröhrchen": tubule_gap}
threats = {
    "ruhender Tropfen": 2 * SURFACE_TENSION / DROP_RADIUS,
    "Regentropfen": WATER_DENSITY * RAIN_SPEED**2 / 2,
    "Nebeltröpfchen": 2 * SURFACE_TENSION / MIST_RADIUS,
}
print("Ebene           Spalt      hält bis zu")
for name, gap in levels.items():
    print(f"{name:13s} {gap * 1e6:7.2f} µm   {holding_pressure(gap) / 1e3:7.1f} kPa")
print()
print("Druck von            kPa     Papillen           Wachsröhrchen")
for name, pressure in threats.items():
    verdict = ["Luft hält" if holding_pressure(g) > pressure else "Wasser dringt ein" for g in levels.values()]
    print(f"{name:17s} {pressure / 1e3:7.1f}   {verdict[0]:18s} {verdict[1]}")
print()
largest_gap = 2 * SURFACE_TENSION * -np.cos(np.radians(THETA_ADVANCING)) / threats["Regentropfen"]
print(f"um dem Regentropfen standzuhalten, müssen Spalten kleiner sein als {largest_gap * 1e6:.1f} µm")
smallest_safe = tubule_gap / -np.cos(np.radians(THETA_ADVANCING))   # hier ist 2γ/r gleich dem Haltedruck
print(f"Tröpfchen mit einem Radius unter {smallest_safe * 1e6:.2f} µm können zwischen die Wachsröhrchen gelangen")

gaps = np.logspace(-8, -4, 200)        # 10 nm bis 100 µm
plt.rcParams["font.size"] = 13      # große Schrift: das Diagramm bleibt auf dem Handy lesbar
fig, ax = plt.subplots(figsize=(6.4, 5.2), layout="constrained")
ax.loglog(gaps * 1e6, holding_pressure(gaps) / 1e3, lw=2.5, label="Druck, den das Luftpolster hält")
for (name, gap), marker, offset in zip(levels.items(), ["s", "o"], [(10, 6), (-4, -24)]):
    ax.plot(gap * 1e6, holding_pressure(gap) / 1e3, marker, ms=10, color="C0")
    ax.annotate(name, (gap * 1e6, holding_pressure(gap) / 1e3), xytext=offset, textcoords="offset points")
for (name, pressure), style in zip(threats.items(), [":", "--", "-."]):
    ax.axhline(pressure / 1e3, color="C1", ls=style, lw=1.6)
    ax.text(90, pressure / 1e3 * 1.25, name, color="C1", ha="right")
ax.set_xlabel("Spalt zwischen den Strukturen (µm)")
ax.set_ylabel("Druck (kPa)")
ax.set_title("Nur die Nanoebene hält Regen stand")
ax.set_xlim(0.01, 100)
ax.set_ylim(0.03, 1e5)
ax.xaxis.set_major_formatter("{x:g}")   # einfache Zahlen: 0.01, 0.1, 1, 10
ax.yaxis.set_major_formatter("{x:g}")
ax.legend(loc="upper right")
plt.show()
