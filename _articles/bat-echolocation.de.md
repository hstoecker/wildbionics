---
id: bat-echolocation
lang: de
ref: bat-echolocation
title: "Wie Fledermäuse mit Schall sehen: Echoortung erklärt"
short_title: "Echoortung der Fledermäuse"
kicker: "Artikel · Akustik"
description: "Fledermäuse jagen im Dunkeln mit Ultraschall: Die Laufzeit des Echos verrät die Entfernung, seine Tonhöhe die Geschwindigkeit der Beute."
dek: "Eine insektenfressende Fledermaus sendet bis zu 200 Ultraschallrufe pro Sekunde aus und setzt aus den Echos ein Bild ihrer Umgebung zusammen. Dieselbe Physik – Echolaufzeit, Bandbreite, Doppler-Verschiebung – steuert heute Roboter, die sich mit Schall orientieren."
date: 2026-09-28
permalink: /de/artikel/echoortung-fledermaeuse/
image: /assets/og/bat-echolocation-de.jpg
image_alt: "Schema einer Fledermaus, die sich einer Motte nähert: Entlang ihrer Flugbahn folgen die Rufe zur Echoortung immer dichter aufeinander, von der Suchphase bis zum abschließenden Buzz."
hero_figure: svg/bat-hunt.svg
hero_caption: "<span class=\"caption__label\">Abb. 1</span> Eine insektenfressende Fledermaus jagt eine Motte. Bei der Suche rufen viele Fledermäuse etwa alle 100 ms. Haben sie Beute entdeckt, rufen sie immer schneller, bis zum Feeding Buzz mit bis zu etwa 200 Rufen pro Sekunde. Die Zeitachse darunter zeigt jeden Ruf als Strich."
educational_level: "Intermediate"
keywords: ["Fledermaus", "Echoortung", "Biosonar", "Ultraschall", "Große Braune Fledermaus", "Eptesicus fuscus", "Feeding Buzz", "Doppler-Verschiebung", "Dopplereffekt-Kompensation", "Optimalfilter", "Entfernungsauflösung", "frequenzmodulierter Ruf", "Bärenspinner", "Sonarstörung", "Robat", "BatSLAM", "Bionik"]
about:
  - { name: "Echoortung (Tiere)", wikidata: Q6921783, wikipedia: "https://de.wikipedia.org/wiki/Echoortung_(Tiere)" }
  - { name: "Fledertiere (Chiroptera)", wikidata: Q28425, wikipedia: "https://de.wikipedia.org/wiki/Fledertiere" }
mentions:
  - { name: "Große Braune Fledermaus", wikidata: Q301254 }
  - { name: "Bertholdia trigona", wikidata: Q13403125 }
  - { name: "Hufeisennasen", wikidata: Q830900 }
  - { name: "Doppler-Effekt", wikidata: Q76436 }
  - { name: "Optimalfilter", wikidata: Q1759577 }
  - { name: "Simultane Lokalisierung und Kartierung", wikidata: Q1203659 }
dimensions:
  time: ["cenozoic", "modern-era"]
  space: ["forest", "lab"]
  physics: ["acoustics"]
  adjacent_sciences: ["biology", "mathematics", "computer-science", "artificial-intelligence", "robotics", "physical-ai", "bionics"]
beings: ["big-brown-bat", "tiger-moth"]
lenses: ["biology", "physics", "math", "cs", "physical-ai"]
key_facts:
  - "Die Rufe zur Echoortung liegen je nach Art zwischen etwa **11 kHz und 212 kHz**; die meisten insektenfressenden Fledermäuse rufen zwischen 20 und 60 kHz – oberhalb des menschlichen Hörbereichs [2](#ref-2){:.cite}."
  - "Fledermäuse gehören zu den **lautesten Tieren in der Luft**: Arten, die über Wasser jagen, erreichen mittlere Quellpegel von etwa 137 dB SPL, im Maximum über **140 dB SPL** [3](#ref-3){:.cite}."
  - "Große Braune Fledermäuse und andere Arten unterscheiden Ziele, deren Entfernungen sich um nur **1–3 cm** unterscheiden [4](#ref-4){:.cite}."
  - "Beim Anflug auf die Beute ruft eine Fledermaus immer schneller – im abschließenden **Feeding Buzz** bis zu etwa 200-mal pro Sekunde [2](#ref-2){:.cite}."
  - "Hufeisennasen senken ihre Ruffrequenz umso stärker, je schneller sie fliegen, damit das Echo trotz Doppler-Verschiebung immer auf der Frequenz ankommt, die sie am besten hören [2](#ref-2){:.cite} [10](#ref-10){:.cite}."
  - "Der Bärenspinner *Bertholdia trigona* **stört das Sonar** angreifender Großer Brauner Fledermäuse mit Ultraschall-Klicks [9](#ref-9){:.cite}."
  - "Roboter mit einem Ultraschall-Lautsprecher und zwei Mikrofonen haben Büros und Gelände im Freien allein anhand von Echos kartiert [11](#ref-11){:.cite} [5](#ref-5){:.cite}."
