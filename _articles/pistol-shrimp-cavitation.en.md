---
id: pistol-shrimp-cavitation
lang: en
ref: pistol-shrimp-cavitation
title: "The Pistol Shrimp and the Physics of Cavitation"
short_title: "Pistol shrimp & cavitation"
kicker: "Flagship article · Fluid dynamics"
description: "How a pistol shrimp boils water without heat: its claw fires a jet that forms a cavitation bubble, a flash of light and a shock wave. Physics, maths and code."
dek: "How a shrimp a few centimetres long makes water boil without heat: one snap of its claw fires a jet, creates a cavitation bubble and ends in a flash of light and a shock wave – explained through physics, mathematics and code."
date: 2026-09-26
permalink: /articles/pistol-shrimp-cavitation/
image: /assets/og/pistol-shrimp-cavitation-en.jpg
image_alt: "Schematic of a pistol shrimp claw firing a water jet that creates a cavitation bubble and a shock wave."
hero_figure: svg/claw.svg
hero_caption: "<span class=\"caption__label\">Fig. 1</span> A pistol shrimp and its oversized snapping claw. A plunger on the movable finger (dactyl) drives water out of a socket; the jet creates a cavitation bubble whose collapse sends out a shock wave."
educational_level: "Intermediate"
keywords: ["pistol shrimp", "snapping shrimp", "Alpheidae", "cavitation", "cavitation bubble", "shrimpoluminescence", "Bernoulli's principle", "Rayleigh–Plesset equation", "cavitation erosion", "shock wave", "bionics"]
about:
  - { name: "Alpheidae (snapping shrimp)", wikidata: Q311534, wikipedia: "https://en.wikipedia.org/wiki/Alpheidae" }
  - { name: "Cavitation", wikidata: Q201666, wikipedia: "https://en.wikipedia.org/wiki/Cavitation" }
mentions:
  - { name: "Alpheus heterochaelis", wikidata: Q3612969 }
  - { name: "Sonoluminescence", wikidata: Q182350 }
  - { name: "Rayleigh–Plesset equation", wikidata: Q7298492 }
  - { name: "Bernoulli's principle", wikidata: Q181328 }
dimensions:
  time: ["modern-era"]
  space: ["coastal", "coral-reef", "seagrass", "lab"]
  physics: ["fluid-dynamics", "thermodynamics", "acoustics", "optics"]
  adjacent_sciences: ["biology", "mathematics", "computer-science", "medical-technology", "bionics"]
beings: ["pistol-shrimp"]
lenses: ["biology", "physics", "math", "cs"]
key_facts:
  - "The loud snap of a pistol shrimp does not come from the claw halves hitting each other. It comes from a **collapsing cavitation bubble** [1](#ref-1){:.cite}."
  - "Closing the claw fires a **water jet of roughly 25 m/s**. At that speed the pressure in the jet falls below the vapour pressure of water, and a vapour bubble forms [1](#ref-1){:.cite} [3](#ref-3){:.cite}."
  - "The bubble collapses in **less than a millisecond**, sending out a shock wave that can stun prey – and a short flash of light, dubbed *shrimpoluminescence* [2](#ref-2){:.cite}."
  - "Inside the collapsing bubble, temperatures reach **at least 5,000 K** [2](#ref-2){:.cite}."
  - "Engineers have 3D-printed a working replica of the claw that reproduces the flash and the shock wave [3](#ref-3){:.cite}."
  - "Snapping shrimp are among the main sources of **biological noise** in shallow seas: a single snap reaches a source level of **183–189 dB re 1 µPa** at 1 m [7](#ref-7){:.cite}."
