---
id: insect-flight
lang: de
ref: insect-flight
title: "Wie Insekten fliegen: Wirbel, Halteren und RoboBees"
short_title: "Insektenflug"
kicker: "Artikel · Aerodynamik"
description: "Insektenflügel erzeugen mehr Auftrieb, als die klassische Aerodynamik erlaubt – dank eines Wirbels an der Vorderkante. Wie Bienen und Fliegen fliegen."
dek: "Eine Honigbiene schlägt etwa 230-mal pro Sekunde mit den Flügeln, und ihre Flügel erzeugen mehr Auftrieb, als ein Flügel in gleichmäßiger Strömung könnte. Das Geheimnis ist ein Wirbel, der auf jedem Flügel sitzt. Ingenieurinnen und Ingenieure haben gelernt, ihn nachzubauen – und herausgefunden, warum Fliegen so schwer wird, wenn man klein ist."
date: 2026-10-04
permalink: /de/artikel/insektenflug/
image: /assets/og/insect-flight-de.jpg
og: { eyebrow: "Biologie · Aerodynamik · Physical AI", title: "Wie Insekten <em>fliegen</em> – und warum Roboterbienen so schwer sind", sub: "Ein Wirbel auf jedem Flügel, Kreisel aus Hinterflügeln und Roboter mit 80 mg.", title_px: 52 }
image_alt: "Schema einer schwebenden Honigbiene von der Seite: Ihre Flügel schwingen etwa 230-mal pro Sekunde vor und zurück; ein Ausschnitt zeigt den Querschnitt eines Flügels mit einem Vorderkantenwirbel auf der Oberseite und dem Auftrieb, den er erzeugt."
hero_figure: svg/insect-flight.svg
hero_caption: "<span class=\"caption__label\">Abb. 1</span> Eine schwebende Honigbiene. Ihre Flügel schwingen etwa 230-mal pro Sekunde um rund 90° vor und zurück und drehen sich an jedem Umkehrpunkt um, sodass immer dieselbe Kante vorn liegt. Der Ausschnitt zeigt einen Flügel im Querschnitt: Auf der Oberseite rollt sich die Luft zu einem Vorderkantenwirbel auf, der während des Schlags am Flügel bleibt und ihn mehr Auftrieb erzeugen lässt als in gleichmäßiger Strömung."
educational_level: "Intermediate"
keywords: ["Insektenflug", "wie fliegen Insekten", "Flügelschlagfrequenz", "Flug der Honigbiene", "Taufliege", "Drosophila", "Vorderkantenwirbel", "Clap-and-Fling", "instationäre Aerodynamik", "Halteren", "Schwingkölbchen", "Reynolds-Zahl", "Skalierung", "Quadrat-Kubik-Gesetz", "Auftriebsbeiwert", "asynchrone Flugmuskeln", "RoboBee", "Roboterinsekten", "Schlagflügelroboter", "Physical AI"]
about:
  - { name: "Insektenflug", wikidata: Q1425266, wikipedia: "https://de.wikipedia.org/wiki/Insektenflug" }
  - { name: "RoboBee", wikidata: Q12779901, wikipedia: "https://en.wikipedia.org/wiki/RoboBee" }
mentions:
  - { name: "Westliche Honigbiene", wikidata: Q30034 }
  - { name: "Drosophila melanogaster", wikidata: Q130888 }
  - { name: "Manduca sexta", wikidata: Q1366539 }
  - { name: "Encarsia formosa", wikidata: Q614882 }
  - { name: "Halteren", wikidata: Q1335456 }
  - { name: "Insektenflügel", wikidata: Q276572 }
  - { name: "Asynchrone Muskulatur", wikidata: Q30681494 }
  - { name: "Reynolds-Zahl", wikidata: Q178932 }
  - { name: "Auftriebsbeiwert", wikidata: Q760106 }
  - { name: "Quadrat-Kubik-Gesetz", wikidata: Q1527983 }
  - { name: "Corioliskraft", wikidata: Q169973 }
  - { name: "Piezoelektrizität", wikidata: Q183759 }
  - { name: "Kleinstdrohne", wikidata: Q773392 }
dimensions:
  time: ["modern-era", "age-of-ai"]
  space: ["atmosphere", "lab"]
  physics: ["fluid-dynamics", "mechanics"]
  adjacent_sciences: ["biology", "mathematics", "computer-science", "robotics", "physical-ai", "bionics"]
beings: ["honey-bee", "fruit-fly"]
lenses: ["biology", "physics", "math", "cs", "physical-ai"]
key_facts:
  - "Honigbienen schweben mit einem kurzen Flügelschlag von etwa 90° und einer hohen Flügelschlagfrequenz von etwa **230 Hz**; Taufliegen schlagen ihre 2,5 mm langen Flügel etwa 200-mal pro Sekunde um 145–165° [1](#ref-1){:.cite}."
  - "Insektenflügel erzeugen typischerweise **2- bis 3-mal mehr Auftrieb**, als die herkömmliche Aerodynamik erklären kann. Die meisten Insekten gewinnen ihn durch einen **Vorderkantenwirbel**, der am Flügel haften bleibt und spiralförmig zur Flügelspitze hinausläuft [2](#ref-2){:.cite} [6](#ref-6){:.cite}."
  - "Fliegen spüren Drehungen mit ihren **Halteren** (Schwingkölbchen) – winzigen, hantelförmigen Organen, die aus den Hinterflügeln entstanden sind. Sie schwingen wie Flügel und messen wie ein Kreisel die Corioliskräfte, wenn sich der Körper dreht [8](#ref-8){:.cite} [9](#ref-9){:.cite}."
  - "Kleinere Flieger müssen schneller schlagen: Bei Körpern gleicher Form wächst die zum Schweben nötige Flügelschlagfrequenz mit eins durch die Wurzel aus der Größe. Eine Formel aus Masse und Flügelfläche erklärt 75 % der Unterschiede in der Flügelschlagfrequenz der Insekten [3](#ref-3){:.cite}."
  - "Harvards RoboBee wog bei ihren gesteuerten Flügen 2013 nur 80 mg; ein vierflügeliger Nachfolger mit 90 mg flog 2019 ohne Kabel, mit Solarzellen und Elektronik an Bord, insgesamt 259 mg [16](#ref-16){:.cite} [17](#ref-17){:.cite}."
