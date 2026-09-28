# range_resolution.py – From “How Bats See with Sound: Echolocation Explained”
# https://wildbionics.com/articles/bat-echolocation/ · Code: MIT licence
# Needs: python3 -m pip install numpy scipy matplotlib
# Run: python3 range_resolution.py   (https://wildbionics.com/run-code/)

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate, find_peaks, hilbert

SPEED_OF_SOUND = 343.0    # m/s, air at 20 °C
RATE = 500_000            # samples per second
CALL_TIME = 2e-3          # call duration (s)
F_START = 80e3            # the sweep starts at 80 kHz …
F_END = 40e3              # … and ends at 40 kHz
F_TONE = 60e3             # the pure tone sits in the middle (Hz)
TARGETS = [1.50, 1.55]    # a moth and a leaf just behind it (m)
NOISE = 0.3               # noise level relative to the echoes


def sweep(t):
    """Frequency-modulated call: the pitch falls linearly from F_START to F_END."""
    rate_of_change = (F_END - F_START) / CALL_TIME           # Hz per second
    return np.sin(2 * np.pi * (F_START * t + rate_of_change * t**2 / 2))


def tone(t):
    """Constant-frequency call of the same duration."""
    return np.sin(2 * np.pi * F_TONE * t)


def record(call, rng):
    """20 ms of noise with one echo per target, each delayed by its round trip."""
    recording = rng.normal(0, NOISE, int(0.02 * RATE))
    for distance in TARGETS:
        start = round(2 * distance / SPEED_OF_SOUND * RATE)
        recording[start:start + call.size] += call
    return recording


def matched_filter(call, recording):
    """Slide the call along the recording; the envelope peaks where an echo starts."""
    return np.abs(hilbert(correlate(recording, call, mode="valid")))


t = np.arange(0, CALL_TIME, 1 / RATE)
window = np.hanning(t.size)               # soft start and end, as in a real call
calls = {"sweep": sweep(t) * window, "tone": tone(t) * window}
rng = np.random.default_rng(1)
metres = np.arange(int(0.02 * RATE) - t.size + 1) / RATE * SPEED_OF_SOUND / 2

bandwidths = {"sweep": abs(F_START - F_END), "tone": 1 / CALL_TIME}
envelopes = {}
for name, call in calls.items():
    envelope = matched_filter(call, record(call, rng))
    envelopes[name] = envelope / envelope.max()
    peaks, _ = find_peaks(envelopes[name], height=0.5, prominence=0.2)
    resolution = SPEED_OF_SOUND / (2 * bandwidths[name])
    print(f"{name}: bandwidth {bandwidths[name] / 1e3:.1f} kHz, "
          f"range resolution about {resolution * 100:.1f} cm")
    found = ", ".join(f"{metres[p]:.2f} m" for p in peaks)
    if len(peaks) == len(TARGETS):
        error = max(abs(metres[p] - d) for p, d in zip(peaks, TARGETS))
        print(f"  {len(peaks)} echoes at {found}, largest error {error * 100:.1f} cm")
    else:
        print(f"  {len(peaks)} echo(es) at {found} instead of {len(TARGETS)}")
print(f"targets: {', '.join(f'{d:.2f} m' for d in TARGETS)}")
print("bats tell apart range differences of 1–3 cm (Simmons 1973)")

plt.rcParams["font.size"] = 13      # large type: the chart stays readable on a phone
fig, axes = plt.subplots(2, 1, figsize=(6.4, 7.6), sharex=True, layout="constrained")
titles = {"sweep": f"Sweep {F_START / 1e3:.0f} → {F_END / 1e3:.0f} kHz",
          "tone": f"Pure tone {F_TONE / 1e3:.0f} kHz"}
for ax, name in zip(axes, calls):
    ax.plot(metres, envelopes[name], lw=2)
    for distance in TARGETS:
        ax.axvline(distance, color="gray", lw=1, ls=":")
    ax.set_title(titles[name], loc="left", fontsize=13)
    ax.set_ylabel("matched filter output")
    ax.set_ylim(0, 1.1)
axes[0].text(TARGETS[-1] + 0.02, 0.85, "dotted:\ntrue targets", color="dimgray", fontsize=11)
axes[-1].set_xlabel("distance (m)")
axes[-1].set_xlim(1.2, 1.85)
fig.suptitle("A sweep separates two echoes, a tone cannot")
plt.show()
