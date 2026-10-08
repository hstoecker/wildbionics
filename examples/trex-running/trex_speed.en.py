# trex_speed.py – From “How Fast Was T. rex? Footprints, Bones and Physics”
# https://wildbionics.com/articles/trex-running/ · Code: MIT licence
# Needs: python3 -m pip install numpy matplotlib
# Run: python3 trex_speed.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt

# How fast was the maker of a fossil trackway? Speed from stride length and hip height.
G = 9.81                 # acceleration of gravity (m/s²)
HIP_TREX = 3.10          # hip height of the adult T. rex "Trix" (m), as used by van Bijlert et al.
HIP_HUMAN = 0.90         # hip height of an adult human (m) – assumed
UNCERTAINTY = 1.5        # mammal data scatter around the rule by factors up to 1.5
TRACKWAYS = {            # name: (stride length λ in m, hip height h in m)
    "tyrannosaurid trackway, straight leg": (3.46, 2.87),
    "tyrannosaurid trackway, bent leg": (3.46, 2.30),
    "same trackway scaled to T. rex": (3.88, HIP_TREX),   # scaled to the foot of "Trix" by van Bijlert et al.
    "human walking (assumed)": (1.40, HIP_HUMAN),
}
SIMULATED_TOP_SPEED = 8.0    # T. rex model limited by muscle only (m/s), leg length 3.089 m


def froude(speed, hip, g=G):
    """Froude number v²/(g·h): the 'speed number' that is equal for dynamically similar gaits."""
    return speed**2 / (g * hip)


def speed_from_trackway(stride, hip, g=G):
    """Alexander's rule for dynamically similar animals, λ/h ≈ 2.3·Fr^0.3, solved for v:
    Fr = (λ / 2.3h)^(1/0.3), v = √(Fr·g·h) ≈ 0.25·√g·λ^1.67·h^-1.17."""
    fr = (stride / (2.3 * hip)) ** (1 / 0.3)
    return np.sqrt(fr * g * hip)


def walking_limit(hip, g=G):
    """At Fr = 1 gravity can no longer hold the body on its arc over the foot: v = √(g·h)."""
    return np.sqrt(g * hip)


for name, (stride, hip) in TRACKWAYS.items():
    v = speed_from_trackway(stride, hip)
    print(f"{name}: λ/h = {stride / hip:.2f} → {v:.1f} m/s = {3.6 * v:.1f} km/h (Fr = {froude(v, hip):.2f})")

v_trex = speed_from_trackway(*TRACKWAYS["same trackway scaled to T. rex"])
print(f"with the scatter of the rule (×/÷ {UNCERTAINTY}), the scaled T. rex trackway gives "
      f"{3.6 * v_trex / UNCERTAINTY:.0f}–{3.6 * v_trex * UNCERTAINTY:.0f} km/h")
v_limit = walking_limit(HIP_TREX)
print(f"walking limit of T. rex (Fr = 1): {v_limit:.1f} m/s = {3.6 * v_limit:.0f} km/h")
print(f"muscle-only simulation: {SIMULATED_TOP_SPEED:.1f} m/s = {3.6 * SIMULATED_TOP_SPEED:.0f} km/h "
      f"(Fr = {froude(SIMULATED_TOP_SPEED, 3.089):.1f}) – a running gait")

plt.rcParams["font.size"] = 13      # large type: the chart stays readable on a phone
fig, ax = plt.subplots(figsize=(6.4, 6.0), layout="constrained")
for hip, label, color, style in ((HIP_TREX, "T. rex, h = 3.1 m", "#1f6f8b", "-"),
                                 (HIP_HUMAN, "human, h = 0.9 m", "#c0392b", "--")):
    stride = np.linspace(0.3, 9.0, 400)
    v = speed_from_trackway(stride, hip)
    walk = v <= walking_limit(hip)
    ax.plot(stride[walk], v[walk], lw=2.5, ls=style, color=color, label=label)
    ax.plot(stride[~walk], v[~walk], lw=1.5, ls=":", color=color)
    i = np.argmax(~walk)
    ax.plot(stride[i], v[i], "o", ms=7, mfc="white", color=color)
ax.text(7.5, 5.0, "Fr = 1:\nend of walking", va="top", ha="center", fontsize=11, color="#1f6f8b")
ax.text(2.1, 3.6, "Fr = 1", ha="center", fontsize=11, color="#c0392b")
for name, (stride, hip) in list(TRACKWAYS.items())[:3]:
    ax.plot(stride, speed_from_trackway(stride, hip), "s", ms=8, color="#c98a1b")
ax.annotate("tyrannosaurid\ntrackways", xy=(3.6, 2.2), xytext=(4.3, 0.6), color="#8a5a00",
            arrowprops=dict(arrowstyle="-", color="#8a5a00"))
ax.axhline(SIMULATED_TOP_SPEED, color="grey", lw=1, ls="-.")
ax.text(4.3, SIMULATED_TOP_SPEED + 0.2, "muscle-only T. rex model", fontsize=11, color="dimgrey")
ax.set_xlabel("stride length λ in the trackway (m)")
ax.set_ylabel("estimated speed (m/s)")
ax.set_xlim(0, 9.2)
ax.set_ylim(0, 10)
ax.set_title("The same stride means a stroll for T. rex")
ax.legend(loc="upper left", fontsize=11)
plt.show()
