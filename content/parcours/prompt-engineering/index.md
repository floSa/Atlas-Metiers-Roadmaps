---
title: Prompt Engineering
tags: [parcours, prompt-engineering, llm, context-engineering, evaluation, ia]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/prompt-engineering
---

Écrire pour un modèle ce qu'on écrirait pour une machine : une instruction, un contexte choisi, un format contraint et une mesure qui dit si la dernière modification a amélioré quoi que ce soit.

## La roadmap

Chaque case mène à sa page et porte le niveau attendu chez un profil **confirmé** — de **notion** (reconnaître le sujet, savoir qui appeler) à **référence** (faire autorité dans la salle). Cochez les étapes acquises en bas de page pour suivre votre progression.

```mermaid
flowchart TD
  F["Fondations et vocabulaire<br/>Autonomie<br/>token, fenêtre, échantillonnage"] --> C["Configuration du modèle<br/>Usage<br/>sampling, budget de raisonnement"]
  C --> S["Sorties structurées<br/>Autonomie<br/>du texte libre à la fonction typée"]
  S --> T["Techniques de prompting<br/>Autonomie<br/>ce qui survit, ce qui est du folklore"]
  T --> E["Évaluation et fiabilité<br/>Référence<br/>le préalable à tout le reste"]
  E --> CE["Context engineering<br/>Référence<br/>quoi mettre, où, quoi retirer"]
  E --> O["Optimisation automatique<br/>Usage<br/>compiler le prompt plutôt que l'écrire"]
  CE --> P["Prompts en production<br/>Autonomie<br/>versionner, tracer, router"]
  O --> P
  SEC["Sécurité du prompt<br/>Autonomie<br/>injection, trio dangereux"] -.-> P

  click F "/parcours/prompt-engineering/fondations-et-vocabulaire"
  click C "/parcours/prompt-engineering/configuration-du-modele"
  click S "/parcours/prompt-engineering/sorties-structurees"
  click T "/parcours/prompt-engineering/techniques-de-prompting"
  click E "/parcours/prompt-engineering/evaluation-et-fiabilite"
  click CE "/parcours/prompt-engineering/context-engineering"
  click O "/parcours/prompt-engineering/optimisation-automatique"
  click P "/parcours/prompt-engineering/prompts-en-production"
  click SEC "/parcours/prompt-engineering/securite-du-prompt"

  classDef transverse stroke:#f9a825,stroke-width:1px,stroke-dasharray:4 3
  class SEC transverse
```

## Ma progression

- [ ] [[parcours/prompt-engineering/fondations-et-vocabulaire|Fondations et vocabulaire]] — ce qu'un modèle fait réellement, et pourquoi un prompt n'est pas portable
- [ ] [[parcours/prompt-engineering/configuration-du-modele|Configuration du modèle]] — les paramètres qui agissent sur la forme, et les deux qui comptent vraiment
- [ ] [[parcours/prompt-engineering/sorties-structurees|Sorties structurées]] — contraindre le décodage plutôt que demander poliment du JSON
- [ ] [[parcours/prompt-engineering/techniques-de-prompting|Techniques de prompting]] — lesquelles sont encore rentables sur un modèle à raisonnement
- [ ] [[parcours/prompt-engineering/evaluation-et-fiabilite|Évaluation et fiabilité]] — jeu de cas versionné, assertions, juge calibré, non-régression
- [ ] [[parcours/prompt-engineering/context-engineering|Context engineering]] — sélection, ordonnancement, compaction, isolation
- [ ] [[parcours/prompt-engineering/optimisation-automatique|Optimisation automatique des prompts]] — recherche guidée par la métrique, portabilité entre modèles
- [ ] [[parcours/prompt-engineering/securite-du-prompt|Sécurité du prompt]] — injection directe et indirecte, et ce qui relève de l'architecture
- [ ] [[parcours/prompt-engineering/prompts-en-production|Prompts en production]] — versionnement, traces, coût par requête, routage
