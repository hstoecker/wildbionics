---
id: flying-squirrel
lang: en
ref: flying-squirrel
title: "Flying Squirrel: The Glide That Ends Going Up"
short_title: "Flying squirrel"
kicker: "Article · Aerodynamics"
description: "Flying squirrels do not fly: they dive, pull up and reach the next tree climbing. How a furry membrane changes shape in mid-air, measured and simulated."
dek: "A flying squirrel has no engine and never flaps. Yet on an 18-metre glide through a forest it does not simply sink along a straight line: it dives, builds up speed, pulls out and reaches the next trunk climbing. This article follows that glide from the first leap to the landing, explains the membrane and the cartilage rod that make it possible, simulates it with measured values and shows what robot builders are copying."
date: 2026-11-08
permalink: /articles/flying-squirrel/
image: /assets/og/flying-squirrel-en.jpg
og: { eyebrow: "Biology · Physics · Mathematics · Physical AI", title: "The glide that ends going <em>up</em>", sub: "A flying squirrel dives, pulls out and reaches the next tree climbing: a steered fall, measured in the wild.", title_px: 62 }
image_alt: "A flying squirrel from above with its furry gliding membrane spread between its limbs and a flat tail. Below it, a computed glide path falls steeply from a branch, flattens and curves upward just before a tree trunk 18 metres away, with arrows for lift, drag and weight."
hero_figure: svg/flying-squirrel.svg
hero_caption: "<span class=\"caption__label\">Fig. 1</span> A glide is a steered fall. The path is computed from values derived from field measurements of wild northern flying squirrels: after a nearly ballistic start, the animal pulls out on a path about 45° steep, reaches its peak speed of about 8.5 m/s, and curves upward before the trunk. The arrows are scaled to body weight: lift grows and tilts backward. A frozen pose at the cruise midpoint would end about 2.5 metres lower. The path is computed, the animal is not to scale, and the first 3 metres were not filmed."
educational_level: "Intermediate"
keywords: ["flying squirrel", "Glaucomys sabrinus", "northern flying squirrel", "Pteromys volans", "Siberian flying squirrel", "do flying squirrels fly", "how do flying squirrels glide", "gliding mammal", "patagium", "gliding membrane", "styliform cartilage", "glide ratio", "lift coefficient", "drag coefficient", "wing loading", "aspect ratio", "non-equilibrium glide", "stall", "winglet", "convergent evolution", "ultraviolet fluorescence", "porphyrin", "bio-inspired drone", "gliding robot", "Physical AI"]
about:
  - { name: "Pteromyini (flying squirrels)", wikidata: Q9490, wikipedia: "https://en.wikipedia.org/wiki/Flying_squirrel" }
  - { name: "Northern flying squirrel", wikidata: Q1094722, wikipedia: "https://en.wikipedia.org/wiki/Northern_flying_squirrel" }
  - { name: "Patagium", wikidata: Q1306961, wikipedia: "https://en.wikipedia.org/wiki/Patagium" }
mentions:
  - { name: "Glaucomys volans", wikidata: Q913350 }
  - { name: "Pteromys volans", wikidata: Q243339 }
  - { name: "Petaurista leucogenys", wikidata: Q1765345 }
  - { name: "Miopetaurista", wikidata: Q6871560 }
  - { name: "Gliding flight", wikidata: Q11705171 }
  - { name: "Lift-to-drag ratio", wikidata: Q845727 }
  - { name: "Aerodynamics", wikidata: Q8424 }
  - { name: "Miocene", wikidata: Q76267 }
  - { name: "Fluorescence", wikidata: Q191807 }
  - { name: "Porphyrins", wikidata: Q422926 }
dimensions:
  time: ["cenozoic", "modern-era"]
  space: ["forest"]
  physics: ["fluid-dynamics", "mechanics", "optics"]
  adjacent_sciences: ["biology", "mathematics", "computer-science", "physical-ai", "robotics", "bionics"]
beings: ["northern-flying-squirrel", "siberian-flying-squirrel"]
lenses: ['biology', 'physics', 'math', 'cs', 'physical-ai']
key_facts:
  - "Flying squirrels **glide; they do not fly**. They have no propulsion in the air: in wild northern flying squirrels, total energy decreased during the glide [1](#ref-1){:.cite}."
  - "In 58 filmed glides of wild northern flying squirrels, **no glide was ever in equilibrium**. Forces and speed changed continuously, and on the 18 m glides lift exceeded body weight for the whole filmed part [1](#ref-1){:.cite}."
  - "On the 18 m glides, the animals lost **7.6 ± 0.5 m** of height, a glide ratio of 2.4, at a mean speed of 7.2 m/s, and were gaining altitude when they landed [1](#ref-1){:.cite}."
  - "A slender **styliform cartilage** extends the membrane outward from the wrist; among gliding mammals, only flying squirrels have one [7](#ref-7){:.cite}."
  - "The oldest flying squirrel skeleton is **11.6 million years** old and already shows the gliding wrist of living species [2](#ref-2){:.cite}."
  - "Under ultraviolet light, the fur of New World flying squirrels fluoresces **pink** [16](#ref-16){:.cite}. Whether this has any function is unknown; it may be a by-product [17](#ref-17){:.cite} [19](#ref-19){:.cite}."
