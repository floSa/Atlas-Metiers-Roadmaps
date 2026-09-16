---
title: AI Red Teaming
tags: [parcours, ai-red-teaming, securite, llm, injection-de-prompt, gouvernance, ia]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/ai-red-teaming
---

Tester un système d'IA en adversaire pour le rendre défendable : trouver ce qu'un attaquant obtiendrait réellement, le démontrer par un chemin complet, et le transformer en mesure qu'on rejoue à chaque changement.

## La roadmap

Chaque case mène à sa page. Cochez les étapes acquises en bas de page pour suivre votre progression.

```mermaid
flowchart TD
  F["Cadrage et socle<br/>ce qui est propre au modèle"] --> M["Modélisation de la menace<br/>surfaces, adversaires, impact"]
  M --> PH["Prompt hacking<br/>jailbreak et filtres"]
  M --> PI["Injection de prompt<br/>directe et indirecte"]
  M --> MV["Vulnérabilités du modèle<br/>empoisonnement, extraction"]
  M --> IN["Infrastructure et chaîne<br/>API, poids, serveurs d'outils"]
  PH --> E["Engagement et mesure<br/>boîte noire à blanche, corpus adverse"]
  PI --> E
  MV --> E
  IN --> E
  E --> R["Restitution et gouvernance<br/>rapport, divulgation, conformité"]

  click F "/parcours/ai-red-teaming/cadrage-et-socle"
  click M "/parcours/ai-red-teaming/modelisation-de-la-menace"
  click PH "/parcours/ai-red-teaming/prompt-hacking"
  click PI "/parcours/ai-red-teaming/injection-de-prompt"
  click MV "/parcours/ai-red-teaming/vulnerabilites-du-modele"
  click IN "/parcours/ai-red-teaming/infrastructure-et-chaine"
  click E "/parcours/ai-red-teaming/engagement-et-mesure"
  click R "/parcours/ai-red-teaming/restitution-et-gouvernance"

  classDef surface fill:#fff8e1,stroke:#f9a825,stroke-width:1px
  class PH,PI,MV,IN surface
```

## Ma progression

- [ ] [[parcours/ai-red-teaming/cadrage-et-socle|Cadrage et socle technique]] — trier ce qui relève de la sécurité applicative et ce qui est propre au modèle
- [ ] [[parcours/ai-red-teaming/modelisation-de-la-menace|Modélisation de la menace]] — surfaces d'entrée, gradation des adversaires, priorisation par impact
- [ ] [[parcours/ai-red-teaming/prompt-hacking|Prompt hacking]] — jailbreak, contournement des filtres, contre-mesures et leur mesure
- [ ] [[parcours/ai-red-teaming/injection-de-prompt|Injection de prompt]] — la forme indirecte, les canaux d'exfiltration, les parades d'architecture
- [ ] [[parcours/ai-red-teaming/vulnerabilites-du-modele|Vulnérabilités du modèle]] — empoisonnement, exemples adverses, inversion, extraction
- [ ] [[parcours/ai-red-teaming/infrastructure-et-chaine|Infrastructure et chaîne d'approvisionnement]] — API, identité, poids, serveurs d'outils, détection
- [ ] [[parcours/ai-red-teaming/engagement-et-mesure|Engagement et mesure]] — niveaux d'accès, outillage, corpus adverse et non-régression
- [ ] [[parcours/ai-red-teaming/restitution-et-gouvernance|Restitution et gouvernance]] — rapport, divulgation responsable, cadres réglementaires, veille

## Ce qui distingue ce métier des rôles voisins

| Rôle | Ce qu'il produit | Où s'arrête sa responsabilité |
|---|---|---|
| Pentesteur applicatif | des faiblesses connues, énumérées contre un référentiel | au périmètre technique convenu |
| AI Engineer | le système et ses garde-fous | à la qualité de ce qu'il construit |
| Auditeur de conformité | la preuve documentaire qu'un cadre est suivi | au dossier |
| **AI Red Teamer** | **ce qu'un adversaire obtiendrait réellement, le chemin complet, et l'atténuation qui tient** | **quand la posture est mesurée et rejouée à chaque changement** |
