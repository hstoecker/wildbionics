# lapping.py – From “How Cats Drink: Inertia Against Gravity”
# https://wildbionics.com/articles/cat-lapping/ · Code: MIT licence
# Needs: python3 -m pip install numpy matplotlib
# Run: python3 lapping.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt

# Typical body masses (kg) – rough values for illustration, not measurements
CATS = {"domestic cat": 4, "ocelot": 11, "cheetah": 45, "jaguar": 80, "lion": 190, "tiger": 220}
EXPONENT = -1 / 6     # frequency ∝ mass^EXPONENT: inertia balancing gravity (see the maths lens)


def relative_frequency(mass, reference=CATS["domestic cat"]):
    """Lapping frequency relative to a domestic cat.

    Inertia balances gravity when the tongue speed U is about √(g·R) (Froude number ≈ 1),
    so one lap takes a time of order R/U = √(R/g). The tongue radius R grows like mass^(1/3)
    for animals of similar shape, hence frequency ∝ √(g/R) ∝ mass^(−1/6).
    """
    return (mass / reference) ** EXPONENT


print("animal          mass    laps relative to a domestic cat")
for name, mass in CATS.items():
    print(f"{name:13s} {mass:5d} kg   {relative_frequency(mass):5.2f}")
lion = relative_frequency(CATS["lion"])
print(f"a lion is {CATS['lion'] / CATS['domestic cat']:.1f} times heavier "
      f"but laps only {1 / lion:.1f} times slower")

masses = np.logspace(0, 2.6, 100)
plt.rcParams["font.size"] = 13      # large type: the chart stays readable on a phone
fig, ax = plt.subplots(figsize=(6.4, 5.2), layout="constrained")
ax.loglog(masses, relative_frequency(masses), lw=2.5, label="inertia vs. gravity: mass^(−1/6)")
ax.loglog(masses, (masses / CATS["domestic cat"]) ** (-1 / 3), "--", lw=1.8,
          label="if speed did not grow: mass^(−1/3)")
for name, mass in CATS.items():
    below = name == "tiger"             # lion and tiger are close: one label above, one below
    ax.plot(mass, relative_frequency(mass), "o", ms=7, color="black")
    ax.annotate(name, (mass, relative_frequency(mass)), textcoords="offset points",
                xytext=(-10, -20) if below else (6, 6), fontsize=11)
ax.set_xlabel("body mass (kg)")
ax.set_ylabel("laps per second (domestic cat = 1)")
ax.set_title("Bigger cats lap only a little slower")
ax.set_ylim(0.15, 2.5)
ax.set_yticks([0.2, 0.3, 0.5, 1, 2])
ax.xaxis.set_major_formatter("{x:g}")   # plain numbers: 1, 10, 100
ax.yaxis.set_major_formatter("{x:g}")
ax.legend(loc="lower left")
plt.show()