faq:
  - q: "Can flying squirrels really fly?"
    a: "No. Flying squirrels glide: they jump from a tree and steer a controlled descent on a membrane of skin stretched between their limbs. They cannot flap and so cannot add energy themselves in the air. Bats are the only mammals that truly fly."
  - q: "How far can a flying squirrel glide?"
    a: "In a study of 100 glides of northern flying squirrels in Canada, horizontal distances ranged from 3.2 to 45 metres, with most between 5 and 25 metres. On average the animals travelled about two metres forward for every metre of height lost."
  - q: "How do flying squirrels land without getting hurt?"
    a: "They raise the body and wing shortly before the tree and usually meet the trunk with all four limbs; on steep approaches they can land forelimbs first, with higher forces. Short jumps in the laboratory produced landing forces of 3 to 10 body weights. Researchers disagree on the aerodynamics: some describe an active stall as a brake, while field data on long glides point to high lift rather than a stall."
  - q: "Are flying squirrels and sugar gliders related?"
    a: "Only distantly. Flying squirrels are rodents, sugar gliders are marsupials. Both evolved a gliding membrane independently, an example of convergent evolution. Colugos and scaly-tailed flying squirrels did so as well."
  - q: "Why do flying squirrels glow under UV light?"
    a: "Their fur fluoresces pink under ultraviolet light, probably because of porphyrins, pigment-like molecules that many mammals deposit in hair. No function has been demonstrated. Comparative studies suggest it may simply be a by-product that shows up mainly in nocturnal animals, because daylight destroys porphyrins."
