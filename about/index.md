---
layout: page
lang: en
ref: about
schema_type: AboutPage
hero_mark: true
title: "About WildBionics"
short_title: "About"
kicker: "Open source · About the project"
description: "WildBionics is an open-source compendium that explains nature with physics, maths, chemistry, computer science and Physical AI – sourced, tested, free to reuse."
dek: "An open-source compendium that explains nature with physics: from animals, plants and our planet to the robots and AI that learn from them. Every claim has a source, every code example runs, and everyone can join in."
permalink: /about/
---
{%- include i18n.html -%}
{%- capture suggest -%}{{ site.repository_url }}/discussions/new?category=suggest-a-topic-thema-vorschlagen{%- endcapture -%}

## What WildBionics is

WildBionics connects biology with physics, mathematics, chemistry, computer science and Physical AI. Each page starts with something you can observe in nature – a bat hunting in the dark, a gecko on a ceiling, a cat landing on its feet – and explains the physics behind it.

The core idea is the **lens**. You look at the same phenomenon through several lenses and switch between them: biology, physics, mathematics, computer science and, where it fits, Physical AI – robots and machines that sense and act in the real world. Every article is also part of a **[knowledge graph]({{ t.graph.url | relative_url }})** that links it to its time, its habitat, the laws of physics involved and the neighbouring sciences.

## What we want

- **Explain nature so you can understand and check it.** Clear language, figures that show the idea, and a source for every statement.
- **Free for everyone.** All content may be read, shared and reused, also in class, under an open licence.
- **Grow every day.** Our goal is a new page every day – on topics that people ask about.
- **In more languages.** WildBionics is written in English and German; more languages follow as soon as volunteers join.

## How we work

- **Every claim has a source.** We cite peer-reviewed research, usually with a DOI, and check every reference against Crossref or PubMed before it goes online.
- **Numbers are calculated, not copied.** Derived values come from small programs, and the calculation is shown on the page with its assumptions.
- **Hypotheses stay hypotheses.** Open questions and future scenarios are marked as such.
- **Every change is reviewed.** Each change is a pull request on GitHub. Automatic checks test terminology, structure, links, structured data and every code example; a review including a fact check follows, and the maintainer approves before anything goes live.
- **AI helps, openly.** Much of the research, writing and checking is done with Claude, an AI assistant. The rules it follows are public in the repository, and every page is still checked against its sources and approved by a human.

## What you can learn and try yourself

- **Switch lenses** in any [article]({{ t.articles.url | relative_url }}) and see the same phenomenon as a biologist, a physicist, a mathematician or a programmer.
- **Run the code.** Every code example is a complete Python program that is tested at every build. [Run it]({{ '/run-code/' | relative_url }}) in your browser with Google Colab or on your own computer, change a value and watch the result change.
- **Explore the [knowledge graph]({{ t.graph.url | relative_url }})** and find out what a pistol shrimp has in common with a lotus leaf.
- **Use the figures.** Each figure can be opened on its own and reused in class or in your own work, with attribution.

## Open source

Everything is public on [GitHub]({{ site.repository_url }}): the texts, the figures, the code and the rules that keep the quality high. The code is under the MIT licence, the content under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Search engines and AI systems are welcome to read and cite WildBionics, with attribution.

## Join in

Anyone can take part – with or without programming:

- **Suggest a topic** at any time: an animal, a plant or a phenomenon you want explained, maybe for a lesson or a project. [Suggest a topic]({{ suggest }}) in GitHub Discussions.
- **Ask and discuss** in the [Discussions]({{ site.repository_url }}/discussions).
- **Write, translate, draw or correct** – the [contribute page]({{ t.guide.url | relative_url }}) shows three ways to do it, with Claude or by hand.
- **No GitHub account?** Write to {% include email.html user=t.footer.email_user %}.
