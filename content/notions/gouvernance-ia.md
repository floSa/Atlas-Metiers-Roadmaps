---
title: Gouvernance de l'IA
tags: [notion, gouvernance, ai-act, conformite, risque]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-red-teaming]
---

Ensemble des dispositifs — inventaire, classification par risque, documentation, supervision humaine, responsabilités nommées — qui rendent une organisation capable de dire ce que font ses systèmes d'IA et qui en répond.

## À quoi ça sert

La gouvernance sert à répondre à une question simple que peu d'organisations savent traiter : **quels systèmes d'IA tournent chez nous, que décident-ils, et qui en est responsable ?** Sans inventaire, il n'y a ni conformité possible ni gestion de risque, seulement des déclarations.

Son second intérêt est d'être le canal par lequel un constat technique atteint une décision. Un risque documenté dans un registre existant est arbitré et financé ; le même risque dans un document isolé est classé. C'est la différence entre un audit qui change quelque chose et un audit qui produit un PDF.

Le cadre réglementaire européen a rendu l'exercice obligatoire pour une partie des usages, avec des obligations qui ressemblent à ce qu'une bonne ingénierie fait déjà : documenter, journaliser, évaluer, garder un humain en position d'intervenir.

## Ce qu'il faut savoir

- **Le règlement européen sur l'IA classe par usage**, pas par technologie : pratiques interdites, systèmes à haut risque, obligations de transparence, modèles à usage général. La même brique technique peut relever de deux catégories selon ce qu'on en fait.
- **Pour un système à haut risque**, les obligations sont un système de gestion des risques, une exigence de qualité des données, une documentation technique, une journalisation, une transparence envers l'utilisateur et une supervision humaine effective.
- **Le NIST AI Risk Management Framework** donne un vocabulaire commun — cartographier, mesurer, gérer, gouverner — et sert surtout à faire remonter les constats dans un registre de risques déjà existant.
- **ISO/IEC 42001** fournit l'ossature d'un système de management de l'IA, pour les organisations qui ont déjà une culture de certification.
- **L'inventaire est le prérequis de tout.** Une organisation qui ne sait pas lister ses systèmes ne peut ni les classer ni les documenter.
- **La supervision humaine n'est réelle que si elle est outillée** : l'humain doit voir ce qui justifie la décision, avoir le temps de l'examiner et le pouvoir de la contredire. Une case « validé par un opérateur » qui est cochée cent fois par heure n'est pas une supervision.
- **Documenter coûte peu au moment de la conception** et beaucoup après. La documentation de conformité fait partie du livrable, pas d'une démarche ultérieure.

## Selon le métier

### Forward Deployed Engineer

L'inscription du système au registre interne du client et la documentation de conformité font partie du livrable. Le réflexe qui fait gagner des semaines : rencontrer les fonctions concernées — protection des données, risques, contrôle interne — pendant la phase d'audit, et leur fournir ce dont elles ont besoin dans leur format, pas dans le sien.

### AI Red Teaming

La gouvernance est ce qui donne une suite aux constats. Le red teaming n'est pas nommé comme une obligation autonome dans le règlement européen, mais il est le moyen le plus direct de produire la preuve que la gestion des risques est effective et non déclarative. D'où l'intérêt de formuler les constats dans le vocabulaire du registre de risques de l'organisation plutôt que dans celui de la sécurité offensive.

> [!warning] Piège
> Traiter la gouvernance comme un document à produire en fin de projet. Les obligations — journalisation, traçabilité des données, supervision humaine — sont des contraintes d'architecture. Découvertes à la recette, elles imposent de reprendre le système ; posées au cadrage, elles ne coûtent presque rien.

## Pour aller plus loin

- [AI Act — Commission européenne](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) — la page officielle du cadre réglementaire.
- [The EU AI Act Explorer](https://artificialintelligenceact.eu/ai-act-explorer/) — le texte navigable par article et par obligation.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — le cadre de gestion du risque, utilisable hors contexte américain.
- [ISO 42001: what it is & why it matters](https://www.itgovernance.co.uk/iso-42001) — l'ossature de management, pour les organisations certifiées.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]
- [[parcours/ai-red-teaming|AI Red Teaming]]

Voisines : [[notions/rgpd]], [[notions/donnees-sensibles]], [[notions/modelisation-de-la-menace]], [[notions/evaluation-llm]].
