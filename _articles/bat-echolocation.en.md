---
id: bat-echolocation
lang: en
ref: bat-echolocation
title: "How Bats See with Sound: Echolocation Explained"
short_title: "Bat echolocation"
kicker: "Article · Acoustics"
description: "Bats hunt in the dark by shouting ultrasound and listening to the echoes: the delay gives the distance, the pitch shift the speed of their prey."
dek: "An insect-eating bat sends out up to 200 ultrasonic calls per second and builds a picture of its surroundings from the echoes. The same physics – echo delay, bandwidth, Doppler shift – now guides robots that find their way by sound."
date: 2026-09-28
permalink: /articles/bat-echolocation/
image: /assets/og/bat-echolocation-en.jpg
image_alt: "Schematic of a bat closing in on a moth: along its flight path the echolocation calls become more and more frequent, from the search phase to the final buzz."
hero_figure: svg/bat-hunt.svg
hero_caption: "<span class=\"caption__label\">Fig. 1</span> An insect-eating bat hunting a moth. While searching, bats often call 5–20 times per second, for example every 100 ms. Once they have detected prey, they call faster and faster, ending in a feeding buzz of up to about 200 calls per second. The timeline below shows each call as a tick."
educational_level: "Intermediate"
keywords: ["bat", "echolocation", "biosonar", "ultrasound", "big brown bat", "Eptesicus fuscus", "feeding buzz", "Doppler shift", "Doppler shift compensation", "matched filter", "range resolution", "frequency-modulated chirp", "tiger moth", "sonar jamming", "Robat", "BatSLAM", "bionics"]
about:
  - { name: "Animal echolocation", wikidata: Q6921783, wikipedia: "https://en.wikipedia.org/wiki/Animal_echolocation" }
  - { name: "Bats (Chiroptera)", wikidata: Q28425, wikipedia: "https://en.wikipedia.org/wiki/Bat" }
mentions:
  - { name: "Big brown bat", wikidata: Q301254 }
  - { name: "Bertholdia trigona", wikidata: Q13403125 }
  - { name: "Horseshoe bats", wikidata: Q830900 }
  - { name: "Doppler effect", wikidata: Q76436 }
  - { name: "Matched filter", wikidata: Q1759577 }
  - { name: "Simultaneous localization and mapping", wikidata: Q1203659 }
dimensions:
  time: ["cenozoic", "modern-era"]
  space: ["forest", "lab"]
  physics: ["acoustics"]
  adjacent_sciences: ["biology", "mathematics", "computer-science", "artificial-intelligence", "robotics", "physical-ai", "bionics"]
beings: ["big-brown-bat", "tiger-moth"]
lenses: ["biology", "physics", "math", "cs", "physical-ai"]
key_facts:
  - "Bat echolocation calls range from about **11 kHz to 212 kHz**; most insect-eating bats call between 20 and 60 kHz – above the range of human hearing [2](#ref-2){:.cite}."
  - "Bat calls are among the **most intense airborne sounds of any animal** [2](#ref-2){:.cite}: bats that hunt over water reach average source levels of about 137 dB SPL, with maxima above **140 dB SPL** [3](#ref-3){:.cite}."
  - "In Simmons' classic experiments, big brown bats and three other species told apart targets whose distances differed by only **1–3 cm** [4](#ref-4){:.cite}."
  - "When closing in on prey, a bat calls faster and faster – in the final **feeding buzz** up to about 200 calls per second [2](#ref-2){:.cite}."
  - "Horseshoe bats lower their call frequency the faster they fly, so that the Doppler-shifted echo returns consistently at the frequency they hear best [2](#ref-2){:.cite} [10](#ref-10){:.cite}."
  - "The tiger moth *Bertholdia trigona* **jams the sonar** of attacking big brown bats with ultrasonic clicks [9](#ref-9){:.cite}."
  - "Robots with one ultrasonic speaker and two microphones have mapped offices and greenhouses by sound, combining the echoes with their own movement data [11](#ref-11){:.cite} [5](#ref-5){:.cite}."
