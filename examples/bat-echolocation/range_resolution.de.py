# range_resolution.py – Aus „Wie Fledermäuse mit Schall sehen: Echoortung erklärt“
# https://wildbionics.com/de/artikel/echoortung-fledermaeuse/ · Code: MIT-Lizenz
# Braucht: python3 -m pip install numpy scipy matplotlib
# Starten: python3 range_resolution.py   (https://wildbionics.com/de/code-ausfuehren/)

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate, find_peaks, hilbert

SPEED_OF_SOUND = 343.0    # m/s, Luft bei 20 °C
RATE = 500_000            # Abtastwerte pro Sekunde
CALL_TIME = 2e-3          # Dauer eines Rufs (s)
F_START = 80e3            # der Sweep beginnt bei 80 kHz …
F_END = 40e3              # … und endet bei 40 kHz
F_TONE = 60e3             # der reine Ton liegt in der Mitte (Hz)
TARGETS = [1.50, 1.55]    # eine Motte und ein Blatt kurz dahinter (m)
NOISE = 0.3               # Rauschpegel im Verhältnis zu den Echos


def sweep(t):
    """Frequenzmodulierter Ruf: Die Tonhöhe fällt linear von F_START auf F_END."""
    rate_of_change = (F_END - F_START) / CALL_TIME           # Hz pro Sekunde
    return np.sin(2 * np.pi * (F_START * t + rate_of_change * t**2 / 2))


def tone(t):
    """Ruf mit konstanter Frequenz und gleicher Dauer."""
    return np.sin(2 * np.pi * F_TONE * t)


def record(call, rng):
    """20 ms Rauschen mit einem Echo pro Ziel, jeweils um den Hin- und Rückweg verzögert."""
    recording = rng.normal(0, NOISE, int(0.02 * RATE))
    for distance in TARGETS:
        start = round(2 * distance / SPEED_OF_SOUND * RATE)
        recording[start:start + call.size] += call
    return recording


def matched_filter(call, recording):
    """Den Ruf über die Aufnahme schieben; die Einhüllende hat dort ein Maximum, wo ein Echo beginnt."""
    return np.abs(hilbert(correlate(recording, call, mode="valid")))


t = np.arange(0, CALL_TIME, 1 / RATE)
window = np.hanning(t.size)               # weicher Anfang und weiches Ende wie bei einem echten Ruf
calls = {"Sweep": sweep(t) * window, "Ton": tone(t) * window}
rng = np.random.default_rng(1)
metres = np.arange(int(0.02 * RATE) - t.size + 1) / RATE * SPEED_OF_SOUND / 2

bandwidths = {"Sweep": abs(F_START - F_END), "Ton": 1 / CALL_TIME}
envelopes = {}
for name, call in calls.items():
    envelope = matched_filter(call, record(call, rng))
    envelopes[name] = envelope / envelope.max()
    peaks, _ = find_peaks(envelopes[name], height=0.5, prominence=0.2)
    resolution = SPEED_OF_SOUND / (2 * bandwidths[name])
    print(f"{name}: Bandbreite {bandwidths[name] / 1e3:.1f} kHz, "
          f"Entfernungsauflösung etwa {resolution * 100:.1f} cm")
    found = ", ".join(f"{metres[p]:.2f} m" for p in peaks)
    if len(peaks) == len(TARGETS):
        error = max(abs(metres[p] - d) for p, d in zip(peaks, TARGETS))
        print(f"  {len(peaks)} Echos bei {found}, größter Fehler {error * 100:.1f} cm")
    else:
        print(f"  {len(peaks)} Echo(s) bei {found} statt {len(TARGETS)}")
print(f"Ziele: {', '.join(f'{d:.2f} m' for d in TARGETS)}")
print("Fledermäuse unterscheiden Entfernungen, die 1–3 cm auseinanderliegen (Simmons 1973)")

plt.rcParams["font.size"] = 13      # große Schrift: Das Diagramm bleibt auf dem Handy lesbar
fig, axes = plt.subplots(2, 1, figsize=(6.4, 7.6), sharex=True, layout="constrained")
titles = {"Sweep": f"Sweep {F_START / 1e3:.0f} → {F_END / 1e3:.0f} kHz",
          "Ton": f"Reiner Ton {F_TONE / 1e3:.0f} kHz"}
for ax, name in zip(axes, calls):
    ax.plot(metres, envelopes[name], lw=2)
    for distance in TARGETS:
        ax.axvline(distance, color="gray", lw=1, ls=":")
    ax.set_title(titles[name], loc="left", fontsize=13)
    ax.set_ylabel("Ausgang Optimalfilter")
    ax.set_ylim(0, 1.1)
axes[0].text(TARGETS[-1] + 0.02, 0.85, "gepunktet:\nwahre Ziele", color="dimgray", fontsize=11)
axes[-1].set_xlabel("Entfernung (m)")
axes[-1].set_xlim(1.2, 1.85)
fig.suptitle("Ein Sweep trennt zwei Echos, ein Ton nicht")
plt.show()
