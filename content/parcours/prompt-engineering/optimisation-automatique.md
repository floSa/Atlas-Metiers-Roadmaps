---
title: Optimisation automatique des prompts
tags: [parcours, prompt-engineering, dspy, optimisation, few-shot, portabilite]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/prompt-engineering
---

**Usage.** Les optimiseurs se conduisent documentation ouverte, et leur bénéfice dépend surtout de la qualité du jeu d'évaluation en amont : l'attendu est de les avoir fait tourner et de savoir quand ils paient, pas de les réimplémenter.

Dès qu'on dispose d'un jeu d'exemples annotés et d'une métrique, l'écriture d'un prompt devient un problème de recherche que la machine résout mieux et plus vite qu'un humain.

```mermaid
flowchart TD
  EV["Évaluation LLM<br/>la métrique borne le résultat"]
  IP["Ingénierie de prompt<br/>ce qu'on automatise exactement"]
  CI["Intégration continue<br/>le prompt compilé est un artefact de build"]
  CM["Choix de modèle<br/>recompiler plutôt que réécrire"]

  click EV "/notions/evaluation-llm"
  click IP "/notions/ingenierie-de-prompt"
  click CI "/notions/integration-continue"
  click CM "/notions/choix-de-modele"
```

## Une recherche locale banale, avec un ingrédient rare

Le principe tient en trois pas : un modèle génère des variantes d'instruction, on les évalue sur un jeu de test, on garde les meilleures, on recommence. C'est l'idée du papier « Large Language Models are Human-Level Prompt Engineers ». Le seul ingrédient rare est la métrique — sans jeu d'évaluation, l'optimisation automatique produit des prompts qui *ont l'air* meilleurs, et la qualité du résultat est exactement bornée par la qualité de la mesure.

Ce qu'on optimise n'est pas seulement l'instruction. La **sélection des démonstrations few-shot** rapporte souvent davantage que la réécriture de la consigne : choisir automatiquement les bons exemples est un levier sous-estimé.

DSPy a rendu l'approche courante en déplaçant le curseur. On déclare une **signature** — entrées, sorties, objectif — et un module ; le compilateur produit le prompt en fonction du modèle cible et de la métrique. Le bénéfice réel n'est pas le gain de score, c'est la **portabilité** : changer de modèle devient une recompilation plutôt qu'une réécriture manuelle de tous les prompts. Les optimiseurs récents exploitent en plus le retour textuel sur les erreurs pour proposer des réécritures ciblées, ce qui converge nettement plus vite que la recherche aléatoire. Le coût de compilation, lui, reste significatif : à budgéter comme un entraînement, pas comme un test.

## Ce qu'il faut savoir faire

- **Refuser de lancer une optimisation sans métrique** : c'est la seule condition d'entrée, et elle n'est pas négociable.
- **Séparer train, dev et test** comme pour n'importe quel modèle. Un prompt optimisé sur cinquante exemples surapprend ces cinquante exemples.
- **Compiler un prompt avec DSPy et battre la version manuelle** sur un jeu de test tenu à l'écart — l'exercice de référence, qui vaut aussi comme test de sérieux du jeu d'évaluation.
- **Optimiser d'abord la sélection d'exemples**, avant de toucher à l'instruction : c'est là que se trouve le gain le plus facile.
- **Traiter le prompt compilé comme un artefact de build** : versionné, jamais édité à la main, régénéré à chaque changement de modèle.
- **Budgéter la compilation** en appels et en euros avant de la lancer, et la sortir du chemin critique de la livraison.

> [!warning] Piège
> Les prompts optimisés automatiquement sont souvent illisibles, et personne dans l'équipe n'ose plus y toucher. Garder sous contrôle de version le couple (signature lisible, prompt compilé) évite qu'un artefact généré devienne du code source que plus personne ne comprend.

## Les notions mobilisées

- [[notions/evaluation-llm]] — le préalable absolu ; l'optimisation ne fait qu'amplifier ce que la métrique récompense, y compris ses défauts.
- [[notions/ingenierie-de-prompt]] — l'angle prompt engineering : ce qui s'automatise ici est exactement la partie du métier qui se mesure.
- [[notions/integration-continue]] — la compilation est une étape de build, avec son cache, son coût et son artefact.
- [[notions/choix-de-modele]] — l'argument décisif de l'approche programmatique : une migration devient une recompilation.

## Pour apprendre

- [Documentation DSPy](https://dspy.ai/) — signatures, modules et optimiseurs ; le meilleur point d'entrée sur l'optimisation programmatique, avec des exemples exécutables.
- [Large Language Models Are Human-Level Prompt Engineers](https://arxiv.org/abs/2211.01910) — le papier fondateur, court, qui pose la boucle génération / notation / sélection.
- [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/abs/2310.03714) — l'article du cadre, utile pour comprendre ce que « compiler un prompt » veut dire précisément.
- [Optimizing Instructions and Demonstrations for Multi-Stage LM Programs](https://arxiv.org/abs/2406.11695) — l'optimiseur MIPRO et la démonstration que le choix des exemples pèse plus que l'instruction.