faq:
  - q: "Wie funktioniert die Echoortung der Fledermäuse?"
    a: "Eine Fledermaus erzeugt in ihrem Kehlkopf kurze, laute Rufe und stößt sie durch Maul oder Nase aus. Der Schall wird von Gegenständen zurückgeworfen, und die Fledermaus hört die Echos mit ihren großen Ohren. Die Laufzeit eines Echos verrät, wie weit ein Gegenstand entfernt ist, der Unterschied zwischen beiden Ohren die Richtung, und Änderungen von Tonhöhe und Lautstärke des Echos zeigen, ob sich der Gegenstand bewegt und wie groß er ist."
  - q: "Warum hören Menschen keine Fledermäuse?"
    a: "Die meisten Fledermausrufe sind Ultraschall. Die Rufe zur Echoortung liegen zwischen etwa 11 und 212 Kilohertz, und die meisten insektenfressenden Fledermäuse rufen zwischen 20 und 60 Kilohertz. Das menschliche Gehör endet bei etwa 20 Kilohertz, wir hören also höchstens die tiefsten Rufe weniger Arten. Ein Fledermausdetektor macht die Rufe hörbar, indem er ihre Frequenz absenkt."
  - q: "Wie laut sind Fledermäuse?"
    a: "Sehr laut. Annemarie Surlykke und Elisabeth Kalko haben wilde Fledermäuse in Panama gemessen: Arten, die im offenen Luftraum und an Vegetationskanten jagen, erreichten Quellpegel von 122 bis 134 Dezibel, und zwei über Wasser jagende Arten im Mittel etwa 137 Dezibel, im Maximum über 140 Dezibel. Solche Werte, gemessen 10 Zentimeter vor dem Maul, gehören zu den stärksten Lauten, die Tiere in der Luft erzeugen. Wir hören sie nur deshalb nicht, weil sie im Ultraschall liegen."
  - q: "Wie genau kann eine Fledermaus Entfernungen messen?"
    a: "In Unterscheidungsversuchen fand James Simmons, dass vier Fledermausarten, darunter die Große Braune Fledermaus, zwei Ziele auseinanderhalten können, deren Entfernungen sich um nur 1 bis 3 Zentimeter unterscheiden. Die Fledermäuse nutzen dafür die Ankunftszeit der Echos. Ein Ruf, der über einen weiten Frequenzbereich gleitet, macht diese Genauigkeit möglich."
  - q: "Können sich Motten gegen Fledermäuse wehren?"
    a: "Ja. Viele Nachtfalter haben Ohren, die Fledermausrufe wahrnehmen und ein Ausweichmanöver auslösen. Manche Bärenspinner antworten auf einen Angriff mit Ultraschall-Klicks: Sie warnen die Fledermaus, dass sie schlecht schmecken, harmlose Arten ahmen diese Warnung nach, und der Bärenspinner Bertholdia trigona stört mit seinen Klicks das Sonar der Großen Braunen Fledermaus."
  - q: "Gibt es Roboter, die sich wie Fledermäuse per Echoortung orientieren?"
    a: "Ja. BatSLAM von Jan Steckel und Herbert Peremans ist ein fahrender Roboter mit einem fledermausähnlichen Sonarkopf, der Büroräume allein aus Echos kartiert. Der Robat der Universität Tel Aviv bewegt sich mit einem Ultraschall-Lautsprecher und zwei Mikrofonen selbstständig durch Gelände im Freien, kartiert Hindernisse und unterscheidet mit einem neuronalen Netz Pflanzen von anderen Objekten."
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