faq:
  - q: "How does bat echolocation work?"
    a: "A bat produces short, loud calls in its larynx and emits them through its mouth or nose. The sound bounces off objects, and the bat listens to the returning echoes with its large ears. The delay of an echo tells it how far away an object is, the difference between its two ears tells it the direction, and changes in the echo's pitch and loudness reveal whether the object moves and how large it is."
  - q: "Why can't humans hear bats?"
    a: "Most bat calls are ultrasound. Bat echolocation calls range from about 11 to 212 kilohertz, and most insect-eating bats call between 20 and 60 kilohertz. Human hearing ends at around 20 kilohertz, so we hear at most the lowest calls of a few species. A bat detector makes the calls audible by shifting them down in frequency."
  - q: "How loud are bats?"
    a: "Very loud. Annemarie Surlykke and Elisabeth Kalko measured wild bats in Panama: open-space and edge-space hunters reached source levels of 122 to 134 decibels, and two species that hunt over water averaged about 137 decibels, with maxima above 140 decibels. Such values, measured 10 centimetres in front of the bat, are among the most intense airborne sounds any animal makes. We do not hear them only because they are ultrasonic."
  - q: "How precisely can a bat measure distance?"
    a: "In discrimination experiments, James Simmons found that four species of bats, including the big brown bat, can tell apart two targets whose distances differ by only 1 to 3 centimetres. Big brown bats use the arrival time of the echoes for this. A call that sweeps over a wide range of frequencies makes this precision possible."
  - q: "Can moths defend themselves against bats?"
    a: "Yes. Many moths have ears that detect bat calls and trigger evasive flight. Some tiger moths answer an attack with ultrasonic clicks: they warn the bat that they taste bad, some harmless species mimic these warnings, and the tiger moth Bertholdia trigona uses its clicks to jam the sonar of big brown bats."
  - q: "Are there robots that use echolocation like bats?"
    a: "Yes. BatSLAM, built by Jan Steckel and Herbert Peremans, is a mobile robot with a bat-like sonar head that maps office environments from its echoes combined with its own movement data. The Robat from Tel Aviv University moves autonomously through greenhouses with one ultrasonic speaker and two microphones, maps obstacles and uses a neural network to tell plants from other objects."
