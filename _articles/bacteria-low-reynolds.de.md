---
id: bacteria-low-reynolds
lang: de
ref: bacteria-low-reynolds
title: "Schwimmen in Honig: die Physik der Bakterien"
short_title: "Schwimmen in Honig"
kicker: "Artikel · Strömungsmechanik"
description: "Für ein Bakterium ist Wasser zäh wie Honig: Trägheit spielt keine Rolle. Wie E. coli trotzdem schwimmt – mit Korkenzieher, Laufen und Taumeln."
dek: "Wärst du so klein wie ein Bakterium, fühlte sich Wasser an wie Honig. Sobald du aufhörst, dich zu bewegen, stehst du still – in einem Bruchteil einer Mikrosekunde. E. coli schwimmt trotzdem: mit einem rotierenden Korkenzieher und einer einfachen Regel, die es zur Nahrung lenkt."
date: 2026-10-03
permalink: /de/artikel/schwimmen-in-honig/
image: /assets/og/bacteria-low-reynolds-de.jpg
image_alt: "Schema eines Bakteriums E. coli in einem Nahrungsgefälle: Es schwimmt gerade Läufe mit gebündelten Flagellen, taumelt und startet in eine neue Richtung – Läufe zu mehr Nahrung dauern länger."
hero_figure: svg/bacteria-run-tumble.svg
hero_caption: "<span class=\"caption__label\">Abb. 1</span> Laufen und Taumeln. Während eines Laufs bündeln sich die rotierenden Flagellen von E. coli und schieben die Zelle wie ein Korkenzieher voran. Dreht ein Motor um, drehen sich die Flagellen nicht mehr gemeinsam, und die Zelle taumelt; der nächste Lauf beginnt in einer neuen Richtung. Läufe, die zu mehr Nahrung führen, dauern länger – so driftet die Zelle das Gefälle hinauf."
educational_level: "Intermediate"
keywords: ["Bakterien schwimmen", "Escherichia coli", "E. coli", "kleine Reynolds-Zahl", "Reynolds-Zahl", "Viskosität", "Leben bei kleiner Reynolds-Zahl", "Muschel-Theorem", "Bakteriengeißel", "Flagellenmotor", "Laufen und Taumeln", "Chemotaxis", "Zufallsbewegung", "Mikroroboter", "künstliche Bakteriengeißeln", "Physical AI"]
about:
  - { name: "Escherichia coli", wikidata: Q25419, wikipedia: "https://de.wikipedia.org/wiki/Escherichia_coli" }
  - { name: "Reynolds-Zahl", wikidata: Q178932, wikipedia: "https://de.wikipedia.org/wiki/Reynolds-Zahl" }
mentions:
  - { name: "Chemotaxis", wikidata: Q658145 }
  - { name: "Geißel (Biologie)", wikidata: Q189998 }
  - { name: "Muschel-Theorem", wikidata: Q7429791 }
  - { name: "Stokes-Strömung", wikidata: Q674202 }
  - { name: "Laufen und Taumeln", wikidata: Q110264195 }
  - { name: "Zufallsbewegung", wikidata: Q856741 }
  - { name: "Viskosität", wikidata: Q128709 }
dimensions:
  time: ["modern-era"]
  space: ["microcosm", "lab"]
  physics: ["fluid-dynamics", "mechanics", "thermodynamics"]
  adjacent_sciences: ["biology", "mathematics", "computer-science", "robotics", "physical-ai", "medical-technology", "bionics"]
beings: ["e-coli"]
lenses: ["biology", "physics", "math", "cs", "physical-ai"]
key_facts:
  - "Für ein Bakterium dominiert die Viskosität, Trägheit spielt keine Rolle: E. coli schwimmt bei einer Reynolds-Zahl von nur wenigen Hunderttausendsteln – Purcell schätzte **0,00003**. Stoppt sein Motor, gleitet es noch etwa 0,1 Ångström – weniger als ein Atom breit ist [1](#ref-1){:.cite}."
  - "Um wie ein Bakterium zu schwimmen, müsste ein Mensch in einem Becken voller Melasse liegen und dürfte keinen Körperteil schneller als 1 cm pro Minute bewegen [1](#ref-1){:.cite}. Honig allein reicht nicht: Darin kommt ein Schwimmer noch auf eine Reynolds-Zahl von mehreren Hundert."
  - "E. coli schwimmt, indem es seine schraubenförmigen Flagellen **dreht** – angetrieben von Rotationsmotoren mit etwa 100 Umdrehungen pro Sekunde [4](#ref-4){:.cite} [5](#ref-5){:.cite}."
  - "Seine Bahn wechselt zwischen geraden **Läufen** und kurzem **Taumeln**. Läufe zu mehr Nahrung dauern länger – eine einfache Regel, die die Zelle das Gefälle hinauf lenkt [1](#ref-1){:.cite}."
  - "Magnetische Mikroroboter kopieren den Korkenzieher der Bakteriengeißel und werden von äußeren Magnetfeldern gesteuert; sie werden für die Medizin entwickelt [9](#ref-9){:.cite} [10](#ref-10){:.cite} [12](#ref-12){:.cite}."
