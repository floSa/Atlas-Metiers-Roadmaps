---
title: AI Engineer
tags: [parcours, ai-engineer, llm, rag, agents, mcp, ia, production]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/ai-engineer
---

Construire un produit sur un modèle qu'on n'a pas entraîné : récupérer le bon contexte, orchestrer, poser des garde-fous, tenir le coût et la latence, et mesurer ce qu'on livre.

## La roadmap

Chaque case mène à sa page. Cochez les étapes acquises en bas de page pour suivre votre progression.

```mermaid
flowchart TD
  F["Fondamentaux LLM<br/>tokens, fenêtre, échantillonnage"] --> P["Prompt et contexte<br/>ce qui occupe la fenêtre"]
  P --> M["Modèles et APIs<br/>choisir, appeler, changer"]
  M --> E["Embeddings et recherche<br/>vecteurs, index, hybride"]
  E --> R["RAG<br/>découper, récupérer, citer"]
  R --> A["Agents et MCP<br/>boucle, outils, protocole"]
  A --> MU["Multimodal et documents<br/>vision, audio, parsing"]
  MU --> PR["Mise en production<br/>évaluation, coût, traces"]
  S["Sécurité et conformité<br/>injection, filtres, AI Act"] -.-> R
  S -.-> A
  S -.-> PR

  click F "/parcours/ai-engineer/fondamentaux-llm"
  click P "/parcours/ai-engineer/prompt-et-contexte"
  click M "/parcours/ai-engineer/modeles-et-apis"
  click E "/parcours/ai-engineer/embeddings-et-recherche"
  click R "/parcours/ai-engineer/rag"
  click A "/parcours/ai-engineer/agents-et-mcp"
  click MU "/parcours/ai-engineer/multimodal-et-documents"
  click PR "/parcours/ai-engineer/mise-en-production"
  click S "/parcours/ai-engineer/securite-et-conformite"

  classDef transverse stroke:#f9a825,stroke-width:1px,stroke-dasharray:4 3
  class S transverse
```

## Ma progression

- [ ] [[parcours/ai-engineer/fondamentaux-llm|Fondamentaux LLM]] — pourquoi un appel coûte ce qu'il coûte et répond ce qu'il répond
- [ ] [[parcours/ai-engineer/prompt-et-contexte|Prompt et context engineering]] — écrire l'instruction, puis décider de ce qui entre dans la fenêtre
- [ ] [[parcours/ai-engineer/modeles-et-apis|Modèles, plateformes et APIs]] — l'arbitrage à cinq axes, et le client qu'on écrit pour en changer
- [ ] [[parcours/ai-engineer/embeddings-et-recherche|Embeddings et recherche]] — vectoriser, indexer, mesurer le rappel, passer à l'hybride
- [ ] [[parcours/ai-engineer/rag|RAG]] — le pipeline complet, et l'étage qui fait réellement échouer les réponses
- [ ] [[parcours/ai-engineer/agents-et-mcp|Agents, outils et MCP]] — la boucle, la qualité des outils, l'exposition standardisée
- [ ] [[parcours/ai-engineer/securite-et-conformite|Sécurité et conformité]] — injection de prompt, filtrage, classification AI Act
- [ ] [[parcours/ai-engineer/multimodal-et-documents|Multimodal et documents]] — vision, audio, parsing de PDF, outils de codage assisté
- [ ] [[parcours/ai-engineer/mise-en-production|Mise en production]] — jeu d'évaluation, traces, budget par requête
