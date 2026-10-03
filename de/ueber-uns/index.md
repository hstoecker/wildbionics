---
layout: page
lang: de
ref: about
schema_type: AboutPage
hero_mark: true
title: "Über WildBionics"
short_title: "Über uns"
kicker: "Open Source · Über das Projekt"
description: "WildBionics ist ein Open-Source-Kompendium, das die Natur mit Physik, Mathematik, Chemie, Informatik und Physical AI erklärt – belegt, getestet, frei nutzbar."
dek: "Ein Open-Source-Kompendium, das die Natur mit Physik erklärt: von Tieren, Pflanzen und unserem Planeten bis zu Robotern und KI, die von ihnen lernen. Jede Aussage hat eine Quelle, jedes Code-Beispiel läuft, und alle können mitmachen."
permalink: /de/ueber-uns/
---
{%- include i18n.html -%}
{%- capture suggest -%}{{ site.repository_url }}/discussions/new?category=suggest-a-topic-thema-vorschlagen{%- endcapture -%}

## Was WildBionics ist

WildBionics verbindet Biologie mit Physik, Mathematik, Chemie, Informatik und Physical AI. Jede Seite beginnt mit etwas, das man in der Natur beobachten kann – eine Fledermaus, die im Dunkeln jagt, ein Gecko an der Decke, eine Katze, die auf den Pfoten landet – und erklärt die Physik dahinter.

Die Kernidee ist die **Linse**. Du betrachtest dasselbe Phänomen durch mehrere Linsen und wechselst zwischen ihnen: Biologie, Physik, Mathematik, Informatik und, wo es passt, Physical AI – Roboter und Maschinen, die in der echten Welt wahrnehmen und handeln. Jeder Artikel ist außerdem Teil eines **[Wissensgraphen]({{ t.graph.url | relative_url }})**, der ihn mit seiner Zeit, seinem Lebensraum, den beteiligten Gesetzen der Physik und den Nachbarwissenschaften verknüpft.

## Was wir wollen

- **Die Natur verständlich und überprüfbar erklären.** Klare Sprache, Abbildungen, die die Idee zeigen, und eine Quelle für jede Aussage.
- **Frei für alle.** Alle Inhalte dürfen gelesen, geteilt und weiterverwendet werden, auch im Unterricht – unter einer offenen Lizenz.
- **Jeden Tag wachsen.** Unser Ziel ist eine neue Seite pro Tag – zu Themen, nach denen Menschen fragen.
- **In mehr Sprachen.** WildBionics erscheint auf Englisch und Deutsch; weitere Sprachen folgen, sobald sich Freiwillige finden.

## Wie wir arbeiten

- **Jede Aussage hat eine Quelle.** Wir zitieren begutachtete Forschung, meist mit DOI, und prüfen jede Angabe bei Crossref oder PubMed, bevor sie online geht.
- **Zahlen werden berechnet, nicht abgeschrieben.** Abgeleitete Werte kommen aus kleinen Programmen, und die Rechnung steht mit ihren Annahmen auf der Seite.
- **Hypothesen bleiben Hypothesen.** Offene Fragen und Zukunftsszenarien sind als solche gekennzeichnet.
- **Jede Änderung wird geprüft.** Jede Änderung ist ein Pull Request auf GitHub. Automatische Prüfungen testen Fachbegriffe, Aufbau, Links, strukturierte Daten und jedes Code-Beispiel; danach folgt eine Prüfung mit Faktencheck, und der Maintainer gibt frei, bevor etwas online geht.
- **KI hilft, offen.** Ein großer Teil der Recherche, des Schreibens und Prüfens geschieht mit Claude, einem KI-Assistenten. Die Regeln, denen er folgt, stehen öffentlich im Repository, und jede Seite wird trotzdem an ihren Quellen geprüft und von einem Menschen freigegeben.

## Was du lernen und selbst ausprobieren kannst

- **Wechsle die Linse** in jedem [Artikel]({{ t.articles.url | relative_url }}) und sieh dasselbe Phänomen wie eine Biologin, ein Physiker, eine Mathematikerin oder ein Programmierer.
- **Führe den Code aus.** Jedes Code-Beispiel ist ein vollständiges Python-Programm, das bei jedem Build getestet wird. [Führe es aus]({{ '/de/code-ausfuehren/' | relative_url }}) – im Browser mit Google Colab oder auf deinem Rechner –, ändere einen Wert und sieh, wie sich das Ergebnis ändert.
- **Erkunde den [Wissensgraphen]({{ t.graph.url | relative_url }})** und finde heraus, was ein Knallkrebs mit einem Lotusblatt gemeinsam hat.
- **Nutze die Abbildungen.** Jede Abbildung lässt sich einzeln öffnen und im Unterricht oder in eigenen Arbeiten weiterverwenden, mit Namensnennung.

## Open Source

Alles liegt öffentlich auf [GitHub]({{ site.repository_url }}): die Texte, die Abbildungen, der Code und die Regeln, die die Qualität hochhalten. Der Code steht unter der MIT-Lizenz, die Inhalte unter [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.de). Suchmaschinen und KI-Systeme dürfen WildBionics gerne lesen und zitieren, mit Namensnennung.

## Mach mit

Alle können mitmachen – mit oder ohne Programmierkenntnisse:

- **Schlag jederzeit ein Thema vor:** ein Tier, eine Pflanze oder ein Phänomen, das du erklärt haben möchtest, vielleicht für eine Unterrichtsstunde oder ein Projekt. [Thema vorschlagen]({{ suggest }}) in den GitHub-Diskussionen.
- **Frag und diskutiere** in den [Diskussionen]({{ site.repository_url }}/discussions).
- **Schreib, übersetze, zeichne oder korrigiere** – die Seite [Mitmachen]({{ t.guide.url | relative_url }}) zeigt drei Wege dazu, mit Claude oder von Hand.
- **Kein GitHub-Konto?** Schreib an {% include email.html user=t.footer.email_user %}.