faq:
  - q: "How does a pistol shrimp make its snapping sound?"
    a: "Not by the claw halves striking each other. When the claw snaps shut, it shoots out a jet of water so fast that the pressure inside it drops below the vapour pressure of water. A cavitation bubble forms, and the sound is emitted when this bubble violently collapses. Versluis and colleagues showed this in 2000 with high-speed video and hydrophone recordings."
  - q: "How hot does the pistol shrimp's bubble get?"
    a: "At the moment of collapse, the bubble emits a flash of light that indicates temperatures of at least 5,000 kelvin inside it (Lohse et al., 2001) – close to the temperature of the Sun's visible surface, about 5,800 kelvin. The heat lasts only a tiny fraction of a second and is confined to the tiny volume of the compressed bubble."
  - q: "What is cavitation?"
    a: "Cavitation is the formation of vapour-filled cavities in a liquid when the local pressure falls below the liquid's vapour pressure – for example in a very fast jet or behind a ship's propeller. When the pressure recovers, the cavities collapse violently and emit shock waves, which can stun animals or erode metal."
  - q: "What is shrimpoluminescence?"
    a: "Shrimpoluminescence is the short flash of light emitted when the cavitation bubble created by a snapping shrimp collapses. It was first reported by Lohse, Schmitz and Versluis in 2001 and resembles sonoluminescence, the light emitted by bubbles driven by ultrasound."
  - q: "Can engineers copy the pistol shrimp?"
    a: "Yes. In 2019, Tang and Staack 3D-printed a claw replica based on a micro-CT scan of a moulted shrimp claw. Driven by springs, it produces a water jet matching the shrimp's cavitation number, and it reproduces the flash of light and the shock wave – more efficiently than other ways of generating plasma in water."
  - q: "How loud is a pistol shrimp?"
    a: "Very loud for its size. For the snapping shrimp Synalpheus parneomeris, Au and Banks (1998) measured peak-to-peak source levels of 183 to 189 decibels re 1 micropascal at 1 metre. Underwater decibels use a different reference pressure than decibels in air, so the numbers cannot be compared directly. Colonies of snapping shrimp are among the main sources of biological noise in shallow seas."
sources:
  - authors: ["Versluis, M.", "Schmitz, B.", "von der Heydt, A.", "Lohse, D."]
    year: 2000
    title: "How snapping shrimp snap: through cavitating bubbles"
    journal: "Science"
    volume: 289
    pages: "2114–2117"
    doi: "10.1126/science.289.5487.2114"
  - authors: ["Lohse, D.", "Schmitz, B.", "Versluis, M."]
    year: 2001
    title: "Snapping shrimp make flashing bubbles"
    journal: "Nature"
    volume: 413
    pages: "477–478"
    doi: "10.1038/35097152"
  - authors: ["Tang, X.", "Staack, D."]
    year: 2019
    title: "Bioinspired mechanical device generates plasma in water via cavitation"
    journal: "Science Advances"
    volume: 5
    pages: "eaau7765"
    doi: "10.1126/sciadv.aau7765"
    open_access: true
  - authors: ["Lord Rayleigh"]
    year: 1917
    title: "On the pressure developed in a liquid during the collapse of a spherical cavity"
    journal: "The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science"
    volume: 34
    pages: "94–98"
    doi: "10.1080/14786440808635681"
  - authors: ["Hughes, M."]
    year: 1996
    title: "Size assessment via a visual signal in snapping shrimp"
    journal: "Behavioral Ecology and Sociobiology"
    volume: 38
    pages: "51–57"
    doi: "10.1007/s002650050216"
  - authors: ["Mellon, D. Jr.", "Stephens, P. J."]
    year: 1978
    title: "Limb morphology and function are transformed by contralateral nerve section in snapping shrimps"
    journal: "Nature"
    volume: 272
    pages: "246–248"
    doi: "10.1038/272246a0"
  - authors: ["Au, W. W. L.", "Banks, K."]
    year: 1998
    title: "The acoustics of the snapping shrimp Synalpheus parneomeris in Kaneohe Bay"
    journal: "The Journal of the Acoustical Society of America"
    volume: 103
    pages: "41–47"
    doi: "10.1121/1.423234"
status: published
---

## A snap that makes water boil – without heat