faq:
  - q: "Stimmt es, dass Bienen eigentlich nicht fliegen können dürften?"
    a: "Nein. Die Behauptung geht auf eine einfache Rechnung von 1934 zurück, deren Annahmen sich später als falsch erwiesen; die herkömmliche Aerodynamik starrer Tragflächen kann den Flug von Bienen und anderen kleinen Insekten nicht erklären. Tatsächlich gilt: Schlagende Flügel erzeugen mit instationären Effekten zusätzlichen Auftrieb, vor allem mit einem Vorderkantenwirbel, der am Flügel haften bleibt. Die herkömmliche Theorie reicht nicht aus, um den Insektenflug zu erklären – die moderne instationäre Aerodynamik erklärt ihn."
  - q: "Wie schnell schlagen Insektenflügel?"
    a: "Sehr unterschiedlich. In einem Datensatz von mehr als 150 Arten reichen die Flügelschlagfrequenzen von 6 Schlägen pro Sekunde bei einem Schmetterling bis zu 480 pro Sekunde bei der Gelbfiebermücke. Eine Honigbiene schlägt etwa 230-mal pro Sekunde mit den Flügeln, eine Taufliege etwa 200-mal."
  - q: "Was ist ein Vorderkantenwirbel?"
    a: "Wenn ein Insektenflügel unter steilem Winkel durch die Luft streicht, löst sich die Strömung an seiner Vorderkante ab und rollt sich auf der Oberseite zu einem Wirbel auf. An einer Flugzeugtragfläche würde sich ein solcher Wirbel ablösen, und die Strömung würde abreißen. An einem schlagenden Insektenflügel bleibt er während des ganzen Schlags haften und läuft spiralförmig zur Flügelspitze hinaus. Der Unterdruck im Wirbel liefert zusätzlichen Auftrieb."
  - q: "Was sind Halteren?"
    a: "Halteren, auch Schwingkölbchen genannt, sind die kleinen, keulenförmigen Organe der Fliegen an der Stelle der Hinterflügel. Sie schwingen im Takt der Flügel auf und ab. Dreht sich die Fliege, drücken Corioliskräfte sie zur Seite, und Sinnesorgane an ihrer Basis messen das. Die Fliege nutzt das Signal wie einen Kreisel, um ihren Körper stabil zu halten."
  - q: "Was ist die RoboBee?"
    a: "Die RoboBee ist eine Familie insektengroßer Flugroboter der Harvard University. Ihre Flügel werden von piezoelektrischen Aktoren angetrieben, dünnen Schichten, die sich unter elektrischer Spannung biegen, denn Elektromotoren arbeiten in dieser Größe schlecht. Die 2013 geflogene Version wog 80 Milligramm und brauchte ein Kabel für Strom und Steuerung; eine vierflügelige Version flog 2019 ohne Kabel, mit Solarzellen als Energiequelle. Ein völlig autonomer Flug mit Sensoren, Rechner und Energie an Bord ist noch ein Forschungsziel."
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

## Die Biene, die „nicht fliegen konnte“