## Sehen mit Schall

In einer Sommernacht kann eine insektenfressende Fledermaus eine Motte durch völlige Dunkelheit verfolgen und aus der Luft schnappen. Licht braucht sie dafür nicht. Die Fledermaus stößt kurze, laute Rufe aus und lauscht den Echos, die von allem um sie herum zurückkommen – von Ästen, vom Boden, von den flatternden Flügeln eines Insekts. Aus diesen Echos setzt ihr Gehirn ein Bild der Umgebung zusammen. Diese Art der Wahrnehmung heißt **Echoortung** oder **Biosonar**.

1944 schrieb der amerikanische Zoologe Donald Griffin einen kurzen Artikel, dessen Titel die Idee zusammenfasst: *Echolocation by blind men, bats and radar* – Echoortung bei blinden Menschen, Fledermäusen und Radar [1](#ref-1){:.cite}. Der Vergleich mit dem Radar passt. Fledermäuse nutzen Lösungen, die auch Ingenieure in Sonar und Radar einsetzen – breitbandige Frequenzsweeps, um Entfernungen zu messen, und die Doppler-Verschiebung, um Geschwindigkeiten zu messen [2](#ref-2){:.cite}.

Die meisten Fledermausrufe sind **Ultraschall**: Sie liegen oberhalb von etwa 20 kHz, der oberen Grenze des menschlichen Hörens. Über alle Arten hinweg reichen die dominanten Frequenzen der Ortungsrufe von etwa 11 kHz bis 212 kHz; die meisten insektenfressenden Fledermäuse rufen zwischen 20 und 60 kHz [2](#ref-2){:.cite}. Die Rufe sind außerdem erstaunlich laut. Fledermäuse, die im offenen Luftraum jagen, erreichen Quellpegel von 122–134 dB SPL, gemessen 10 cm vor dem Maul; zwei Arten von Hasenmäulern, die dicht über dem Wasser jagen, kommen im Mittel auf etwa 137 dB SPL, im Maximum auf über **140 dB SPL** [3](#ref-3){:.cite}. Das gehört zu den stärksten Lauten, die Tiere in der Luft erzeugen [2](#ref-2){:.cite}.

Mit diesen Rufen messen Fledermäuse Entfernungen erstaunlich genau. In Trainingsversuchen konnten vier Arten – darunter die Große Braune Fledermaus, *Eptesicus fuscus* – zwei Ziele unterscheiden, deren Entfernungen sich um nur **1–3 cm** unterschieden [4](#ref-4){:.cite}.

## Die Jagd in drei Phasen

1. **Suche.** Die Fledermaus fliegt durch ihr Jagdgebiet und ruft in gleichmäßigem Takt. Fledermäuse im offenen Luftraum rufen länger und in größeren Abständen als Fledermäuse zwischen Hindernissen [2](#ref-2){:.cite}; viele jagende Fledermäuse rufen etwa alle 100 ms [5](#ref-5){:.cite}.
2. **Annäherung.** Sobald die Fledermaus ein Insekt entdeckt, wendet sie sich ihm zu. Mit der Entfernung schrumpft die Echolaufzeit, also ruft sie in immer kürzeren Abständen. Außerdem verkürzt sie jeden Ruf, denn der laute ausgehende Ruf darf sich nicht mit dem leisen zurückkehrenden Echo überlappen [2](#ref-2){:.cite}.
3. **Buzz.** Kurz vor dem Fang verschmelzen die Rufe zu einem schnellen **Feeding Buzz** mit bis zu etwa 200 Rufen pro Sekunde [2](#ref-2){:.cite}. Die Fledermaus aktualisiert die Position ihrer Beute nun alle paar Millisekunden.

Wie genau eine Fledermaus jagt, hängt vom Ort ab. Im offenen Luftraum hebt sich ein Insekt als einzelnes Echo ab; nahe an Vegetation oder am Boden muss die Fledermaus das Echo ihrer Beute aus einem Gewirr von Hintergrundechos heraushören. Verschiedene Arten haben für diese Situationen verschiedene Strategien entwickelt [6](#ref-6){:.cite}.

{% include lens-tabs.html lenses="biology,physics,math,cs,physical-ai" %}

{% include lens-start.html lens="biology" %}

## Biologie-Linse: ein Wettrüsten im Ultraschall

Die Echoortung machte Fledermäuse zu gefürchteten Nachtjägern – und ihre Beute zu Zuhörern. Viele Nachtfalter haben **Ohren** entwickelt, die für hohe Frequenzen empfindlich sind. Bei Insekten sind Ohren an bemerkenswert vielen Stellen des Körpers entstanden, und bei Nachtfaltern lösen sie Abwehrverhalten aus, etwa ein plötzliches Ausweichmanöver, wenn sich eine Fledermaus nähert [7](#ref-7){:.cite}.

Manche **Bärenspinner** gehen weiter und antworten einer angreifenden Fledermaus mit eigenen Ultraschall-Klicks. Jesse Barber und William Conner filmten Fledermäuse bei der Jagd auf Bärenspinner mit Infrarot-Hochgeschwindigkeitskameras. Unerfahrene Rote Fledermäuse und Große Braune Fledermäuse lernten schnell, die erste ungenießbare, klickende Falterart zu meiden, die man ihnen anbot – sie verbanden das Geräusch mit schlechtem Geschmack. Danach mieden sie auch eine zweite klickende Art – ob sie ungenießbar war oder nicht. Die Klicks wirken als akustisches Warnsignal, und harmlose Arten können es nachahmen [8](#ref-8){:.cite}.

Der Bärenspinner *Bertholdia trigona* nutzt seine Klicks noch anders. Er ist genießbar, doch wenn eine Große Braune Fledermaus angreift, antwortet er mit Ultraschall-Klicks, die **das Sonar der Fledermaus stören**. Frühere Hinweise auf eine solche Sonarstörung waren nicht eindeutig gewesen; Aaron Corcoran und Kollegen wiesen sie mit Ultraschallaufnahmen und Infrarot-Hochgeschwindigkeitsvideos nach [9](#ref-9){:.cite}.

Fledermäuse wiederum zeigen Gegenanpassungen. Manche rufen auf Frequenzen außerhalb des Hörbereichs der meisten Nachtfalter mit Ohren, manche ändern Muster und Frequenz ihrer Rufe während der Verfolgung, und manche nutzen leise Echoortung, eine Art „Tarnkappen-Ortung“ [7](#ref-7){:.cite}.

Die Rufe selbst werden stärker vom Lebensraum geprägt als vom Stammbaum. Lange Rufe mit konstanter Frequenz und hohem Tastgrad (Duty Cycle) – der Schall ist die meiste Zeit „an“ – entstanden unabhängig voneinander bei den Hufeisennasen und bei der Schnurrbartfledermaus *Pteronotus parnellii*: ein Lehrbuchbeispiel für **konvergente Evolution** [2](#ref-2){:.cite}.

{% include lens-end.html %}

{% include lens-start.html lens="physics" %}

## Physik-Linse: Wellenlänge, Lautstärke und Doppler-Verschiebung

Schall breitet sich in Luft bei 20 °C mit etwa 343 m/s aus. Seine Wellenlänge ist die Schallgeschwindigkeit geteilt durch die Frequenz, *λ* = *c* / *f*. Bei 20 kHz ist eine Schallwelle etwa 17 mm lang, bei 100 kHz nur 3,4 mm. Das ist wichtig, weil ein Gegenstand Schall nur dann gut zurückwirft, wenn er nicht viel kleiner ist als die Wellenlänge. Sinkt die Flügellänge eines Insekts von einer Wellenlänge auf ein Fünftel davon, wird sein Echo um etwa 25 dB schwächer. Kleine Beute verlangt deshalb hohe Frequenzen [2](#ref-2){:.cite}.

Hohe Frequenzen haben allerdings ihren Preis: Luft dämpft sie viel stärker als tiefe Frequenzen, und das begrenzt die Reichweite der Echoortung [2](#ref-2){:.cite}. Hinzu kommt, dass sich der Schall auf dem Weg zum Ziel und noch einmal auf dem Rückweg ausbreitet. Bei einem kleinen Ziel fällt die Intensität des Echos mit der vierten Potenz der Entfernung: Bei doppelter Entfernung ist das Echo 16-mal, also um 12 dB, schwächer. Fledermäuse gleichen diese Verluste mit Lautstärke aus. Surlykke und Kalko fanden, dass die Fledermäuse mit den höchsten Schallintensitäten auch die höchsten Frequenzen nutzten – so kamen Arten mit sehr unterschiedlichen Ruffrequenzen auf ähnliche Entdeckungsdistanzen für Beute [3](#ref-3){:.cite}. Nähern sie sich Vegetation oder Boden, senken Fledermäuse ihre Lautstärke wieder, um 4–7 dB je Halbierung der Entfernung [3](#ref-3){:.cite}.

Der dritte Effekt ist die **Doppler-Verschiebung**. Fliegt eine Fledermaus auf einen Gegenstand zu, kommt das Echo mit höherer Frequenz zurück, als sie gerufen hat – die Fledermaus ist eine bewegte Schallquelle und für das zurückkehrende Echo zugleich ein bewegter Empfänger. Hufeisennasen und die Schnurrbartfledermaus machen daraus ein Präzisionsinstrument: Sie senken die Frequenz ihrer Rufe umso stärker, je schneller sie fliegen, sodass die Echos immer auf der Frequenz ankommen, die sie am besten hören [2](#ref-2){:.cite}. Diese **Dopplereffekt-Kompensation** hält die Echos in ihrer **akustischen Fovea**: einem gedehnten Bereich des Innenohrs, der einem schmalen Band um diese Frequenz vorbehalten ist und entlang der ganzen Hörbahn von vielen scharf abgestimmten Nervenzellen verarbeitet wird. Dort heben sich die rhythmischen Änderungen des Echos, die die schlagenden Flügel eines Insekts verursachen – das „Flattern“ –, selbst in dichter Vegetation ab [10](#ref-10){:.cite}.

{% include lens-end.html %}

{% include lens-start.html lens="math" %}

## Mathematik-Linse: Entfernung, Richtung und Geschwindigkeit aus einem Echo

**Entfernung.** Der Ruf läuft zum Ziel und zurück, also ist die Entfernung *d* die Hälfte des Wegs, den der Schall während der Echolaufzeit Δ*t* zurücklegt:

<div class="formula" role="math" aria-label="d gleich c mal Delta t durch 2"><var>d</var> = <span class="frac"><span class="frac__num"><var>c</var> · Δ<var>t</var></span><span class="frac__den">2</span></span></div>

Jeder Meter Entfernung verlängert die Laufzeit um 2 m / 343 m/s ≈ **5,8 ms**. Ein Echo nach 17,5 ms bedeutet also: Die Motte ist 343 m/s · 17,5 ms / 2 ≈ **3,0 m** entfernt.

**Auflösung.** Wie nah dürfen zwei Ziele beieinanderliegen, bevor ihre Echos zu einem verschmelzen? Die Signaltheorie gibt die Antwort: Die Entfernungsauflösung hängt von der **Bandbreite** *B* des Rufs ab – dem Frequenzbereich, den er überstreicht –, nicht von seiner Dauer:

<div class="formula" role="math" aria-label="Delta d ungefähr gleich c durch 2 B">Δ<var>d</var> ≈ <span class="frac"><span class="frac__num"><var>c</var></span><span class="frac__den">2 <var>B</var></span></span></div>

Ein Ruf, der von 80 auf 40 kHz gleitet, hat *B* = 40 kHz und eine Auflösung von etwa 343 / 80.000 m ≈ **4 mm**. Ein reiner Ton von 2 ms Dauer hat nur eine Bandbreite von etwa 1 / (2 ms) = 0,5 kHz – und eine Auflösung von etwa 34 cm. Gemessene Fledermäuse erreichen 1–3 cm [4](#ref-4){:.cite} – gröber als diese ideale Grenze, aber weit feiner, als ein reiner Ton es erlauben würde. Die Informatik-Linse prüft die Formel mit einem Programm.

**Richtung.** Schall von der Seite erreicht das nähere Ohr etwas früher. Für Ohren im Abstand *b* und Schall, der unter dem Winkel *θ* zur Blickrichtung eintrifft, beträgt der interaurale Laufzeitunterschied

<div class="formula" role="math" aria-label="Delta tau gleich b mal Sinus theta durch c">Δ<var>τ</var> = <span class="frac"><span class="frac__num"><var>b</var> · sin <var>θ</var></span><span class="frac__den"><var>c</var></span></span></div>

Bei einem angenommenen Ohrabstand von 2 cm ergibt eine Richtung 10° neben der Mittellinie Δ*τ* = 0,02 m · sin 10° / 343 m/s ≈ **10 µs** – zehn Millionstel Sekunden. Fledermäuse und andere kleine Säugetiere bestimmen Richtungen genauer als etwa 10° [5](#ref-5){:.cite}; zusammen mit der Laufzeit ergibt das eine Position im Raum. Fledermäuse nutzen außerdem den Lautstärkeunterschied zwischen ihren Ohren und die Art, wie ihre Ohrmuscheln den Schall filtern [11](#ref-11){:.cite}.

**Geschwindigkeit.** Fliegt eine Fledermaus mit der Geschwindigkeit *v* auf einen ruhenden Gegenstand zu, kommt das Echo mit der Frequenz

<div class="formula formula--steps"><span><var>f</var><sub>Echo</sub> = <var>f</var><sub>0</sub> · <span class="frac"><span class="frac__num"><var>c</var> + <var>v</var></span><span class="frac__den"><var>c</var> − <var>v</var></span></span></span><span>≈ <var>f</var><sub>0</sub> · (1 + 2<var>v</var>/<var>c</var>)</span></div>

zurück. Bei *v* = 5 m/s und *f*<sub>0</sub> = 50 kHz ist das Echo etwa **1,5 kHz** höher. Der Faktor 2 entsteht, weil die Frequenz zweimal verschoben wird: einmal, wenn die bewegte Fledermaus den Ruf aussendet, und noch einmal, wenn sie das Echo empfängt.

{% include lens-end.html %}

{% include lens-start.html lens="cs" %}

## Informatik-Linse: Warum Fledermäuse gleiten – ein Optimalfilter in Code

Wie findet eine Fledermaus ein schwaches Echo im Rauschen, und wie hält sie zwei nahe Ziele auseinander? Simmons verglich die Leistung von Fledermäusen mit der Mathematik ihrer Rufe und schloss, dass Fledermäuse eine Art neuronales Gegenstück zu einem **Optimalfilter** (Matched Filter) besitzen: einem idealen Sonarempfänger, der eine Kopie des ausgesendeten Rufs mit dem zurückkehrenden Echo kreuzkorreliert, um es zu entdecken und seine Ankunftszeit zu bestimmen [4](#ref-4){:.cite}. Ingenieure nutzen dieselbe Methode in Radar und Sonar.

Das Programm unten simuliert ein Echo von zwei Zielen im Abstand von 5 cm – einer Motte und einem Blatt kurz dahinter –, verborgen im Rauschen. Es vergleicht zwei gleich lange Rufe: einen **Frequenzsweep** von 80 auf 40 kHz, ähnlich den Rufen der Großen Braunen Fledermaus, und einen **reinen Ton** mit 60 kHz. Die Frage: Mit welchem Ruf trennt der Optimalfilter die beiden Echos, und wie gut sagt die Auflösungsformel der Mathematik-Linse das Ergebnis voraus?

```python
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
```
{% include code-result.html file="range_resolution.py" label="Abb. 2" caption="Ausgabe des Programms oben: die Einhüllende des Optimalfilter-Ausgangs über der Entfernung für zwei Ziele im Abstand von 5 cm (gepunktete Linien). Oben: Ein Sweep von 80 auf 40 kHz ergibt zwei scharfe Spitzen genau an den Zielen. Unten: Ein reiner 60-kHz-Ton gleicher Dauer ergibt zwei breite Buckel an den falschen Stellen – die überlappenden Echos interferieren. Die Signale sind simuliert." alt="Zwei übereinanderliegende Liniendiagramme des Optimalfilter-Ausgangs von 0 bis 1 über der Entfernung von 1,2 bis 1,85 Metern, mit gepunkteten senkrechten Linien an den wahren Zielen bei 1,50 und 1,55 Metern. Oben, für einen Sweep von 80 auf 40 Kilohertz: Zwei schmale Spitzen der Höhe 1 liegen genau auf den gepunkteten Linien, das Rauschen daneben bleibt unter 0,1. Unten, für einen reinen 60-Kilohertz-Ton: Zwei breite Buckel haben ihr Maximum bei etwa 1,43 und 1,62 Metern, mehrere Zentimeter neben den wahren Zielen, mit einer Senke dazwischen." %}

Was das Ergebnis lehrt:

- **Bandbreite schlägt Dauer.** Beide Rufe dauern 2 ms und tragen dieselbe Energie. Der Sweep trennt die beiden Ziele exakt (Fehler unter 0,1 cm), genau wie die Formel Δ*d* ≈ *c* / (2*B*) ≈ 0,4 cm vorhersagt. Der Ton hat eine Auflösung von etwa 34 cm – weit mehr als die 5 cm zwischen den Zielen.
- **Überlappende Echos verwischen nicht nur.** Die beiden Echos des Tons überlappen und interferieren: Je nach Phasenunterschied verstärken oder schwächen sie sich. Hier meldet das Programm zwei Echos bei 1,43 und 1,62 m – beide etwa 7 cm daneben. Ein reiner Ton ist schlicht das falsche Werkzeug für Entfernungsmessungen; Fledermäuse mit langen Rufen konstanter Frequenz wie die Hufeisennasen nutzen für die Entfernung den frequenzmodulierten Teil am Ende ihrer Rufe [4](#ref-4){:.cite}.
- **Das Modell ist idealisiert.** Die simulierten Echos sind perfekte Kopien des Rufs; echte Echos sind abgeschwächt, vom Ziel und von der Luft gefiltert und durch den Doppler-Effekt verschoben. Die Auflösung von 0,4 cm ist deshalb eine untere Grenze, keine Vorhersage für eine echte Fledermaus. Gemessene Fledermäuse erreichen 1–3 cm [4](#ref-4){:.cite}.

Auch ein paar Programmierideen lohnen einen Blick:

- **Korrelation als Suche.** `correlate` schiebt den bekannten Ruf über die Aufnahme und multipliziert beide; wo sie übereinstimmen, wird die Summe groß. Diese Kreuzkorrelation macht `hilbert` zu einer glatten Einhüllenden, deren Spitzen die Echos markieren.
- **Fensterfunktion.** `np.hanning` blendet jeden Ruf weich ein und aus. Ohne das würden der abrupte Anfang und das abrupte Ende Nebenkeulen erzeugen, die `find_peaks` für zusätzliche Echos halten könnte.
- **Validierung.** Das Programm vergleicht sein Ergebnis mit den bekannten Zielpositionen und mit der Auflösungsformel – eine Gewohnheit, die sich bei jedem Sensorprogramm lohnt.

Probier es selbst – jede Änderung ist eine Zeile:

- Setze `TARGETS = [1.50, 1.51]`: Der Sweep trennt auch Ziele, die nur 1 cm auseinanderliegen, mit einem Fehler von 0,1 cm; der Ton meldet ein einziges Echo.
- Setze `NOISE = 1.0`: Das Rauschen ist jetzt so stark wie die Echos, doch der Sweep findet beide Ziele weiterhin mit einem Fehler unter 0,1 cm – der Optimalfilter sammelt die Energie des ganzen Rufs.
- Setze `CALL_TIME = 5e-3`: Ein längerer Ruf verringert die Bandbreite des Tons auf 0,2 kHz, und seine Auflösung verschlechtert sich auf etwa 85,8 cm. Der Sweep behält seine 0,4 cm, weil seine Bandbreite weiterhin 40 kHz beträgt.

{% include code-variant.html file="range_resolution.py" id="close" replace="TARGETS = [1.50, 1.55]" with="TARGETS = [1.50, 1.51]" expect="1.50 1.51 0.1 1" %}
{% include code-variant.html file="range_resolution.py" id="noise" replace="NOISE = 0.3" with="NOISE = 1.0" expect="1.50 1.55 0.0" %}
{% include code-variant.html file="range_resolution.py" id="longer" replace="CALL_TIME = 2e-3" with="CALL_TIME = 5e-3" expect="0.2 85.8 0.4" %}

{% include lens-end.html %}

{% include lens-start.html lens="physical-ai" %}

## Physical-AI-Linse: Roboter, die sich mit Schall orientieren

Bei Physical AI – verkörperter künstlicher Intelligenz – geht es um Maschinen, die in der physischen Welt wahrnehmen und handeln. Kameras brauchen Licht; Schall funktioniert im Dunkeln. Einfache Ultraschall-Abstandssensoren sind in Robotern und Autos verbreitet, doch Fledermäuse entnehmen ihren Echos weit mehr. Zwei Forschungsroboter zeigen, was passiert, wenn Ingenieure die ganze Fledermaus nachbauen – einen Sender, zwei Ohren und fledermausähnliche Signalverarbeitung – statt nur die Abstandsmessung [5](#ref-5){:.cite}.

**BatSLAM.** Jan Steckel und Herbert Peremans von der Universität Antwerpen setzten einen fledermausähnlichen Sonarkopf auf einen fahrenden Roboter [11](#ref-11){:.cite}:

- Ein Ultraschallsender stößt einen 3 ms langen Ruf aus, der von 100 auf 20 kHz gleitet.
- Zwei Mikrofone sitzen in Kunststoffnachbildungen der Ohrmuscheln der Fledermaus *Micronycteris microtis*, 1,5-fach vergrößert.
- Ein Modell der Cochlea von Säugetieren wandelt die Echos in Zeit-Frequenz-Muster um.
- Ein Navigationsmodell nach dem Vorbild des Hippocampus von Ratten (RatSLAM) verknüpft diese Muster mit Orten.

Der Roboter kartierte unveränderte Büroumgebungen effizient und konsistent. Er erkannte bereits besuchte Orte wieder, ohne einzelne Objekte in den Echos zu identifizieren [11](#ref-11){:.cite}. SLAM steht für **simultane Lokalisierung und Kartierung**: Der Roboter baut eine Karte und bestimmt gleichzeitig seine eigene Position darin.

**Robat.** Itamar Eliakim, Yossi Yovel und Kollegen von der Universität Tel Aviv bauten einen vollständig autonomen Roboter, der sich allein mithilfe von Echos durch unbekanntes Gelände im Freien bewegt [5](#ref-5){:.cite}. Wie eine Fledermaus hat er einen Ultraschall-Lautsprecher als „Maul“ und zwei Ultraschallmikrofone als „Ohren“. Alle 0,5 m sandte er breitbandige frequenzmodulierte Rufe in drei Richtungen aus – wie eine Fledermaus, die mit 5 m/s fliegt und alle 100 ms ruft. Aus den Echos markierte er Hindernisse auf einer Karte, mied Sackgassen und steuerte um Objekte herum. Im Mittel lagen die geschätzten Ränder der Objekte 42 cm neben ihrer wahren Position. Ein neuronales Netz ordnete Objekte mit einer balancierten Genauigkeit von 68 % als Pflanzen oder Nicht-Pflanzen ein – deutlich über den 50 %, die der Zufall erwarten ließe [5](#ref-5){:.cite}.

Diese Zahlen zeigen das Versprechen und die Lücke. Ein Roboter kann seine Umgebung allein mit Schall kartieren, doch echte Fledermäuse nehmen in ihren Echos weit mehr Einzelheiten wahr – und das im Flug. Die Lehre für Physical AI: Die Form des Sensors selbst – Ohren, Nasenaufsatz, ein gut gestalteter Ruf – erledigt einen Teil der Verarbeitung, bevor überhaupt ein Computer beteiligt ist [11](#ref-11){:.cite}.

{% include lens-end.html %}

## Von Fledermäusen zur Technik

Die Echoortung ist eines der deutlichsten Beispiele dafür, dass Natur und Technik zu ähnlichen Lösungen kommen: breitbandige Sweeps zur Entfernungsmessung, die Doppler-Verschiebung zur Geschwindigkeitsmessung und Optimalfilter, um ein schwaches Signal im Rauschen zu finden [2](#ref-2){:.cite} [4](#ref-4){:.cite}. Sonar, Radar und die Ultraschallsensoren von Robotern und Autos beruhen alle auf derselben Physik.

Offene Fragen bleiben. Simmons schlug 1973 vor, dass Fledermäuse eine Art neuronales Gegenstück zu einem Optimalfilter besitzen [4](#ref-4){:.cite}; wie ihr Nervensystem das tatsächlich leistet, wird noch erforscht. Bei vielen Merkmalen von Fledermäusen ist schwer zu sagen, ob sie als Gegenanpassung an Beute mit Ohren entstanden sind oder aus anderen Gründen [7](#ref-7){:.cite}. Und Roboter sind noch weit davon entfernt, in Echos so viele Einzelheiten wahrzunehmen wie eine Fledermaus [5](#ref-5){:.cite}.