faq:
  - q: "Warum ist Wasser für ein Bakterium wie Honig?"
    a: "Entscheidend ist nicht die Flüssigkeit allein, sondern das Verhältnis von Trägheit zu zäher Reibung, die Reynolds-Zahl. Sie hängt von Größe und Geschwindigkeit des Schwimmers ab. Ein Bakterium ist wenige Mikrometer lang und schwimmt einige zehn Mikrometer pro Sekunde, seine Reynolds-Zahl liegt deshalb nur bei etwa 0,00003 bis 0,00006 – je nachdem, ob man seine Breite oder seine Länge als Größe nimmt. Ein Mensch käme auf einen so kleinen Wert nur in einer Flüssigkeit, die zäher ist als Honig, und wenn er sich extrem langsam bewegt."
  - q: "Wie schwimmt E. coli?"
    a: "E. coli hat mehrere dünne, schraubenförmige Flagellen. An der Basis jeder Flagelle sitzt ein Rotationsmotor, der sie etwa hundertmal pro Sekunde dreht. Während eines Laufs bündeln sich die Flagellen und wirken wie ein Korkenzieher, der die Zelle voranschiebt. Dreht ein Motor um, drehen sich die Flagellen nicht mehr gemeinsam, die Zelle taumelt und schwimmt dann in eine neue Richtung."
  - q: "Was ist das Muschel-Theorem?"
    a: "Bei kleiner Reynolds-Zahl kommt ein Schwimmer, der sich nur öffnet und schließt – wie eine Muschel mit einem einzigen Gelenk –, nicht vom Fleck: Was er mit dem einen Schlag gewinnt, verliert er auf dem Rückweg, egal wie schnell oder langsam er sich bewegt. Mikroorganismen nutzen deshalb Bewegungen, die nicht umkehrbar sind, etwa einen rotierenden Korkenzieher oder einen biegsamen, schlagenden Schwanz."
  - q: "Wie finden Bakterien Nahrung?"
    a: "E. coli kann nicht direkt steuern. Es schwimmt gerade Läufe und wechselt beim Taumeln zufällig die Richtung. Aber es vergleicht die Nahrungskonzentration über die Zeit: Wird es besser, läuft es länger bis zum nächsten Taumeln. Im Mittel trägt diese gerichtete Zufallsbewegung das Bakterium zu mehr Nahrung."
  - q: "Was sind Mikroroboter nach dem Vorbild von Bakterien?"
    a: "Das sind künstliche Schwimmer in der Größe eines Bakteriums, zum Beispiel winzige magnetische Korkenzieher in der Form einer Bakteriengeißel. Schwache Magnetfelder von außen treiben und steuern sie. Sie können kleine Teilchen schieben oder Chemikalien transportieren und werden für die Medizin entwickelt, etwa um Medikamente zu bringen; der Einsatz in der Medizin ist noch ein Forschungsziel."
sources:
  - authors: ["Purcell, E. M."]
    year: 1977
    title: "Life at low Reynolds number"
    journal: "American Journal of Physics"
    volume: 45
    pages: "3–11"
    doi: "10.1119/1.10903"
  - authors: ["Afonso, M.", "Magalhães, M.", "Fernandes, L.", "Castro, M.", "Ramalhosa, E."]
    year: 2018
    title: "Temperature effect on rheological behavior of Portuguese honeys"
    journal: "Polish Journal of Food and Nutrition Sciences"
    volume: 68
    pages: "217–222"
    doi: "10.1515/pjfns-2017-0030"
    open_access: true
  - authors: ["Lauga, E.", "Powers, T. R."]
    year: 2009
    title: "The hydrodynamics of swimming microorganisms"
    journal: "Reports on Progress in Physics"
    volume: 72
    pages: "096601"
    doi: "10.1088/0034-4885/72/9/096601"
    open_access: true
  - authors: ["Berg, H. C.", "Anderson, R. A."]
    year: 1973
    title: "Bacteria swim by rotating their flagellar filaments"
    journal: "Nature"
    volume: 245
    pages: "380–382"
    doi: "10.1038/245380a0"
  - authors: ["Turner, L.", "Ryu, W. S.", "Berg, H. C."]
    year: 2000
    title: "Real-time imaging of fluorescent flagellar filaments"
    journal: "Journal of Bacteriology"
    volume: 182
    pages: "2793–2801"
    doi: "10.1128/JB.182.10.2793-2801.2000"
    open_access: true
  - authors: ["Berg, H. C.", "Purcell, E. M."]
    year: 1977
    title: "Physics of chemoreception"
    journal: "Biophysical Journal"
    volume: 20
    pages: "193–219"
    doi: "10.1016/S0006-3495(77)85544-6"
    open_access: true
  - authors: ["Purcell, E. M."]
    year: 1997
    title: "The efficiency of propulsion by a rotating flagellum"
    journal: "Proceedings of the National Academy of Sciences"
    volume: 94
    pages: "11307–11311"
    doi: "10.1073/pnas.94.21.11307"
    open_access: true
  - authors: ["Dhariwal, A.", "Sukhatme, G. S.", "Requicha, A. A. G."]
    year: 2004
    title: "Bacterium-inspired robots for environmental monitoring"
    journal: "Proceedings of the IEEE International Conference on Robotics and Automation (ICRA 2004)"
    volume: 2
    pages: "1436–1443"
    doi: "10.1109/ROBOT.2004.1308026"
  - authors: ["Zhang, L.", "Abbott, J. J.", "Dong, L.", "Kratochvil, B. E.", "Bell, D.", "Nelson, B. J."]
    year: 2009
    title: "Artificial bacterial flagella: fabrication and magnetic control"
    journal: "Applied Physics Letters"
    volume: 94
    pages: "064107"
    doi: "10.1063/1.3079655"
  - authors: ["Ghosh, A.", "Fischer, P."]
    year: 2009
    title: "Controlled propulsion of artificial magnetic nanostructured propellers"
    journal: "Nano Letters"
    volume: 9
    pages: "2243–2245"
    doi: "10.1021/nl900186w"
  - authors: ["Dreyfus, R.", "Baudry, J.", "Roper, M. L.", "Fermigier, M.", "Stone, H. A.", "Bibette, J."]
    year: 2005
    title: "Microscopic artificial swimmers"
    journal: "Nature"
    volume: 437
    pages: "862–865"
    doi: "10.1038/nature04090"
  - authors: ["Nelson, B. J.", "Kaliakatsos, I. K.", "Abbott, J. J."]
    year: 2010
    title: "Microrobots for minimally invasive medicine"
    journal: "Annual Review of Biomedical Engineering"
    volume: 12
    pages: "55–85"
    doi: "10.1146/annurev-bioeng-010510-103409"
  - authors: ["Sitti, M.", "Ceylan, H.", "Hu, W.", "Giltinan, J.", "Turan, M.", "Yim, S.", "Diller, E."]
    year: 2015
    title: "Biomedical applications of untethered mobile milli/microrobots"
    journal: "Proceedings of the IEEE"
    volume: 103
    pages: "205–224"
    doi: "10.1109/JPROC.2014.2385105"
