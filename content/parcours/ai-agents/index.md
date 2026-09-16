---
title: AI Agents
tags: [parcours, ai-agents, llm, mcp, orchestration, memoire, evaluation, ia]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/ai-agents
---

Mettre un agent en production plutôt qu'une démonstration : une boucle bornée, des outils dont les erreurs se corrigent, une mémoire qui oublie, et une trace qui permet de rejouer l'incident.

## La roadmap

Chaque case mène à sa page, et porte en deuxième ligne le niveau attendu chez un profil confirmé — **notion** (reconnaître le sujet, savoir qui appeler), **usage** (s'en servir sur un chemin balisé), **autonomie** (concevoir, déboguer sous pression, arbitrer et défendre), **référence** (faire autorité dans la salle). Cochez les étapes acquises en bas de page pour suivre votre progression.

```mermaid
flowchart TD
  S["Socle LLM<br/>Autonomie<br/>backend, tokens, échantillonnage"] --> B["La boucle agentique<br/>Référence<br/>observer, décider, agir"]
  B --> O["Outils et MCP<br/>Référence<br/>définitions, erreurs, protocole"]
  O --> M["Mémoire<br/>Autonomie<br/>court terme, long terme, oubli"]
  M --> A["Architectures<br/>Autonomie<br/>ReAct, DAG, multi-agents"]
  A --> C["Construire l'agent<br/>Autonomie<br/>à la main, puis framework"]
  C --> E["Évaluation et observabilité<br/>Autonomie<br/>trajectoire, traces, coût"]
  SE["Sécurité<br/>Usage<br/>injection, bac à sable, validation"] -.-> O
  SE -.-> C
  SE -.-> E

  click S "/parcours/ai-agents/socle-llm"
  click B "/parcours/ai-agents/la-boucle-agentique"
  click O "/parcours/ai-agents/outils-et-mcp"
  click M "/parcours/ai-agents/memoire"
  click A "/parcours/ai-agents/architectures"
  click C "/parcours/ai-agents/construire-l-agent"
  click E "/parcours/ai-agents/evaluation-et-observabilite"
  click SE "/parcours/ai-agents/securite"

  classDef transverse stroke:#f9a825,stroke-width:1px,stroke-dasharray:4 3
  class SE transverse
```

## Ma progression

- [ ] [[parcours/ai-agents/socle-llm|Socle LLM et backend]] — un agent est d'abord un service asynchrone qui appelle une API payante
- [ ] [[parcours/ai-agents/la-boucle-agentique|La boucle agentique]] — ce qui sépare un agent d'un appel de modèle, et le prompt qui la spécifie
- [ ] [[parcours/ai-agents/outils-et-mcp|Outils, actions et MCP]] — écrire des définitions que le modèle lit, et les exposer une seule fois
- [ ] [[parcours/ai-agents/memoire|Mémoire de l'agent]] — court terme, long terme, profil utilisateur, stratégies d'oubli
- [ ] [[parcours/ai-agents/architectures|Architectures d'agents]] — du graphe déterministe au multi-agents, et ce qui justifie de monter
- [ ] [[parcours/ai-agents/construire-l-agent|Construire l'agent]] — la boucle à la main, l'appel de fonction natif, puis le framework
- [ ] [[parcours/ai-agents/evaluation-et-observabilite|Évaluation et observabilité]] — évaluer la trajectoire, tracer, mesurer la queue de distribution
- [ ] [[parcours/ai-agents/securite|Sécurité de l'agent]] — triade létale, bac à sable, permissions, validation humaine