Pistol shrimp, also called snapping shrimp, belong to the family *Alpheidae*. They are only a few centimetres long and live in warm and temperate coastal waters – in coral reefs, seagrass meadows and burrows on the sea floor. One of their two claws is hugely enlarged. With it, they produce a sharp crack that can stun or even kill prey [1](#ref-1){:.cite} and that they also use for defence and communication [3](#ref-3){:.cite}. Where many shrimp live together, their snapping merges into a crackling noise that is loud enough to disturb underwater communication [2](#ref-2){:.cite}.

For a long time, it seemed obvious where the sound came from: the two halves of the claw striking each other. In 2000, a team led by Michel Versluis and Detlef Lohse at the University of Twente filmed the snap with high-speed cameras while recording it with a hydrophone. The recordings showed that the sound is emitted **when a cavitation bubble collapses – not when the claw closes** [1](#ref-1){:.cite}.

## The snap in four steps

1. **Cocking.** The shrimp opens its snapping claw and builds up muscle tension while the claw stays locked open.
2. **Jet.** When the claw is released, a plunger on the movable finger – the *dactyl* – plunges into a matching socket in the claw. The water in the socket is shot out as a narrow jet.
3. **Cavitation.** The jet is so fast that the pressure inside it drops below the vapour pressure of water. The water "tears" and forms a bubble filled with vapour.
4. **Collapse.** Once the jet has passed, the surrounding water crushes the bubble. It implodes within a fraction of a millisecond, emitting a shock wave and a brief flash of light [1](#ref-1){:.cite} [2](#ref-2){:.cite}.

{% include lens-tabs.html lenses="biology,physics,math,cs" %}

{% include lens-start.html lens="biology" %}

## Biology lens: weapon, signal – and a claw that can switch sides

For the shrimp, the snapping claw is a multi-purpose tool. The shock wave stuns or kills small prey [1](#ref-1){:.cite}; the same snap serves for defence and communication [3](#ref-3){:.cite}. Even without a sound, the claw carries information: in experiments by Hughes, male snapping shrimp reacted aggressively to isolated claws fixed open in the display posture – and how strongly they reacted depended on the size of the claw relative to their own [5](#ref-5){:.cite}. The open claw works as a **visual signal of body size**, which lets rivals assess each other before a fight escalates.

The claw is also remarkably plastic. In snapping shrimp of the genus *Alpheus*, the large snapping claw and the small pincer claw can swap roles: after the snapper is lost, the pincer on the opposite side is rebuilt into a new snapping claw over the following moults. Mellon and Stephens showed in 1978 that the form and function of a claw can be transformed even by cutting a nerve on the opposite side of the body – the nervous system controls which claw becomes the weapon [6](#ref-6){:.cite}.

Snapping shrimp shape entire habitats acoustically. They are among the main sources of **biological noise** in shallow bays, harbours and coastal waters. For the species *Synalpheus parneomeris*, Au and Banks measured peak-to-peak source levels of 183 to 189 dB re 1 µPa at 1 m, with energy spread from a few kilohertz up to 200 kHz. This crackling can limit human sonar and may interfere with the sounds of dolphins and whales [7](#ref-7){:.cite}. Note that underwater decibels use a reference pressure of 1 µPa instead of 20 µPa in air, so they cannot be compared directly with sound levels in air.

{% include lens-end.html %}

{% include lens-start.html lens="physics" %}

## Physics lens: why fast water boils

We usually make water boil by heating it. But boiling depends on *pressure* just as much as on temperature: at the top of Mount Everest, water boils at around 70 °C. Lower the pressure far enough, and water boils even at room temperature. The pistol shrimp lowers the pressure – with speed.

**Bernoulli's principle** says that along a streamline, the static pressure *p* plus the dynamic pressure ½*ρv*² stays constant. The faster the water flows, the lower its static pressure:

<div class="formula" role="math" aria-label="p equals p zero minus one half rho v squared"><var>p</var> = <var>p</var><sub>0</sub> − <span class="frac"><span class="frac__num">1</span><span class="frac__den">2</span></span> <var>ρ</var> <var>v</var><sup>2</sup></div>

With *p*<sub>0</sub> = 101 kPa (atmospheric pressure) and *ρ* = 998 kg/m³ for water, the dynamic pressure at 25 m/s is ½ · 998 · 25² ≈ 312 kPa – three times the atmospheric pressure. Long before that point, at about **14 m/s**, the static pressure reaches the vapour pressure of water (2.3 kPa at 20 °C). The water can no longer stay liquid: it cavitates.

<figure class="figure">
{% include svg/bernoulli.svg %}
<figcaption class="caption"><span class="caption__label">Fig. 2</span> Static pressure in a water jet according to Bernoulli. Above about 14 m/s it falls below the vapour pressure of water. The shrimp's jet, at roughly 25 m/s, is deep in the cavitation zone.</figcaption>
</figure>

Engineers capture this with the **cavitation number** σ = (*p*<sub>∞</sub> − *p*<sub>v</sub>) / (½*ρv*²). The smaller σ, the more likely cavitation. For a jet of 25 m/s, σ ≈ 0.3. The mechanical replica of the claw built by Tang and Staack produced jets with σ = 0.14 to 0.30 – comparable to the real shrimp [3](#ref-3){:.cite}.

The dramatic part comes next. When the jet has passed, the full ambient pressure acts on the bubble, and it collapses faster and faster. The little gas left inside is compressed so violently that it heats up to **at least 5,000 K** and glows for an instant – *shrimpoluminescence*, to the authors' knowledge the first observation of this kind of light production in any animal [2](#ref-2){:.cite}. At the same moment, a shock wave races outwards at the speed of sound in water, about 1,500 m/s [3](#ref-3){:.cite}.

The same physics that the shrimp uses as a weapon is a nuisance for engineers: cavitation bubbles collapsing on ship propellers and pump impellers slowly erode even hardened steel – a process known as *cavitation erosion*.

{% include lens-end.html %}

{% include lens-start.html lens="math" %}

## Mathematics lens: how long does the collapse take?

In 1917, Lord Rayleigh calculated how an empty spherical cavity in a liquid collapses under a constant pressure difference [4](#ref-4){:.cite}. His result for the collapse time is remarkably simple:

<div class="formula" role="math" aria-label="t c approximately 0.915 times R max times the square root of rho over p infinity minus p v"><var>t</var><sub>c</sub> ≈ 0.915 · <var>R</var><sub>max</sub> · <span class="sqrt">√<span class="sqrt__arg"><span class="frac"><span class="frac__num"><var>ρ</var></span><span class="frac__den"><var>p</var><sub>∞</sub> − <var>p</var><sub>v</sub></span></span></span></span></div>

Let us assume a bubble with a maximum radius of *R*<sub>max</sub> = 3 mm – a bubble a few millimetres across. With *ρ* = 998 kg/m³ and *p*<sub>∞</sub> − *p*<sub>v</sub> = 101,325 Pa − 2,339 Pa ≈ 99,000 Pa:

<div class="formula formula--steps"><span><var>t</var><sub>c</sub> ≈ 0.915 · 0.003 m · √(998 / 99,000) s/m</span><span>≈ 0.915 · 0.003 · 0.1004 s ≈ 2.76 · 10<sup>−4</sup> s ≈ <strong>276 µs</strong></span></div>

Two things follow directly from the formula. The collapse time grows in **proportion to the bubble size**: a bubble twice as large takes twice as long to collapse. And it is **inversely proportional to the square root of the pressure difference**: in deeper water, where the ambient pressure is higher, bubbles collapse faster.

<figure class="figure figure--dark">
{% include svg/cavitation.svg %}
<figcaption class="caption caption--dark"><span class="caption__label">Fig. 3</span> Life of a cavitation bubble: rapid growth, violent collapse, weak rebounds. The whole cycle takes less than a millisecond.</figcaption>
</figure>

Why does the collapse get so hot? If the gas inside is compressed quickly, it has no time to give off heat – the compression is *adiabatic*. For an ideal gas, the temperature then rises as

<div class="formula" role="math" aria-label="T max equals T zero times R max over R min to the power of 3 times gamma minus 1"><var>T</var><sub>max</sub> = <var>T</var><sub>0</sub> · <span class="paren">(</span><span class="frac"><span class="frac__num"><var>R</var><sub>max</sub></span><span class="frac__den"><var>R</var><sub>min</sub></span></span><span class="paren">)</span><sup>3(<var>γ</var> − 1)</sup></div>

where *γ* is the adiabatic index, the ratio of the gas's heat capacities *c*<sub>p</sub>/*c*<sub>V</sub> (1.4 for air). A bubble that shrinks to one tenth of its radius already reaches 293 K · 10<sup>1.2</sup> ≈ **4,600 K** – the same order of magnitude as the at least 5,000 K derived from the flash [2](#ref-2){:.cite}. The energy spread over the whole bubble is focused into a volume 10³ = 1,000 times smaller. Real bubbles contain water vapour and lose some heat, so this estimate is a rough guide, not a precise prediction.

{% include lens-end.html %}

{% include lens-start.html lens="cs" %}

## Computer science lens: simulating a bubble

Rayleigh's formula assumes an empty bubble. To model a real one – with gas inside, surface tension and viscosity – physicists use the **Rayleigh–Plesset equation**, an ordinary differential equation for the bubble radius *R*(*t*). Versluis and colleagues used a model of this type to reproduce both the bubble radius over time and the sound emitted by the shrimp [1](#ref-1){:.cite}:

<div class="formula" role="math" aria-label="R times R double dot plus three halves R dot squared equals p B minus p infinity over rho"><var>R</var> <var>R̈</var> + <span class="frac"><span class="frac__num">3</span><span class="frac__den">2</span></span> <var>Ṙ</var><sup>2</sup> = <span class="frac"><span class="frac__num"><var>p</var><sub>B</sub> − <var>p</var><sub>∞</sub></span><span class="frac__den"><var>ρ</var></span></span></div>

Here *p*<sub>B</sub> is the pressure in the liquid at the bubble wall: gas pressure plus vapour pressure, minus the effects of surface tension and viscosity. Solving it numerically takes a few lines of Python:

```python
import numpy as np
from scipy.integrate import solve_ivp

# Water at 20 °C
RHO, P_INF, P_V = 998.0, 101_325.0, 2_339.0   # density (kg/m³), ambient and vapour pressure (Pa)
SIGMA, MU = 0.0728, 1.0e-3                    # surface tension (N/m), viscosity (Pa·s)

R_MAX = 3.0e-3        # bubble radius at its largest (m)
P_GAS = 100.0         # pressure of non-condensable gas at R_MAX (Pa), assumed
GAMMA = 1.4           # polytropic exponent of the gas

def rayleigh_plesset(t, y):
    """Bubble radius R and wall speed dR/dt → their time derivatives."""
    R, dR = y
    p_gas = P_GAS * (R_MAX / R) ** (3 * GAMMA)
    p_wall = p_gas + P_V - 2 * SIGMA / R - 4 * MU * dR / R
    ddR = ((p_wall - P_INF) / RHO - 1.5 * dR**2) / R
    return [dR, ddR]

def minimum(t, y):        # event: the bubble wall turns around
    return y[1]
minimum.terminal, minimum.direction = True, 1

sol = solve_ivp(rayleigh_plesset, (0, 2e-3), [R_MAX, 0.0], method="LSODA",
                events=minimum, rtol=1e-10, atol=1e-13, max_step=1e-6)

rayleigh = 0.915 * R_MAX * np.sqrt(RHO / (P_INF - P_V))
print(f"collapse after {sol.t[-1] * 1e6:.0f} µs (Rayleigh: {rayleigh * 1e6:.0f} µs)")
# → collapse after 276 µs (Rayleigh: 276 µs)
```

A few things are worth noticing:

- **Stiffness.** Near the collapse, the radius changes extremely fast. An adaptive solver such as LSODA shrinks its time step automatically where needed.
- **Events.** Instead of guessing how long to simulate, the code stops exactly when the bubble wall turns around – the moment of maximum compression.
- **Validation.** With almost no gas inside, the simulation must agree with Rayleigh's analytical result – and it does, to the microsecond. Comparing numerics with a known limit is a habit worth keeping.

Try it yourself: double `R_MAX` and check that the collapse time doubles, or raise `P_INF` to simulate a bubble in deeper water.

{% include lens-end.html %}

## From shrimp to technology

In 2019, Xin Tang and David Staack at Texas A&M University turned the shrimp's trick into a machine. They scanned the exuvia of a shrimp claw – the shell shed during moulting – with micro-computed tomography (µCT), 3D-printed it at five times its natural size and drove it with torsion springs that mimic the shrimp's muscle. The device produced a jet with the same cavitation and Reynolds numbers as the animal – and with it, light flashes and shock waves. According to the authors, it generates plasma in water more efficiently than electrical, acoustic or laser-based methods [3](#ref-3){:.cite}. Such compact, low-cost plasma sources could one day be useful wherever energy has to be focused into a tiny volume of liquid.

Controlled cavitation already plays a role in medicine: in extracorporeal shock wave lithotripsy, shock waves break up kidney stones, and the collapse of cavitation bubbles is part of how they work. The pistol shrimp has been using the same principle for far longer – as a weapon a few millimetres in size.
