---
id: walking
lang: de
ref: walking
title: "Wie wir gehen: Pendel, Federn und humanoide Roboter"
short_title: "Gehen"
kicker: "Artikel · Biomechanik"
description: "Gehen ist ein Pendel, Laufen eine Feder. Warum wir bei etwa 2 m/s die Gangart wechseln, wie Sehnen Energie sparen und wie Roboter gehen lernen."
dek: "Bei jedem Schritt schwingt dein Körper über ein steifes Bein wie ein umgedrehtes Pendel. Wirst du schneller, kann die Schwerkraft dich nicht mehr auf diesem Bogen halten – also fängst du an zu laufen und federst auf deinen Beinen. Eine einzige Zahl aus der Physik sagt voraus, wann: für ein Kind, einen Erwachsenen oder einen Menschen bei geringer Schwerkraft. Mit denselben Ideen bauen Ingenieurinnen und Ingenieure Roboter, die gehen."
date: 2026-10-05
permalink: /de/artikel/gehen/
image: /assets/og/walking-de.jpg
og: { eyebrow: "Biologie · Mechanik · Physical AI", title: "Warum wir wie ein Pendel <em>gehen</em> – und Roboter es lernen", sub: "Ein umgedrehtes Pendel, eine Feder in jedem Bein und Roboter, die durch Ausprobieren gehen lernen.", title_px: 50 }
image_alt: "Ein gehender Mensch und ein humanoider Roboter nebeneinander in derselben Phase eines Schritts. Bei beiden ist das Standbein als Stab eines umgedrehten Pendels vom Fuß zur Hüfte eingezeichnet und die Bahn der Hüfte als Bogen über dem Fuß."
hero_figure: svg/walking.svg
hero_caption: "<span class=\"caption__label\">Abb. 1</span> Gehen als inverses Pendel. Bei jedem Schritt schwingt der Körper über das Standbein, das wie ein steifer Stab vom Fuß zur Hüfte wirkt: Die Hüfte, nahe am Schwerpunkt, bewegt sich auf einem Bogen und ist in der Mitte des Schritts am höchsten. Ein humanoider Roboter, der mit steifen Beinen geht, folgt demselben Bogen – dieselbe Physik in einer Maschine."
educational_level: "Intermediate"
keywords: ["Gehen", "Laufen", "menschlicher Gang", "Biomechanik", "Bipedie", "Zweibeinigkeit", "inverses Pendel", "Feder-Masse-Modell", "Übergang vom Gehen zum Laufen", "Froude-Zahl", "dynamische Ähnlichkeit", "Achillessehne", "Fußgewölbe", "elastische Energie", "Transportkosten", "passiv-dynamisches Gehen", "humanoider Roboter", "Laufroboter", "bestärkendes Lernen", "Reinforcement Learning", "Physical AI"]
about:
  - { name: "Gehen", wikidata: Q6537379, wikipedia: "https://de.wikipedia.org/wiki/Gehen" }
  - { name: "Humanoider Roboter", wikidata: Q584529, wikipedia: "https://de.wikipedia.org/wiki/Humanoider_Roboter" }
mentions:
  - { name: "Homo sapiens", wikidata: Q15978631 }
  - { name: "Laufen", wikidata: Q105674 }
  - { name: "Bipedie", wikidata: Q372949 }
  - { name: "Gangart", wikidata: Q2370000 }
  - { name: "Inverses Pendel", wikidata: Q550134 }
  - { name: "Froude-Zahl", wikidata: Q273090 }
  - { name: "Achillessehne", wikidata: Q223172 }
  - { name: "Passive Dynamik", wikidata: Q7142798 }
  - { name: "Laufroboter", wikidata: Q1424704 }
  - { name: "Bestärkendes Lernen", wikidata: Q830687 }
dimensions:
  time: ["cenozoic", "modern-era", "age-of-ai"]
  space: ["urban", "lab"]
  physics: ["mechanics"]
  adjacent_sciences: ["biology", "mathematics", "computer-science", "artificial-intelligence", "robotics", "physical-ai", "bionics"]
beings: ["human"]
lenses: ['biology', 'physics', 'math', 'cs', 'physical-ai']
key_facts:
  - "Beim Gehen schwingt der Körper über ein steifes Bein wie ein **inverses Pendel**: Kinetische und potenzielle Energie werden hin und her getauscht, und dieser Austausch kann bis zu **70 %** der Energieänderungen innerhalb eines Doppelschritts ausmachen; nur 30 % bleiben für die Muskeln [1](#ref-1){:.cite}."
  - "Beim Laufen arbeitet das Bein wie eine **Feder**: Sehnen und das Fußgewölbe speichern Energie, wenn der Fuß aufsetzt, und geben sie durch elastischen Rückstoß zurück – wie ein springender Gummiball [1](#ref-1){:.cite} [7](#ref-7){:.cite}."
  - "Menschen wechseln vom Gehen ins Laufen bei einer **Froude-Zahl** *v*²/(*g L*) von etwa **0,5** – ob mit kurzen oder langen Beinen und sogar bei simulierter geringerer Schwerkraft [11](#ref-11){:.cite}. In einer Laufbandstudie wechselten Erwachsene bei **2,06 m/s** [13](#ref-13){:.cite}."
  - "Das Pendel setzt eine Geschwindigkeitsgrenze: Die Schwerkraft muss den Körper auf seinem Bogen über dem Fuß halten, daher kann man im Pendelmodell nicht schneller gehen als etwa √(*g L*), rund 3 m/s bei 0,9 m Beinlänge – eine Rechnung in diesem Artikel."
  - "**Passiv-dynamische Laufmaschinen** – Maschinen ohne Motor und ohne Steuerung – gehen eine flache Rampe hinunter, mit menschenähnlichem Gang und angetrieben nur von der Schwerkraft [14](#ref-14){:.cite} [15](#ref-15){:.cite}. Heute lernen humanoide Roboter das Gehen durch **bestärkendes Lernen** (Reinforcement Learning) in der Simulation und übertragen es auf den echten Roboter [18](#ref-18){:.cite}."