status: published
---

## Leben, wo sich Wasser wie Honig anfühlt

Stell dir vor, du wärst so klein wie ein Bakterium. Wasser, das einen Schwimmer trägt und ein Boot gleiten lässt, benimmt sich plötzlich wie ein dicker Sirup. Hörst du auf zu paddeln, gleitest du nicht weiter – du stehst sofort still. Der Physiker Edward Purcell hat diese Welt 1976 in einem berühmten Vortrag beschrieben, 1977 veröffentlicht: Für ein Bakterium spielt **Trägheit überhaupt keine Rolle**; was es in jedem Moment tut, bestimmen allein die Kräfte, die genau in diesem Moment auf es wirken [1](#ref-1){:.cite}.

Purcells Bild war anschaulich. Um so zu schwimmen wie ein Mikroorganismus, müsstest du in einem Schwimmbecken voller Melasse liegen – und dürftest keinen Teil deines Körpers schneller als 1 cm pro Minute bewegen. Schaffst du unter diesen Regeln in ein paar Wochen ein paar Meter, giltst du als Schwimmer bei kleiner Reynolds-Zahl [1](#ref-1){:.cite}. Honig täte es fast genauso gut wie Melasse: Selbst ein dünnflüssiger Rosmarinhonig ist bei 30 °C über 6.000-mal so zäh wie Wasser [2](#ref-2){:.cite} [1](#ref-1){:.cite}. Doch wie die Physik-Linse zeigt, reicht eine zähe Flüssigkeit allein nicht – die Langsamkeit zählt genauso.

In dieser Welt lebt die überwältigende Mehrheit der Organismen [1](#ref-1){:.cite}. Mikroorganismen wie das Darmbakterium *Escherichia coli* schwimmen jede Sekunde darin [1](#ref-1){:.cite} [3](#ref-3){:.cite}. Dieser Artikel erklärt, wie sie das schaffen – und warum heute winzige Roboter nach ihrem Vorbild gebaut werden.

## Laufen und Taumeln in drei Schritten

1. **Laufen.** Mehrere dünne, schraubenförmige Flagellen drehen sich mit etwa 100 Umdrehungen pro Sekunde [4](#ref-4){:.cite} [5](#ref-5){:.cite}. Sie bündeln sich und schieben die Zelle wie ein Korkenzieher voran, mit typischerweise 20–40 µm pro Sekunde, ein bis zwei Sekunden lang [1](#ref-1){:.cite}.
2. **Taumeln.** Ein oder mehrere Motoren drehen um, die Flagellen drehen sich nicht mehr gemeinsam, und die Zelle taumelt auf der Stelle. Schon eine einzige umkehrende Flagelle kann ein Taumeln auslösen [5](#ref-5){:.cite}.
3. **Neue Richtung.** Die Zelle startet einen neuen Lauf in eine neue Richtung. Wird es besser – mehr Nahrung –, läuft sie länger, bevor sie wieder taumelt [1](#ref-1){:.cite}.

{% include lens-tabs.html lenses="biology,physics,math,cs,physical-ai" %}

{% include lens-start.html lens="biology" %}

## Biologie-Linse: ein Rotationsmotor und ein Geruchssinn

*E. coli* ist ein stäbchenförmiges Bakterium, etwa 2 µm lang [1](#ref-1){:.cite}. Es trägt mehrere Flagellen; jede ist einige Mikrometer lang, aber nur etwa 20 Nanometer dick [5](#ref-5){:.cite}. Lange glaubte man, solche Flagellen schlügen wie ein Schwanz. 1973 argumentierten Howard Berg und Robert Anderson, dass Bakterien schwimmen, indem sie ihre Flagellen **drehen** [4](#ref-4){:.cite}, und Experimente bestätigten das bald: Klebte der Haken an der Basis einer Flagelle auf einem Objektträger fest, drehte sich der ganze Zellkörper mit konstanter Geschwindigkeit [1](#ref-1){:.cite}. An der Basis jeder Flagelle sitzt ein echter Rotationsmotor, und er kann sich in beide Richtungen drehen [1](#ref-1){:.cite}.

Die Drehrichtung der Motoren entscheidet zwischen Laufen und Taumeln. Filmt man die Flagellen in Echtzeit, zeigt sich, wie vielfältig das Taumeln ist: Nicht jede Flagelle muss umkehren, und ein Taumeln kann schon von einer einzigen ausgelöst werden [5](#ref-5){:.cite}. Beim Taumeln ändern die Flagellen außerdem ihre Form – sie wechseln zwischen verschiedenen Schraubenformen [5](#ref-5){:.cite}.

Warum überhaupt schwimmen? Nicht, um das Wasser umzurühren: Zu einem Bakterium gelangt Nahrung durch Diffusion, und Rühren rund um die Zelle bringt nichts [1](#ref-1){:.cite}. Schwimmen lohnt sich anders – es trägt die Zelle an Orte, an denen es mehr Nahrung gibt. Berg verfolgte einzelne Bakterien in drei Dimensionen und fand, dass sie sich allmählich ein Gefälle eines Lockstoffs hinaufarbeiten. Die Regel, der sie folgen, ist einfach: **Wenn es besser wird, hör nicht so früh auf** [1](#ref-1){:.cite}. Läufe das Gefälle hinauf werden länger; Läufe hinab werden nicht kürzer [1](#ref-1){:.cite}.

Um einem Gefälle zu folgen, muss eine Zelle Konzentrationen messen. Berg und Purcell berechneten, wie genau eine Zelle physikalisch messen kann, die Moleküle mit Rezeptoren auf ihrer Oberfläche zählt – und fanden, dass die chemotaktische Empfindlichkeit von *E. coli* nahe an die einer optimal gebauten Zelle heranreicht [6](#ref-6){:.cite}. Diese Fähigkeit, sich nach chemischen Signalen zu richten, heißt **Chemotaxis**.

{% include lens-end.html %}

{% include lens-start.html lens="physics" %}

## Physik-Linse: wenn Zähigkeit die Trägheit schlägt

Ob ein Schwimmer gleitet oder sofort stillsteht, entscheidet eine einzige dimensionslose Zahl, die **Reynolds-Zahl**. Sie vergleicht die Trägheitskräfte in einer Strömung mit den Reibungskräften [1](#ref-1){:.cite}:

<div class="formula" role="math" aria-label="Re gleich rho mal v mal L geteilt durch eta"><var>Re</var> = <span class="frac"><span class="frac__num"><var>ρ</var> · <var>v</var> · <var>L</var></span><span class="frac__den"><var>η</var></span></span></div>

Dabei ist *ρ* die Dichte der Flüssigkeit, *η* ihre Viskosität, *v* die Geschwindigkeit des Schwimmers und *L* seine Größe. Für *E. coli* – größenordnungsmäßig 1 µm groß, mit 30 µm/s in Wasser – schätzte Purcell **Re ≈ 3 · 10<sup>−5</sup>** [1](#ref-1){:.cite}. Bei solchen Werten kann man die Trägheitsterme der Navier-Stokes-Gleichung weglassen; was übrig bleibt, beschreibt die **Stokes-Strömung**, und sie hat kein Gedächtnis [1](#ref-1){:.cite} [3](#ref-3){:.cite}.

Das Programm unten berechnet die Reynolds-Zahl für ein paar Schwimmer und stellt die Honig-Frage: Wie nah kommt ein Mensch in Honig an die Welt eines Bakteriums? Größe, Geschwindigkeit und die Dichte von Honig sind **grobe typische Werte** zur Veranschaulichung; die Viskosität von Honig ist der gemessene Wert für einen dünnflüssigen Rosmarinhonig bei 30 °C [2](#ref-2){:.cite}, die von Wasser 1 mPa·s [1](#ref-1){:.cite}.

```python
import numpy as np
import matplotlib.pyplot as plt

# Flüssigkeiten: Dichte (kg/m³) und Viskosität (Pa·s)
WATER = (1000, 1.0e-3)       # Wasser: Viskosität 1 mPa·s
HONEY = (1400, 6.1)          # dünnflüssiger Honig: 6,1 Pa·s (Rosmarinhonig, 30 °C); Dichte angenommen
COLI_FLUID = WATER           # die Flüssigkeit, in der E. coli schwimmt
# Schwimmer: (Name, Größe L in m, Geschwindigkeit v in m/s, Flüssigkeit) – grobe typische Werte, siehe Text
SWIMMERS = [
    ("Mensch in Wasser", 1.8, 1.0, WATER),
    ("Goldfisch", 0.05, 0.1, WATER),
    ("Mensch in Honig", 1.8, 1.0, HONEY),
    ("Mensch in Honig, 1 cm/min", 1.8, 0.01 / 60, HONEY),
    ("E. coli", 2e-6, 30e-6, COLI_FLUID),
]


def reynolds(size, speed, fluid):
    """Re = ρ·v·L/η: Trägheitskräfte geteilt durch Reibungskräfte."""
    density, viscosity = fluid
    return density * speed * size / viscosity


for name, size, speed, fluid in SWIMMERS:
    print(f"{name:27s} Re = {reynolds(size, speed, fluid):8.1g}")

# Wie weit gleitet E. coli, wenn sein Motor stoppt? Eine Kugel mit Radius a wird in einer zähen
# Flüssigkeit exponentiell langsamer, mit der Zeitkonstante τ = m / (6πηa) (Stokes-Reibung).
radius, speed, cell_density = 1e-6, 30e-6, 1000      # m, m/s, kg/m³ (Zelle ≈ Wasser)
mass = cell_density * 4 / 3 * np.pi * radius**3
tau = mass / (6 * np.pi * WATER[1] * radius)
print(f"E. coli steht nach {tau * 1e6:.1g} µs still und gleitet {speed * tau * 1e10:.1g} Å weit "
      f"(ein Atom ist grob 1 Å groß)")

SUPERSCRIPT = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")


def power_of_ten(value, _pos=None):
    """Achsenbeschriftung 10⁻⁴ als einfacher Text (ohne Mathtext)."""
    return "10" + str(int(round(np.log10(value)))).translate(SUPERSCRIPT)


names = [s[0] for s in SWIMMERS]
values = [reynolds(*s[1:]) for s in SWIMMERS]
plt.rcParams["font.size"] = 13      # große Schrift: das Diagramm bleibt auf dem Handy lesbar
fig, ax = plt.subplots(figsize=(6.4, 5.4), layout="constrained")
ax.axvspan(1e-6, 1, color="#c98a1b", alpha=0.12)
ax.axvline(1, color="black", lw=1.5, ls="--")
ax.text(1.6e-6, 4.6, "Zähigkeit gewinnt", fontsize=11)
ax.text(2, 4.6, "Trägheit gewinnt", fontsize=11)
for row, (name, value) in enumerate(zip(names, values)):
    ax.plot(value, row, "o", ms=9, color="black")
    near_line = 1e-3 < value < 1        # diese Beschriftung bleibt links der gestrichelten Linie
    ax.annotate(name, (value, row), xytext=(8 if near_line else 0, 10), textcoords="offset points",
                ha="right" if near_line else "center", fontsize=11)
ax.set_xscale("log")
ax.set_xlim(1e-6, 1e8)
ax.set_ylim(4.9, -0.7)
ax.set_yticks([])
ax.xaxis.set_major_locator(plt.LogLocator(numticks=8))
ax.xaxis.set_major_formatter(power_of_ten)
ax.set_xlabel("Reynolds-Zahl Re = ρvL/η (log. Skala)")
ax.set_title("Bakterien leben weit unter Re = 1")
plt.show()
```
{% include code-result.html file="reynolds.py" label="Abb. 2" caption="Ausgabe des Programms oben: die Reynolds-Zahlen von fünf Schwimmern auf einer logarithmischen Achse. Links der gestrichelten Linie bei Re = 1 gewinnt die Zähigkeit, rechts davon die Trägheit. Größen, Geschwindigkeiten und die Dichte von Honig sind typische Werte zur Veranschaulichung." alt="Punktdiagramm auf einer logarithmischen Achse von 10 hoch minus 6 bis 10 hoch 8. Ein schattierter Bereich links einer gestrichelten Linie bei Re = 1 ist mit Zähigkeit gewinnt beschriftet, der Bereich rechts mit Trägheit gewinnt. Ein Mensch, der in Wasser schwimmt, liegt bei etwa 2 Millionen, ein Goldfisch bei etwa 5.000, ein Mensch, der in Honig schwimmt, bei etwa 400 – alle auf der Seite der Trägheit. Ein Mensch in Honig mit 1 Zentimeter pro Minute liegt bei etwa 0,07, E. coli in Wasser bei etwa 0,00006 – beide auf der Seite der Zähigkeit." %}

Was das Ergebnis zeigt:

- **Honig allein reicht nicht.** Ein Mensch, der normal in Honig schwimmt, kommt noch auf Re ≈ 400 – die Trägheit zählt noch. Erst wenn er sich zusätzlich auf 1 cm pro Minute verlangsamt, wie in Purcells Regel, fällt die Reynolds-Zahl unter 1 (0,07).
- **Das Bakterium lebt in einer eigenen Welt.** Mit Re ≈ 6 · 10<sup>−5</sup> – doppelt so viel wie Purcells Wert, weil das Programm die Zelllänge von 2 µm nimmt – liegt *E. coli* mehr als tausendmal unter selbst dem langsamen Menschen in Honig. Unsere Schätzung für einen schwimmenden Menschen, 2 · 10<sup>6</sup>, liegt höher als Purcells grober Wert von 10<sup>4</sup> [1](#ref-1){:.cite}; es kommt auf die Größenordnung an, und mit 1,8 m Körperlänge und 1 m/s liefert die Formel Millionen.
- **Kein Ausgleiten.** Stoppt sein Motor, steht das Bakterium nach 0,2 µs still und gleitet 0,07 Å weit – ein Bruchteil eines Atomdurchmessers. Purcell nannte dieselbe Größenordnung: etwa 0,1 Å in deutlich weniger als einer Mikrosekunde [1](#ref-1){:.cite}.

Probier es selbst:

- Setz *E. coli* in Honig: `COLI_FLUID = HONEY`. Seine Reynolds-Zahl fällt auf 1e-08 – doch für das Bakterium ändert sich kaum etwas: Es war schon tief in der zähen Welt.
- Lass den Menschen 1 cm pro Sekunde statt pro Minute schwimmen: Ändere `0.01 / 60` zu `0.01`. Die Reynolds-Zahl steigt auf 4 – wieder über 1.

{% include code-variant.html file="reynolds.py" id="coli-honey" replace="COLI_FLUID = WATER" with="COLI_FLUID = HONEY" expect="1e-08" %}
{% include code-variant.html file="reynolds.py" id="faster" replace="0.01 / 60" with="0.01" expect="4" %}

**Das Muschel-Theorem.** Weil die Zeit aus der Stokes-Strömung herausfällt, kommt ein Schwimmer, der seine Bewegung einfach umkehrt, nicht vom Fleck. Purcells Beispiel ist eine Kammmuschel: Sie öffnet ihre Schale langsam und schließt sie schnell, doch mit nur einem Gelenk kann sie sich nur hin und her bewegen – und bei kleiner Reynolds-Zahl landete sie genau dort, wo sie angefangen hat, egal wie schnell oder langsam sie sich bewegt [1](#ref-1){:.cite}. Ein Mikroschwimmer braucht eine Bewegung, die nicht umkehrbar ist: ein **biegsames Ruder**, das sich beim Schlag in die eine und auf dem Rückweg in die andere Richtung biegt, oder einen **Korkenzieher**, der sich immer weiterdreht [1](#ref-1){:.cite}.

**Wie ein Korkenzieher schiebt.** Eine zähe Flüssigkeit bremst einen dünnen Faden stärker, wenn er sich quer bewegt, als wenn er sich längs bewegt [1](#ref-1){:.cite} [3](#ref-3){:.cite}. Dieser Unterschied macht aus Drehung Vortrieb: Eine Schraube, die man dreht, bewegt sich zwangsläufig vorwärts, und eine Schraube, die man zieht, dreht sich zwangsläufig [7](#ref-7){:.cite}. Purcell schätzte, dass eine Kugel mit einem solchen Schraubenantrieb nur etwa **1 %** der Arbeit des Motors in nützlichen Vortrieb umsetzt [1](#ref-1){:.cite}. Dem Bakterium ist das fast egal: Mit 30 µm/s zu schwimmen kostet es etwa 0,5 W pro Kilogramm, einen kleinen Teil seines Energiebudgets [1](#ref-1){:.cite}.

{% include lens-end.html %}

{% include lens-start.html lens="math" %}

## Mathematik-Linse: eine Zufallsbewegung mit Vorliebe

**Der Diffusion davonschwimmen.** Nahrungsmoleküle breiten sich durch Diffusion aus. In einer Zeit *t* kommen sie etwa √(*D t*) weit, wobei *D* ihre Diffusionskonstante ist – für typische kleine Moleküle in Wasser etwa 10<sup>−5</sup> cm<sup>2</sup>/s, also 1.000 µm<sup>2</sup>/s [1](#ref-1){:.cite}. Schwimmend legt die Zelle eine Strecke *ℓ* in der Zeit *ℓ*/*v* zurück; die Diffusion braucht dafür etwa *ℓ*<sup>2</sup>/*D*. Schwimmen gewinnt nur, wenn

<div class="formula" role="math" aria-label="l ist mindestens D geteilt durch v"><var>ℓ</var> ≥ <span class="frac"><span class="frac__num"><var>D</var></span><span class="frac__den"><var>v</var></span></span></div>

Mit *v* = 30 µm/s ergibt das etwa **30 µm** – ungefähr die Länge eines Bakterienlaufs. „Wenn du nicht so weit schwimmst, bist du nirgends hingekommen“, wie Purcell es sinngemäß ausdrückte [1](#ref-1){:.cite}.

**Laufen und Taumeln breitet sich aus wie Diffusion.** Modellieren wir das Bakterium in zwei Dimensionen: Es läuft mit der Geschwindigkeit *v*, jeder Lauf dauert eine zufällige Zeit mit dem Mittelwert *τ*, und jedes Taumeln wählt eine völlig neue Richtung. Laufzeiten dieser Art folgen einer Exponentialverteilung, bei der das mittlere Quadrat der Dauer 2*τ*<sup>2</sup> beträgt. Ein Lauf legt also im Mittel die quadrierte Strecke 2*v*<sup>2</sup>*τ*<sup>2</sup> zurück, und in einer Zeit *t* gibt es etwa *t*/*τ* unabhängige Läufe:

<div class="formula formula--steps"><span>⟨<var>r</var><sup>2</sup>⟩ ≈ (<var>t</var>/<var>τ</var>) · 2<var>v</var><sup>2</sup><var>τ</var><sup>2</sup> = 2<var>v</var><sup>2</sup><var>τ</var> <var>t</var></span><span>⟨<var>r</var><sup>2</sup>⟩ = 4<var>D</var><var>t</var> in 2D ⇒ <var>D</var> = <var>v</var><sup>2</sup><var>τ</var> / 2</span></div>

Mit *v* = 20 µm/s und *τ* = 1 s ist *D* = 200 µm<sup>2</sup>/s – eine Population schwimmender Bakterien breitet sich etwa fünfmal langsamer aus, als ein kleines Molekül diffundiert.

**Die Vorliebe.** Nun sollen Läufe, die das Gefälle hinauf zeigen (nach +*x*), im Mittel *b*-mal länger dauern. Nach einem Taumeln zeigt die neue Richtung mit der Wahrscheinlichkeit ½ das Gefälle hinauf. Gewichtet mit ihrer Dauer nehmen Läufe hinauf den Anteil *b*/(1 + *b*) der Zeit ein, Läufe hinab 1/(1 + *b*). Gemittelt über alle Richtungen einer Hälfte ist die Geschwindigkeitskomponente entlang *x* gleich (2/π) *v*. Die Driftgeschwindigkeit ist deshalb

<div class="formula" role="math" aria-label="Driftgeschwindigkeit gleich v mal 2 durch pi mal b minus 1 durch b plus 1"><var>v</var><sub>Drift</sub> = <var>v</var> · <span class="frac"><span class="frac__num">2</span><span class="frac__den">π</span></span> · <span class="frac"><span class="frac__num"><var>b</var> − 1</span><span class="frac__den"><var>b</var> + 1</span></span></div>

Für *b* = 2 – Läufe hinauf dauern doppelt so lang – beträgt die Drift (2/π) · (1/3) ≈ 21 % der Schwimmgeschwindigkeit. Die Informatik-Linse prüft dieses Ergebnis mit einer Simulation.

{% include lens-end.html %}

{% include lens-start.html lens="cs" %}

## Informatik-Linse: Laufen und Taumeln als Algorithmus

Das Bakterium hat keine Karte und kein Gehirn. Es kann nicht einmal wahrnehmen, in welcher Richtung die Nahrung liegt – es merkt nur, ob es mit der Zeit besser wird. Sein Suchalgorithmus passt in eine Zeile: **Wenn es besser wird, hör nicht so früh auf** [1](#ref-1){:.cite}. Das Programm unten simuliert 2.000 Bakterien mit und ohne diese Regel. Die Geschwindigkeit von 20 µm/s liegt in dem Bereich, den Berg gemessen hat [1](#ref-1){:.cite}; die mittlere Laufzeit von 1 s, der Faktor 2 für Läufe hinauf und die völlig zufällige neue Richtung nach jedem Taumeln sind **Modellannahmen**.

```python
import numpy as np
import matplotlib.pyplot as plt

# Modellparameter – typische Werte, siehe Artikel
SPEED = 20.0       # Schwimmgeschwindigkeit im Lauf (µm/s); Berg maß 20–40 µm/s
RUN_TIME = 1.0     # mittlere Laufdauer (s), wenn nichts besser wird
BOOST = 2.0        # Läufe das Nahrungsgefälle hinauf dauern im Mittel BOOST-mal länger
N_CELLS = 2000     # Bakterien pro Population
T_END = 100.0      # simulierte Zeit (s)
DT = 0.01          # Zeitschritt (s)
rng = np.random.default_rng(1)


def swim(boost):
    """Laufen und Taumeln in 2D. Nach +x gibt es mehr Nahrung, „besser werden“ heißt also: nach +x.

    Ein Taumeln dauert keine Zeit und wählt eine völlig zufällige neue Richtung (eine Vereinfachung).
    In jedem Schritt taumelt eine Zelle mit der Wahrscheinlichkeit DT / mittlere Laufdauer. Bergs
    Regel: Wenn es besser wird, hör nicht so früh auf – Läufe nach +x dauern RUN_TIME × boost.
    """
    steps = int(T_END / DT)
    angle = rng.uniform(0, 2 * np.pi, N_CELLS)
    track = np.zeros((steps + 1, N_CELLS, 2))
    for i in range(steps):
        heading = np.column_stack((np.cos(angle), np.sin(angle)))
        track[i + 1] = track[i] + SPEED * DT * heading
        mean_run = np.where(heading[:, 0] > 0, RUN_TIME * boost, RUN_TIME)
        tumble = rng.random(N_CELLS) < DT / mean_run
        angle = np.where(tumble, rng.uniform(0, 2 * np.pi, N_CELLS), angle)
    return track


t = np.arange(int(T_END / DT) + 1) * DT
late = t > 20                     # Fit nach den ersten Läufen, wenn der Start vergessen ist
plain = swim(boost=1.0)
biased = swim(boost=BOOST)

# 1) Ohne Gefälle: eine Zufallsbewegung. Ausbreitung <r²> = 4 D t mit D = v² τ / 2 in 2D.
msd = (plain ** 2).sum(axis=2).mean(axis=1)
d_sim = np.polyfit(t[late], msd[late], 1)[0] / 4
print(f"Zufallsbewegung: D = {d_sim:.0f} µm²/s (Formel v²τ/2 = {SPEED**2 * RUN_TIME / 2:.0f} µm²/s)")

# 2) Bergs Regel: Die Population driftet das Gefälle hinauf. Formel: v · (2/π) · (b − 1)/(b + 1).
drift_sim = np.polyfit(t[late], biased[late, :, 0].mean(axis=1), 1)[0]
drift_theory = SPEED * 2 / np.pi * (BOOST - 1) / (BOOST + 1)
# round(...) + 0.0 macht aus einem gerundeten „-0.0“ ein „0.0“
print(f"mit der Regel: Drift {round(drift_sim, 1) + 0.0} µm/s (Formel {drift_theory:.1f} µm/s), "
      f"{round(100 * drift_sim / SPEED) + 0} % der Schwimmgeschwindigkeit")
print(f"nach {T_END:.0f} s ist die mittlere Zelle {biased[-1, :, 0].mean():.0f} µm weiter oben im Gefälle")

plt.rcParams["font.size"] = 13      # große Schrift: das Diagramm bleibt auf dem Handy lesbar
fig, (top, bottom) = plt.subplots(2, 1, figsize=(6.4, 8.4), layout="constrained")
for k, style in zip(range(3, 6), ["-", "--", ":"]):   # drei der Zellen, erste 60 s
    path = biased[: int(60 / DT) : 5, k]
    top.plot(path[:, 0], path[:, 1], style, lw=1.6, label=f"Zelle {k}")
top.plot(0, 0, "ko", ms=6)
top.annotate("Start", (0, 0), textcoords="offset points", xytext=(6, -16))
top.set_aspect("equal", adjustable="datalim")
top.set_xlabel("x (µm) – rechts mehr Nahrung →")
top.set_ylabel("y (µm)")
top.set_title("Laufen und Taumeln: drei Zellen, 60 s")
top.legend(loc="upper left", fontsize=11)

bottom.plot(t, biased[..., 0].mean(axis=1), lw=2.5, label="Läufe nach oben dauern länger")
bottom.plot(t, plain[..., 0].mean(axis=1), "--", lw=2, label="ohne Regel: alle Läufe gleich")
bottom.set_xlabel("Zeit (s)")
bottom.set_ylabel("mittlere Position x (µm)")
bottom.set_title("Eine einfache Regel führt bergauf")
bottom.legend(loc="upper left", fontsize=11)
plt.show()
```
{% include code-result.html file="run_and_tumble.py" label="Abb. 3" caption="Ausgabe des Programms oben. Oben: die Bahnen von drei simulierten Bakterien über 60 Sekunden; gerade Läufe wechseln sich mit Taumeln ab, rechts liegt mehr Nahrung. Unten: die mittlere Position von 2.000 Bakterien über die Zeit – mit der Regel (Läufe hinauf dauern länger) driftet die Population stetig das Gefälle hinauf, ohne sie bleibt sie, wo sie gestartet ist." alt="Zwei Diagramme übereinander. Oben: drei Zickzackbahnen, die im Ursprung beginnen und aus geraden Stücken unterschiedlicher Länge bestehen; nach 60 Sekunden enden sie etwa 250 bis 420 Mikrometer rechts vom Start. Unten: mittlere Position entlang x über 100 Sekunden; eine durchgezogene Linie für die Population mit der Regel steigt gleichmäßig auf etwa 416 Mikrometer, eine gestrichelte Linie für die Population ohne Regel bleibt nahe null." %}

Was das Ergebnis zeigt:

- **Die Simulation bestätigt die Mathematik.** Ohne die Regel breiten sich die Bakterien mit *D* ≈ 195 µm<sup>2</sup>/s aus; die Formel *v*<sup>2</sup>*τ*/2 liefert 200 µm<sup>2</sup>/s. Mit der Regel driftet die Population mit 4,3 µm/s; die Formel der Mathematik-Linse liefert 4,2 µm/s. Die kleinen Abweichungen sind zufällig und ändern sich mit dem Seed.
- **Eine schwache Vorliebe genügt.** Keine einzelne Zelle schwimmt geradewegs zur Nahrung; jede Bahn sieht aus wie ein zufälliges Zickzack. Trotzdem driftet die Population mit etwa einem Fünftel der Schwimmgeschwindigkeit und ist nach 100 s im Mittel 416 µm weiter oben im Gefälle.
- **Verglichen wird nur die Zeit, nicht der Raum.** Das Programm nutzt die Richtung des Gefälles nie zum Steuern – nur, um zu entscheiden, ob es besser wird. Mehr kann eine Zelle von 2 µm nicht messen.

Probier es selbst:

- Setz `BOOST = 1.0`: Die Regel ist ausgeschaltet, die Drift fällt auf 0,0 µm/s.
- Setz `BOOST = 4.0`: Läufe hinauf dauern viermal so lang, und die Drift steigt auf etwa 7,6 µm/s – die Formel sagt 7,6 µm/s voraus.

{% include code-variant.html file="run_and_tumble.py" id="off" replace="BOOST = 2.0 " with="BOOST = 1.0 " expect="0.0" %}
{% include code-variant.html file="run_and_tumble.py" id="strong" replace="BOOST = 2.0 " with="BOOST = 4.0 " expect="7.6" %}

**Von Bakterien zu Robotern.** Derselbe Algorithmus funktioniert für Maschinen, die die Quelle eines Signals suchen. Amit Dhariwal und Kollegen entwickelten Roboter, die mit einer gerichteten Zufallsbewegung nach dem Vorbild der Chemotaxis zur Quelle eines Signals finden, testeten das in umfangreichen Simulationen und an einem kleinen Roboter, der Licht folgte. In ihrem Vergleich war der Gradientenabstieg – immer in Richtung des steilsten Anstiegs – schneller, doch die Bakterienstrategie schnitt bei mehreren Quellen und bei Quellen, die sich verflüchtigen, besser ab, und sie eignete sich besser, um den Rand eines Gebiets abzudecken [8](#ref-8){:.cite}.

{% include lens-end.html %}

{% include lens-start.html lens="physical-ai" %}

## Physical-AI-Linse: Mikroroboter nach dem Vorbild der Geißel

Für die Physical AI – Roboter, die in der echten Welt wahrnehmen und handeln – ist das Bakterium ein besonderes Vorbild. Ein Roboter in seiner Größe trifft auf seine Physik: keine Trägheit, kein Gleiten, und das Muschel-Theorem verbietet jeden einfachen Hin-und-her-Schlag [1](#ref-1){:.cite} [3](#ref-3){:.cite}. Ingenieurinnen und Ingenieure haben deshalb die beiden Lösungen der Natur kopiert.

**Der Korkenzieher.** 2009 bauten Li Zhang, Bradley Nelson und Kollegen **künstliche Bakteriengeißeln**: einen schraubenförmigen Schwanz in Form und Größe einer natürlichen Flagelle mit einem dünnen weichmagnetischen „Kopf“ an einem Ende. Schwache Magnetfelder aus drei Paaren elektromagnetischer Spulen treiben und steuern den Schwimmer – die ersten mikroskopischen künstlichen Schwimmer mit Schraubenantrieb. Sie konnten Mikrokügelchen verschieben [9](#ref-9){:.cite}. Im selben Jahr zeigten Ambarish Ghosh und Peer Fischer schraubenförmige Propeller aus nanostrukturierten Oberflächen, die sich in großer Zahl herstellen und mit homogenen Magnetfeldern mikrometergenau durch Wasser steuern lassen; sie können Chemikalien transportieren und Lasten schieben [10](#ref-10){:.cite}.

**Das biegsame Ruder.** Rémi Dreyfus und Kollegen verbanden magnetische Teilchen mit DNA zu einer biegsamen Kette und hefteten sie an ein rotes Blutkörperchen. Ein schwingendes Magnetfeld ließ die Kette wie einen Schwanz schlagen und trieb das Gebilde voran; über die Felder ließen sich Geschwindigkeit und Richtung steuern [11](#ref-11){:.cite}.

**Wo steckt die Intelligenz?** Bei diesen Robotern sitzt sie außen: Wahrnehmen, Planen und Steuern übernehmen die Spulen und der Computer, der sie regelt, während der Schwimmer selbst nur das Feld in Bewegung umsetzt [12](#ref-12){:.cite}. Das Bakterium zeigt das andere Ende der Skala – einen Körper, in dem Sinnesorgane, eine einfache Entscheidungsregel und der Motor fest eingebaut sind. Mehr von dieser verkörperten Intelligenz in so kleine Maschinen zu bringen, ist aus unserer Sicht eine der großen offenen Fragen; Sitti und Kollegen geben einen Überblick über die Herausforderungen, so kleine Roboter für den Einsatz im Körper zu entwerfen [13](#ref-13){:.cite}. Die Medizin ist die wichtigste Motivation: Kabellose, drahtlos gesteuerte Mikroroboter könnten Diagnose und Therapie schonender machen und schwer zugängliche Stellen im Körper erreichen [12](#ref-12){:.cite} [13](#ref-13){:.cite}. Das ist noch weitgehend ein Forschungsziel, keine Routine.

{% include lens-end.html %}

## Was wir von einem Bakterium lernen können

Das Bakterium zeigt, wie anders sich Physik auf einer anderen Größenskala anfühlt. Wo wir auf Schwung setzen, setzt es auf Reibung; wo wir rühren würden, wartet es auf Diffusion; wo wir vorausschauen würden, vergleicht es die Gegenwart mit der jüngsten Vergangenheit. Seine Schwimmmaschine – ein Rotationsmotor, der einen Korkenzieher dreht – ist nach Maßstäben der Technik ineffizient und trotzdem völlig ausreichend [1](#ref-1){:.cite}.

Viele Fragen sind offen: Wie Flagellen miteinander und mit nahen Wänden wechselwirken, wie Mikroorganismen in komplexen Flüssigkeiten wie Schleim schwimmen und wie man künstliche Schwimmer baut, die auf dieser Skala gut funktionieren, sind aktive Forschungsfelder [3](#ref-3){:.cite}. Und für Mikroroboter in der Medizin ist der Weg vom Labor in den Körper noch weit [13](#ref-13){:.cite}.
