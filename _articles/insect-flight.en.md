---
id: insect-flight
lang: en
ref: insect-flight
title: "How Insects Fly: Vortices, Halteres and RoboBees"
short_title: "Insect flight"
kicker: "Article · Aerodynamics"
description: "Insect wings make more lift than classical aerodynamics allows – thanks to a vortex on the leading edge. How bees and flies fly, and how robots copy them."
dek: "A honeybee beats its wings about 230 times per second, and its wings produce more lift than a wing in steady flow could. The secret is a whirlwind that sits on top of each wing. Engineers have learned to copy it – and found out why flying gets so hard when you are small."
date: 2026-10-04
permalink: /articles/insect-flight/
image: /assets/og/insect-flight-en.jpg
og: { eyebrow: "Biology · Aerodynamics · Physical AI", title: "How insects <em>fly</em> – and why robot bees are hard", sub: "A vortex on every wing, gyroscopes made from hind wings, and robots that weigh 80 mg.", title_px: 56 }
image_alt: "Schematic of a hovering honeybee seen from the side: its wings sweep forward and back about 230 times per second; an inset shows the cross-section of a wing with a leading-edge vortex on top and the lift it creates."
hero_figure: svg/insect-flight.svg
hero_caption: "<span class=\"caption__label\">Fig. 1</span> A hovering honeybee. Its wings sweep forward and back through about 90° roughly 230 times per second and flip over at every turn, so that the leading edge always leads. The inset shows a wing in cross-section: air rolls up into a leading-edge vortex on the upper side, which stays attached during the stroke and makes the wing produce more lift than in steady flow."
educational_level: "Intermediate"
keywords: ["insect flight", "how do insects fly", "wingbeat frequency", "honeybee flight", "fruit fly", "Drosophila", "leading-edge vortex", "clap and fling", "unsteady aerodynamics", "halteres", "Reynolds number", "scaling", "square-cube law", "lift coefficient", "asynchronous muscle", "RoboBee", "robot insects", "flapping-wing robot", "micro air vehicle", "Physical AI"]
about:
  - { name: "Insect flight", wikidata: Q1425266, wikipedia: "https://en.wikipedia.org/wiki/Insect_flight" }
  - { name: "RoboBee", wikidata: Q12779901, wikipedia: "https://en.wikipedia.org/wiki/RoboBee" }
mentions:
  - { name: "Western honey bee", wikidata: Q30034 }
  - { name: "Drosophila melanogaster", wikidata: Q130888 }
  - { name: "Manduca sexta", wikidata: Q1366539 }
  - { name: "Encarsia formosa", wikidata: Q614882 }
  - { name: "Halteres", wikidata: Q1335456 }
  - { name: "Insect wing", wikidata: Q276572 }
  - { name: "Asynchronous muscles", wikidata: Q30681494 }
  - { name: "Reynolds number", wikidata: Q178932 }
  - { name: "Lift coefficient", wikidata: Q760106 }
  - { name: "Square–cube law", wikidata: Q1527983 }
  - { name: "Coriolis force", wikidata: Q169973 }
  - { name: "Piezoelectricity", wikidata: Q183759 }
  - { name: "Micro air vehicle", wikidata: Q773392 }
dimensions:
  time: ["modern-era", "age-of-ai"]
  space: ["atmosphere", "lab"]
  physics: ["fluid-dynamics", "mechanics"]
  adjacent_sciences: ["biology", "mathematics", "computer-science", "robotics", "physical-ai", "bionics"]
beings: ["honey-bee", "fruit-fly"]
lenses: ["biology", "physics", "math", "cs", "physical-ai"]
key_facts:
  - "Honeybees hover with a short stroke of about 90° and a high wingbeat frequency of about **230 Hz**; fruit flies beat their 2.5 mm wings about 200 times per second through 145–165° [1](#ref-1){:.cite}."
  - "Insect wings produce typically **2–3 times more lift** than conventional aerodynamics can account for. Most insects get it from a **leading-edge vortex** that stays attached to the wing and spirals out towards the tip [2](#ref-2){:.cite} [6](#ref-6){:.cite}."
  - "Flies sense rotations with **halteres** – tiny, dumbbell-shaped organs that evolved from the hind wings. They beat like wings and detect the Coriolis forces of a turning body, like a gyroscope [8](#ref-8){:.cite} [9](#ref-9){:.cite}."
  - "Smaller flyers must beat faster: for bodies of the same shape, the wingbeat frequency needed to hover grows as one over the square root of the size. A formula with mass and wing area explains 75 % of the variation in wingbeat frequency across insects [3](#ref-3){:.cite}."
  - "Harvard's RoboBee weighed 80 mg in its controlled flights of 2013; a four-winged successor of 90 mg flew untethered in 2019 with solar cells and electronics on board, 259 mg in total [16](#ref-16){:.cite} [17](#ref-17){:.cite}."