faq:
  - q: "Warum vergleicht man Gehen mit einem umgedrehten Pendel?"
    a: "Während eines Schritts bleibt das Standbein fast gestreckt, und der Körper schwingt darüber wie ein Gewicht auf einem steifen Stab. Am Anfang und am Ende des Schritts ist der Körper am tiefsten und am schnellsten, in der Mitte am höchsten und am langsamsten. Kinetische Energie wird in potenzielle Energie umgewandelt und wieder zurück, wie bei einem Pendel – die Muskeln müssen deshalb nur einen Teil der Energie aufbringen."
  - q: "Warum fangen wir an zu laufen, wenn wir schneller gehen?"
    a: "Im Pendelmodell muss die Schwerkraft den Körper auf seinem Bogen über dem Fuß halten. Je schneller man geht, desto mehr Zug braucht es, und bei einer Froude-Zahl von 1 reicht die Schwerkraft nicht mehr aus. Menschen wechseln schon deutlich früher ins Laufen, bei einer Froude-Zahl von etwa 0,5 – bei Erwachsenen um 2 Meter pro Sekunde. Warum genau an diesem Punkt, ist noch umstritten; es ist jedenfalls nicht einfach die Geschwindigkeit, ab der Laufen sparsamer wird."
  - q: "Was ist die Froude-Zahl?"
    a: "Die Froude-Zahl Fr = v²/(gL) vergleicht die Zentripetalbeschleunigung eines Körpers, der sich mit der Geschwindigkeit v auf einem Bogen mit dem Radius L bewegt, mit der Schwerebeschleunigung g. Beim Gehen ist L die Beinlänge. Tiere unterschiedlicher Größe bewegen sich ähnlich, wenn ihre Froude-Zahlen gleich sind – ein Kind und ein Erwachsener, ein Hund und ein Pferd."
  - q: "Wie spart die Achillessehne Energie?"
    a: "Die Achillessehne verbindet die Wadenmuskeln mit der Ferse. Wird der Fuß belastet, dehnt sich die Sehne wie ein Gummiband und speichert elastische Energie, die sie beim Abstoßen des Fußes zurückgibt. Beim Gehen dehnt sich die Sehne um einige Millimeter, während der Wadenmuskel seine Länge kaum ändert; beim einbeinigen Hüpfen liefert ihr Rückstoß etwa ein Sechstel der Arbeit jedes Sprungs."
  - q: "Wie lernen humanoide Roboter gehen?"
    a: "Viele moderne Laufroboter lernen das Gehen durch bestärkendes Lernen (Reinforcement Learning): Ein neuronales Netz steuert einen simulierten Roboter, erhält eine Belohnung, wenn er gut geht, und verbessert sich durch Versuch und Irrtum über viele simulierte Durchläufe. Das trainierte Netz wird dann auf den echten Roboter übertragen. Frühere Ansätze nutzten sorgfältig entworfene Modelle und Regler; besonders sparsame Laufmaschinen nutzen sogar die passive Pendeldynamik ihrer Beine."
