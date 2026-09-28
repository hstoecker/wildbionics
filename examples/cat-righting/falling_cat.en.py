# falling_cat.py – From “How Cats Land on Their Feet: Angular Momentum Explained”
# https://wildbionics.com/articles/cat-righting/ · Code: MIT licence
# Needs: python3 -m pip install numpy matplotlib
# Run: python3 falling_cat.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt

# Two halves of the cat turn about the same axis (the spine), in the "tuck and turn" model.
I_TUCKED = 1.0      # moment of inertia of a half with its legs pulled in (relative units)
I_EXTENDED = 3.0    # the same half with its legs stretched out – assumed 3 times larger
TWIST = 180.0       # how far the front half twists against the rear half in each step (degrees)
STEP_TIME = 0.1     # duration of one twist (s), assumed
G = 9.81            # gravitational acceleration (m/s²)


def twist(i_front, i_rear, d_relative):
    """Twist the halves against each other by d_relative with zero total angular momentum.
    I_f·Δθ_f + I_r·Δθ_r = 0 and Δθ_f − Δθ_r = d_relative give each half's rotation."""
    d_front = d_relative * i_rear / (i_front + i_rear)
    d_rear = -d_relative * i_front / (i_front + i_rear)
    return d_front, d_rear


# One cycle: (1) front legs tucked, twist the front half; (2) rear legs tucked, untwist.
steps = [(I_TUCKED, I_EXTENDED, +TWIST), (I_EXTENDED, I_TUCKED, -TWIST)]
front, rear, time = [0.0], [0.0], [0.0]
largest_momentum = 0.0
for cycle in range(2):
    for i_front, i_rear, d_relative in steps:
        for _ in range(50):                     # each twist in 50 small steps
            d_front, d_rear = twist(i_front, i_rear, d_relative / 50)
            rate_front, rate_rear = d_front / (STEP_TIME / 50), d_rear / (STEP_TIME / 50)
            largest_momentum = max(largest_momentum, abs(i_front * rate_front + i_rear * rate_rear))
            front.append(front[-1] + d_front)
            rear.append(rear[-1] + d_rear)
            time.append(time[-1] + STEP_TIME / 50)

per_cycle = front[100]
print(f"largest total angular momentum during the turn: {largest_momentum:.3f}")
if abs(per_cycle) < 1e-6:
    print("turn per cycle: 0° – without changing shape the cat cannot turn")
else:
    cycles = 180.0 / per_cycle
    fall_time = cycles * 2 * STEP_TIME
    print(f"turn per cycle: {per_cycle:.1f}° (front and rear half alike)")
    print(f"cycles needed to land on its feet (180°): {cycles:.1f}")
    print(f"time needed: {fall_time:.2f} s  →  it falls {0.5 * G * fall_time**2 * 100:.0f} cm meanwhile")

time = np.array(time)
plt.rcParams["font.size"] = 13      # large type: the chart stays readable on a phone
fig, ax = plt.subplots(figsize=(6.4, 5.2), layout="constrained")
for k in range(4):                      # shade the steps in which the front legs are tucked
    if k % 2 == 0:
        ax.axvspan(k * STEP_TIME, (k + 1) * STEP_TIME, color="0.92")
ax.plot(time, front, lw=2.5, label="front half")
ax.plot(time, rear, "--", lw=2.5, label="rear half")
ax.axhline(180, color="gray", lw=1, ls=":")
ax.text(0.005, 186, "feet down (180°)", color="dimgray", fontsize=11)
ax.text(0.205, -52, "grey: front legs\ntucked", color="dimgray", fontsize=11)
ax.set_xlabel("time (s)")
ax.set_ylabel("rotation about the spine (degrees)")
ax.set_title("Changing shape turns the cat – with zero spin")
ax.set_ylim(-60, 230)
ax.legend(loc="lower right")
plt.show()