1934 schlossen August Magnan und André Sainte-Laguë aus einer einfachen Rechnung, dass der Flug der Bienen „unmöglich“ sei. Seitdem stehen Bienen für die Kluft zwischen aerodynamischer Theorie und lebenden Tieren [1](#ref-1){:.cite}. Die Rechnung war falsch – aber sie wies auf etwas Wahres hin: Ein Insektenflügel, im Windkanal in gleichmäßiger Strömung getestet, erzeugt zu wenig Auftrieb, um das Tier zu tragen [1](#ref-1){:.cite}. Typischerweise erzeugen Insektenflügel **2- bis 3-mal mehr Auftrieb**, als die herkömmliche Aerodynamik erklären kann [2](#ref-2){:.cite}.

Insekten fliegen trotzdem, und zwar mit erstaunlichen Frequenzen. Eine Honigbiene mit 9,7 mm langen Flügeln schlägt sie etwa **230-mal pro Sekunde**; eine viel kleinere Taufliege schlägt ihre 2,5 mm langen Flügel etwa 200-mal pro Sekunde [1](#ref-1){:.cite}. Über mehr als 150 Arten reichen die Flügelschlagfrequenzen von 6 Schlägen pro Sekunde bei einem Schmetterling, dem Grünaderweißling, bis zu 480 bei der Gelbfiebermücke [3](#ref-3){:.cite}.

Dieser Artikel erklärt, woher der fehlende Auftrieb kommt, wie Fliegen mit einem eingebauten Kreisel das Gleichgewicht halten, warum kleine Flieger schneller schlagen müssen – und warum Ingenieurinnen und Ingenieure, die Roboterinsekten bauen, auf dieselbe Physik stoßen. Mit der Größe ihrer Welt liegen Insekten zwischen zwei anderen Artikeln dieser Seite: dem Bakterium, für das sich Wasser wie Honig anfühlt ([Schwimmen in Honig](/de/artikel/schwimmen-in-honig/)), und uns.

## Ein Flügelschlag in vier Schritten

Ein schwebendes Insekt schlägt seine Flügel nicht auf und ab wie ein Vogel im Streckenflug. Beim „normalen Schweben“, wie Torkel Weis-Fogh es nannte, schlagen die Flügel fast waagerecht vor und zurück [4](#ref-4){:.cite}:

1. **Vorschlag.** Der Flügel streicht unter steilem Anstellwinkel nach vorn. Die Luft löst sich an der Vorderkante ab und rollt sich auf der Oberseite zu einem **Vorderkantenwirbel** auf, der während des Schlags haften bleibt – ein „verzögerter Strömungsabriss“ [5](#ref-5){:.cite} [6](#ref-6){:.cite}.
2. **Umkehr.** Am Ende des Schlags bremst der Flügel ab und dreht sich rasch um seine Längsachse, sodass auf dem Rückweg dieselbe Kante vorn liegt. Die Drehung selbst erzeugt zusätzliche Kraft [5](#ref-5){:.cite}.
3. **Rückschlag.** Der umgedrehte Flügel streicht zurück; wieder bildet sich ein Vorderkantenwirbel, und der Flügel erzeugt Auftrieb.
4. **Begegnung mit dem eigenen Nachlauf.** Nach der nächsten Umkehr bewegt sich der Flügel durch die Luft, die er gerade in Bewegung gesetzt hat, und gewinnt daraus Kraft („Wake Capture“) [5](#ref-5){:.cite}.

{% include lens-tabs.html lenses="biology,physics,math,cs,physical-ai" %}

{% include lens-start.html lens="biology" %}

## Biologie-Linse: ein Flugmotor und ein Kreisel

**Zwei Arten zu schweben.** Nicht alle Insekten schlagen ihre Flügel auf dieselbe Weise. Taufliegen schwingen ihre Flügel über einen großen Winkel von 145–165°. Honigbienen nutzen kurze Schläge von etwa 90° bei einer hohen Frequenz von etwa 230 Hz – und sie gewinnen einen großen Teil ihrer Kraft an den Umkehrpunkten, aus instationären Effekten wie der schnellen Drehung des Flügels, der Beschleunigung der Luft und dem Zusammenspiel mit dem eigenen Nachlauf [1](#ref-1){:.cite}. Douglas Altshuler und Kollegen ließen Honigbienen in **Heliox** schweben, einem atembaren Gemisch aus Sauerstoff und Helium, das nur etwa ein Drittel so dicht ist wie Luft. Die Bienen hielten ihre Flügelschlagfrequenz fast konstant und machten ihre Schläge stattdessen fast 50 % weiter [1](#ref-1){:.cite}.

**Ein Motor, der von selbst läuft.** Hunderte Kontraktionen pro Sekunde fallen einem gewöhnlichen Muskel schwer, denn er braucht für jede Kontraktion einen Nervenimpuls. Manche Insekten nutzen stattdessen eine besondere Art von Flugmuskel: **asynchrone Muskeln**, bei denen elektrische und mechanische Aktivität nicht im Gleichtakt sind. Ein solcher Muskel wird verzögert aktiviert, wenn er gedehnt wird, und deaktiviert, wenn er sich verkürzt; von einer gleichmäßigen Folge von Nervenimpulsen angetrieben, kann er in einem schwingenden System immer wieder Arbeit leisten [7](#ref-7){:.cite}. Insekten mit kleinen Flügeln und schweren Körpern wie Bienen brauchen solche Muskeln, um die nötigen Frequenzen zu erreichen [3](#ref-3){:.cite}. Und weil die Flügel an jedem Umkehrpunkt beschleunigt und abgebremst werden müssen, sind die meisten Insekten auf ein wirksames elastisches System im Thorax angewiesen, das die Energie der Flügelbewegung speichert und zurückgibt [4](#ref-4){:.cite}.

**Ein Kreisel aus Hinterflügeln.** Fliegen (Diptera) haben nur ein Flügelpaar. Ihre Hinterflügel haben sich zu **Halteren** entwickelt, auch Schwingkölbchen genannt: kleinen, hantelförmigen Organen mit Sinnesorganen an ihrer Basis [8](#ref-8){:.cite}. Eine Haltere schwingt um etwa 150° auf und ab, mit einer Frequenz, die ihre eigene mechanische Resonanz bestimmt [9](#ref-9){:.cite}. Dreht sich der Körper der Fliege, wirken auf die schwingende Haltere Kreisel- oder **Corioliskräfte** quer zu ihrer Schwingung, und die Sinnesorgane an ihrer Basis erfassen sie [9](#ref-9){:.cite} [8](#ref-8){:.cite}. Michael Dickinson schwenkte eine Flugarena mit Taufliegen darin hin und her: Die Fliegen antworteten mit ausgleichenden Änderungen ihrer Flügelschläge, und diese Reflexe verschwanden, wenn die Halteren entfernt wurden [8](#ref-8){:.cite}. Schon 1948 fotografierte John Pringle eine Fliege ohne Halteren im freien Flug – sie zeigte die spiralförmige Instabilität, die man bei einer Fliege erwartet, die ihre Drehungen nicht stabilisieren kann [9](#ref-9){:.cite}.

Bienen haben keine Halteren, und wie sie aufrecht bleiben, ist nicht sicher bekannt. Ein Vorschlag sind die **Ocellen**, drei einfache Lichtsensoren oben auf dem Kopf, die die Helligkeit des Himmels messen; Schwärmer dagegen spüren Drehungen mit ihren schwingenden Antennen, nach einem ähnlichen Prinzip wie die Halteren [10](#ref-10){:.cite}.

{% include lens-end.html %}

{% include lens-start.html lens="physics" %}

## Physik-Linse: zwischen Honig und Luft

**Wo Insekten in der Welt der Strömungen leben.** Die Reynolds-Zahl *Re* = *ρ v L* / *η* vergleicht Trägheitskräfte mit Zähigkeitskräften (siehe [Schwimmen in Honig](/de/artikel/schwimmen-in-honig/)). Ein Bakterium schwimmt bei etwa 10<sup>−5</sup>: Die Zähigkeit herrscht, die Trägheit spielt keine Rolle. Ein schwimmender Mensch erreicht Millionen. Insekten liegen dazwischen: In einem Datensatz von mehr als 150 Arten gehört der niedrigste Wert, etwa 8, zu einer kleinen Blattlaus; abgesehen von einigen Blattläusen und Mottenschildläusen sind Werte über 100 – typisch um 1.000 – die Regel [3](#ref-3){:.cite}. Die winzige Wespe *Encarsia formosa* fliegt bei *Re* = 10–20 [4](#ref-4){:.cite}, eine Taufliege bei 100–200 [11](#ref-11){:.cite}. In diesem mittleren Bereich zählen beide Kräfte: Die Luft ist zäh genug, um die Leistung gewöhnlicher Flügel zu verderben, aber der Körper des Insekts hat noch Trägheit. Wenn eine Taufliege eine Kurve fliegt, bestimmt die Trägheit, nicht die Reibung, die Flugdynamik ihres Körpers [12](#ref-12){:.cite}.

**Der Vorderkantenwirbel.** 1996 machten Charles Ellington und Kollegen die Strömung um die Flügel des Tabakschwärmers *Manduca sexta* sichtbar, zusammen mit einem großen mechanischen Modell eines Schlagflügels, dem „Flapper“. Beim Abschlag fanden sie einen kräftigen **Vorderkantenwirbel**, stark genug, um den hohen Auftrieb zu erklären. Er entsteht durch dynamischen Strömungsabriss und läuft spiralförmig zur Flügelspitze hinaus, mit einer Geschwindigkeit entlang der Spannweite, die der Schlaggeschwindigkeit vergleichbar ist; die Strömung ähnelt dem kegelförmigen Wirbel an einem Deltaflügel, und die Strömung entlang der Spannweite stabilisiert den Wirbel [6](#ref-6){:.cite}. An einem nicht schlagenden Flügel würde sich der Wirbel bei so steilem Winkel in den Nachlauf ablösen; am schlagenden Insektenflügel bleibt er stabil haften und verstärkt die Kräfte erheblich [13](#ref-13){:.cite}. Sogar Modellflügel eines Schwärmers, die sich einfach wie ein Propeller drehen, erzeugen dank dieses Wirbels hohe Kraftbeiwerte [14](#ref-14){:.cite}.

**Drehung und Wake Capture.** Michael Dickinson, Fritz-Olaf Lehmann und Sanjay Sane beschrieben drei zusammenwirkende Mechanismen: den verzögerten Strömungsabriss während der Schläge sowie Rotationszirkulation und Wake Capture an den Umkehrpunkten. Die beiden Rotationsmechanismen geben dem Insekt außerdem ein wirksames Mittel, Größe und Richtung seiner Flugkräfte beim Steuern zu verändern [5](#ref-5){:.cite}.

**Clap-and-Fling.** Manche Insekten führen ihre Flügel über dem Körper zusammen und schleudern sie dann auf wie ein Buch. Weis-Fogh entdeckte diesen Mechanismus 1973 bei *Encarsia formosa*: Bei ihrer niedrigen Reynolds-Zahl braucht die Wespe einen Auftriebsbeiwert von 2 oder 3, den die stationäre Aerodynamik nicht liefern kann. Das Aufschleudern baut die Zirkulation um jeden Flügel schon vor dem Abschlag auf, und der Auftrieb entsteht fast sofort [4](#ref-4){:.cite}. An einem Modellflügel der Taufliege erhöhte Clap-and-Fling den Gesamtauftrieb um bis zu 17 %, aber nur, wenn sich die Flügel bis auf 10–12° näherten [11](#ref-11){:.cite}. Die meisten Insekten verlassen sich jedoch auf den Vorderkantenwirbel [2](#ref-2){:.cite}.

{% include lens-end.html %}

{% include lens-start.html lens="math" %}

## Mathematik-Linse: warum kleine Flieger schneller schlagen

**Der Auftrieb eines bewegten Flügels.** Ein Flügel der Fläche *S*, der sich mit der Geschwindigkeit *U* durch Luft der Dichte *ρ* bewegt, erzeugt den Auftrieb

<div class="formula" role="math" aria-label="L gleich ein halb mal rho mal C L mal S mal U Quadrat"><var>L</var> = ½ · <var>ρ</var> · <var>C</var><sub>L</sub> · <var>S</var> · <var>U</var><sup>2</sup></div>

Dabei ist *C*<sub>L</sub> der Auftriebsbeiwert, eine Zahl, die beschreibt, wie gut der Flügel geformt und angestellt ist. Ein Schlagflügel der Länge *R*, der mit der Frequenz *f* über den Schlagwinkel *Φ* schwingt, bewegt seine Spitze im Mittel mit *U* = 2 *Φ R f* – zwei Schläge pro Flügelschlag. Die aerodynamischen Kräfte wachsen deshalb mit dem Quadrat der Spitzengeschwindigkeit, und die ist ein Produkt aus Schlagamplitude, Flügelschlagfrequenz und Flügellänge [1](#ref-1){:.cite}.

**Das Quadrat-Kubik-Gesetz.** Nun verkleinern wir ein Insekt, ohne seine Form zu ändern: Jede Länge wird mit einem Faktor *k* multipliziert. Die Masse – und mit ihr das Gewicht *W* – sinkt mit dem Volumen, also wie *k*<sup>3</sup>; die Flügelfläche sinkt nur wie *k*<sup>2</sup>. Zum Schweben muss der Auftrieb das Gewicht tragen:

<div class="formula formula--steps"><span>½ <var>ρ</var> <var>C</var><sub>L</sub> <var>S</var> <var>U</var><sup>2</sup> = <var>W</var> ⇒ <var>U</var><sup>2</sup> ∝ <var>W</var>/<var>S</var> ∝ <var>k</var><sup>3</sup>/<var>k</var><sup>2</sup> = <var>k</var></span><span><var>f</var> = <var>U</var> / (2<var>Φ</var><var>R</var>) ∝ <var>k</var><sup>1/2</sup>/<var>k</var> = <var>k</var><sup>−1/2</sup></span></div>

Die Flügel eines kleineren Insekts dürfen sich langsamer bewegen, aber weil sie so kurz sind, müssen sie **schneller** schlagen. Eine Honigbiene, auf die halbe Länge geschrumpft, bräuchte die √2 ≈ 1,41-fache Frequenz: etwa 325 statt 230 Schläge pro Sekunde.

**Was die Daten sagen.** Echte Insekten sind keine maßstäblichen Modelle voneinander – Zweiflügler sind anders gebaut als Schmetterlinge. Der Mathematiker Michael Deakin leitete mit einer Dimensionsanalyse eine Formel für die Flügelschlagfrequenz *n* aus der Masse *m* und der Flügelfläche *A* her und prüfte sie an mehr als 150 Arten [3](#ref-3){:.cite}:

<div class="formula" role="math" aria-label="n gleich K mal Wurzel aus m geteilt durch A"><var>n</var> = <var>K</var> · <span class="frac"><span class="frac__num">√<var>m</var></span><span class="frac__den"><var>A</var></span></span></div>

Diese Formel erklärt 75 % der Unterschiede in den gemessenen Frequenzen; die Masse allein tut es nicht – bei Schmetterlingen gibt es keinen signifikanten Zusammenhang zwischen Masse und Flügelschlagfrequenz [3](#ref-3){:.cite}. Für Insekten gleicher Form gilt *m* ∝ *k*<sup>3</sup> und *A* ∝ *k*<sup>2</sup>, also √*m*/*A* ∝ *k*<sup>−1/2</sup> – dasselbe Gesetz wie oben. Honigbiene und Taufliege zeigen die Grenzen von „gleicher Form“: Mit viermal kürzeren Flügeln müsste die Fliege mit etwa 450 Hz schlagen, sie kommt aber mit 200 Hz aus – unter anderem, indem sie ihre Flügel über den 1,6- bis 1,8-fachen Winkel schwingt [1](#ref-1){:.cite}, und weil sie leichter ist, als eine geschrumpfte Biene wäre.

**Leistung und Gewicht.** Wie viel Leistung kostet das Schweben pro Newton Gewicht? Eine einfache Abschätzung behandelt die schlagenden Flügel wie einen Rotor, der Luft nach unten drückt: Die Leistung pro Gewicht ist dann die Geschwindigkeit des Abwinds, und die wächst mit der Wurzel aus dem Gewicht pro überstrichener Fläche, √(*W*/*ρ A*<sub>überstrichen</sub>) ∝ *k*<sup>1/2</sup>. Auf dem Papier sollten kleine Flieger also billiger schweben. In Wirklichkeit wird die Luft für sie „zäher“: Das Verhältnis von Auftrieb zu Widerstand eines Flügels verschlechtert sich bei niedrigen Reynolds-Zahlen, und Weis-Fogh fand, dass die aerodynamische Leistung schwebender Tiere – zwischen 1,3 und 4,7 W pro Newton Gewicht – nicht systematisch mit der Größe variiert [4](#ref-4){:.cite}. Bei der Taufliege ist die Profilleistung – der Aufwand, den Widerstand der Flügel zu überwinden – etwa doppelt so groß wie die induzierte Leistung, der Aufwand für den Auftrieb [15](#ref-15){:.cite}.

Für eine Maschine ist das Verkleinern noch schlimmer. Das Gewicht sinkt mit *k*<sup>3</sup>, aber die Wärme, die ein Elektromotor pro Masse erzeugt, wächst wie 1/*k*<sup>2</sup>, und die Reibung wächst im Verhältnis zum Volumen. Die Drehbeschleunigungen eines fliegenden Körpers wachsen wie 1/*k*, also muss seine Regelung immer schneller reagieren [10](#ref-10){:.cite}. Leistung und Gewicht laufen auseinander – darum brauchen insektengroße Roboter ganz andere Motoren.

{% include lens-end.html %}

{% include lens-start.html lens="cs" %}

## Informatik-Linse: ein einfaches Modell eines Schlagflügels

Wie groß muss der Auftriebsbeiwert eines Bienenflügels sein, damit die Biene schweben kann? Das Programm unten beantwortet das mit einem **quasistationären Modell**: In jedem Augenblick wird der Flügel so behandelt, als bewege er sich gleichmäßig mit seiner momentanen Geschwindigkeit, und der Auftrieb all seiner Streifen wird aufsummiert. Die Masse von 102 mg ist ein Schätzwert für die Honigbiene aus der Literatur [10](#ref-10){:.cite}; Flügellänge (9,7 mm), Flügelschlagfrequenz (230 Hz), Schlagamplitude (90°) und die Dichten von Luft und Heliox sind Messwerte [1](#ref-1){:.cite}. **Modellannahmen:** Der Flügel ist ein Rechteck von 3 mm Breite, er schwingt waagerecht und sinusförmig, und sein Auftriebsbeiwert bleibt während des Schlags konstant.

```python
import numpy as np
import matplotlib.pyplot as plt

# Schwebende Honigbiene – Messwerte, siehe Artikel
MASS = 102e-6              # Körpermasse (kg)
WING_LENGTH = 9.7e-3       # Flügellänge R, von der Basis zur Spitze (m)
FREQUENCY = 230.0          # Flügelschläge pro Sekunde (Hz)
AMPLITUDE = 90.0           # Schlagamplitude Φ: der Winkel, den ein Flügel überstreicht (Grad)
AIR = 1.21                 # Dichte der Luft (kg/m³)
HELIOX = 0.41              # Dichte von Heliox, einem Sauerstoff-Helium-Gemisch (kg/m³)
# Modellannahmen
CHORD = 3.0e-3             # Flügelbreite (m): der Flügel als Rechteck konstanter Breite
SCALE = 1.0                # die ganze Biene verkleinern oder vergrößern: Längen × SCALE, Masse × SCALE³
G = 9.81                   # Schwerebeschleunigung (m/s²)
VISCOSITY = 1.8e-5         # dynamische Viskosität der Luft (Pa·s)

mass, length, chord = MASS * SCALE**3, WING_LENGTH * SCALE, CHORD * SCALE
weight = mass * G
t = np.linspace(0, 2 / FREQUENCY, 800, endpoint=False)          # zwei Flügelschläge


def stroke(amplitude_deg):
    """Sinusförmiger Schlag φ(t) = Φ/2 · sin(2πft) und seine Winkelgeschwindigkeit ω(t) = dφ/dt."""
    phi_max = np.radians(amplitude_deg) / 2
    phase = 2 * np.pi * FREQUENCY * t
    return phi_max * np.sin(phase), phi_max * 2 * np.pi * FREQUENCY * np.cos(phase)


def lift(lift_coefficient, omega, density):
    """Quasistationärer Auftrieb beider Flügel. Ein Streifen im Abstand r bewegt sich mit u = ω·r
    und liefert ½·ρ·C_L·c·u²·dr; von der Basis bis zur Spitze summiert ergibt das ½·ρ·C_L·ω²·c·R³/3 pro Flügel."""
    return 2 * 0.5 * density * lift_coefficient * omega**2 * chord * length**3 / 3


def needed_cl(amplitude_deg, density):
    """Der Auftriebsbeiwert, bei dem der mittlere Auftrieb über einen Flügelschlag das Gewicht trägt."""
    _, omega = stroke(amplitude_deg)
    return weight / lift(1.0, omega, density).mean()


tip_speed = 2 * np.radians(AMPLITUDE) * length * FREQUENCY   # zwei Schläge von Φ·R pro Flügelschlag
reynolds = AIR * tip_speed * chord / VISCOSITY
cl = needed_cl(AMPLITUDE, AIR)
angle, omega = stroke(AMPLITUDE)
force = lift(cl, omega, AIR)
print(f"Gewicht {weight * 1e3:.2f} mN, mittlere Geschwindigkeit der Flügelspitze {tip_speed:.1f} m/s, "
      f"Reynolds-Zahl etwa {round(reynolds, -1):.0f}")
print(f"zum Schweben nötiger Auftriebsbeiwert: C_L = {cl:.1f}")
print(f"Auftrieb in der Schlagmitte bis zum {force.max() / weight:.1f}-Fachen des Gewichts, 0 an jeder Umkehr")
print(f"in Heliox mit gleichem Schlag: C_L = {needed_cl(AMPLITUDE, HELIOX):.1f}; "
      f"mit 50 % weiterem Schlag: C_L = {needed_cl(1.5 * AMPLITUDE, HELIOX):.1f}")

plt.rcParams["font.size"] = 13      # große Schrift: Das Diagramm bleibt auf dem Handy lesbar
fig, (top, bottom) = plt.subplots(2, 1, figsize=(6.4, 8.4), layout="constrained", sharex=True)
ms = t * 1e3
for ax in (top, bottom):
    for turn in np.arange(0.25, 2, 0.5) / FREQUENCY * 1e3:    # die vier Umkehrpunkte
        ax.axvline(turn, color="#c98a1b", lw=6, alpha=0.18)
top.plot(ms, np.degrees(angle), lw=2.5, color="black")
top.axhline(0, color="grey", lw=0.8)
top.set_ylabel("Schlagwinkel φ (°)")
top.set_title("Der Flügel schwingt vor und zurück")
top.text(0.25 / FREQUENCY * 1e3 + 0.07, -40, "Umkehr:\nFlügel dreht", fontsize=11)
bottom.plot(ms, force * 1e3, lw=2.5, label="Auftrieb, quasistationäres Modell")
bottom.axhline(weight * 1e3, color="black", ls="--", lw=1.5, label="Körpergewicht")
bottom.set_xlabel("Zeit (ms)")
bottom.set_ylabel("Auftrieb (mN)")
bottom.set_ylim(0, 2.6)
bottom.set_title("Auftrieb: Spitze mitten im Schlag")
bottom.legend(loc="upper right", fontsize=11)
plt.show()
```
{% include code-result.html file="flapping_wing.py" label="Abb. 2" caption="Ausgabe des Programms oben: das quasistationäre Modell einer schwebenden Honigbiene über zwei Flügelschläge. Oben: der Schlagwinkel des Flügels; die schattierten Bänder markieren die Umkehrpunkte, an denen sich der Flügel umdreht. Unten: der Auftrieb beider Flügel im Vergleich mit dem Körpergewicht. Das Modell nimmt einen rechteckigen Flügel und einen konstanten Auftriebsbeiwert an." alt="Zwei Diagramme übereinander, Zeitachse von 0 bis 8,7 Millisekunden. Oben: Der Schlagwinkel schwingt sinusförmig zwischen plus und minus 45 Grad, zwei volle Flügelschläge; vier schattierte Bänder markieren die Umkehrpunkte an den Extremen, eines ist mit Umkehr, Flügel dreht beschriftet. Unten: Der Auftrieb des quasistationären Modells steigt in der Mitte jedes Schlags auf etwa 2 Millinewton und fällt an jedem Umkehrpunkt auf null; eine gestrichelte Linie bei 1 Millinewton markiert das Körpergewicht, das der Auftrieb im Mittel bei einem Auftriebsbeiwert von 1,4 trägt." %}

Was das Ergebnis lehrt:

- **Der Flügel muss hart arbeiten.** Um ihr Gewicht von 1,00 mN zu tragen, braucht der Bienenflügel einen mittleren Auftriebsbeiwert von **1,4** – bei einer mittleren Geschwindigkeit der Flügelspitze von 7,0 m/s und einer Reynolds-Zahl von etwa 1410. Das ist ein anspruchsvoller Wert: Die herkömmliche Aerodynamik erklärt nur ein Drittel bis die Hälfte des Auftriebs, den Insekten brauchen, und der Vorderkantenwirbel hilft, die Lücke zu schließen [2](#ref-2){:.cite} [14](#ref-14){:.cite}. Für echte schwebende Honigbienen geben Altshuler und Kollegen eine Reynolds-Zahl von etwa 1.100 an [1](#ref-1){:.cite}; der 3 mm breite Modellflügel ist vermutlich etwas zu breit, der wahre Auftriebsbeiwert wäre dann noch höher.
- **Das Modell übersieht die Umkehrpunkte.** Im quasistationären Modell erreicht der Auftrieb in der Schlagmitte das 2,0-Fache des Körpergewichts und fällt an jeder Umkehr auf 0. Messungen an einem Roboterflügel einer Biene zeigen zusätzliche Kraftspitzen am Anfang und Ende jedes Schlags, aus der Drehung des Flügels, der beschleunigten Luft und dem Nachlauf – ein großer Teil des Auftriebs der Biene [1](#ref-1){:.cite}. Hier stößt das Modell an seine Grenze; es ist eine erste Abschätzung, nicht die Wahrheit.
- **Dünne Luft.** In Heliox bräuchte die Biene mit gleichem Schlag *C*<sub>L</sub> = 4,2 – unerreichbar. Mit einem 50 % weiteren Schlag, wie ihn die Bienen tatsächlich machten, sinkt der Bedarf auf 1,8. Der weitere Schlag leistet den Großteil; der Rest muss vom Flügel selbst kommen.

Probier es selbst:

- Verkleinere die Biene auf die halbe Größe: Setze `SCALE = 0.5`. Bei gleicher Frequenz verdoppelt sich der nötige Auftriebsbeiwert auf 2,8, und die Reynolds-Zahl sinkt auf etwa 350 – die Mathematik-Linse in Aktion: Ein kleineres Insekt muss schneller schlagen.
- Nimm die niedrigere Flügelschlagfrequenz, die eine andere Arbeit für Honigbienen angibt: Setze `FREQUENCY = 197.0` [10](#ref-10){:.cite}. Der nötige Auftriebsbeiwert steigt auf 1,9 – das Ergebnis hängt empfindlich von der Frequenz ab, weil der Auftrieb mit ihrem Quadrat wächst.

{% include code-variant.html file="flapping_wing.py" id="half" replace="SCALE = 1.0 " with="SCALE = 0.5 " expect="2.8 350" %}
{% include code-variant.html file="flapping_wing.py" id="slower" replace="FREQUENCY = 230.0 " with="FREQUENCY = 197.0 " expect="1.9" %}

{% include lens-end.html %}

{% include lens-start.html lens="physical-ai" %}

## Physical-AI-Linse: Roboterinsekten

Für Physical AI – verkörperte künstliche Intelligenz, also Roboter, die in der physischen Welt wahrnehmen und handeln – setzen Insekten den Maßstab: Fliegen fliegen Wendungen in Millisekunden und landen kopfüber an der Decke, mit einem Nervensystem aus nur 10<sup>5</sup>–10<sup>7</sup> Neuronen [10](#ref-10){:.cite}. Wer sie nachbauen will, trifft frontal auf die Skalierungsgesetze der Mathematik-Linse.

**Künstliche Flugmuskeln.** Elektromotoren arbeiten in Insektengröße schlecht. Deshalb treibt die Gruppe von Robert Wood an der Harvard University die Flügel ihrer Roboterinsekten, bekannt als **RoboBees**, mit **piezoelektrischen Aktoren** an: dünnen Schichten, die sich unter elektrischer Spannung biegen, in einer muskelähnlichen Hin-und-her-Bewegung. Piezoelektrische Aktoren lassen sich günstiger verkleinern als elektromagnetische Motoren [10](#ref-10){:.cite}. Die Gelenke des Roboters sind dünne Biegegelenke statt Scharniere, hergestellt mit einem Fertigungsverfahren für den schnellen Prototypenbau gelenkiger Mechanismen unter einem Millimeter. 2013 berichteten Kevin Ma und Kollegen über gesteuerte Flüge eines 80 mg schweren Roboters, lose nach dem Vorbild von Fliegen gebaut: stabiles Schweben und einfache Flugmanöver, an einem dünnen Kabel, sonst aber frei [16](#ref-16){:.cite}.

**Aufrecht bleiben.** Wie bei vielen Insekten hängt der Schwerpunkt des Roboters unterhalb der Flügel. Das gibt ihm eine instabile, pendelartige Dynamik: Ohne ständige Korrekturen gerät er ins Taumeln und stürzt ab. Sawyer Fuller und Kollegen stabilisierten ihn mit einem 25 mg leichten Lichtsensor nach dem Vorbild der Ocellen der Insekten. Die Regelung erzeugt ein Drehmoment proportional dazu, wie schnell sich das Licht von oben scheinbar bewegt – der erste bekannte Einsatz von Sensoren an Bord in dieser Größe [10](#ref-10){:.cite}. Zuvor kamen die Korrekturen von externen Kameras, die den Roboter verfolgten [10](#ref-10){:.cite}. Die RoboBee schlug mit 120 Hz; für Honigbienen nennt dieselbe Arbeit 197 Hz [10](#ref-10){:.cite}.

**Ohne Kabel.** 2019 ließen Noah Jafferis und Kollegen einen vierflügeligen Roboter ohne Kabel fliegen: ein 90 mg leichtes Fahrzeug mit vier Flügeln, angetrieben von zwei piezoelektrischen Aktoren, mit einem maximalen Auftrieb vom 4,1-Fachen seines Gewichts und, zusammen mit Solarzellen und der Elektronik, die die Aktoren ansteuert, insgesamt 259 mg. Es verbrauchte 110–120 mW Leistung – nach Angaben der Autoren dieselbe Schubeffizienz wie ähnlich große Insekten, etwa Bienen – und war nach Angaben der Autoren damals das leichteste insektengroße Fahrzeug, das einen anhaltenden Flug ohne Kabel schaffte [17](#ref-17){:.cite}.

**Weiche Muskeln und Roboter als Forschungswerkzeug.** Starre Mikroaktoren brechen bei Zusammenstößen leicht. Yufeng Chen und Kollegen bauten deshalb fliegende Mikroroboter mit **weichen künstlichen Muskeln** – mehrlagigen dielektrischen Elastomeraktoren von je 100 mg mit einer Leistungsdichte von 600 W/kg. Diese Roboter überstehen Zusammenstöße mit Wänden und miteinander; Energie und Steuerung kommen jedoch noch von außen, von externen Verstärkern und einem Motion-Capture-System [18](#ref-18){:.cite}. Größere Schlagflügelroboter helfen auch der Biologie: Matěj Karásek und Kollegen bauten einen schwanzlosen, programmierbaren Schlagflügelroboter, 55-mal so groß wie eine Taufliege, der ihre schnellen Fluchtmanöver nachahmt. Bei abgeschalteter Gierregelung drehte er sich trotzdem in Fluchtrichtung – ein Hinweis, dass diese Drehung bei Fliegen passiv aus einer aerodynamischen Kopplung entstehen kann [19](#ref-19){:.cite}.

**Wo steckt die Intelligenz?** In heutigen Roboterinsekten sitzt ein großer Teil davon außerhalb: in externen Kameras, externen Verstärkern oder bestenfalls in einem einzigen Lichtsensor und einer einfachen Regel. Eine Fliege trägt alles – Sensoren, ein kleines Gehirn, Muskeln und Treibstoff – in einem Körper von wenigen Milligramm. Ob insektengroße Roboter eines Tages lange Zeit selbstständig wahrnehmen, entscheiden und mit eigener Energie fliegen, ist eine offene Frage. Die Autoren des vierflügeligen Roboters sehen in seiner Nutzlast Platz für zusätzliche Geräte an Bord [17](#ref-17){:.cite}, und Karáseks Gruppe hält ihren Roboter für geeignet für Flugeinsätze in der realen Welt [19](#ref-19){:.cite}; für völlig autonome Roboterinsekten bleiben Sensorik und Regelung in dieser Größe [10](#ref-10){:.cite} und die hohen Energiekosten des Fliegens im Kleinen [17](#ref-17){:.cite} die großen Herausforderungen.

{% include lens-end.html %}

## Was wir von einer Biene lernen können

Die Biene, die „nicht fliegen konnte“, zeigt, wie aus einer schlechten Rechnung eine gute Frage werden kann. Die Antwort – ein Wirbel, der auf dem Flügel sitzt, statt die Strömung abreißen zu lassen, Flügel, die sich an jedem Umkehrpunkt drehen, Muskeln, die von selbst schwingen, und ein Kreisel aus einem Flügelpaar – brauchte Hochgeschwindigkeitsvideo, Strömungsvisualisierung sowie mechanische und Computermodelle [13](#ref-13){:.cite}.

Offene Fragen bleiben: wie Bienen und andere Insekten ohne Halteren das Gleichgewicht halten [10](#ref-10){:.cite}, wie eine umfassende Theorie der Kräfte während der Schläge und an den Umkehrpunkten die vielen Flügelbewegungen verschiedener Insekten erklären kann [5](#ref-5){:.cite}, und wie man Flugmaschinen in Insektengröße baut, die ihre eigene Energie und ihre eigene Intelligenz tragen. Auch der umgekehrte Weg funktioniert: Roboter, die wie Insekten fliegen, werden zu Instrumenten, mit denen sich Ideen über den Insektenflug prüfen lassen [19](#ref-19){:.cite}.
