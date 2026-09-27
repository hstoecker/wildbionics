# sonar.py – From the WildBionics home page
# https://wildbionics.com/ · Code: MIT licence
# Needs: python3 -m pip install numpy
# Run: python3 sonar.py   (https://wildbionics.com/run-code/)

import numpy as np

SPEED_OF_SOUND = 343.0  # m/s, air at 20 °C

def echo_distance(chirp, recording, sample_rate):
    """Find the echo with a matched filter; return metres."""
    corr = np.correlate(recording, chirp, mode="valid")
    delay = np.argmax(np.abs(corr)) / sample_rate  # round trip, s
    return SPEED_OF_SOUND * delay / 2

# Demo: a 2 ms call sweeping 80 → 40 kHz, echo from a moth 1.7 m away
rate = 250_000                                   # samples per second
t = np.arange(0, 0.002, 1 / rate)
chirp = np.sin(2 * np.pi * (80_000 * t - 1e7 * t**2))
recording = np.random.default_rng(1).normal(0, 1, 5_000)  # 20 ms of noise
start = round(2 * 1.7 / SPEED_OF_SOUND * rate)
recording[start:start + chirp.size] += 0.5 * chirp  # echo weaker than the noise
print(f"moth at {echo_distance(chirp, recording, rate):.2f} m")
