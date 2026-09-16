---
title: Prompt et context engineering
tags: [parcours, ai-engineer, prompt, contexte, sortie-structuree, cache]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/ai-engineer
---

**Référence.** C'est l'un des deux domaines où un AI Engineer confirmé doit faire autorité dans la salle : décider ce qui occupe la fenêtre à chaque tour est ce qui reste du métier quand on retire le modèle et l'infrastructure, et personne d'autre ne le tranchera à sa place.

Le prompt engineering optimise une instruction ; le context engineering décide de ce qui occupe la fenêtre à chaque tour — et sur une application réelle, le second pèse bien plus lourd.

```mermaid
flowchart TD
  IP["Ingénierie de prompt<br/>ce qui marche, ce qui est du folklore"]
  RG["RAG<br/>la récupération comme source de contexte"]
  CA["Contrôle d'accès<br/>filtrer par identité à la requête"]
  CT["Coût et latence<br/>cache de préfixe, streaming"]
  EV["Évaluation LLM<br/>trancher une consigne par la mesure"]

  click IP "/notions/ingenierie-de-prompt"
  click RG "/notions/rag"
  click CA "/notions/controle-d-acces"
  click CT "/notions/cout-et-latence-inference"
  click EV "/notions/evaluation-llm"
```

## Pourquoi le contexte l'emporte sur le prompt

Un agent qui tourne dix tours voit sa fenêtre se remplir de sorties d'outils, et c'est là que la qualité s'effondre — pas dans la formulation du prompt système. Celui-ci fixe rôle, comportement et contraintes ; il est stable, il se versionne comme du code, et il ne bouge presque plus une fois calibré. Ce qui bouge à chaque tour, c'est le reste : historique, documents récupérés, résultats d'outils. Décider quoi y mettre, quoi résumer et quoi retirer est le vrai travail.

## Ce qu'il faut savoir faire

- **Verrouiller un format par l'exemple.** Trois à cinq exemples bien choisis valent mieux qu'une page de consignes abstraites, surtout pour imposer une structure de sortie.
- **Structurer l'entrée.** Délimiter les blocs par des balises XML ou du Markdown, placer les instructions **après** les données longues, rappeler les contraintes en fin de prompt.
- **Imposer un schéma côté API plutôt que dans le prompt.** La sortie structurée et l'appel de fonction sont la même mécanique — le modèle renvoie un objet typé que votre code valide et exécute — et suppriment une classe entière d'erreurs d'analyse.
- **Organiser le prompt pour le cache.** Les préfixes stables sont facturés bien moins cher en relecture : stable d'abord, variable ensuite. Le streaming sauve la latence perçue mais repousse la validation en fin de flux.
- **Appliquer les quatre gestes de context engineering** — mémoire externe pour sortir l'historique de la fenêtre, compaction dès la moitié de la fenêtre, isolation de chaque sous-tâche dans son propre contexte, et filtrage dynamique de la récupération par utilisateur, date et source.
- **Renvoyer un résumé de sortie d'outil plutôt que le blob brut.** C'est le geste qui rend le plus, parce qu'il évite que le contexte se remplisse de bruit que le modèle devra ensuite ignorer.

> [!warning] Piège
> Empiler une consigne à chaque incident jusqu'au prompt système de 4 000 tokens dont personne ne sait quelle ligne fait quoi. Tenir un jeu de cas de test dès le début, et supprimer toute consigne qui ne fait plus bouger le score. Les contraintes dures se codent dans l'application — validation, permissions — pas dans le prompt.

## Les notions mobilisées

- [[notions/ingenierie-de-prompt]] — angle AI Engineer : la partie du folklore qui a survécu tient en une page, le reste est de la gestion de contexte.
- [[notions/rag]] — la récupération est le principal producteur de contexte dynamique, donc le principal responsable de sa saturation.
- [[notions/controle-d-acces]] — le filtrage dynamique de la récupération est le point où les droits d'accès s'appliquent réellement ; appliqué à la requête, jamais après coup.
- [[notions/cout-et-latence-inference]] — le cache de préfixe change l'économie d'une boucle longue, à condition d'ordonner le prompt pour lui.
- [[notions/evaluation-llm]] — sans jeu de cas figés, une modification de prompt est une opinion : c'est ce qui permet de supprimer une consigne sans peur.

## Pour apprendre

- [Claude — Prompt engineering](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) — la présentation la plus structurée des techniques, par ordre d'effet réel.
- [Gemini — Stratégies de prompt](https://ai.google.dev/gemini-api/docs/prompting-strategies) — le même terrain vu par un autre éditeur ; les écarts sont instructifs.
- [OpenAI — Appel de fonctions](https://developers.openai.com/api/docs/guides/function-calling) — le mécanisme qui transforme un modèle en pièce d'un système.
- [Gemini — Sortie structurée](https://ai.google.dev/gemini-api/docs/structured-output) — contraindre la forme de la réponse, la seule façon de chaîner sans analyser du texte libre.
- [Chain-of-Thought Prompting Elicits Reasoning in LLMs](https://arxiv.org/abs/2201.11903) — Wei et al., 2022 : l'article d'origine, à lire plutôt que ses résumés.