sources:
  - authors: ["Griffin, D. R."]
    year: 1944
    title: "Echolocation by blind men, bats and radar"
    journal: "Science"
    volume: 100
    pages: "589–590"
    doi: "10.1126/science.100.2609.589"
  - authors: ["Jones, G.", "Holderied, M. W."]
    year: 2007
    title: "Bat echolocation calls: adaptation and convergent evolution"
    journal: "Proceedings of the Royal Society B: Biological Sciences"
    volume: 274
    pages: "905–912"
    doi: "10.1098/rspb.2006.0200"
    open_access: true
  - authors: ["Surlykke, A.", "Kalko, E. K. V."]
    year: 2008
    title: "Echolocating bats cry out loud to detect their prey"
    journal: "PLoS ONE"
    volume: 3
    pages: "e2036"
    doi: "10.1371/journal.pone.0002036"
    open_access: true
  - authors: ["Simmons, J. A."]
    year: 1973
    title: "The resolution of target range by echolocating bats"
    journal: "Journal of the Acoustical Society of America"
    volume: 54
    pages: "157–173"
    doi: "10.1121/1.1913559"
  - authors: ["Eliakim, I.", "Cohen, Z.", "Kosa, G.", "Yovel, Y."]
    year: 2018
    title: "A fully autonomous terrestrial bat-like acoustic robot"
    journal: "PLOS Computational Biology"
    volume: 14
    pages: "e1006406"
    doi: "10.1371/journal.pcbi.1006406"
    open_access: true
  - authors: ["Simmons, J. A.", "Fenton, M. B.", "O'Farrell, M. J."]
    year: 1979
    title: "Echolocation and pursuit of prey by bats"
    journal: "Science"
    volume: 203
    pages: "16–21"
    doi: "10.1126/science.758674"
  - authors: ["ter Hofstede, H. M.", "Ratcliffe, J. M."]
    year: 2016
    title: "Evolutionary escalation: the bat–moth arms race"
    journal: "Journal of Experimental Biology"
    volume: 219
    pages: "1589–1602"
    doi: "10.1242/jeb.086686"
  - authors: ["Barber, J. R.", "Conner, W. E."]
    year: 2007
    title: "Acoustic mimicry in a predator–prey interaction"
    journal: "Proceedings of the National Academy of Sciences"
    volume: 104
    pages: "9331–9334"
    doi: "10.1073/pnas.0703627104"
    open_access: true
  - authors: ["Corcoran, A. J.", "Barber, J. R.", "Conner, W. E."]
    year: 2009
    title: "Tiger moth jams bat sonar"
    journal: "Science"
    volume: 325
    pages: "325–327"
    doi: "10.1126/science.1174096"
  - authors: ["Schnitzler, H.-U.", "Denzinger, A."]
    year: 2011
    title: "Auditory fovea and Doppler shift compensation: adaptations for flutter detection in echolocating bats using CF-FM signals"
    journal: "Journal of Comparative Physiology A"
    volume: 197
    pages: "541–559"
    doi: "10.1007/s00359-010-0569-6"
  - authors: ["Steckel, J.", "Peremans, H."]
    year: 2013
    title: "BatSLAM: simultaneous localization and mapping using biomimetic sonar"
    journal: "PLoS ONE"
    volume: 8
    pages: "e54076"
    doi: "10.1371/journal.pone.0054076"
    open_access: true
status: published
---

## Seeing with sound

On a summer night, an insect-eating bat can chase a moth through complete darkness and snatch it out of the air. It does not need light for this. The bat produces short, loud calls and listens to the echoes that come back from everything around it – branches, the ground, the fluttering wings of an insect. From these echoes its brain builds a picture of its surroundings. This way of sensing is called **echolocation**, or **biosonar**.