sources:
  - authors: ["Cavagna, G. A.", "Heglund, N. C.", "Taylor, C. R."]
    year: 1977
    title: "Mechanical work in terrestrial locomotion: two basic mechanisms for minimizing energy expenditure"
    journal: "American Journal of Physiology – Regulatory, Integrative and Comparative Physiology"
    volume: 233
    pages: "R243–R261"
    doi: "10.1152/ajpregu.1977.233.5.r243"
  - authors: ["Saibene, F.", "Minetti, A. E."]
    year: 2003
    title: "Biomechanical and physiological aspects of legged locomotion in humans"
    journal: "European Journal of Applied Physiology"
    volume: 88
    pages: "297–316"
    doi: "10.1007/s00421-002-0654-9"
  - authors: ["Bramble, D. M.", "Lieberman, D. E."]
    year: 2004
    title: "Endurance running and the evolution of Homo"
    journal: "Nature"
    volume: 432
    pages: "345–352"
    doi: "10.1038/nature03052"
  - authors: ["Kuo, A. D.", "Donelan, J. M.", "Ruina, A."]
    year: 2005
    title: "Energetic Consequences of Walking Like an Inverted Pendulum: Step-to-Step Transitions"
    journal: "Exercise and Sport Sciences Reviews"
    volume: 33
    pages: "88–97"
    doi: "10.1097/00003677-200504000-00006"
  - authors: ["Kuo, A. D."]
    year: 2007
    title: "The six determinants of gait and the inverted pendulum analogy: A dynamic walking perspective"
    journal: "Human Movement Science"
    volume: 26
    pages: "617–656"
    doi: "10.1016/j.humov.2007.04.003"
  - authors: ["Fukunaga, T.", "Kubo, K.", "Kawakami, Y.", "Fukashiro, S.", "Kanehisa, H.", "Maganaris, C. N."]
    year: 2001
    title: "In vivo behaviour of human muscle tendon during walking"
    journal: "Proceedings of the Royal Society of London. Series B: Biological Sciences"
    volume: 268
    pages: "229–233"
    doi: "10.1098/rspb.2000.1361"
    open_access: true
  - authors: ["Ker, R. F.", "Bennett, M. B.", "Bibby, S. R.", "Kester, R. C.", "Alexander, R. M."]
    year: 1987
    title: "The spring in the arch of the human foot"
    journal: "Nature"
    volume: 325
    pages: "147–149"
    doi: "10.1038/325147a0"
  - authors: ["Lichtwark, G. A.", "Wilson, A. M."]
    year: 2005
    title: "In vivo mechanical properties of the human Achilles tendon during one-legged hopping"
    journal: "Journal of Experimental Biology"
    volume: 208
    pages: "4715–4725"
    doi: "10.1242/jeb.01950"
    open_access: true
  - authors: ["Alexander, R. M."]
    year: 1984
    title: "The Gaits of Bipedal and Quadrupedal Animals"
    journal: "The International Journal of Robotics Research"
    volume: 3
    pages: "49–59"
    doi: "10.1177/027836498400300205"
  - authors: ["Blickhan, R."]
    year: 1989
    title: "The spring-mass model for running and hopping"
    journal: "Journal of Biomechanics"
    volume: 22
    pages: "1217–1227"
    doi: "10.1016/0021-9290(89)90224-8"
  - authors: ["Kram, R.", "Domingo, A.", "Ferris, D. P."]
    year: 1997
    title: "Effect of Reduced Gravity on the Preferred Walk–Run Transition Speed"
    journal: "Journal of Experimental Biology"
    volume: 200
    pages: "821–826"
    doi: "10.1242/jeb.200.4.821"
  - authors: ["Alexander, R. M.", "Jayes, A. S."]
    year: 1983
    title: "A dynamic similarity hypothesis for the gaits of quadrupedal mammals"
    journal: "Journal of Zoology"
    volume: 201
    pages: "135–152"
    doi: "10.1111/j.1469-7998.1983.tb04266.x"
  - authors: ["Hreljac, A."]
    year: 1993
    title: "Preferred and energetically optimal gait transition speeds in human locomotion"
    journal: "Medicine & Science in Sports & Exercise"
    volume: 25
    pages: "1158–1162"
    doi: "10.1249/00005768-199310000-00012"
  - authors: ["McGeer, T."]
    year: 1990
    title: "Passive Dynamic Walking"
    journal: "The International Journal of Robotics Research"
    volume: 9
    pages: "62–82"
    doi: "10.1177/027836499000900206"
  - authors: ["Collins, S.", "Ruina, A.", "Tedrake, R.", "Wisse, M."]
    year: 2005
    title: "Efficient Bipedal Robots Based on Passive-Dynamic Walkers"
    journal: "Science"
    volume: 307
    pages: "1082–1085"
    doi: "10.1126/science.1107799"
  - authors: ["Raibert, M. H.", "Brown, H. B.", "Chepponis, M."]
    year: 1984
    title: "Experiments in Balance with a 3D One-Legged Hopping Machine"
    journal: "The International Journal of Robotics Research"
    volume: 3
    pages: "75–92"
    doi: "10.1177/027836498400300207"
  - authors: ["Hwangbo, J.", "Lee, J.", "Dosovitskiy, A.", "Bellicoso, D.", "Tsounis, V.", "Koltun, V.", "Hutter, M."]
    year: 2019
    title: "Learning agile and dynamic motor skills for legged robots"
    journal: "Science Robotics"
    volume: 4
    pages: "eaau5872"
    doi: "10.1126/scirobotics.aau5872"
    open_access: true
  - authors: ["Radosavovic, I.", "Xiao, T.", "Zhang, B.", "Darrell, T.", "Malik, J.", "Sreenath, K."]
    year: 2024
    title: "Real-world humanoid locomotion with reinforcement learning"
    journal: "Science Robotics"
    volume: 9
    pages: "eadi9579"
    doi: "10.1126/scirobotics.adi9579"
  - authors: ["Haarnoja, T.", "Moran, B.", "Lever, G.", "Huang, S. H.", "Tirumala, D.", "Humplik, J.", "Wulfmeier, M.", "Tunyasuvunakool, S.", "Siegel, N. Y.", "Hafner, R.", "Bloesch, M.", "Hartikainen, K.", "Byravan, A.", "Hasenclever, L.", "Tassa, Y.", "Sadeghi, F.", "Batchelor, N.", "Casarini, F.", "Saliceti, S.", "Game, C.", "Sreendra, N.", "Patel, K.", "Gwira, M.", "Huber, A.", "Hurley, N.", "Nori, F.", "Hadsell, R.", "Heess, N."]
    year: 2024
    title: "Learning agile soccer skills for a bipedal robot with deep reinforcement learning"
    journal: "Science Robotics"
    volume: 9
    pages: "eadi8022"
    doi: "10.1126/scirobotics.adi8022"
    open_access: true
  - authors: ["Tong, Y.", "Liu, H.", "Zhang, Z."]
    year: 2024
    title: "Advancements in Humanoid Robots: A Comprehensive Review and Future Prospects"
    journal: "IEEE/CAA Journal of Automatica Sinica"
    volume: 11
    pages: "301–328"
    doi: "10.1109/jas.2023.124140"
status: published
---

## Zwei Arten, sich auf zwei Beinen zu bewegen