sources:
  - authors: ["Bahlman, J. W.", "Swartz, S. M.", "Riskin, D. K.", "Breuer, K. S."]
    year: 2013
    title: "Glide performance and aerodynamics of non-equilibrium glides in northern flying squirrels (Glaucomys sabrinus)"
    journal: "Journal of The Royal Society Interface"
    volume: 10
    pages: "20120794"
    doi: "10.1098/rsif.2012.0794"
    open_access: true
  - authors: ["Casanovas-Vilar, I.", "Garcia-Porta, J.", "Fortuny, J.", "Sanisidro, Ó.", "Prieto, J.", "Querejeta, M.", "Llácer, S.", "Robles, J. M.", "Bernardini, F.", "Alba, D. M."]
    year: 2018
    title: "Oldest skeleton of a fossil flying squirrel casts new light on the phylogeny of the group"
    journal: "eLife"
    volume: 7
    pages: "e39270"
    doi: "10.7554/elife.39270"
    open_access: true
  - authors: ["Thorington, R. W.", "Heaney, L. R."]
    year: 1981
    title: "Body Proportions and Gliding Adaptations of Flying Squirrels (Petauristinae)"
    journal: "Journal of Mammalogy"
    volume: 62
    pages: "101–114"
    doi: "10.2307/1380481"
  - authors: ["Newar, S. L.", "Schneiderová, I.", "Hughes, B.", "Bowman, J."]
    year: 2024
    title: "Ultrasound and ultraviolet: crypsis in gliding mammals"
    journal: "PeerJ"
    volume: 12
    pages: "e17048"
    doi: "10.7717/peerj.17048"
    open_access: true
  - authors: ["Wehrenberg, G.", "Kiebler, A.", "Greve, C.", "Beltrán‐Sanz, N.", "Ben Hamadou, A.", "Meißner, R.", "Winter, S.", "Prost, S."]
    year: 2025
    title: "A Prelude to Conservation Genomics: First Chromosome‐Level Genome Assembly of a Flying Squirrel (Pteromyini: Pteromys volans)"
    journal: "Ecology and Evolution"
    volume: 15
    pages: "e71905"
    doi: "10.1002/ece3.71905"
    open_access: true
  - authors: ["Paskins, K. E.", "Bowyer, A.", "Megill, W. M.", "Scheibe, J. S."]
    year: 2007
    title: "Take-off and landing forces and the evolution of controlled gliding in northern flying squirrels Glaucomys sabrinus"
    journal: "Journal of Experimental Biology"
    volume: 210
    pages: "1413–1423"
    doi: "10.1242/jeb.02747"
  - authors: ["Thorington, R. W.", "Darrow, K.", "Anderson, C. G."]
    year: 1998
    title: "Wing Tip Anatomy and Aerodynamics in Flying Squirrels"
    journal: "Journal of Mammalogy"
    volume: 79
    pages: "245–250"
    doi: "10.2307/1382860"
  - authors: ["Thorington, Jr., R. W.", "Stafford, B. J."]
    year: 2001
    title: "Homologies of the carpal bones in flying squirrels (Pteromyinae): A review."
    journal: "Mammal Study"
    volume: 26
    pages: "61–68"
    doi: "10.3106/mammalstudy.26.61"
    open_access: true
  - authors: ["Kawashima, T.", "Thorington, R. W.", "Bohaska, P. W.", "Sato, F."]
    year: 2017
    title: "Evolutionary Transformation of the Palmaris Longus Muscle in Flying Squirrels (Pteromyini: Sciuridae): An Anatomical Consideration of the Origin of the Uniquely Specialized Styliform Cartilage"
    journal: "The Anatomical Record"
    volume: 300
    pages: "340–352"
    doi: "10.1002/ar.23471"
  - authors: ["Moreno, J. A.", "Dudchenko, O.", "Feigin, C. Y.", "Mereby, S. A.", "Chen, Z.", "Ramos, R.", "Almet, A. A.", "Sen, H.", "Brack, B. J.", "Johnson, M. R.", "Li, S.", "Wang, W.", "Gaska, J. M.", "Ploss, A.", "Weisz, D.", "Omer, A. D.", "Yao, W.", "Colaric, Z.", "Kaur, P.", "Leger, J. S.", "Nie, Q.", "Mena, A.", "Flanagan, J. P.", "Keller, G.", "Sanger, T.", "Ostrow, B.", "Plikus, M. V.", "Kvon, E. Z.", "Aiden, E. L.", "Mallarino, R."]
    year: 2024
    title: "Emx2 underlies the development and evolution of marsupial gliding membranes"
    journal: "Nature"
    volume: 629
    pages: "127–135"
    doi: "10.1038/s41586-024-07305-3"
    open_access: true
  - authors: ["Flaherty, E. A.", "Ben-David, M.", "Smith, W. P."]
    year: 2010
    title: "Quadrupedal locomotor performance in two species of arboreal squirrels: predicting energy savings of gliding"
    journal: "Journal of Comparative Physiology B"
    volume: 180
    pages: "1067–1078"
    doi: "10.1007/s00360-010-0470-1"
  - authors: ["Scheibe, J. S.", "Paskins, K. E.", "Ferdous, S.", "Birdsill, D."]
    year: 2007
    title: "Kinematics and Functional Morphology of Leaping, Landing, and Branch use in Glaucomys sabrinus"
    journal: "Journal of Mammalogy"
    volume: 88
    pages: "850–861"
    doi: "10.1644/06-mamm-s-331r1.1"
  - authors: ["Suzuki, K.", "Yanagawa, H."]
    year: 2019
    title: "Gliding patterns of Siberian flying squirrels in relation to forest structure"
    journal: "iForest - Biogeosciences and Forestry"
    volume: 12
    pages: "114–117"
    doi: "10.3832/ifor2954-011"
    open_access: true
  - authors: ["Vernes, K."]
    year: 2001
    title: "GLIDING PERFORMANCE OF THE NORTHERN FLYING SQUIRREL (GLAUCOMYS SABRINUS) IN MATURE MIXED FOREST OF EASTERN CANADA"
    journal: "Journal of Mammalogy"
    volume: 82
    pages: "1026–1033"
    doi: "10.1644/1545-1542(2001)082<1026:gpotnf>2.0.co;2"
  - authors: ["Murrant, M. N.", "Bowman, J.", "Garroway, C. J.", "Prinzen, B.", "Mayberry, H.", "Faure, P. A."]
    year: 2013
    title: "Ultrasonic Vocalizations Emitted by Flying Squirrels"
    journal: "PLoS ONE"
    volume: 8
    pages: "e73045"
    doi: "10.1371/journal.pone.0073045"
    open_access: true
  - authors: ["Kohler, A. M.", "Olson, E. R.", "Martin, J. G.", "Anich, P. S."]
    year: 2019
    title: "Ultraviolet fluorescence discovered in New World flying squirrels (Glaucomys)"
    journal: "Journal of Mammalogy"
    volume: 100
    pages: "21–30"
    doi: "10.1093/jmammal/gyy177"
  - authors: ["TOUSSAINT, S. L. D.", "PONSTEIN, J.", "THOURY, M.", "MÉTIVIER, R.", "KALTHOFF, D. C.", "HABERMEYER, B.", "GUILARD, R.", "BOCK, S.", "MORTENSEN, P.", "SANDBERG, S.", "GUERIAU, P.", "AMSON, E."]
    year: 2023
    title: "Fur glowing under ultraviolet: in situ analysis of porphyrin accumulation in the skin appendages of mammals"
    journal: "Integrative Zoology"
    volume: 18
    pages: "15–26"
    doi: "10.1111/1749-4877.12655"
    open_access: true
  - authors: ["Sobral, G.", "Souza-Gudinho, F."]
    year: 2022
    title: "Fluorescence and UV–visible reflectance in the fur of several Rodentia genera"
    journal: "Scientific Reports"
    volume: 12
    pages: "12293"
    doi: "10.1038/s41598-022-15952-7"
    open_access: true
  - authors: ["Nicolaï, M. P. J.", "Bok, M. J.", "Abalos, J.", "D'Alba, L.", "Shawkey, M. D.", "Goldenberg, J."]
    year: 2024
    title: "The function and consequences of fluorescence in tetrapods"
    journal: "Proceedings of the National Academy of Sciences"
    volume: 121
    pages: "e2318189121"
    doi: "10.1073/pnas.2318189121"
    open_access: true
  - authors: ["Stafford, B. J.", "Thorington Jr., R. W.", "Kawamichi, T."]
    year: 2002
    title: "GLIDING BEHAVIOR OF JAPANESE GIANT FLYING SQUIRRELS (PETAURISTA LEUCOGENYS)"
    journal: "Journal of Mammalogy"
    volume: 83
    pages: "553–562"
    doi: "10.1644/1545-1542(2002)083<0553:gbojgf>2.0.co;2"
  - authors: ["Bishop, K. L."]
    year: 2006
    title: "The relationship between 3-D kinematics and gliding performance in the southern flying squirrel, Glaucomys volans"
    journal: "Journal of Experimental Biology"
    volume: 209
    pages: "689–701"
    doi: "10.1242/jeb.02062"
  - authors: ["Song, A.", "Tian, X.", "Israeli, E.", "Galvao, R.", "Bishop, K.", "Swartz, S.", "Breuer, K."]
    year: 2008
    title: "Aeromechanics of Membrane Wings with Implications for Animal Flight"
    journal: "AIAA Journal"
    volume: 46
    pages: "2096–2106"
    doi: "10.2514/1.36694"
  - authors: ["Bishop, K. L.", "Brim‐DeForest, W."]
    year: 2008
    title: "Kinematics of turning maneuvers in the southern flying squirrel, Glaucomys volans"
    journal: "Journal of Experimental Zoology Part A: Ecological Genetics and Physiology"
    volume: 309A
    pages: "225–242"
    doi: "10.1002/jez.447"
  - authors: ["Byrnes, G.", "Lim, N. T. L.", "Spence, A. J."]
    year: 2008
    title: "Take-off and landing kinetics of a free-ranging gliding mammal, the Malayan colugo (Galeopterus variegatus)"
    journal: "Proceedings of the Royal Society B: Biological Sciences"
    volume: 275
    pages: "1007–1013"
    doi: "10.1098/rspb.2007.1684"
    open_access: true
  - authors: ["Berghäuser, T.", "Nyakatura, J. A.", "Wölfer, J."]
    year: 2023
    title: "Evolution of gliding in squirrel‐related rodents (Mammalia: Sciuromorpha) did not induce a new optimum on the cortical thickness of the scapular glenoid fossa"
    journal: "The Anatomical Record"
    volume: 306
    pages: "2716–2728"
    doi: "10.1002/ar.25146"
    open_access: true
  - authors: ["Zheng, L.", "van Zuijlen, A.", "Hamaza, S."]
    year: 2026
    title: "A squirrel-inspired drone with enhanced stability, agility and maneuverability via whole-body morphing"
    journal: "Nature Communications"
    volume: 17
    pages: "6365"
    doi: "10.1038/s41467-026-72822-w"
    open_access: true
  - authors: ["Fan, M.", "Wang, J.", "Liu, T.", "Ren, Z.", "Zhu, G.", "Ma, J."]
    year: 2025
    title: "PteroBot: A Forest Exploration Robot Bioinspired by Pteromyini Gliding Mechanism"
    journal: "Biomimetics"
    volume: 10
    pages: "661"
    doi: "10.3390/biomimetics10100661"
    open_access: true
  - authors: ["Kang, J. G.", "Lee, D.", "Han, S."]
    year: 2023
    title: "A Highly Maneuverable Flying Squirrel Drone with Controllable Foldable Wings"
    journal: "2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)"
    pages: "6652–6659"
    doi: "10.1109/iros55552.2023.10341386"
    open_access: true
  - authors: ["Novati, G.", "Mahadevan, L.", "Koumoutsakos, P."]
    year: 2019
    title: "Controlled gliding and perching through deep-reinforcement-learning"
    journal: "Physical Review Fluids"
    volume: 4
    pages: "093902"
    doi: "10.1103/physrevfluids.4.093902"
    open_access: true
