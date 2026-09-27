---
layout: page
lang: en
ref: run-code
title: "Run the code examples"
short_title: "Run the code"
kicker: "Guide · Python"
description: "How to run the tested Python examples on WildBionics – in the browser with Google Colab or on your own computer – and what result to expect."
dek: "Every code example on WildBionics is a complete, tested Python program. Run it in your browser or on your own computer, check the result and start experimenting."
permalink: /run-code/
---

## Every example is tested

Each code example on WildBionics is a complete Python program, not a fragment. Every time the site is built, it runs every example. The **Output** box under the code and the chart come from exactly that run. If an example crashes, prints a warning or no longer does what the page says, the build stops and nothing goes live.

Under every example you find three tools:

- **Copy** (top right of the code) copies the program to the clipboard.
- **Download .py** saves the same program as a file, with a short header that says where it comes from and which libraries it needs.
- **Open in Colab** opens the program as a notebook in Google Colab, ready to run.

## Option 1: in your browser with Google Colab

Nothing to install. [Google Colab](https://colab.research.google.com/) is a free service by Google that runs Python in the cloud; you need a Google account to run code there. NumPy, SciPy and Matplotlib are already installed.

1. Click **Open in Colab** below an example.
2. Choose **Runtime → Run all** (or click into the code cell and press Shift+Enter). Colab warns that the notebook was not written by Google – confirm with **Run anyway**.
3. After a few seconds the output and the chart appear below the cell. They should match the output on WildBionics.
4. Change a value – for example one of the "Try it yourself" suggestions in the article – and run the cell again. To keep your version, choose **File → Save a copy in Drive**.

## Option 2: on your own computer

You need Python 3.9 or newer and three libraries. The first time takes about five minutes.

1. **Install Python.** macOS: `brew install python` (with [Homebrew](https://brew.sh/)) or the installer from [python.org](https://www.python.org/downloads/). Windows: the installer from python.org – tick "Add python.exe to PATH". Linux: usually preinstalled; otherwise install `python3` and `python3-venv` with your package manager. Then check in a terminal:

   ```bash
   python3 --version
   ```

   On Windows, type `py` instead of `python3` in all commands on this page.

2. **Create a folder with its own environment**, so the libraries don't interfere with anything else on your computer:

   ```bash
   mkdir wildbionics-code
   cd wildbionics-code
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   On Windows, the last line is `.venv\Scripts\activate`. Your prompt now starts with `(.venv)`. Next time, `cd` into the folder and run only the last line.

3. **Install the libraries:**

   ```bash
   python3 -m pip install numpy scipy matplotlib
   ```

4. **Save the program** in this folder: click **Download .py** and move the file there, or click **Copy** and paste the code into a new text file with the name shown, for example `rayleigh_plesset.py`.

5. **Run it:**

   ```bash
   python3 rayleigh_plesset.py
   ```

   The printed result appears in the terminal. If the program draws a chart, a window opens; the program ends when you close it.

## What you should see

Your output should match the **Output** box under the example exactly. With much newer or older library versions, a last digit can occasionally differ; the conclusions don't change.

Every example is written to teach one idea. The article explains below the code what the result means, and its "Try it yourself" suggestions show what happens when you turn one knob – a bigger bubble, deeper water, a noisier recording. Change one value at a time and compare with the original output.

## If something goes wrong

- **`python3: command not found`** – Python is not installed or not on the PATH. On Windows, use `py`.
- **`ModuleNotFoundError: No module named 'numpy'`** – the environment is not active (step 2, last line) or the libraries are not installed (step 3).
- **No chart window appears**, for example on a server via SSH – replace the last line `plt.show()` with `plt.savefig("chart.png")` and open the image file.
- **`SyntaxError` in the first line** – some text around the code was copied, too. Use the **Copy** button or **Download .py**.
- **Jupyter or VS Code** – paste the whole program into one cell or into an empty `.py` file and run it there.

## How the examples are tested

The script [`code_examples.py`]({{ site.repository_url }}/blob/main/.github/scripts/code_examples.py) finds every example on the site, runs it with Python 3.12 and the library versions in [`examples/requirements.txt`]({{ site.repository_url }}/blob/main/examples/requirements.txt), and writes the output, the chart, the `.py` download and the Colab notebook. It runs for every pull request and before every deployment, so what you see on a page is what the code really does.

Found an example that doesn't run, or a result that doesn't make sense? [Open an issue]({{ site.repository_url }}/issues/new) – or fix it yourself: [contributing to WildBionics]({{ '/contribute/' | relative_url }}) explains how.