In 1944, the American zoologist Donald Griffin wrote a short paper whose title sums up the idea: *Echolocation by blind men, bats and radar* [1](#ref-1){:.cite}. The comparison with radar was apt. Bats use solutions that engineers also adopted in sonar and radar – broadband sweeps to measure distance, and the Doppler shift to measure speed [2](#ref-2){:.cite}.

Most bat calls are **ultrasound**: they lie above about 20 kHz, the upper limit of human hearing. Across all species, the dominant frequencies of echolocation calls range from about 11 kHz to 212 kHz; most insect-eating bats call between 20 and 60 kHz [2](#ref-2){:.cite}. The calls are also remarkably loud. Bats hunting in open space and along the edges of vegetation reach source levels of 122–134 dB SPL, measured 10 cm in front of the mouth; two species of bulldog bats that hunt low over water average about 137 dB SPL, with maxima above **140 dB SPL** [3](#ref-3){:.cite}. These are among the most intense airborne sounds produced by any animal [2](#ref-2){:.cite}.

With these calls, bats measure distance with astonishing precision. In James Simmons' classic training experiments, four species – among them the big brown bat, *Eptesicus fuscus* – could tell apart two targets whose distances differed by only **1–3 cm** [4](#ref-4){:.cite}.

## The hunt in three phases

1. **Search.** The bat flies through its hunting ground and calls at a steady rhythm. Bats in open space use longer calls and longer intervals than bats in clutter; in flight, bats often call 5–20 times per second [2](#ref-2){:.cite} – a call every 100 ms is typical of many foraging bats [5](#ref-5){:.cite}.
2. **Approach.** As soon as the bat detects an insect, it turns towards it. The echo delay shrinks as the distance shrinks, so the bat calls at shorter and shorter intervals. It also shortens each call, because the loud outgoing call must not overlap with the faint returning echo [2](#ref-2){:.cite}.
3. **Buzz.** Just before the capture, the calls merge into a rapid **feeding buzz** of up to about 200 calls per second [2](#ref-2){:.cite}. The bat now updates the position of its prey every few milliseconds.

How exactly a bat hunts depends on where. In open air, an insect stands out as an isolated echo; near vegetation or the ground, the bat must pick the echo of its prey out of a clutter of background echoes. Different species have evolved different strategies for these situations [6](#ref-6){:.cite}.

{% include lens-tabs.html lenses="biology,physics,math,cs,physical-ai" %}

{% include lens-start.html lens="biology" %}

## Biology lens: an arms race in ultrasound

Echolocation made bats formidable night hunters – and it turned their prey into listeners. Many moths have evolved **ears** that are sensitive to high frequencies. Ears arose in a remarkable number of places on the body across insects, and in moths they trigger defensive behaviour such as sudden evasive flight when a bat approaches [7](#ref-7){:.cite}.

Some **tiger moths** go further and answer an attacking bat with ultrasonic clicks of their own. Jesse Barber and William Conner filmed bats hunting tiger moths with infrared high-speed cameras. Naive red bats and big brown bats quickly learned to avoid the first noxious, clicking moth species they were offered, associating the sound with a bad taste. Afterwards they also avoided a second clicking species – whether it was distasteful or not. The clicks work as an acoustic warning signal, and harmless species can mimic it [8](#ref-8){:.cite}.

The tiger moth *Bertholdia trigona* uses its clicks in yet another way. It is palatable, but when a big brown bat attacks, it answers with ultrasonic clicks that **jam the bat's sonar**. Earlier evidence for such jamming had been inconclusive; Aaron Corcoran and colleagues showed it with ultrasonic recordings and infrared high-speed video [9](#ref-9){:.cite}.

Bats, in turn, show counter-adaptations. Some call at frequencies outside the hearing range of most eared moths, some change the pattern and frequency of their calls during pursuit, and some use quiet, "stealth" echolocation [7](#ref-7){:.cite}.

Echolocation calls themselves are often shaped more by the habitat than by the family tree. Long constant-frequency calls with a high duty cycle – the sound is "on" most of the time – evolved independently in horseshoe bats and in the moustached bat *Pteronotus parnellii*: a textbook case of **convergent evolution** [2](#ref-2){:.cite}.

{% include lens-end.html %}

{% include lens-start.html lens="physics" %}

## Physics lens: wavelength, loudness and the Doppler shift

Sound travels through air at about 343 m/s at 20 °C. Its wavelength is the speed divided by the frequency, *λ* = *c* / *f*. At 20 kHz, a sound wave is about 17 mm long; at 100 kHz, only 3.4 mm. This matters because an object reflects sound well only if it is not much smaller than the wavelength. When the wing length of an insect drops from one wavelength to a fifth of it, its echo becomes about 25 dB weaker. Small prey therefore calls for high frequencies [2](#ref-2){:.cite}.

High frequencies have a price, though: air absorbs them much more strongly than low frequencies, which limits the range of echolocation [2](#ref-2){:.cite}. In addition, sound spreads out on the way to the target and again on the way back. For a small target, the intensity of the echo falls with the fourth power of the distance: at twice the distance, the echo is 16 times, or 12 dB, weaker. Bats counter these losses with volume. Surlykke and Kalko found that the bats emitting the highest intensities also used the highest frequencies. Their estimates suggest that, as a result, species calling at very different frequencies have similar detection distances for prey [3](#ref-3){:.cite}. When closing in on vegetation or the ground, bats lower their output again, by 4–7 dB per halving of the distance [3](#ref-3){:.cite}.

The third effect is the **Doppler shift**. When a bat flies towards an object, the echo returns at a higher frequency than the call – the bat is a moving source and, for the returning echo, a moving receiver. Horseshoe bats and the moustached bat turn this into a precision instrument: they lower the frequency of their calls the faster they fly, so that the echoes return consistently at the frequency they hear best [2](#ref-2){:.cite}. This **Doppler shift compensation** keeps the echoes in their **auditory fovea**: an expanded region of the inner ear devoted to a narrow band around this frequency, served along the whole auditory pathway by many sharply tuned nerve cells. There, the rhythmic changes in the echo caused by the beating wings of an insect – the "flutter" – stand out even in clutter such as vegetation [10](#ref-10){:.cite}.

{% include lens-end.html %}

{% include lens-start.html lens="math" %}

## Mathematics lens: distance, direction and speed from an echo

**Distance.** The call travels to the target and back, so the distance *d* is half the path that sound covers during the echo delay Δ*t*:

<div class="formula" role="math" aria-label="d equals c times delta t over 2"><var>d</var> = <span class="frac"><span class="frac__num"><var>c</var> · Δ<var>t</var></span><span class="frac__den">2</span></span></div>

Every metre of distance adds 2 m / 343 m/s ≈ **5.8 ms** of delay. An echo after 17.5 ms therefore puts a moth 343 m/s · 17.5 ms / 2 ≈ **3.0 m** away.

**Resolution.** How close can two targets be before their echoes blur into one? Signal theory gives the answer: the range resolution depends on the **bandwidth** *B* of the call – the range of frequencies it covers – not on its duration:

<div class="formula" role="math" aria-label="delta d is approximately c over 2 B">Δ<var>d</var> ≈ <span class="frac"><span class="frac__num"><var>c</var></span><span class="frac__den">2 <var>B</var></span></span></div>

A call sweeping from 80 to 40 kHz has *B* = 40 kHz and a resolution of about 343 / 80,000 m ≈ **4 mm**. A pure tone lasting 2 ms has a bandwidth of only about 1 / (2 ms) = 0.5 kHz – and a resolution of about 34 cm. In Simmons' 1973 discrimination tests, bats resolved 1–3 cm [4](#ref-4){:.cite} – coarser than this ideal limit, but far finer than a pure tone would allow. The computer science lens tests the formula with a program.

**Direction.** A sound from the side reaches the nearer ear slightly earlier. For ears a distance *b* apart and a sound arriving at an angle *θ* from straight ahead, the difference in arrival time is

<div class="formula" role="math" aria-label="delta tau equals b times sine theta over c">Δ<var>τ</var> = <span class="frac"><span class="frac__num"><var>b</var> · sin <var>θ</var></span><span class="frac__den"><var>c</var></span></span></div>

With an assumed ear spacing of 2 cm, a direction 10° off the centre line gives Δ*τ* = 0.02 m · sin 10° / 343 m/s ≈ **10 µs** – ten millionths of a second. Bats and other small mammals estimate direction to better than about 10°, which corresponds to time differences below about 10 µs [5](#ref-5){:.cite}; together with the delay, this gives a position in space. Bats also use the loudness difference between their ears and the way their outer ears filter the sound [11](#ref-11){:.cite}.

**Speed.** For a bat flying at speed *v* towards a stationary object, the echo returns with the frequency

<div class="formula formula--steps"><span><var>f</var><sub>echo</sub> = <var>f</var><sub>0</sub> · <span class="frac"><span class="frac__num"><var>c</var> + <var>v</var></span><span class="frac__den"><var>c</var> − <var>v</var></span></span></span><span>≈ <var>f</var><sub>0</sub> · (1 + 2<var>v</var>/<var>c</var>)</span></div>

At *v* = 5 m/s and *f*<sub>0</sub> = 50 kHz, the echo comes back about **1.5 kHz** higher. The factor 2 appears because the frequency is shifted twice: once when the moving bat emits the call, and again when it receives the echo.

{% include lens-end.html %}

{% include lens-start.html lens="cs" %}

## Computer science lens: why bats sweep – a matched filter in code

How does a bat find a faint echo in noise and tell two nearby targets apart? Simmons compared the performance of bats with the mathematics of their calls and concluded that bats possess some neural equivalent of a **matched filter**: an ideal sonar receiver that cross-correlates a copy of the outgoing call with the returning echo to detect it and determine its arrival time [4](#ref-4){:.cite}. Engineers use the same method in radar and sonar.

The program below simulates an echo from two targets 5 cm apart – a moth and a leaf just behind it – buried in noise. It compares two calls of the same duration: a **frequency sweep** from 80 to 40 kHz, similar to the calls of big brown bats, and a **pure tone** at 60 kHz. The question: which call lets the matched filter separate the two echoes, and how well does the resolution formula of the mathematics lens predict the result?

```python
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
```
{% include code-result.html file="range_resolution.py" label="Fig. 2" caption="Output of the program above: the envelope of the matched filter output over distance for two targets 5 cm apart (dotted lines). Top: a sweep from 80 to 40 kHz gives two sharp peaks exactly at the targets. Bottom: a pure 60 kHz tone of the same duration gives two broad humps in the wrong places – the overlapping echoes interfere. Signals are simulated." alt="Two line charts stacked vertically, both showing the matched filter output from 0 to 1 over distance from 1.2 to 1.85 metres, with dotted vertical lines at the true targets at 1.50 and 1.55 metres. Top, for a sweep from 80 to 40 kilohertz: two narrow peaks of height 1 sit exactly on the dotted lines, and the noise elsewhere stays below 0.1. Bottom, for a pure 60 kilohertz tone: two broad humps peak at about 1.43 and 1.62 metres, several centimetres outside the true targets, with a dip between them." %}

What the result teaches:

- **Bandwidth beats duration.** Both calls last 2 ms and carry the same energy. The sweep separates the two targets exactly (error below 0.1 cm), just as the formula Δ*d* ≈ *c* / (2*B*) ≈ 0.4 cm predicts. The tone has a resolution of about 34 cm, far more than the 5 cm between the targets.
- **Overlapping echoes do more than blur.** The two tone echoes overlap and interfere: depending on their phase difference, they add up or cancel. Here, the program reports two echoes at 1.43 and 1.62 m – both about 7 cm off. A pure tone is simply the wrong tool for measuring distance; bats that use long constant-frequency calls, like horseshoe bats, use the frequency-modulated part at the end of their calls for ranging [4](#ref-4){:.cite}.
- **The model is idealised.** The simulated echoes are perfect copies of the call; real echoes are weakened, filtered by the target and the air, and shifted by the Doppler effect. The resolution of 0.4 cm is therefore a lower limit, not a prediction for a real bat. In Simmons' 1973 tests, bats resolved 1–3 cm [4](#ref-4){:.cite}.

A few programming ideas are worth noticing, too:

- **Correlation as a search.** `correlate` slides the known call along the recording and multiplies them; where the two match, the sum is large. `hilbert` turns the oscillating result into a smooth envelope, whose peaks mark the echoes.
- **Windowing.** `np.hanning` fades each call in and out. Without it, the abrupt start and end would add side lobes that `find_peaks` could mistake for extra echoes.
- **Validation.** The program compares its result with the known target positions and with the resolution formula – a habit worth keeping for any sensor code.

Try it yourself – each change takes one line:

- Set `TARGETS = [1.50, 1.51]`: the sweep still separates targets only 1 cm apart, with an error of 0.1 cm; the tone reports a single echo.
- Set `NOISE = 1.0`: the noise is now as strong as the echoes, but the sweep still finds both targets with an error below 0.1 cm – the matched filter collects the energy of the whole call.
- Set `CALL_TIME = 5e-3`: a longer call narrows the tone's bandwidth to 0.2 kHz, and its resolution worsens to about 85.8 cm. The sweep keeps its 0.4 cm, because its bandwidth is still 40 kHz.

{% include code-variant.html file="range_resolution.py" id="close" replace="TARGETS = [1.50, 1.55]" with="TARGETS = [1.50, 1.51]" expect="1.50 1.51 0.1 1" %}
{% include code-variant.html file="range_resolution.py" id="noise" replace="NOISE = 0.3" with="NOISE = 1.0" expect="1.50 1.55 0.0" %}
{% include code-variant.html file="range_resolution.py" id="longer" replace="CALL_TIME = 2e-3" with="CALL_TIME = 5e-3" expect="0.2 85.8 0.4" %}

{% include lens-end.html %}

{% include lens-start.html lens="physical-ai" %}

## Physical AI lens: robots that find their way by sound

Physical AI is about machines that sense and act in the physical world. Cameras need light; sound works in the dark. Simple ultrasonic distance sensors are common in robots and cars, but bats extract far more from their echoes. Two research robots show what happens when engineers copy the whole bat – one emitter, two ears and bat-like signal processing – instead of just the distance measurement [5](#ref-5){:.cite}.

**BatSLAM.** Jan Steckel and Herbert Peremans at the University of Antwerp put a bat-like sonar head on a mobile robot [11](#ref-11){:.cite}:

- one ultrasonic emitter sends a 3 ms call that sweeps from 100 down to 20 kHz;
- two microphones sit in plastic copies of the outer ears of the bat *Micronycteris microtis*, enlarged 1.5 times;
- a model of the mammalian cochlea turns the echoes into time–frequency patterns;
- a navigation model based on the hippocampus of rats (RatSLAM) links these patterns to places.

The robot combined the echoes with its own movement commands (odometry). Odometry alone did not produce a useful map; together with the echoes, the robot mapped unmodified office environments efficiently and consistently. It recognised places it had visited before without identifying individual objects in the echoes [11](#ref-11){:.cite}. SLAM stands for **simultaneous localisation and mapping**: the robot builds a map and finds its own position in it at the same time.

**Robat.** Itamar Eliakim, Yossi Yovel and colleagues at Tel Aviv University built a fully autonomous robot that maps unknown surroundings by sound alone [5](#ref-5){:.cite}. They tested it in two greenhouses of the university's botanical garden. Like a bat, it has one ultrasonic speaker as its "mouth" and two ultrasonic microphones as its "ears". Every 0.5 m – measured by its odometry – it stopped and emitted wide-band frequency-modulated calls in three directions – mimicking a bat that flies at 5 m/s and calls every 100 ms. From the echoes it marked obstacles on a map, avoided dead ends and steered around objects. On average, the estimated borders of the objects were 42 cm from their real position. A neural network classified objects as plants or non-plants with a balanced accuracy of 68 %, clearly above the 50 % expected by chance [5](#ref-5){:.cite}.

These numbers show both the promise and the gap. A robot can map its surroundings with sound alone, but real bats still perceive far more detail from their echoes – and do it in flight. The lesson for Physical AI: the shape of the sensor itself – ears, noseleaf, a well-designed call – does part of the processing before any computer gets involved [11](#ref-11){:.cite}.

{% include lens-end.html %}

## From bats to technology

Echolocation is one of the clearest examples of nature and engineering arriving at similar solutions: broadband sweeps for measuring distance, the Doppler shift for measuring speed, and matched filtering to find a faint signal in noise [2](#ref-2){:.cite} [4](#ref-4){:.cite}. Sonar, radar and the ultrasonic sensors of robots and cars all rely on the same physics.

Open questions remain. Simmons proposed in 1973 that bats contain some neural equivalent of a matched filter [4](#ref-4){:.cite}; how their nervous system actually does it is still being studied. For many bat traits it is hard to tell whether they evolved as counter-adaptations to eared prey or for other reasons [7](#ref-7){:.cite}. And robots are still far from perceiving as much detail in echoes as a bat [5](#ref-5){:.cite}.
