---
title: Forward Deployed Engineer
tags: [parcours, forward-deployed-engineer, fde, ia, conseil, deploiement, terrain]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/forward-deployed-engineer
---

Un ingénieur logiciel qui travaille **à l'intérieur** de l'environnement d'un client, pour y construire et y faire adopter un système d'IA qui tienne dans son infrastructure et dans ses habitudes.

## La roadmap

Chaque case mène à sa page et porte le niveau attendu chez un FDE confirmé — de **notion** (reconnaître le sujet, savoir qui appeler) à **usage** (s'en servir sur un chemin balisé), **autonomie** (concevoir, déboguer sous pression, arbitrer et défendre l'arbitrage) et **référence** (faire autorité dans la salle). Cochez les étapes acquises en bas de page pour suivre votre progression.

```mermaid
flowchart TD
  S["Socle technique<br/>Autonomie"] --> C["Cycle de mission<br/>Référence"]
  C --> P1["Phase 1 — Audit<br/>Référence"]
  P1 --> P2["Phase 2 — Arbitrage<br/>Référence"]
  P2 --> P3["Phase 3 — Industrialisation<br/>Autonomie"]
  P3 --> P4["Phase 4 — Sortie<br/>Référence"]
  R["Compétences relationnelles<br/>Autonomie"] -.-> P1
  R -.-> P2
  R -.-> P3
  R -.-> P4

  click S "/parcours/forward-deployed-engineer/socle-technique/"
  click C "/parcours/forward-deployed-engineer/cycle-mission"
  click P1 "/parcours/forward-deployed-engineer/audit-et-cartographie"
  click P2 "/parcours/forward-deployed-engineer/arbitrage-technologique"
  click P3 "/parcours/forward-deployed-engineer/industrialisation/index"
  click P4 "/parcours/forward-deployed-engineer/sortie-de-mission/index"
  click R "/parcours/forward-deployed-engineer/competences-relationnelles"

  classDef transverse stroke:#f9a825,stroke-width:1px,stroke-dasharray:4 3
  class R transverse
```

## Ma progression

- [ ] [[parcours/forward-deployed-engineer/socle-technique/index|Socle technique]] — ce qu'il faut savoir faire, et à quelle profondeur
- [ ] [[parcours/forward-deployed-engineer/cycle-mission/index|Cycle de mission]] — les quatre phases et leurs portes de sortie
- [ ] [[parcours/forward-deployed-engineer/audit-et-cartographie/index|Phase 1 — Audit et cartographie]] — observer le travail réel, modéliser le processus
- [ ] [[parcours/forward-deployed-engineer/arbitrage-technologique/index|Phase 2 — Arbitrage technologique]] — simplifier avant d'automatiser, déterministe ou probabiliste
- [ ] [[parcours/forward-deployed-engineer/industrialisation/index|Phase 3 — Industrialisation]] — interfaçage, sécurité, évaluation, exploitation
- [ ] [[parcours/forward-deployed-engineer/sortie-de-mission/index|Phase 4 — Sortie de mission]] — transfert de compétences, maintenance
- [ ] [[parcours/forward-deployed-engineer/competences-relationnelles/index|Compétences relationnelles]] — parties prenantes, politique interne, conduite du changement
