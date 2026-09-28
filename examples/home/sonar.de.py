# sonar.py – Aus der WildBionics-Startseite
# https://wildbionics.com/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy
# Starten: python3 sonar.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np

SPEED_OF_SOUND = 343.0  # m/s, Luft bei 20 °C

def echo_distance(chirp, recording, sample_rate):
    """Echo mit einem Optimalfilter finden; Entfernung in Metern."""
    corr = np.correlate(recording, chirp, mode="valid")
    delay = np.argmax(np.abs(corr)) / sample_rate  # Hin- und Rückweg, s
    return SPEED_OF_SOUND * delay / 2

# Demo: ein 2 ms langer Ruf von 80 → 40 kHz, Echo einer Motte in 1,7 m Entfernung
rate = 250_000                                   # Abtastwerte pro Sekunde
t = np.arange(0, 0.002, 1 / rate)
chirp = np.sin(2 * np.pi * (80_000 * t - 1e7 * t**2))
recording = np.random.default_rng(1).normal(0, 1, 5_000)  # 20 ms Rauschen
start = round(2 * 1.7 / SPEED_OF_SOUND * rate)
recording[start:start + chirp.size] += 0.5 * chirp  # Echo schwächer als das Rauschen
print(f"Motte in {echo_distance(chirp, recording, rate):.2f} m Entfernung")