faq:
  - q: "Is it true that bees should not be able to fly?"
    a: "No. The claim goes back to a simple calculation published in 1934, which treated an insect wing like a rigid aeroplane wing in steady flow. That calculation was wrong for insects: flapping wings produce extra lift with unsteady effects, above all a leading-edge vortex that stays attached to the wing. Conventional theory is not enough to explain insect flight, but modern unsteady aerodynamics does explain it."
  - q: "How fast do insect wings beat?"
    a: "It varies enormously. In a dataset of more than 150 species, wingbeat frequencies range from 6 beats per second in a butterfly to 480 per second in the yellow-fever mosquito. A honeybee beats its wings about 230 times per second, a fruit fly about 200 times."
  - q: "What is a leading-edge vortex?"
    a: "When an insect wing sweeps through the air at a steep angle, the flow separates at its front edge and rolls up into a vortex on the upper side. On an aeroplane wing such a vortex would detach and the wing would stall. On a flapping insect wing it stays attached for the whole stroke and spirals out towards the wingtip. The low pressure in the vortex adds lift."
  - q: "What are halteres?"
    a: "Halteres are the small, club-shaped organs of flies in place of the hind wings. They beat up and down in time with the wings. When the fly turns, Coriolis forces push them sideways, and sense organs at their base measure this. The fly uses the signal like a gyroscope to keep its body stable."
  - q: "What is the RoboBee?"
    a: "The RoboBee is a family of insect-sized flying robots from Harvard University. Its wings are driven by piezoelectric actuators, thin layers that bend when a voltage is applied, because electric motors work poorly at this size. The version flown in 2013 weighed 80 milligrams and needed a wire for power and control; a four-winged version flew without a wire in 2019, powered by solar cells. Fully autonomous flight with onboard sensing, computing and power is still a research goal."
