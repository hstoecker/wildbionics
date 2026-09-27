---
layout: page
lang: de
ref: run-code
title: "Die Code-Beispiele ausführen"
short_title: "Code ausführen"
kicker: "Anleitung · Python"
description: "So führst du die getesteten Python-Beispiele von WildBionics aus – in Google Colab oder auf deinem Rechner – und welches Ergebnis du erwarten kannst."
dek: "Jedes Code-Beispiel auf WildBionics ist ein vollständiges, getestetes Python-Programm. Führe es im Browser oder auf deinem Rechner aus, prüfe das Ergebnis und experimentiere los."
permalink: /de/code-ausfuehren/
---

## Jedes Beispiel ist getestet

Jedes Code-Beispiel auf WildBionics ist ein vollständiges Python-Programm, kein Bruchstück. Bei jedem Build der Website wird jedes Beispiel ausgeführt. Der Kasten **Ausgabe** unter dem Code und das Diagramm stammen genau aus diesem Lauf. Stürzt ein Beispiel ab, gibt es eine Warnung aus oder tut es nicht mehr, was die Seite beschreibt, bricht der Build ab und nichts geht online.

Unter jedem Beispiel findest du drei Werkzeuge:

- **Kopieren** (oben rechts am Code) kopiert das Programm in die Zwischenablage.
- **.py herunterladen** speichert dasselbe Programm als Datei, mit einem kurzen Kopf, der sagt, woher es stammt und welche Bibliotheken es braucht.
- **In Colab öffnen** öffnet das Programm als Notebook in Google Colab, fertig zum Ausführen.

## Weg 1: im Browser mit Google Colab

Nichts zu installieren. [Google Colab](https://colab.research.google.com/) ist ein kostenloser Dienst von Google, der Python in der Cloud ausführt; zum Ausführen brauchst du ein Google-Konto. NumPy, SciPy und Matplotlib sind bereits installiert.

1. Klicke unter einem Beispiel auf **In Colab öffnen**.
2. Wähle **Laufzeit → Alle ausführen** (oder klicke in die Code-Zelle und drücke Umschalt+Enter). Colab warnt, dass das Notebook nicht von Google stammt – bestätige mit **Trotzdem ausführen**.
3. Nach wenigen Sekunden erscheinen Ausgabe und Diagramm unter der Zelle. Sie sollten mit der Ausgabe auf WildBionics übereinstimmen.
4. Ändere einen Wert – zum Beispiel einen der „Probier es selbst aus“-Vorschläge im Artikel – und führe die Zelle erneut aus. Um deine Fassung zu behalten, wähle **Datei → Kopie in Drive speichern**.

## Weg 2: auf deinem eigenen Rechner

Du brauchst Python 3.9 oder neuer und drei Bibliotheken. Beim ersten Mal dauert das etwa fünf Minuten.

1. **Python installieren.** macOS: `brew install python` (mit [Homebrew](https://brew.sh/)) oder das Installationsprogramm von [python.org](https://www.python.org/downloads/). Windows: das Installationsprogramm von python.org – setze den Haken bei „Add python.exe to PATH“. Linux: meist vorinstalliert, sonst `python3` und `python3-venv` über die Paketverwaltung installieren. Prüfe dann in einem Terminal:

   ```bash
   python3 --version
   ```

   Unter Windows tippst du in allen Befehlen auf dieser Seite `py` statt `python3`.

2. **Einen Ordner mit eigener Umgebung anlegen**, damit die Bibliotheken nichts anderes auf deinem Rechner stören:

   ```bash
   mkdir wildbionics-code
   cd wildbionics-code
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   Unter Windows lautet die letzte Zeile `.venv\Scripts\activate`. Deine Eingabezeile beginnt jetzt mit `(.venv)`. Beim nächsten Mal wechselst du mit `cd` in den Ordner und führst nur die letzte Zeile aus.

3. **Die Bibliotheken installieren:**

   ```bash
   python3 -m pip install numpy scipy matplotlib
   ```

4. **Das Programm speichern** – in diesem Ordner: Klicke auf **.py herunterladen** und verschiebe die Datei dorthin, oder klicke auf **Kopieren** und füge den Code in eine neue Textdatei mit dem angezeigten Namen ein, zum Beispiel `rayleigh_plesset.py`.

5. **Ausführen:**

   ```bash
   python3 rayleigh_plesset.py
   ```

   Das Ergebnis erscheint im Terminal. Zeichnet das Programm ein Diagramm, öffnet sich ein Fenster; das Programm endet, wenn du es schließt.

## Was du sehen solltest

Deine Ausgabe sollte genau dem Kasten **Ausgabe** unter dem Beispiel entsprechen. Mit deutlich neueren oder älteren Bibliotheksversionen kann gelegentlich eine letzte Stelle abweichen; an den Schlussfolgerungen ändert das nichts.

Jedes Beispiel soll eine Idee vermitteln. Der Artikel erklärt unter dem Code, was das Ergebnis bedeutet, und seine „Probier es selbst aus“-Vorschläge zeigen, was passiert, wenn du an einer Stellschraube drehst – eine größere Blase, tieferes Wasser, eine verrauschtere Aufnahme. Ändere immer nur einen Wert und vergleiche mit der ursprünglichen Ausgabe.

## Wenn etwas nicht klappt

- **`python3: command not found`** – Python ist nicht installiert oder nicht im PATH. Unter Windows nutze `py`.
- **`ModuleNotFoundError: No module named 'numpy'`** – die Umgebung ist nicht aktiv (Schritt 2, letzte Zeile) oder die Bibliotheken sind nicht installiert (Schritt 3).
- **Es öffnet sich kein Diagrammfenster**, etwa auf einem Server per SSH – ersetze die letzte Zeile `plt.show()` durch `plt.savefig("chart.png")` und öffne die Bilddatei.
- **`SyntaxError` in der ersten Zeile** – beim Kopieren ist Text um den Code herum mitgerutscht. Nutze den Button **Kopieren** oder **.py herunterladen**.
- **Jupyter oder VS Code** – füge das ganze Programm in eine Zelle oder in eine leere `.py`-Datei ein und führe es dort aus.

## So werden die Beispiele getestet

Das Skript [`code_examples.py`]({{ site.repository_url }}/blob/main/.github/scripts/code_examples.py) findet jedes Beispiel auf der Website, führt es mit Python 3.12 und den Bibliotheksversionen aus [`examples/requirements.txt`]({{ site.repository_url }}/blob/main/examples/requirements.txt) aus und schreibt Ausgabe, Diagramm, `.py`-Download und Colab-Notebook. Es läuft bei jedem Pull Request und vor jeder Veröffentlichung – was du auf einer Seite siehst, tut der Code also wirklich.

Ein Beispiel läuft nicht, oder ein Ergebnis ergibt keinen Sinn? [Eröffne ein Issue]({{ site.repository_url }}/issues/new) – oder behebe es selbst: [Bei WildBionics mitmachen]({{ '/de/mitmachen/' | relative_url }}) erklärt, wie.