status: published
---

## It does not fly

A flying squirrel cannot fly. It has no engine and it does not flap. What it does is jump off a tree and steer its own fall so well that it arrives somewhere useful. **Gliding** like this occurs in every major group of land vertebrates [1](#ref-1){:.cite}, and the flying squirrels (tribe Pteromyini) are the only group of gliding mammals with a remarkable diversity and a wide geographical range [2](#ref-2){:.cite}. They range from less than 90 mm to more than 400 mm in head and body length [3](#ref-3){:.cite}. All mammals that glide today are strictly nocturnal [4](#ref-4){:.cite}, which is why most people have never seen one. Europe has a single species, *Pteromys volans*, the Siberian flying squirrel [5](#ref-5){:.cite}.

For a long time, a glide was described with a simple model: the animal sinks at a constant speed along a straight line, and the air exactly balances its weight. In 2013, Bahlman and colleagues tested this on wild northern flying squirrels, *Glaucomys sabrinus*, in Maine. They filmed animals in 3D as they left a feeding platform and glided down a forested hillside to the trunks below. At least six animals made 58 glides over distances of 7 to 20 metres. **Not one of the glides was in equilibrium at any point** [1](#ref-1){:.cite}.

What they do instead is more interesting. On the longest well-sampled route, to a tree 18 metres away, lift exceeded body weight for the entire filmed part of the glide, and the squirrels were climbing when they arrived [1](#ref-1){:.cite}. A caution from the start: this is one site with one population, downhill, and the animals could not be weighed. The lenses below ask how far that picture goes.

## One glide in four steps

The 23 glides to the 18-metre tree followed a consistent pattern [1](#ref-1){:.cite}:

1. **Launch.** The squirrel jumps off with about 5.4 m/s (five launches filmed, 3.3–8.4 m/s). In short jumps in the laboratory, the take-off forces reached 1 to 10 body weights [6](#ref-6){:.cite}.
2. **Dive.** For the first 3 metres, the only way to match the later trajectory in a simulation was almost no aerodynamic force: a nearly ballistic start. This stretch was not filmed. The result could mean a streamlined body or a membrane that is only partly open [1](#ref-1){:.cite}. Gravity turns height into speed.
3. **Pull-out.** Then the force coefficients rise sharply. On entering the camera view, the path is about 45° steep, and at that angle lift, which acts at right angles to the path, points partly forward. It pushed forward about twice as hard as drag pushed back, so the animal kept accelerating horizontally. Speed peaked at about 8.5 m/s, 5 to 6 metres from the start [1](#ref-1){:.cite}.
4. **Arrival.** During the last third, the squirrels raised the lift coefficient and lowered the drag coefficient at the same time. The path bent upward, and the animal met the trunk with its body nearly vertical [1](#ref-1){:.cite}. The full gliding posture spreads the impact over all four limbs [6](#ref-6){:.cite}.

{% include lens-tabs.html lenses="biology,physics,math,cs,physical-ai" %}

{% include lens-start.html lens="biology" %}

## Biology lens: a membrane, a rod and a forest at night

**The wing is skin.** The **gliding membrane**, or patagium, is a fold of furred skin between the forelimbs and the hindlimbs. Its leading corners are held open by something no other gliding mammal has: the **styliform cartilage**, a slender rod at the wrist that extends the wing outward [7](#ref-7){:.cite}. Limb and membrane shape can change in flight. As Bahlman and colleagues list, gliders can flex and extend their limb joints, and tense or relax the muscles in the membrane to change its area and curvature [1](#ref-1){:.cite}.

**Where the rod came from has long been debated.** Thorington and colleagues concluded that it corresponds to the small hypothenar cartilage in the hand of ordinary tree squirrels [7](#ref-7){:.cite} [8](#ref-8){:.cite}. One hypothesis held that the rod is the pisiform bone of other mammals [9](#ref-9){:.cite}. Kawashima and colleagues examined wrists again in 2017 and found both a pisiform bone and the styliform cartilage, so the two cannot be the same structure. A true palmaris longus muscle inserts on the cartilage, and they propose that it formed from a superficial anlage on the ulnar side of the wrist [9](#ref-9){:.cite}.

**Twelve million years with little change.** At Abocador de Can Mata in Catalonia, Spain, Isaac Casanovas-Vilar and colleagues found the partial skeleton of *Miopetaurista neogrivensis*, more than 80 bones, dated to 11.63 million years. It is the oldest skeleton of a flying squirrel, and its wrist already has the gliding features of living species. It was about the size of today’s giant flying squirrels, with an estimated body mass of 1.3 kg. The group has changed little in morphology for almost 12 million years [2](#ref-2){:.cite}. How old the group is remains less certain: earlier molecular estimates gave about 23 million years, while the combined analysis places the split from tree squirrels between 36.5 and 24.9 million years ago (95 % interval), consistent with teeth of about 36 million years if those belong to the group. Teeth alone, the authors warn, are not unique to flying squirrels [2](#ref-2){:.cite}.

**The same idea, invented several times.** Six living groups of mammals glide [4](#ref-4){:.cite}. Flying squirrels and scaly-tailed flying squirrels are separate groups of rodents; sugar gliders are marsupials. In marsupials, gliding species show accelerated evolution of the DNA that controls one developmental gene, *Emx2*, with different regulatory elements in separate lineages [10](#ref-10){:.cite}. Whether flying squirrels used the same route is not shown by that study.

**Why glide at all?** Nobody knows for certain. On a treadmill, northern flying squirrels used 1.26 to 1.65 times as much oxygen as predicted for their mass; the study’s authors conclude that they are poorly adapted to long bouts of running [11](#ref-11){:.cite}. Saving energy is one explanation. Paskins and colleagues argue instead that controlling landing forces most likely stimulated the first aerial control [6](#ref-6){:.cite}. Bahlman and colleagues add that fast glides shorten commuting time and so exposure to predators [1](#ref-1){:.cite}. These explanations do not exclude each other.

**A glide is a route choice.** Siberian flying squirrels used efficient glides to land on shorter trees for feeding or nesting, and inefficient ones to reach tall trees from which the next long glide could start [13](#ref-13){:.cite}. In eastern Canada, northern flying squirrels launched from a mean height of 9.8 m and landed at 2.0 m [14](#ref-14){:.cite}. Forest structure can shape the routes [13](#ref-13){:.cite}. The European species, a flagship of old-growth boreal forests, is considered of least concern across its huge range but is listed as vulnerable or critically endangered in parts of it [5](#ref-5){:.cite}.

**Signals in the dark.** North American flying squirrels call in ultrasound, sometimes entirely above human hearing, and may use it to exchange information [15](#ref-15){:.cite}. The calls of gliding mammals reach higher frequencies than those of their non-gliding relatives [4](#ref-4){:.cite}.

**The pink glow.** Under ultraviolet light, the fur of New World flying squirrels fluoresces pink, in 109 museum specimens and five wild animals, whereas three diurnal squirrel species did not [16](#ref-16){:.cite}. It is tempting to see a secret signal, but the evidence is thin. In a comparison of 82 species, nocturnality was the only significant predictor, and gliding was not linked to it; the preserved specimens varied greatly, and live animals glowed much more strongly [4](#ref-4){:.cite}. The spectra of *Glaucomys* fur show peaks in the red typical of porphyrins, which daylight breaks down, so the glow may be merely a by-product that survives in nocturnal animals [17](#ref-17){:.cite}. Other mechanisms exist too: in some other rodents, green fluorescence seems linked to keratinised structures [18](#ref-18){:.cite}. Reviewers warn against assuming a communication function without testing whether anything can see it under natural light [19](#ref-19){:.cite}.

{% include lens-end.html %}

{% include lens-start.html lens="physics" %}

## Physics lens: how a falling animal makes the air work

**Two forces and a weight.** Moving through air, the membrane produces **lift**, at right angles to the direction of travel, and **drag**, against it. Note the definition: lift is not “up”. On a steep path it also points forward. That is why the squirrel keeps accelerating horizontally while its descent is already slowing [1](#ref-1){:.cite}.

**Short and stubby wings.** A wing’s **aspect ratio** compares span and chord. Flying squirrels have aspect ratios of only 1.0 to 2.2 [3](#ref-3){:.cite}; Japanese giant flying squirrels averaged 1.42 in mid-glide [20](#ref-20){:.cite}. Such wings are poor at long-distance efficiency. Measured **glide ratios**, the distance forward per metre of height lost, are correspondingly modest: 1.98 for northern flying squirrels in Canada [14](#ref-14){:.cite}, an average of 1.87 for Japanese giant flying squirrels, with about 3–3.5 as the apparent upper limit [20](#ref-20){:.cite}. Yet the glides observed in the wild do not maximise the glide ratio, which suggests that speed matters too [1](#ref-1){:.cite}. Paskins and colleagues, from short-range jumps, read the falling glide angle at longer range as a sign of optimisation for long-distance travel [6](#ref-6){:.cite}.

**A wing beyond the stall.** The air flows smoothly over a wing only up to a certain tilt, the **angle of attack**. Above it, the flow separates, and the wing **stalls**. In short glides from a height of 4 m, southern flying squirrels used angles of attack of 35.4° to 53.5°, far above where an aircraft wing would typically stall [21](#ref-21){:.cite}. Bahlman’s analysis found equivalent lift coefficients above what most aircraft wings can reach, especially near landing. Partly separated flow or vortices at the leading edge, like those of delta wings, could explain this [1](#ref-1){:.cite}, but we found no measurement of the flow around a living, gliding squirrel.

**A flexible wing helps.** Wind-tunnel tests of low-aspect-ratio membrane wings showed higher lift slopes, higher maximum lift and a delayed stall compared with rigid wings. The air itself bulges the membrane, giving it camber [22](#ref-22){:.cite}. These were model wings for mammalian fliers, not squirrels; whether the principle carries over has not been tested.

**The little winglet.** The wing tips, held by the cartilage, angle upward. Thorington and colleagues proposed that they reduce induced drag, as winglets do on airliners [7](#ref-7){:.cite}. That is a hypothesis from anatomy; we found no flow measurement that tests it.

**Steering.** Turns are not a simple matter of tilting. Two southern flying squirrels turned differently: the better performer banked and used lift, the poorer one crabbed and used drag. Limb movements went on all through the turn, without a simple relation to the body’s rotation [23](#ref-23){:.cite}. The sample is two animals.

**The landing, disputed.** In short laboratory jumps, landing forces reached 3 to 10 body weights, the pitch-up may stall the wing, and the gliding posture spreads the impact over all four limbs [6](#ref-6){:.cite}. Angle of attack at landing rose with distance, again suggesting active stalling [12](#ref-12){:.cite}. On 18-metre glides in the wild, however, lift was high and drag falling near the tree: Bahlman and colleagues describe the landing as a natural end product of high lift, not a stall [1](#ref-1){:.cite}. One reading, ours and not tested, is that the two groups studied different things: jumps of up to a few metres, and long glides. Data on landing forces do not settle it either: in northern flying squirrels they rose with distance over 0.5–2.5 m [6](#ref-6){:.cite}, and colugos, a different group, landed more gently after longer glides [24](#ref-24){:.cite}. Shoulder bone gives no sign of extra loading in gliders compared with climbing relatives [25](#ref-25){:.cite}.

{% include lens-end.html %}

{% include lens-start.html lens="math" %}

## Mathematics lens: what equilibrium would look like

**The textbook glide.** If a glider moved at constant velocity, lift *L* and drag *D* together would exactly balance its weight *mg*. The geometry fixes the glide angle θ, which depends only on the ratio of drag to lift:

<div class="formula" role="math" aria-label="tangent of theta equals D over L equals C D over C L">tan <var>θ</var> = <span class="frac"><span class="frac__num"><var>D</var></span><span class="frac__den"><var>L</var></span></span> = <span class="frac"><span class="frac__num"><var>C</var><sub>D</sub></span><span class="frac__den"><var>C</var><sub>L</sub></span></span></div>

Here *C*<sub>L</sub> and *C*<sub>D</sub> are the **lift coefficient** and the **drag coefficient**: dimensionless measures of how much force a wing shape produces. Forces grow with air density *ρ*, wing area *S* and the square of speed *V*. Requiring the total force to equal the weight gives the equilibrium speed:

<div class="formula" role="math" aria-label="V equals the square root of 2 m g over rho S times the square root of C L squared plus C D squared"><var>V</var> = <span class="sqrt"><span class="frac"><span class="frac__num">2 <var>m</var> <var>g</var></span><span class="frac__den"><var>ρ</var> <var>S</var> √(<var>C</var><sub>L</sub><sup>2</sup> + <var>C</var><sub>D</sub><sup>2</sup>)</span></span></span></div>

**A worked example (calculation for this article).** With the values Bahlman and colleagues used, *m* = 92.7 g, *S* = 154 cm², *ρ* = 1.204 kg/m³ [1](#ref-1){:.cite}, and the midpoint of the values implied by the reported start values and percentage changes for the cruise, *C*<sub>L</sub> = 1.75 and *C*<sub>D</sub> = 0.88, the formulas give *θ* ≈ 27° and *V* ≈ 7.1 m/s. Simulations in the paper reach equilibrium within at most 16 metres of horizontal travel, and about half of the filmed glides were 10 metres or shorter, so for those, the simulations suggest, equilibrium is out of reach. On longer glides it would be possible, but the animals do not use it [1](#ref-1){:.cite}.

**Why the forward push?** At a path angle θ, the forward component of lift is *L* sin θ, and the rearward component of drag is *D* cos θ. Their ratio is (*C*<sub>L</sub>/*C*<sub>D</sub>) · tan θ. With the values at the start of the filmed part (1.4 and 0.78) and θ = 45°, this gives about 1.8 (our calculation), in line with the “approximately twice” in the paper [1](#ref-1){:.cite}.

**Big and small squirrels.** Among flying squirrels, weight varies by a factor of almost 64 and membrane area by a factor of almost 16, close to what geometry predicts: if every length grows fourfold, area grows 4² = 16-fold and weight 4³ = 64-fold. So the **wing loading**, weight per area, grows roughly fourfold, estimated from about 30 N/m² in small species to 110 N/m² in large ones [3](#ref-3){:.cite}. Since the formula above gives *V* ∝ √(*mg*/*S*), a fourfold loading means twice the speed for the same pose (calculation for this article). Thorington and Heaney considered it probable that large squirrels must fly faster for their best glide ratio, and that small ones are more manoeuvrable [3](#ref-3){:.cite}.

{% include lens-end.html %}

{% include lens-start.html lens="cs" %}

## Computer science lens: simulating 18 metres

What does it cost in height to hold still, and what does changing shape buy? The program below integrates Newton’s second law along the glide. **Inputs and assumptions:** mass 92.7 g, wing area 154 cm², air density 1.204 kg/m³, launch speed 5.37 m/s and the force coefficients as we read them from the text of the paper [1](#ref-1){:.cite}: almost none for the first 3 m, 1.4 and 0.78 on entering the camera view, +50 % and +25 % through the middle phase (placed at 12 m, our choice), then lift up to about +300 % and drag falling towards zero at the tree. The time-resolved curve exists only as a figure in the paper, so the program connects these anchor values with straight lines. These are **equivalent** coefficients, based on a mass taken from another population and a published wing loading. Their uncertainty is largest at the end of the glide (from digitising error alone, ±0.56 for lift and ±0.27 for drag at the 95 % level). The “frozen pose” uses the midpoint of the values implied for the cruise phase (*C*<sub>L</sub> = 1.75, *C*<sub>D</sub> = 0.88), a choice for this article.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# How much height does an 18 m glide cost a flying squirrel, and what does changing the pose buy?
# Values from Bahlman et al. 2013 (northern flying squirrel, 23 glides of 18 m).
MASS = 0.0927            # body mass (kg), from another population: these animals were not weighed
AREA = 0.0154            # wing area (m²), from the mass and a published wing loading of 59 N/m²
RHO = 1.204              # air density (kg/m³)
G = 9.81                 # gravity (m/s²)
LAUNCH = 5.37            # horizontal launch speed (m/s), the paper's best-matched simulation
TREE = 18.0              # horizontal distance to the landing tree (m)
DIVE_CL = 0.01           # lift coefficient in the first 3 m (the paper also gives 0.05)
END_CL = 5.6             # lift coefficient on arrival: 1.4 plus about 300 %, very uncertain

# Equivalent force coefficients along the glide, our reading of the text of the paper
X_NODES = [0.0, 3.0, 3.6, 12.0, 18.0]             # horizontal distance (m)
CL_NODES = [DIVE_CL, DIVE_CL, 1.4, 2.1, END_CL]   # 1.4 on entering the camera view, +50 % by 12 m
CD_NODES = [0.05, 0.05, 0.78, 0.975, 0.0]         # 0.78 on entering the view, +25 %, then towards 0


def changing_pose(x):
    return np.interp(x, X_NODES, CL_NODES), np.interp(x, X_NODES, CD_NODES)


def frozen_pose(x):
    return 1.75, 0.88    # midpoint of the values implied for the cruise phase, held from launch to landing


def no_wing(x):
    return 0.0, 0.0      # a thrown stone: no aerodynamic force at all


def forces(t, state, pose):
    """Newton's second law. Lift acts across the direction of travel, drag against it."""
    x, z, vx, vz = state
    speed = np.hypot(vx, vz)
    cl, cd = pose(x)
    k = 0.5 * RHO * speed**2 * AREA / MASS       # dynamic pressure × area / mass
    ax = k * (-cd * vx - cl * vz) / speed
    az = k * (-cd * vz + cl * vx) / speed - G
    return [vx, vz, ax, az]


def glide(pose):
    def reached_tree(t, state, pose):
        return state[0] - TREE
    reached_tree.terminal = True
    sol = solve_ivp(forces, (0, 20), [0, 0, LAUNCH, 0], args=(pose,), events=reached_tree, max_step=0.005)
    return sol.t, *sol.y


def report(name, pose):
    t, x, z, vx, vz = glide(pose)
    speed = np.hypot(vx, vz)
    drop = -z[-1]
    print(f"{name}: drop {drop:.1f} m, glide ratio {TREE / drop:.2f}, "
          f"mean speed {np.trapezoid(speed, t) / t[-1]:.1f} m/s, "
          f"peak {speed.max():.1f} m/s at {x[speed.argmax()]:.1f} m, arrival {speed[-1]:.1f} m/s, "
          f"final path angle {np.degrees(np.arctan2(vz[-1], vx[-1])):+.0f}°")
    return x, z, speed


print("Measured (18 m glides): drop 7.6 ± 0.5 m, glide ratio 2.4, mean speed 7.2 m/s, peak about 8.5 m/s at 5-6 m")
curves = [(report("changing pose", changing_pose), "changing pose", "-", "#1f6f8b"),
          (report("frozen pose", frozen_pose), "frozen pose", "--", "#c0392b")]
report("no wing at all", no_wing)

plt.rcParams["font.size"] = 13
fig, (top, bottom) = plt.subplots(2, 1, figsize=(6.4, 8.4), layout="constrained", sharex=True)
for (x, z, speed), label, style, colour in curves:
    top.plot(x, z, ls=style, lw=2.5, color=colour, label=label)
    bottom.plot(x, speed, ls=style, lw=2.5, color=colour, label=label)
top.errorbar(TREE, -7.6, yerr=0.5, fmt="s", ms=7, color="black", capsize=4, label="measured (mean ± s.d.)")
top.set_ylabel("height (m)")
top.set_ylim(-12, 1)
top.set_title("Changing pose: less height lost, faster")
top.legend(loc="lower left", fontsize=11)
bottom.plot(5.5, 8.5, "s", ms=7, color="black", label="measured peak (approx.)")
bottom.set_xlabel("horizontal distance (m)")
bottom.set_ylabel("speed (m/s)")
bottom.set_ylim(0, 10)
bottom.legend(loc="lower left", fontsize=11)
plt.show()
```
{% include code-result.html file="squirrel_glide.py" label="Fig. 2" caption="Output of the program above. Top: the flight path of a simulated northern flying squirrel over 18 m with force coefficients that change along the glide (solid) and held constant (dashed), and the measured height at the tree. Bottom: speed along the path, with the measured peak." alt="Two stacked line charts over horizontal distance from 0 to 18 metres. Top chart, height: the solid curve falls to about minus 8.2 metres at 15 metres and rises to minus 7.3 at the tree, next to a black square with an error bar at minus 7.6; the dashed curve falls steadily to minus 9.8. Bottom chart, speed: the solid curve rises to 8.5 metres per second at 6 metres and falls to 4.5; the dashed curve rises to 7.5 near 10.6 metres and ends at 7.1. A black square marks a measured peak of 8.5 near 5.5 metres." %}

What the result teaches:

- **The anchor values alone reproduce the measurement.** Without fitting, the program gives a drop of 7.3 m (measured 7.6 ± 0.5), a glide ratio of 2.45 (2.4), a mean speed of 7.1 m/s (7.2) and a peak of 8.5 m/s at 6 m (about 8.5 m/s at 5–6 m). The agreement is a consistency check, because the coefficients themselves come from the same glides.
- **This frozen pose loses on both counts.** Held at the cruise midpoint, the same animal loses 9.8 m instead of 7.3 m, and is slower on average. That holds only for this choice of pose: another constant pose could win on distance or on speed. In Bahlman’s simulations, some constant poses had a higher glide ratio or a higher speed than the simulation matched to the observed glides, but none beat it on both. Against a constant pose with the same glide ratio it was 27 % faster, and against one with the same speed its glide ratio was 46 % greater [1](#ref-1){:.cite}.
- **A throw would be useless.** With no wing at all, the same launch would need a drop of 55 m to cover the 18 m.
- **The last metres are the weak point.** The program ends with the path angled +35°, more than the moderate climb the paper describes. The final lift value is the most uncertain number in the model. Just after the dive, the model’s lift is also slightly below one body weight, although the measured lift was above it throughout the filmed part, and the straight lines between the anchor values are our choice.

Try it yourself:

- Lower the arrival lift: set `END_CL = 4.0`. The drop grows to 8.2 m and the final climb shrinks to +13°.
- Use the other value the paper gives for the dive: set `DIVE_CL = 0.05`. The result hardly changes: the drop stays at 7.3 m, because almost no force acts in either case.
- Launch at the lowest measured speed: set `LAUNCH = 3.3`. The drop rises to 11.3 m: most of the difference from the frozen pose disappears, because the animal must first make up the missing speed by falling.

{% include code-variant.html file="squirrel_glide.py" id="end" replace="END_CL = 5.6" with="END_CL = 4.0" expect="8.2 +13" %}
{% include code-variant.html file="squirrel_glide.py" id="dive" replace="DIVE_CL = 0.01" with="DIVE_CL = 0.05" expect="7.3" %}
{% include code-variant.html file="squirrel_glide.py" id="launch" replace="LAUNCH = 5.37" with="LAUNCH = 3.3" expect="11.3" %}

{% include lens-end.html %}

{% include lens-start.html lens="physical-ai" %}

## Physical AI lens: robots with skin wings

Physical AI means embodied artificial intelligence: machines that sense and act in the physical world. Flying squirrels are attractive models for it, because one body can climb, jump and glide. A clear limit first: **the two machines below that come closest to the animal are clever mechanics with classical control, not learning systems.**

**A drone that changes its whole body.** Liming Zheng, Alexander van Zuijlen and Salua Hamaza built the SquirrelDrone, a 0.689 kg aircraft with a span of 0.7 m and a soft membrane moved by four limbs and a tail. In a wind tunnel, ribs that were free to deflect under the air increased camber and raised the lift coefficient by more than 0.1 at angles of attack below 24°, compared with fixed ribs. Limbs and tail handled roll and pitch without conventional ailerons or elevators, while yaw came from differential thrust of two propellers. Outdoors, on a windy day with gusts of up to 10 m/s in the weather records, a human pilot flew it by remote control, assisted by onboard attitude stabilisation. Three things to keep in mind: this machine has **propellers**, so it does not glide like an animal; a person steered it; and its stabiliser is a classical cascaded PID controller. The authors name coupling between roll and pitch as a limit and plan other control methods [26](#ref-26){:.cite}.

**A glider for the forest.** PteroBot, by Minghao Fan and colleagues, adjusts its gliding posture with a flexible membrane. Under closed-loop attitude control it reached an average glide ratio of 2.02, the same order as the animals. Against drones, its authors report advantages in energy use and noise, which matter for watching wildlife [27](#ref-27){:.cite}.

**Where learning comes in.** Jun-Gill Kang and colleagues built a drone with foldable silicone wings whose movements are controlled by reinforcement learning, trained from human-demonstrated data. Its wings deliberately induce drag and so provide extra force, capturing aerodynamics that are hard to model [28](#ref-28){:.cite}. It too flies with thrust. In a purely simulated study without any squirrel in it, Guido Novati, L. Mahadevan and Petros Koumoutsakos showed that reinforcement learning finds gliding and perching strategies that outperform model-based optimal control and are robust to disturbances [29](#ref-29){:.cite}. It is a hint of where the field could go, not a flying machine.

{% include lens-end.html %}

## What we still do not know

We found no measurement of the airflow around a living flying squirrel in a glide. The landing mechanism remains disputed, the winglet idea untested, and the first 3 metres of the wild glides were inferred rather than filmed [1](#ref-1){:.cite}. The function of the pink glow, if there is one, is unknown [19](#ref-19){:.cite}. A chromosome-level genome of the Siberian flying squirrel was published only in 2025 [5](#ref-5){:.cite}, so, in our view, the genetics of the membrane in this group can now be studied in earnest. Meanwhile, the animals depend on tall trees to start their next glide [13](#ref-13){:.cite}: the physics of their travel is also a reason to keep old forests standing.