sources:
  - authors: ["Altshuler, D. L.", "Dickson, W. B.", "Vance, J. T.", "Roberts, S. P.", "Dickinson, M. H."]
    year: 2005
    title: "Short-amplitude high-frequency wing strokes determine the aerodynamics of honeybee flight"
    journal: "Proceedings of the National Academy of Sciences"
    volume: 102
    pages: "18213–18218"
    doi: "10.1073/pnas.0506590102"
    open_access: true
  - authors: ["Ellington, C. P."]
    year: 1999
    title: "The novel aerodynamics of insect flight: applications to micro-air vehicles"
    journal: "Journal of Experimental Biology"
    volume: 202
    pages: "3439–3448"
    doi: "10.1242/jeb.202.23.3439"
  - authors: ["Deakin, M. A. B."]
    year: 2010
    title: "Formulae for Insect Wingbeat Frequency"
    journal: "Journal of Insect Science"
    volume: 10
    pages: "1–9"
    doi: "10.1673/031.010.9601"
    open_access: true
  - authors: ["Weis-Fogh, T."]
    year: 1973
    title: "Quick Estimates of Flight Fitness in Hovering Animals, Including Novel Mechanisms for Lift Production"
    journal: "Journal of Experimental Biology"
    volume: 59
    pages: "169–230"
    doi: "10.1242/jeb.59.1.169"
  - authors: ["Dickinson, M. H.", "Lehmann, F. O.", "Sane, S. P."]
    year: 1999
    title: "Wing Rotation and the Aerodynamic Basis of Insect Flight"
    journal: "Science"
    volume: 284
    pages: "1954–1960"
    doi: "10.1126/science.284.5422.1954"
  - authors: ["Ellington, C. P.", "van den Berg, C.", "Willmott, A. P.", "Thomas, A. L. R."]
    year: 1996
    title: "Leading-edge vortices in insect flight"
    journal: "Nature"
    volume: 384
    pages: "626–630"
    doi: "10.1038/384626a0"
    open_access: true
  - authors: ["Josephson, R. K.", "Malamud, J. G.", "Stokes, D. R."]
    year: 2000
    title: "Asynchronous Muscle: A Primer"
    journal: "Journal of Experimental Biology"
    volume: 203
    pages: "2713–2722"
    doi: "10.1242/jeb.203.18.2713"
  - authors: ["Dickinson, M. H."]
    year: 1999
    title: "Haltere–mediated equilibrium reflexes of the fruit fly, Drosophila melanogaster"
    journal: "Philosophical Transactions of the Royal Society of London. Series B: Biological Sciences"
    volume: 354
    pages: "903–916"
    doi: "10.1098/rstb.1999.0442"
    open_access: true
  - authors: ["Pringle, J. W. S."]
    year: 1948
    title: "The gyroscopic mechanism of the halteres of Diptera"
    journal: "Philosophical Transactions of the Royal Society of London. Series B, Biological Sciences"
    volume: 233
    pages: "347–384"
    doi: "10.1098/rstb.1948.0007"
  - authors: ["Fuller, S. B.", "Karpelson, M.", "Censi, A.", "Ma, K. Y.", "Wood, R. J."]
    year: 2014
    title: "Controlling free flight of a robotic fly using an onboard vision sensor inspired by insect ocelli"
    journal: "Journal of The Royal Society Interface"
    volume: 11
    pages: "20140281"
    doi: "10.1098/rsif.2014.0281"
    open_access: true
  - authors: ["Lehmann, F. O.", "Sane, S. P.", "Dickinson, M."]
    year: 2005
    title: "The aerodynamic effects of wing–wing interaction in flapping insect wings"
    journal: "Journal of Experimental Biology"
    volume: 208
    pages: "3075–3092"
    doi: "10.1242/jeb.01744"
    open_access: true
  - authors: ["Fry, S. N.", "Sayaman, R.", "Dickinson, M. H."]
    year: 2003
    title: "The Aerodynamics of Free-Flight Maneuvers in Drosophila"
    journal: "Science"
    volume: 300
    pages: "495–498"
    doi: "10.1126/science.1081944"
  - authors: ["Sane, S. P."]
    year: 2003
    title: "The aerodynamics of insect flight"
    journal: "Journal of Experimental Biology"
    volume: 206
    pages: "4191–4208"
    doi: "10.1242/jeb.00663"
  - authors: ["Usherwood, J. R.", "Ellington, C. P."]
    year: 2002
    title: "The aerodynamics of revolving wings I. Model hawkmoth wings"
    journal: "Journal of Experimental Biology"
    volume: 205
    pages: "1547–1564"
    doi: "10.1242/jeb.205.11.1547"
  - authors: ["Lehmann, F. O.", "Dickinson, M. H."]
    year: 1997
    title: "The Changes in Power Requirements and Muscle Efficiency During Elevated Force Production in the Fruit Fly Drosophila Melanogaster"
    journal: "Journal of Experimental Biology"
    volume: 200
    pages: "1133–1143"
    doi: "10.1242/jeb.200.7.1133"
  - authors: ["Ma, K. Y.", "Chirarattananon, P.", "Fuller, S. B.", "Wood, R. J."]
    year: 2013
    title: "Controlled Flight of a Biologically Inspired, Insect-Scale Robot"
    journal: "Science"
    volume: 340
    pages: "603–607"
    doi: "10.1126/science.1231806"
  - authors: ["Jafferis, N. T.", "Helbling, E. F.", "Karpelson, M.", "Wood, R. J."]
    year: 2019
    title: "Untethered flight of an insect-sized flapping-wing microscale aerial vehicle"
    journal: "Nature"
    volume: 570
    pages: "491–495"
    doi: "10.1038/s41586-019-1322-0"
  - authors: ["Chen, Y.", "Zhao, H.", "Mao, J.", "Chirarattananon, P.", "Helbling, E. F.", "Hyun, N. P.", "Clarke, D. R.", "Wood, R. J."]
    year: 2019
    title: "Controlled flight of a microrobot powered by soft artificial muscles"
    journal: "Nature"
    volume: 575
    pages: "324–329"
    doi: "10.1038/s41586-019-1737-7"
    open_access: true
  - authors: ["Karásek, M.", "Muijres, F. T.", "De Wagter, C.", "Remes, B. D. W.", "de Croon, G. C. H. E."]
    year: 2018
    title: "A tailless aerial robotic flapper reveals that flies use torque coupling in rapid banked turns"
    journal: "Science"
    volume: 361
    pages: "1089–1094"
    doi: "10.1126/science.aat0350"
    open_access: true
status: published
---

## The bee that "could not fly"