Du gehst, ohne darüber nachzudenken, und doch ist jeder Schritt ein kleines Stück angewandte Physik. Beim Gehen schwingt dein Körper über ein steifes Bein; beim Laufen federt er auf einem Bein, das wie eine Feder arbeitet. Diese beiden Tricks sparen auf unterschiedliche Weise Energie, und so verschiedene Tiere wie Truthühner, Hunde und Kängurus nutzen dieselben beiden [1](#ref-1){:.cite}. Gehen und Laufen, die beiden grundlegenden Gangarten des Menschen, sind sehr komplexe Bewegungen – lassen sich aber mit zwei einfachen Modellen beschreiben: einem **inversen Pendel** und einer **Feder** [2](#ref-2){:.cite}.

Der aufrechte Gang auf zwei Beinen ist alt: Die schreitende Zweibeinigkeit ist möglicherweise schon bald nach der Trennung der Linien von Mensch und Schimpanse entstanden. Ausdauerndes Laufen über lange Strecken kam später; nach Dennis Bramble und Daniel Lieberman ist der Ausdauerlauf eine Fähigkeit der Gattung *Homo*, die vor etwa 2 Millionen Jahren entstand und den menschlichen Körperbau geprägt haben könnte [3](#ref-3){:.cite}.

Dieser Artikel erklärt, wie Pendel und Feder funktionieren, warum du ungefähr bei derselben „Geschwindigkeitskennzahl“ vom Gehen ins Laufen wechselst wie ein Kind, ein Erwachsener oder ein Mensch bei simulierter geringer Schwerkraft – und wie Ingenieurinnen und Ingenieure Roboter bauen und trainieren, die auf zwei Beinen gehen. Die Kennzahl ist dieselbe, die in [Wie Katzen trinken](/de/artikel/wie-katzen-trinken/) den Takt der Katzenzunge bestimmt.

## Ein Schritt in vier Phasen

1. **Fersenaufsatz.** Der vordere Fuß setzt auf, während der hintere noch am Boden ist. Für einen Moment tragen beide Beine den Körper, und seine Bahn muss von abwärts nach aufwärts umgelenkt werden [4](#ref-4){:.cite}.
2. **Überschwingen.** Der hintere Fuß hebt ab und schwingt nach vorn. Der Körper schwingt über das fast gestreckte Standbein; beim Aufsteigen wird er langsamer und ist in der Mitte des Schritts am höchsten [5](#ref-5){:.cite}.
3. **Vorwärtsfallen.** Hinter dem höchsten Punkt fällt der Körper auf seinem Bogen nach vorn und unten und wird wieder schneller. Potenzielle Energie verwandelt sich zurück in kinetische Energie [1](#ref-1){:.cite}.
4. **Abstoßen.** Wadenmuskeln und Achillessehne stoßen den Fuß vom Boden ab, während der andere Fuß aufsetzt – und die nächste Pendelschwingung beginnt [6](#ref-6){:.cite}.

{% include lens-tabs.html lenses="biology,physics,math,cs,physical-ai" %}

{% include lens-start.html lens="biology" %}

## Biologie-Linse: Federn im Bein

**Muskeln, die halten, Sehnen, die sich dehnen.** Ein Muskel ist über eine Sehne am Knochen befestigt, ein festes, leicht elastisches Gewebeband. Tetsuo Fukunaga und Kollegen filmten den Wadenmuskel von sechs Männern mit Ultraschall, während sie auf einem Laufband mit 3 km/h gingen. In der Standphase änderten die Muskelfasern ihre Länge kaum – sie kontrahierten nahezu isometrisch, was wenig Energie kostet. Die Achillessehne dagegen dehnte sich um etwa **7 mm**, während der Körper von einem Bein getragen wurde, und federte beim Abstoßen zurück: Sie speicherte elastische Energie und gab sie wieder ab, wie eine Feder [6](#ref-6){:.cite}.

**Eine Feder im Fußgewölbe.** Beim Laufen leisten die elastischen Strukturen noch mehr. In der ersten Hälfte der Standphase verliert der Körper kinetische und potenzielle Energie; sie wird kurz als elastische Verformungsenergie gespeichert und in der zweiten Hälfte durch elastischen Rückstoß zurückgegeben – der Läufer hüpft dahin wie ein Gummiball. Robert Ker und Kollegen zeigten, dass nicht nur die Sehnen des Unterschenkels als solche Federn wirken, sondern auch das **Fußgewölbe** [7](#ref-7){:.cite}. Wie viel eine Sehne zurückgeben kann, maßen Glen Lichtwark und Alan Wilson beim einbeinigen Hüpfen: Im Mittel kamen **38 J** pro Sprung aus dem Rückstoß der Achillessehne zurück, 16 % der gesamten mechanischen Arbeit des Sprungs (254 J). Die Sehne dehnte sich auf dem Höhepunkt um 8,3 % ihrer Länge, und ihre Steifigkeit unterschied sich deutlich von Person zu Person [8](#ref-8){:.cite}.

**Was Fortbewegung kostet.** Beide Mechanismen senken die Energie, die die Muskeln aufbringen müssen. Gehen ist am sparsamsten – etwa 2 J pro Kilogramm Körpermasse und Meter – bei etwa 1,11 m/s. Laufen kostet etwa 4 J pro Kilogramm und Meter, unabhängig von der Geschwindigkeit [2](#ref-2){:.cite}. Robert McNeill Alexander zeigte, dass die Kraftverläufe beim menschlichen Gehen und Laufen die Arbeit der Muskeln bei jeder Geschwindigkeit minimieren und dass die Elastizität der Sehnen beim Laufen einen großen Teil der sonst nötigen Energie spart [9](#ref-9){:.cite}.

**Zum Gehen gebaut, zum Laufen gemacht?** Menschen sind, wie Menschenaffen, im Vergleich zu den meisten Vierbeinern schlechte Sprinter. Bramble und Lieberman argumentieren aber, dass Menschen im Langstreckenlauf bemerkenswert gut sind – dank vieler Merkmale, die Spuren im Skelett hinterlassen. Dadurch lässt sich diese Fähigkeit im Fossilbericht auf die Gattung *Homo* datieren [3](#ref-3){:.cite}.

{% include lens-end.html %}

{% include lens-start.html lens="physics" %}

## Physik-Linse: Pendel und Feder

**Gehen: ein umgedrehtes Pendel.** Ein normales Pendel hängt unter seinem Drehpunkt. Beim Gehen ist der Drehpunkt der Fuß am Boden, und der Körper sitzt oben auf dem Bein – ein **inverses Pendel**. Das Standbein zwingt den Schwerpunkt auf einen Kreisbogen statt auf eine gerade Linie [5](#ref-5){:.cite}. In der ersten Hälfte des Schritts wird der Körper langsamer und steigt: Kinetische Energie wird zu potenzieller Energie. In der zweiten Hälfte fällt er nach vorn und wird wieder schneller. Giovanni Cavagna, Norman Heglund und Richard Taylor maßen diesen Austausch bei Tieren vom Truthuhn bis zum Schafbock: Er ist bei mittleren Gehgeschwindigkeiten am größten und kann bis zu **70 %** der gesamten Energieänderungen eines Doppelschritts ausmachen, sodass die Muskeln nur 30 % aufbringen müssen [1](#ref-1){:.cite}.

**Warum Gehen trotzdem Energie kostet.** Ein ideales Pendel würde ohne Arbeit ewig schwingen. Beim Gehen muss aber bei jedem Schritt eine Pendelschwingung durch die nächste ersetzt werden: Wenn der vordere Fuß aufsetzt, muss die Bahn des Körpers von abwärts nach aufwärts umgelenkt werden. Dieser **Schritt-zu-Schritt-Übergang** kostet unvermeidlich mechanische Arbeit, und Arthur Kuo, Maxwell Donelan und Andy Ruina zeigten, dass er einen großen Teil des Stoffwechselaufwands beim Gehen ausmacht [4](#ref-4){:.cite}. Eine flachere Bahn würde nicht helfen: Ginge man mit einer geraderen Bahn des Schwerpunkts, bräuchten die Muskeln mehr Arbeit und Kraft [5](#ref-5){:.cite}.

**Laufen: ein Feder-Masse-System.** Beim Laufen, Traben und Hüpfen werden kinetische und potenzielle Energie nicht gegeneinander getauscht. Stattdessen spart ein anderer Mechanismus Energie: ein elastisches Federn des Körpers [1](#ref-1){:.cite}. Reinhard Blickhan beschrieb Laufen und Hüpfen mit einem sehr einfachen **Feder-Masse-Modell**: einer Punktmasse auf einer masselosen Feder. Das Modell verknüpft Kontaktzeit, Sprungfrequenz und die Auf-und-ab-Bewegung des Körpers und zeigt, dass ein hüpfender Mensch eine Frequenz wählt, bei der sich die größte Energiemenge noch elastisch speichern lässt [10](#ref-10){:.cite}.

| | Gehen | Laufen |
|---|---|---|
| Modell | inverses Pendel | Feder-Masse-System |
| Bein | steif, fast gestreckt | beugt sich und federt zurück |
| Energie gespart durch | Austausch von kinetischer und potenzieller Energie | elastische Energie, z. B. in Sehnen und Fußgewölbe |

{% include lens-end.html %}

{% include lens-start.html lens="math" %}

## Mathematik-Linse: die Froude-Zahl und der Wechsel ins Laufen

**Ein Tempolimit aus der Geometrie.** Am höchsten Punkt seines Bogens bewegt sich der Körper auf einem Kreis mit dem Radius *L*, der Beinlänge. Ein Körper, der sich mit der Geschwindigkeit *v* auf einem Kreis bewegt, braucht eine Zentripetalbeschleunigung *v*²/*L* zum Mittelpunkt hin – hier nach unten, zum Fuß. Beim Gehen kann nur die Schwerkraft sie liefern, also darf *v*²/*L* nicht größer als *g* sein [11](#ref-11){:.cite}. Das Verhältnis der beiden ist die **Froude-Zahl**:

<div class="formula" role="math" aria-label="Fr gleich v Quadrat durch g mal L"><var>Fr</var> = <span class="frac"><span class="frac__num"><var>v</var><sup>2</sup></span><span class="frac__den"><var>g</var> · <var>L</var></span></span></div>

Ist *Fr* größer als 1, kann die Schwerkraft den Körper nicht mehr auf seinem Bogen über dem Fuß halten: Er würde abheben. Das schnellste Gehen, das das Modell erlaubt, ist daher

<div class="formula" role="math" aria-label="v max gleich Wurzel aus g mal L"><var>v</var><sub>max</sub> = √(<var>g</var> · <var>L</var>)</div>

Bei einer Beinlänge von 0,9 m sind das etwa **3,0 m/s** oder 10,7 km/h – eine Rechnung aus dem Modell, durchgeführt in der Informatik-Linse.

**Dynamische Ähnlichkeit.** Die Froude-Zahl ist dieselbe Kennzahl, die in [Wie Katzen trinken](/de/artikel/wie-katzen-trinken/) den Takt der Katzenzunge bestimmt – dort vergleicht sie die Trägheit einer hochgezogenen Wassersäule mit der Schwerkraft, hier die Zentripetalbeschleunigung des Körpers. Robert McNeill Alexander und A. S. Jayes stellten die Hypothese auf, dass sich Säugetiere unterschiedlicher Größe **dynamisch ähnlich** bewegen, wenn sie sich mit derselben Froude-Zahl bewegen: Schrittlänge, der Anteil der Zeit, in der ein Fuß am Boden ist, und der Kraftverlauf sollten dann übereinstimmen [12](#ref-12){:.cite}. Für Gehen und Laufen setzte Alexander für *L* die Höhe des Hüftgelenks ein [9](#ref-9){:.cite}. Kinder, kleinwüchsige Menschen und größere Erwachsene gewinnen bei jedem Schritt auf dieselbe Weise Energie zurück, wenn man ihre Geschwindigkeit als Froude-Zahl ausdrückt [2](#ref-2){:.cite}.

**Der Wechsel bei Fr ≈ 0,5.** Menschen und andere Zweibeiner mit unterschiedlicher Beinlänge wechseln bei unterschiedlichen Geschwindigkeiten vom Gehen ins Laufen, aber bei etwa derselben Froude-Zahl: **0,5**. Rodger Kram, Antoinette Domingo und Daniel Ferris prüften das, indem sie ihre Versuchspersonen mit einer nahezu konstanten Kraft nach oben zogen und so eine geringere Schwerkraft simulierten. Je geringer die simulierte Schwerkraft, desto langsamer die Geschwindigkeit, bei der die Personen ins Laufen wechselten – die Froude-Zahl beim Wechsel blieb aber etwa gleich [11](#ref-11){:.cite}. Löst man *Fr* = 0,5 nach der Geschwindigkeit auf, erhält man

<div class="formula" role="math" aria-label="v Wechsel gleich Wurzel aus 0,5 mal g mal L"><var>v</var><sub>Wechsel</sub> = √(0,5 · <var>g</var> · <var>L</var>) ≈ 2,1 m/s für <var>L</var> = 0,9 m</div>

Das passt gut zu Messungen, wenn man eine Beinlänge von 0,9 m annimmt: In einer Studie von Alan Hreljac mit 20 jungen Erwachsenen wechselten die Personen im Mittel bei **2,06 m/s** [13](#ref-13){:.cite}.

**Nicht dort, wo es am sparsamsten ist.** Laufen wir, weil Laufen bei dieser Geschwindigkeit sparsamer ist? Hreljac maß auch die Geschwindigkeit, ab der Laufen energetisch günstiger war als Gehen: 2,24 m/s, deutlich schneller als die Geschwindigkeit, die die Personen wählten. Bei der Wechselgeschwindigkeit empfanden sie Gehen als anstrengender als Laufen. Das spricht dafür, dass Menschen die Gangart nicht wechseln, um ihren Energieverbrauch zu minimieren [13](#ref-13){:.cite}. Das Pendel erklärt, warum Gehen mit steigendem *Fr* schwieriger wird; was genau den Wechsel unterhalb der Grenze von 1 auslöst, ist noch eine Forschungsfrage.

{% include lens-end.html %}

{% include lens-start.html lens="cs" %}

## Informatik-Linse: ein Pendel, das geht

Wie schnell kann ein inverses Pendel gehen, und wo wechseln echte Menschen ins Laufen? Das Programm unten modelliert den Körper als Punktmasse an der Hüfte, die verlustfrei über ein steifes, masseloses Bein schwingt. Es berechnet die Energien während eines Schritts, die Geschwindigkeitsgrenze √(*g L*) und die Froude-Zahlen der von Hreljac gemessenen Wechselgeschwindigkeiten [13](#ref-13){:.cite}. **Modellannahmen:** eine Beinlänge von 0,90 m und eine Schrittlänge von 0,70 m, typisch für Erwachsene, aber in den zitierten Studien nicht gemessen; eine Geschwindigkeit von 1,1 m/s in der Mitte der Standphase, nahe der sparsamsten Gehgeschwindigkeit [2](#ref-2){:.cite}; und der Wechsel bei *Fr* = 0,5 [11](#ref-11){:.cite}.

```python
import numpy as np
import matplotlib.pyplot as plt

# Ein gehender Mensch als inverses Pendel: Der Körper (eine Punktmasse an der Hüfte) schwingt über ein steifes Bein.
G = 9.81                 # Schwerebeschleunigung (m/s²)
LEG = 0.90               # Beinlänge L, Hüftgelenk bis Boden (m) – angenommen für Erwachsene
STEP = 0.70              # Schrittlänge (m) – angenommen
WALK = 1.1               # Gehgeschwindigkeit in der Mitte der Standphase (m/s), nahe der sparsamsten
FR_SWITCH = 0.5          # Froude-Zahl, bei der Menschen vom Gehen ins Laufen wechseln (gemessen)
SWITCH_SPEEDS = {"bevorzugter Wechsel": 2.06, "energetisch günstigster Wechsel": 2.24}   # gemessen (m/s)


def froude(speed, leg=LEG, g=G):
    """Froude-Zahl Fr = v²/(g·L): Zentripetal- im Verhältnis zur Schwerebeschleunigung."""
    return speed**2 / (g * leg)


def max_walking_speed(leg=LEG, g=G):
    """Am höchsten Punkt bewegt sich der Körper auf einem Kreis mit Radius L. Nur die Schwerkraft
    kann ihn auf der Kurve halten, also v²/L ≤ g, d. h. Fr ≤ 1 und v ≤ √(g·L) – schneller, und er hebt ab."""
    return np.sqrt(g * leg)


# Ein Schritt: Das Bein schwingt von −θ0 bis +θ0 um die Senkrechte, ohne Verluste (Energieerhaltung)
theta0 = np.arcsin(STEP / 2 / LEG)
theta = np.linspace(-theta0, theta0, 201)
x = LEG * np.sin(theta)                                   # Position der Hüfte über dem Fuß (m)
height = LEG * np.cos(theta)                              # Höhe der Hüfte (m)
speed = np.sqrt(WALK**2 + 2 * G * (LEG - height))         # oben am langsamsten, an den Enden am schnellsten
potential = G * (height - height.min())                   # Energie pro kg Körpermasse (J/kg)
kinetic = 0.5 * (speed**2 - speed.min()**2)
total = potential + kinetic

v_max = max_walking_speed()
print(f"ein Pendelschritt: Die Hüfte steigt um {100 * (height.max() - height.min()):.1f} cm, "
      f"Geschwindigkeit oben {speed.min():.2f} m/s, an den Enden {speed.max():.2f} m/s")
print(f"kinetische und potenzielle Energie tauschen die Rollen; ihre Summe ändert sich um {np.ptp(total):.1f} J/kg")
print(f"schnellstmögliches Gehen (Fr = 1): v = √(g·L) = {v_max:.2f} m/s = {3.6 * v_max:.1f} km/h")
print(f"vorhergesagter Wechsel ins Laufen bei Fr = {FR_SWITCH}: {np.sqrt(FR_SWITCH * G * LEG):.2f} m/s")
for name, v in SWITCH_SPEEDS.items():
    print(f"gemessen, {name}: {v:.2f} m/s → Fr = {froude(v):.2f}, "
          f"Beinkraft oben = {1 - froude(v):.2f} × Körpergewicht")

plt.rcParams["font.size"] = 13      # große Schrift: Das Diagramm bleibt auf dem Handy lesbar
fig, (top, bottom) = plt.subplots(2, 1, figsize=(6.4, 8.4), layout="constrained")
cm = 100 * x
top.plot(cm, potential, lw=2.5, color="#1f6f8b")
top.plot(cm, kinetic, lw=2.5, ls="--", color="#c0392b")
top.plot(cm, total, lw=1.5, ls=":", color="black")
top.text(0, potential.max() - 0.12, "potenziell", ha="center", va="top", color="#1f6f8b")
top.annotate("kinetisch", xy=(cm[20], kinetic[20]), xytext=(cm[0], 0.98), color="#c0392b",
             arrowprops=dict(arrowstyle="-", color="#c0392b"))
top.text(0, total[0] + 0.05, "Summe: konstant", ha="center", va="bottom")
top.set_xlabel("Position der Hüfte über dem Fuß (cm)")
top.set_ylabel("Energie (J pro kg)")
top.set_ylim(0, total[0] + 0.45)
top.set_title(f"Ein Pendelschritt bei {WALK} m/s: Energien tauschen")

v = np.linspace(0, 3.4, 400)
force = 1 - froude(v)                                     # Beinkraft oben, in Körpergewichten
valid = v <= v_max
bottom.plot(v[valid], force[valid], lw=2.5, color="black", label="Pendelmodell")
bottom.plot(v[~valid], force[~valid], lw=2, ls=":", color="grey", label="Modell ungültig: Körper hebt ab")
bottom.axhline(0, color="grey", lw=0.8)
bottom.axvline(v_max, color="grey", lw=0.8)
bottom.text(v_max + 0.05, 0.85, "Fr = 1", va="top")
for (name, s), marker in zip(SWITCH_SPEEDS.items(), ("o", "s")):
    bottom.plot(s, 1 - froude(s), marker, ms=9, color="#c98a1b", label=f"gemessen: {name}")
bottom.set_xlabel("Gehgeschwindigkeit (m/s)")
bottom.set_ylabel("Beinkraft oben (× Gewicht)")
bottom.set_ylim(-0.45, 1.1)
bottom.set_title("Wir laufen lange, bevor das Bein entlastet")
bottom.legend(loc="lower left", fontsize=11)
plt.show()
```
{% include code-result.html file="walking_pendulum.py" label="Abb. 2" caption="Ausgabe des Programms oben. Oben: Während eines Schritts im Pendelmodell bei 1,1 m/s tauschen potenzielle und kinetische Energie die Rollen, ihre Summe bleibt konstant. Unten: Die Kraft, die das Bein am höchsten Punkt des Bogens tragen muss, sinkt mit steigender Gehgeschwindigkeit und erreicht bei der Froude-Zahl 1 null; die Markierungen zeigen die gemessenen Wechselgeschwindigkeiten. Das Modell nimmt ein steifes, masseloses Bein von 0,9 m Länge und keine Verluste an." alt="Zwei Diagramme übereinander. Oben: Energie in Joule pro Kilogramm über der Position der Hüfte über dem Fuß, von minus 35 bis plus 35 Zentimeter. Die potenzielle Energie bildet einen Buckel mit dem Maximum von etwa 0,7 Joule pro Kilogramm in der Mitte; die kinetische Energie bildet ein spiegelbildliches Tal; ihre Summe ist eine flache gepunktete Linie. Unten: Die Beinkraft am höchsten Punkt des Bogens in Körpergewichten fällt von 1 bei der Geschwindigkeit null entlang einer abwärts gekrümmten Kurve und erreicht bei 2,97 Metern pro Sekunde null, markiert mit Fr gleich 1; danach ist die Kurve gepunktet. Zwei Markierungen zeigen die gemessenen Wechselgeschwindigkeiten 2,06 und 2,24 Meter pro Sekunde bei Beinkräften von etwa 0,5 und 0,4 Körpergewichten." %}

Was das Ergebnis lehrt:

- **Das Pendel tauscht Energie kostenlos.** Im Modell steigt die Hüfte um 7,1 cm, wird oben auf 1,10 m/s langsamer und an den Enden des Schritts auf 1,61 m/s schneller, während sich die Summe der Energien nicht ändert. Echte Menschen gewinnen nur einen Teil der Energie zurück – bis zu 70 % [1](#ref-1){:.cite} –, weil jeder Schritt-zu-Schritt-Übergang Arbeit kostet [4](#ref-4){:.cite}.
- **Ein Tempolimit.** Das schnellstmögliche Gehen des Pendels liegt bei 2,97 m/s oder 10,7 km/h. Das ist eine Obergrenze des Modells, keine gemessene Höchstgeschwindigkeit.
- **Menschen wechseln früh.** Bei *Fr* = 0,5 sagt das Modell den Wechsel bei 2,10 m/s voraus; die gemessene bevorzugte Wechselgeschwindigkeit von 2,06 m/s entspricht *Fr* = 0,48 – für die angenommene Beinlänge. Bei dieser Geschwindigkeit trägt das Bein am höchsten Punkt des Bogens noch das 0,52-Fache des Körpergewichts: Menschen fangen an zu laufen, lange bevor das Pendel abheben würde.

Probier es selbst:

- Ein Kind mit 0,5 m Beinlänge: Setze `LEG = 0.50`. Das schnellste Gehen sinkt auf 2,21 m/s und der vorhergesagte Wechsel auf 1,57 m/s – ein Kind muss früher anfangen zu laufen.
- Gehen auf dem Mond: Setze `G = 1.62`. Das schnellste Gehen sinkt auf 1,21 m/s, und wenn der Wechsel weiterhin bei *Fr* = 0,5 stattfindet, käme er bei 0,85 m/s. Das ist eine Extrapolation: Kram und Kollegen simulierten geringere Schwerkraft auf der Erde, indem sie ihre Versuchspersonen nach oben zogen, nicht auf dem Mond [11](#ref-11){:.cite}.

Zeigt die Ausgabe für eine gemessene Wechselgeschwindigkeit der Erwachsenen eine negative Beinkraft, liegt diese Geschwindigkeit für das geänderte Bein oder die geänderte Schwerkraft jenseits von *Fr* = 1: Dort gilt das Pendelmodell nicht mehr.

{% include code-variant.html file="walking_pendulum.py" id="child" replace="LEG = 0.90 " with="LEG = 0.50 " expect="2.21 1.57" %}
{% include code-variant.html file="walking_pendulum.py" id="moon" replace="G = 9.81 " with="G = 1.62 " expect="1.21 0.85" %}

{% include lens-end.html %}

{% include lens-start.html lens="physical-ai" %}

## Physical-AI-Linse: Roboter, die gehen

Physical AI – verkörperte künstliche Intelligenz, also Roboter, die in der physischen Welt wahrnehmen und handeln – muss das Problem lösen, das jedes Kleinkind löst: auf zwei Beinen aufrecht bleiben und vorankommen, ohne zu fallen. Ingenieurinnen und Ingenieure haben zwei sehr unterschiedliche Wege versucht: die Physik in die Maschine einbauen oder die Maschine lernen lassen.

**Gehen ohne Motor.** 1990 beschrieb Tad McGeer eine Klasse zweibeiniger Maschinen, für die Gehen eine natürliche Bewegung ist. Auf einer flachen Rampe gestartet, findet eine solche Maschine in einen gleichmäßigen Gang, der dem menschlichen Gehen recht ähnlich ist – **ohne Motor, ohne Steuerung und ohne Energiezufuhr** außer der Schwerkraft [14](#ref-14){:.cite}. Diese **passiv-dynamischen Laufmaschinen** sind inverse Pendel aus starren Teilen, die durch Gelenke verbunden sind. 2005 stellten Steven Collins, Andy Ruina, Russ Tedrake und Martijn Wisse drei Roboter nach diesem Prinzip vor, bei denen kleine Antriebe die Rolle der Rampe übernahmen. Sie gingen auf ebenem Boden mit weniger Steuerung und weniger Energie als andere angetriebene Roboter, und natürlicher – ein Hinweis darauf, dass passive Dynamik auch beim menschlichen Gehen wichtig ist [15](#ref-15){:.cite}.

**Ein Roboter auf einer Feder.** Auch die Feder des laufenden Beins fand ihren Weg in Maschinen. 1984 bauten Marc Raibert und Kollegen einen Roboter, der auf einem federnden Bein hüpfte und lief und dabei auf freiem Boden ohne Stütze das Gleichgewicht hielt. Seine Steuerung bestand aus drei einfachen Teilen: einem für die Vorwärtsgeschwindigkeit, einem für die Haltung des Körpers und einem für die Sprunghöhe [16](#ref-16){:.cite}.

**Lernen durch Ausprobieren.** Heute lernen viele Laufroboter das Gehen durch **bestärkendes Lernen** (Reinforcement Learning): Ein neuronales Netz steuert einen simulierten Roboter, erhält eine Belohnung für gutes Verhalten und verbessert sich durch Versuch und Irrtum über viele simulierte Versuche. Jemin Hwangbo und Kollegen trainierten ein solches Netz in der Simulation und übertrugen es auf den vierbeinigen Roboter ANYmal, so groß wie ein mittelgroßer Hund. Der gelernte Regler folgte Geschwindigkeitsvorgaben genauer und energieeffizienter als der bisherige, lief 25 % schneller als der bisherige Rekord des Roboters und stand nach Stürzen wieder auf; jedes Training dauerte höchstens elf Stunden auf einem gewöhnlichen PC [17](#ref-17){:.cite}.

**Humanoide Roboter.** Ilija Radosavovic und Kollegen trainierten einen Regler für einen humanoiden Roboter in voller Größe, nach Angaben der Autoren etwa 1,6 m groß und 45 kg schwer, vollständig in der Simulation – mit Tausenden zufällig variierter virtueller Umgebungen – und übertrugen ihn ohne weiteres Training auf den echten Roboter. Der Regler ist ein Transformer, eine Art neuronales Netz, die auch in großen Sprachmodellen steckt; er liest den jüngsten Verlauf der eigenen Sensorwerte und Aktionen des Roboters und sagt die nächste Aktion voraus. Der Roboter ging über verschiedene Gelände im Freien und war robust gegenüber äußeren Störungen wie Stößen mit einem Stock; in einer Woche ganztägiger Tests im Freien beobachteten die Autoren keinen Sturz [18](#ref-18){:.cite}. In viel kleinerem Maßstab trainierten Tuomas Haarnoja und Kollegen 51 cm große Miniatur-Humanoide, eins gegen eins Fußball zu spielen. Mit den gelernten Fähigkeiten gingen die Roboter 181 % schneller, drehten sich 302 % schneller und brauchten 63 % weniger Zeit zum Aufstehen als mit den vorprogrammierten Bewegungen des Roboters [19](#ref-19){:.cite}.

**Vom Pendel zur Strategie.** Die beiden Wege treffen sich: Ein lernender Roboter bewegt sich in einer simulierten Welt, die derselben Physik von Pendeln und Federn gehorcht, und ein Roboter, der diese Physik nutzt – wie die passiven Laufmaschinen –, braucht weniger Energie und weniger Steuerung. Eine Übersichtsarbeit von Yuchuan Tong und Kollegen zählt auf, was humanoiden Robotern noch fehlt: ein tieferes Verständnis biologischer Bewegung, bessere mechanische Strukturen und Materialien, bessere Antriebe und Regelung sowie eine effizientere Nutzung von Energie [20](#ref-20){:.cite}.

{% include lens-end.html %}

## Wie es weitergeht

Humanoide Roboter, die selbstständig in alltäglicher Umgebung arbeiten, hätten das Potenzial, gegen Arbeitskräftemangel in Fabriken zu helfen, ältere Menschen zu Hause zu unterstützen und neue Planeten zu besiedeln – so beschreiben Radosavovic und Kollegen ihr Ziel [18](#ref-18){:.cite}. Das ist ein Szenario, keine Prognose: Die Übersichtsarbeit von Tong und Kollegen nennt Energieeffizienz, Antriebe, Materialien und Regelung unter den offenen Herausforderungen und sieht eine vielversprechende Richtung darin, Bionik, vom Gehirn inspirierte Intelligenz, Mechanik und Regelung zu verbinden [20](#ref-20){:.cite}.

Die Natur setzt weiterhin den Maßstab. Das menschliche Gehen verbindet ein Pendel, das Energie fast kostenlos tauscht, Federn, die bei jedem Schritt Energie zurückgeben, und ein Nervensystem, das das Ganze auf unebenem Boden aufrecht hält. Auf beiden Seiten bleiben offene Fragen: was genau Menschen unterhalb der Grenze des Pendels vom Gehen ins Laufen wechseln lässt [13](#ref-13){:.cite} und wie Roboter lernen können, so sparsam zu gehen wie ein Mensch – oder wie eine passive Maschine, die ganz ohne Motor eine Rampe hinuntergeht [15](#ref-15){:.cite}.