In 1934, August Magnan and André Sainte-Laguë concluded from a simple calculation that the flight of bees was "impossible". Ever since, bees have stood for the gap between aerodynamic theory and living animals [1](#ref-1){:.cite}. The calculation was wrong – but it pointed at something real: an insect wing, tested in a wind tunnel in steady flow, produces too little lift to carry the animal [1](#ref-1){:.cite}. Typically, insect wings produce **2–3 times more lift** than conventional aerodynamics can account for [2](#ref-2){:.cite}.

Insects fly anyway, and they do it at astonishing rates. A honeybee with wings 9.7 mm long beats them about **230 times per second**; a fruit fly, much smaller, flaps its 2.5 mm wings about 200 times per second [1](#ref-1){:.cite}. Across more than 150 species, wingbeat frequencies span from 6 beats per second in a butterfly, the green-veined white, to 480 in the yellow-fever mosquito [3](#ref-3){:.cite}.

This article explains where the missing lift comes from, how flies keep their balance with a built-in gyroscope, why small flyers have to beat faster – and why engineers who build robot insects run into the same physics. In the size of their world, insects sit between two other articles on this site: the bacterium, for which water feels like honey ([Swimming in honey](/articles/bacteria-low-reynolds/)), and us.

## A wingbeat in four steps

A hovering insect does not flap its wings up and down like a bird in cruising flight. In what Torkel Weis-Fogh called "normal hovering", the wings beat almost horizontally, forward and back [4](#ref-4){:.cite}:

1. **Forward stroke.** The wing sweeps forward at a steep angle of attack. Air separates at the leading edge and rolls up into a **leading-edge vortex** on the upper side, which stays attached during the stroke – a "delayed stall" [5](#ref-5){:.cite} [6](#ref-6){:.cite}.
2. **Turn.** At the end of the stroke the wing slows down and rotates rapidly about its long axis, so that the same edge leads on the way back. The rotation itself creates extra force [5](#ref-5){:.cite}.
3. **Backstroke.** The flipped wing sweeps back; again a leading-edge vortex forms and the wing produces lift.
4. **Meeting its own wake.** After the next turn, the wing moves through the air it has just set in motion and gains force from it ("wake capture") [5](#ref-5){:.cite}.

{% include lens-tabs.html lenses="biology,physics,math,cs,physical-ai" %}

{% include lens-start.html lens="biology" %}

## Biology lens: a flight motor and a gyroscope

**Two ways to hover.** Insects do not all beat their wings in the same way. Fruit flies sweep their wings through a large angle of 145–165°. Honeybees use short strokes of about 90° at a high frequency of about 230 Hz – and they get a large part of their force at the turns, from the rapid rotation of the wing [1](#ref-1){:.cite}. Douglas Altshuler and colleagues let honeybees hover in **heliox**, a breathable mixture of oxygen and helium that is only about a third as dense as air. The bees kept their wingbeat frequency almost constant and made their strokes nearly 50 % wider instead [1](#ref-1){:.cite}.

**A motor that runs by itself.** Hundreds of contractions per second are hard for an ordinary muscle, which needs one nerve impulse per contraction. Some insects use a special kind of flight muscle instead: **asynchronous muscle**, in which electrical and mechanical activity are not in step. Such a muscle is activated with a delay when it is stretched and deactivated when it shortens; driven by a steady train of nerve impulses, it can do work over and over in an oscillating system [7](#ref-7){:.cite}. Insects with small wings and heavy bodies, such as bees, need such muscles to reach the frequencies they need [3](#ref-3){:.cite}. And because the wings must be accelerated and stopped at every turn, most insects depend on an effective elastic system in the thorax that stores and returns the energy of the wing motion [4](#ref-4){:.cite}.

**A gyroscope from hind wings.** Flies (Diptera) have only one pair of wings. Their hind wings evolved into **halteres**: small, dumbbell-shaped organs with sense organs at their base [8](#ref-8){:.cite}. A haltere beats up and down through about 150°, at a frequency set by its own mechanical resonance [9](#ref-9){:.cite}. When the body of the fly rotates, the moving haltere experiences gyroscopic or **Coriolis forces** at right angles to its beat, and the sense organs at its base detect them [9](#ref-9){:.cite} [8](#ref-8){:.cite}. Michael Dickinson swung a flight arena with fruit flies inside back and forth: the flies responded with compensatory changes of their wing strokes, and these reflexes vanished when the halteres were removed [8](#ref-8){:.cite}. As early as 1948, John Pringle photographed flies without halteres in free flight – they showed the spiral instability expected of a fly that cannot stabilise its turns [9](#ref-9){:.cite}.

Bees have no halteres, and it is not known for certain how they stay upright. One suggestion is the **ocelli**, three simple light sensors on top of the head that sense the brightness of the sky; hawkmoths, on the other hand, sense rotations with their vibrating antennae, by a mechanism similar to the halteres [10](#ref-10){:.cite}.

{% include lens-end.html %}

{% include lens-start.html lens="physics" %}

## Physics lens: between honey and air

**Where insects live in the world of flows.** The Reynolds number *Re* = *ρ v L* / *η* compares inertial forces with viscous forces (see [Swimming in honey](/articles/bacteria-low-reynolds/)). A bacterium swims at about 10<sup>−5</sup>: viscosity rules, and inertia plays no role. A human swimmer reaches millions. Insects lie in between: in a dataset of more than 150 species, the lowest value, about 8, belongs to a small aphid; apart from a few aphids and whiteflies, values above 100 – typically around 1,000 – are the rule [3](#ref-3){:.cite}. The tiny wasp *Encarsia formosa* flies at *Re* = 10–20 [4](#ref-4){:.cite}, a fruit fly at 100–200 [11](#ref-11){:.cite}. In this middle range, both forces matter: the air is viscous enough to spoil the performance of ordinary wings, but the insect's body still has inertia. When a fruit fly turns, it is inertia, not friction, that dominates the flight dynamics of its body [12](#ref-12){:.cite}.

**The leading-edge vortex.** In 1996, Charles Ellington and colleagues made the airflow around the wings of the hawkmoth *Manduca sexta* visible, together with a large mechanical model of a flapping wing, the "flapper". On the downstroke they found an intense **leading-edge vortex**, strong enough to explain the high lift. It is created by dynamic stall and spirals out towards the wingtip with a spanwise speed comparable to the flapping speed; the flow resembles the conical vortex on a delta wing, and the spanwise flow stabilises the vortex [6](#ref-6){:.cite}. On a wing in steady flow at such a steep angle, the vortex would be shed into the wake; on the flapping insect wing it remains stably attached and greatly enhances the forces [13](#ref-13){:.cite}. Even model hawkmoth wings that simply revolve like a propeller produce high force coefficients because of this vortex [14](#ref-14){:.cite}.

**Rotation and wake capture.** Michael Dickinson, Fritz-Olaf Lehmann and Sanjay Sane described three interacting mechanisms: delayed stall during the strokes, and rotational circulation and wake capture at the turns. The two rotational mechanisms also give the insect a powerful way to change the size and direction of its flight forces when it steers [5](#ref-5){:.cite}.

**Clap and fling.** Some insects bring their wings together above the body and then fling them open like a book. Weis-Fogh discovered this mechanism in 1973 in *Encarsia formosa*: at its low Reynolds number, the wasp needs a lift coefficient of 2 or 3, which steady-state aerodynamics cannot deliver. The fling sets up the circulation around each wing before the downstroke begins, and lift is produced almost instantly [4](#ref-4){:.cite}. On a model fruit fly wing, clap and fling increased total lift by up to 17 %, but only if the wings came within 10–12° of each other [11](#ref-11){:.cite}. Most insects, however, rely on the leading-edge vortex [2](#ref-2){:.cite}.

{% include lens-end.html %}

{% include lens-start.html lens="math" %}

## Mathematics lens: why small flyers beat faster

**The lift of a moving wing.** A wing of area *S* that moves through air of density *ρ* at speed *U* produces the lift

<div class="formula" role="math" aria-label="L equals one half times rho times C L times S times U squared"><var>L</var> = ½ · <var>ρ</var> · <var>C</var><sub>L</sub> · <var>S</var> · <var>U</var><sup>2</sup></div>

where *C*<sub>L</sub> is the lift coefficient, a number that describes how well the wing is shaped and angled. A flapping wing of length *R* that sweeps through the stroke angle *Φ* with frequency *f* moves its tip on average at *U* = 2 *Φ R f* – two strokes per wingbeat. Aerodynamic forces therefore grow with the square of the tip speed, which is a product of stroke amplitude, wingbeat frequency and wing length [1](#ref-1){:.cite}.

**The square–cube law.** Now shrink an insect while keeping its shape: every length is multiplied by a factor *k*. The mass – and with it the weight *W* – falls with the volume, as *k*<sup>3</sup>; the wing area falls only as *k*<sup>2</sup>. To hover, lift must equal weight:

<div class="formula formula--steps"><span>½ <var>ρ</var> <var>C</var><sub>L</sub> <var>S</var> <var>U</var><sup>2</sup> = <var>W</var> ⇒ <var>U</var><sup>2</sup> ∝ <var>W</var>/<var>S</var> ∝ <var>k</var><sup>3</sup>/<var>k</var><sup>2</sup> = <var>k</var></span><span><var>f</var> = <var>U</var> / (2<var>Φ</var><var>R</var>) ∝ <var>k</var><sup>1/2</sup>/<var>k</var> = <var>k</var><sup>−1/2</sup></span></div>

The wings of a smaller insect need to move more slowly, but because they are so short, they must beat **faster**. A honeybee shrunk to half its length would need √2 ≈ 1.41 times the frequency: about 325 instead of 230 beats per second.

**What the data say.** Real insects are not scale models of each other – Diptera are shaped differently from butterflies. The mathematician Michael Deakin used dimensional analysis to derive a formula for the wingbeat frequency *n* from mass *m* and wing area *A* and tested it on more than 150 species [3](#ref-3){:.cite}:

<div class="formula" role="math" aria-label="n equals K times the square root of m divided by A"><var>n</var> = <var>K</var> · <span class="frac"><span class="frac__num">√<var>m</var></span><span class="frac__den"><var>A</var></span></span></div>

This formula explains 75 % of the variation in the measured frequencies; mass alone does not – among butterflies there is no significant correlation between mass and wingbeat frequency [3](#ref-3){:.cite}. For insects of the same shape, *m* ∝ *k*<sup>3</sup> and *A* ∝ *k*<sup>2</sup>, so √*m*/*A* ∝ *k*<sup>−1/2</sup> – the same law as above. The honeybee and the fruit fly show the limits of "same shape": with wings four times shorter, the fly would be expected to beat at about 450 Hz, yet it gets by with 200 Hz – by sweeping its wings through 1.6–1.8 times the angle [1](#ref-1){:.cite}.

**Power and weight.** How much power does hovering cost per newton of weight? A simple estimate treats the beating wings like a rotor that pushes air downwards: the power per weight is then the speed of the downwash, which grows with the square root of the weight per swept area, √(*W*/*ρ A*<sub>swept</sub>) ∝ *k*<sup>1/2</sup>. On paper, small flyers should hover more cheaply. In reality the air gets "stickier" for them: the lift-to-drag ratio of a wing deteriorates at low Reynolds numbers, and Weis-Fogh found that the aerodynamic power of hovering animals – between 1.3 and 4.7 W per newton of weight – does not vary systematically with size [4](#ref-4){:.cite}. In the fruit fly, the profile power – the cost of overcoming the drag of the wings – is about twice the induced power, the cost of producing lift [15](#ref-15){:.cite}.

For a machine, shrinking is worse. The weight falls with *k*<sup>3</sup>, but the heat an electric motor produces per unit of its mass grows as 1/*k*<sup>2</sup>, and friction grows relative to volume. The rotational accelerations of a flying body grow as 1/*k*, so its control must react ever faster [10](#ref-10){:.cite}. Power and weight diverge – which is why insect-sized robots need different motors altogether.

{% include lens-end.html %}

{% include lens-start.html lens="cs" %}

## Computer science lens: a simple model of a flapping wing

How large must the lift coefficient of a honeybee's wing be for it to hover? The program below answers this with a **quasi-steady model**: at every instant, the wing is treated as if it were moving steadily at its current speed, and the lift of all its strips is added up. The mass of 102 mg is an estimate for the honeybee from the literature [10](#ref-10){:.cite}; wing length (9.7 mm), wingbeat frequency (230 Hz), stroke amplitude (90°) and the densities of air and heliox are measured values [1](#ref-1){:.cite}. **Model assumptions:** the wing is a rectangle 3 mm wide, it sweeps horizontally and sinusoidally, and its lift coefficient is constant during the stroke.

```python
import numpy as np
import matplotlib.pyplot as plt

# Honeybee hovering – measured values, see the article
MASS = 102e-6              # body mass (kg)
WING_LENGTH = 9.7e-3       # wing length R, base to tip (m)
FREQUENCY = 230.0          # wingbeats per second (Hz)
AMPLITUDE = 90.0           # stroke amplitude Φ: the angle one wing sweeps (degrees)
AIR = 1.21                 # density of air (kg/m³)
HELIOX = 0.41              # density of heliox, an oxygen–helium mixture (kg/m³)
# Model assumptions
CHORD = 3.0e-3             # wing width (m): the wing as a rectangle of constant width
SCALE = 1.0                # shrink or grow the whole bee: lengths × SCALE, mass × SCALE³
G = 9.81                   # gravity (m/s²)
VISCOSITY = 1.8e-5         # dynamic viscosity of air (Pa·s)

mass, length, chord = MASS * SCALE**3, WING_LENGTH * SCALE, CHORD * SCALE
weight = mass * G
t = np.linspace(0, 2 / FREQUENCY, 801)           # two wingbeats


def stroke(amplitude_deg):
    """Sinusoidal stroke φ(t) = Φ/2 · sin(2πft) and its angular speed ω(t) = dφ/dt."""
    phi_max = np.radians(amplitude_deg) / 2
    phase = 2 * np.pi * FREQUENCY * t
    return phi_max * np.sin(phase), phi_max * 2 * np.pi * FREQUENCY * np.cos(phase)


def lift(lift_coefficient, omega, density):
    """Quasi-steady lift of both wings. A strip at distance r moves at u = ω·r and adds
    ½·ρ·C_L·c·u²·dr; summed from base to tip this gives ½·ρ·C_L·ω²·c·R³/3 per wing."""
    return 2 * 0.5 * density * lift_coefficient * omega**2 * chord * length**3 / 3


def needed_cl(amplitude_deg, density):
    """The lift coefficient at which the mean lift over a wingbeat equals the weight."""
    _, omega = stroke(amplitude_deg)
    return weight / lift(1.0, omega, density).mean()


tip_speed = 2 * np.radians(AMPLITUDE) * length * FREQUENCY   # two strokes of Φ·R per wingbeat
reynolds = AIR * tip_speed * chord / VISCOSITY
cl = needed_cl(AMPLITUDE, AIR)
angle, omega = stroke(AMPLITUDE)
force = lift(cl, omega, AIR)
print(f"weight {weight * 1e3:.2f} mN, mean wing-tip speed {tip_speed:.1f} m/s, "
      f"Reynolds number about {round(reynolds, -2):.0f}")
print(f"lift coefficient needed to hover: C_L = {cl:.1f}")
print(f"lift peaks at {force.max() / weight:.1f} × body weight in mid-stroke, 0 at each turn")
print(f"in heliox with the same stroke: C_L = {needed_cl(AMPLITUDE, HELIOX):.1f}; "
      f"with a 50 % wider stroke: C_L = {needed_cl(1.5 * AMPLITUDE, HELIOX):.1f}")

plt.rcParams["font.size"] = 13      # large type: the chart stays readable on a phone
fig, (top, bottom) = plt.subplots(2, 1, figsize=(6.4, 8.4), layout="constrained", sharex=True)
ms = t * 1e3
for ax in (top, bottom):
    for turn in np.arange(0.25, 2, 0.5) / FREQUENCY * 1e3:    # the four turns
        ax.axvline(turn, color="#c98a1b", lw=6, alpha=0.18)
top.plot(ms, np.degrees(angle), lw=2.5, color="black")
top.axhline(0, color="grey", lw=0.8)
top.set_ylabel("stroke angle φ (°)")
top.set_title("The wing sweeps forward and back")
top.text(0.25 / FREQUENCY * 1e3 + 0.07, -40, "turn:\nwing flips", fontsize=11)
bottom.plot(ms, force * 1e3, lw=2.5, label="lift, quasi-steady model")
bottom.axhline(weight * 1e3, color="black", ls="--", lw=1.5, label="body weight")
bottom.set_xlabel("time (ms)")
bottom.set_ylabel("lift (mN)")
bottom.set_ylim(0, 2.6)
bottom.set_title("Lift: peaks mid-stroke, zero at turns")
bottom.legend(loc="upper right", fontsize=11)
plt.show()
```
{% include code-result.html file="flapping_wing.py" label="Fig. 2" caption="Output of the program above: the quasi-steady model of a hovering honeybee over two wingbeats. Top: the stroke angle of the wing; the shaded bands mark the turns, where the wing flips over. Bottom: the lift of both wings compared with the body weight. The model assumes a rectangular wing and a constant lift coefficient." alt="Two charts stacked, time axis from 0 to 8.7 milliseconds. Top: the stroke angle swings sinusoidally between plus and minus 45 degrees, two full wingbeats; four shaded bands mark the turns at the extremes, one labelled turn, wing flips. Bottom: the lift of the quasi-steady model rises to about 2 millinewtons in the middle of each stroke and falls to zero at each turn; a dashed line at 1 millinewton marks the body weight, which the lift equals on average with a lift coefficient of 1.4." %}

What the result teaches:

- **The wing must work hard.** To carry its weight of 1.00 mN, the bee's wing needs an average lift coefficient of **1.4** – at a mean wing-tip speed of 7.0 m/s and a Reynolds number of about 1400. That is a demanding value: conventional aerodynamics accounts for only a third to a half of the lift insects need, and the leading-edge vortex helps to close the gap [2](#ref-2){:.cite} [14](#ref-14){:.cite}.
- **The model misses the turns.** In the quasi-steady model, lift peaks at 2.0 times the body weight in mid-stroke and drops to 0 at each turn. Measurements on a robotic bee wing show additional force peaks at the beginning and end of each stroke, from the rotation of the wing – a large part of the bee's lift [1](#ref-1){:.cite}. That is where the model breaks down; it is a first estimate, not the truth.
- **Thin air.** In heliox with the same stroke, the bee would need *C*<sub>L</sub> = 4.1 – out of reach. With a 50 % wider stroke, as the bees actually did, the requirement falls to 1.8. The wider stroke does most of the work; the rest has to come from the wing itself.

Try it yourself:

- Shrink the bee to half its size: set `SCALE = 0.5`. At the same frequency, the needed lift coefficient doubles to 2.8, and the Reynolds number falls to about 400 – the mathematics lens in action: a smaller insect has to beat faster.
- Use the lower wingbeat frequency that another study gives for honeybees: set `FREQUENCY = 197.0` [10](#ref-10){:.cite}. The needed lift coefficient rises to 1.9 – the result is sensitive to the frequency, because lift grows with its square.

{% include code-variant.html file="flapping_wing.py" id="half" replace="SCALE = 1.0 " with="SCALE = 0.5 " expect="2.8 400" %}
{% include code-variant.html file="flapping_wing.py" id="slower" replace="FREQUENCY = 230.0 " with="FREQUENCY = 197.0 " expect="1.9" %}

{% include lens-end.html %}

{% include lens-start.html lens="physical-ai" %}

## Physical AI lens: robot insects

For Physical AI – robots that sense and act in the physical world – insects set the standard: flies perform turns within milliseconds and land upside down on ceilings, with a nervous system of only 10<sup>5</sup>–10<sup>7</sup> neurons [10](#ref-10){:.cite}. Copying them means meeting the scaling laws of the mathematics lens head on.

**Artificial flight muscles.** Electric motors work poorly at insect size, so Robert Wood's group at Harvard University drives the wings of its robot insects, known as **RoboBees**, with **piezoelectric actuators**, thin layers that bend when a voltage is applied, in a muscle-like back-and-forth motion. Piezoelectric actuators scale down more favourably than electromagnetic motors [10](#ref-10){:.cite}. The robot's joints are thin flexures instead of hinges, made with a manufacturing method for rapid prototyping of articulated sub-millimetre mechanisms. In 2013, Kevin Ma and colleagues reported controlled flights of an 80 mg robot, modelled loosely on flies: stable hovering and basic flight manoeuvres, tethered to a thin wire but otherwise unconstrained [16](#ref-16){:.cite}.

**Staying upright.** Like many insects, the robot has its centre of mass below its wings, which makes it unstable like a pendulum standing on its head: without constant corrections, it tumbles. Sawyer Fuller and colleagues stabilised it with a 25 mg light sensor inspired by the ocelli of insects. The controller applies a torque in proportion to how fast the light from above appears to move – the first use of onboard sensors at this scale [10](#ref-10){:.cite}. Before, the corrections came from external cameras that tracked the robot [10](#ref-10){:.cite}. The RoboBee flapped at 120 Hz, a honeybee in the same study at 197 Hz [10](#ref-10){:.cite}.

**Cutting the wire.** In 2019, Noah Jafferis and colleagues flew a four-winged robot without a tether: a 90 mg vehicle with four wings driven by two piezoelectric actuators, a peak lift of 4.1 times its weight and, together with solar cells and the electronics that drive the actuators, 259 mg in total. It used 110–120 mW of power – according to the authors, the same thrust efficiency as similarly sized insects such as bees – and was the lightest vehicle so far to achieve sustained untethered flight [17](#ref-17){:.cite}.

**Soft muscles and robots as research tools.** Rigid microactuators break easily in collisions. Yufeng Chen and colleagues therefore built flying microrobots with **soft artificial muscles** – multilayered dielectric elastomer actuators of 100 mg each with a power density of 600 W/kg. These robots survive collisions with walls and with each other; their power and control, however, still come from outside, from offboard amplifiers and a motion-capture system [18](#ref-18){:.cite}. Larger flapping robots are useful to biology, too: Matěj Karásek and colleagues built a tailless, programmable flapping robot 55 times the size of a fruit fly that imitates its rapid escape manoeuvres. With the robot's yaw control switched off, it still turned towards the escape heading – showing that this turn in flies can arise passively from aerodynamic coupling [19](#ref-19){:.cite}.

**Where is the intelligence?** In today's insect robots, a large part of it sits outside: in external cameras, offboard amplifiers or, at best, a single light sensor and a simple control rule. A fly carries everything – sensors, a small brain, muscles and fuel – in a body of a few milligrams. Whether insect-sized robots will one day sense, decide and fly on their own power over long periods is an open question. The authors of the X-Wing see room for additional onboard devices in its payload capacity [17](#ref-17){:.cite}, and Karásek's group sees its robot as suitable for real-world flight missions [19](#ref-19){:.cite}; for fully autonomous robot insects, sensing and control at this scale [10](#ref-10){:.cite} and the high energy cost of flying small [17](#ref-17){:.cite} remain the big challenges.

{% include lens-end.html %}

## What we can learn from a bee

The bee that "could not fly" shows how a good question can come out of a bad calculation. The answer – a vortex that stays on the wing instead of being shed, wings that flip at every turn, muscles that oscillate by themselves and a gyroscope made from a pair of wings – took high-speed video, flow visualisation and mechanical and computer models to find [13](#ref-13){:.cite}.

Open questions remain: how bees and other insects without halteres keep their balance [10](#ref-10){:.cite}, how a comprehensive theory of the forces during the strokes and at the turns can explain the many wing motions of different insects [5](#ref-5){:.cite}, and how to build flying machines the size of an insect that carry their own power and their own intelligence. The reverse direction works, too: robots that fly like insects are becoming instruments for testing ideas about how insects fly [19](#ref-19){:.cite}.
