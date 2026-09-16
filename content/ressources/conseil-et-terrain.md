---
title: Ressources — Conseil et terrain
tags: [ressources, conseil, fde, processus, bpmn, parties-prenantes, conformite, reference]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/forward-deployed-engineer
---

> [!abstract] Cadrage du besoin, modélisation de processus, jeu des parties prenantes, conformité, sortie de mission. La famille la plus mal servie par l'amont, et celle où la sélection a le plus écarté : sur un sujet neuf et rentable, le contenu promotionnel déguisé en pédagogie est la norme.

## Ce que l'amont propose, et pourquoi c'est mince

La roadmap `forward-deployed-engineer` compte trente ressources pour vingt nœuds de
contenu, et son socle technique n'est qu'un renvoi vers sept autres roadmaps. Sur ces
trente ressources, une bonne part sont des pages d'éditeurs de logiciels : un fournisseur de gestion des exigences explique le
recueil des exigences, un éditeur de flux de travail explique la gestion des flux de
travail, une agence de formation explique la session de cadrage. Ce n'est pas
disqualifiant — ces pages sont souvent les seules à traiter le sujet de façon
structurée — mais ça se dit.

D'où la règle appliquée ici : **quand une ressource est un contenu d'éditeur, la colonne
« ce qu'elle apporte » le dit**. Le lecteur décide ensuite.

## Cadrer le besoin

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| article | [Requirements Gathering in Software Engineering](https://www.jamasoftware.com/requirements-management-guide/requirements-gathering-and-management-processes/what-is-requirements-gathering/) | le plus consistant sur le recueil des exigences. **Contenu d'un éditeur d'outil de gestion des exigences**, à lire en le sachant | intermédiaire |
| cours | [Requirements Gathering in Business Analysis](https://www.coursera.org/learn/requirements-gathering-in-business-analysis) | cours complet, format long. Utile si le cadrage est le point faible | débutant |
| article | [Use Case Discovery & System Scoping](https://academy.openai.com/public/clubs/builders-etkn1/videos/ai-techniques-production-use-case-discovery-and-system-scoping-2025-12-11) | le plus proche du métier réel, et daté — ce qui compte sur un sujet qui bouge | intermédiaire |
| article | [Project management triangle](https://asana.com/resources/project-management-triangle) | le triangle périmètre-délai-qualité, correctement exposé. L'outil de conversation le plus utile en comité de pilotage | débutant |

Voir [[notions/cadrage-besoin]] et [[notions/arbitrage-deterministe-probabiliste]].

> [!warning] Piège
> Le recueil des exigences produit la liste de ce que le client dit vouloir. Le cadrage
> produit la liste de ce qui vaut la peine d'être construit. Confondre les deux, c'est
> livrer exactement ce qui a été demandé et constater dans six mois que personne ne s'en
> sert.

## Modéliser un processus

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| norme | [Spécification BPMN 2.0 (OMG)](https://www.omg.org/spec/BPMN/2.0/) | la norme elle-même. On n'en lit qu'une petite partie, mais c'est la seule référence qui ne soit pas l'interprétation d'un outil | intermédiaire |

C'est la seule entrée de cette section, et c'est un constat en soi : le catalogue amont
ne propose rien d'autre sur la modélisation de processus. La réingénierie — décortiquer
un processus, repérer les redondances, simplifier *avant* d'automatiser — est traitée
comme un apport propre de cet atlas dans [[notions/reingenierie-de-processus]] et
[[notions/bpmn]].

## Parties prenantes et conduite du changement

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| article | [Stakeholder Management Guide](https://simplystakeholders.com/resources/guides/stakeholder-management/) | le cadre classique — cartographie influence/intérêt, plan d'engagement. Généraliste, et **contenu d'un éditeur de logiciel** | débutant |
| article | [15 Rules for Negotiating a Job Offer](https://hbr.org/2014/04/15-rules-for-negotiating-a-job-offer) | rangé ici et non dans une rubrique carrière : c'est le meilleur texte court sur la négociation quand les deux parties doivent continuer à travailler ensemble après | débutant |
| officiel | [Roadmap Technical Writer](https://roadmap.sh/technical-writer) | le renvoi de l'amont pour la rédaction technique. Ce qui reste quand le FDE part est de la documentation, ou rien | débutant |

Voir [[notions/gestion-parties-prenantes]] et [[notions/conduite-du-changement]].

## Conformité et gouvernance côté mission

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| norme | [Règlement (UE) 2024/1689 — texte intégral](https://publications.europa.eu/resource/celex/32024R1689) | le règlement sur l'IA. À lire plutôt que les résumés, au moins pour la classification des systèmes | confirmé |
| norme | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | le cadre à utiliser pour structurer un dossier de conformité qui ne sera pas retoqué | intermédiaire |
| norme | [OWASP GenAI Security Project](https://genai.owasp.org/) | la check-list à passer avant toute revue de sécurité. C'est le référentiel que l'équipe sécurité du client connaît déjà | intermédiaire |
| norme | [Texte du RGPD](https://gdpr-info.eu/) | la source. Les résumés commerciaux se trompent systématiquement sur les bases légales | intermédiaire |
| officiel | [EU AI Act Explorer](https://artificialintelligenceact.eu/ai-act-explorer/) | le règlement navigable article par article. Un confort de lecture, pas une source de droit | intermédiaire |

Voir [[notions/gouvernance-ia]], [[notions/rgpd]] et [[notions/donnees-sensibles]].

> [!tip] Ajout 2026
> L'adresse officielle du règlement sur EUR-Lex, `eur-lex.europa.eu/eli/reg/2024/1689/oj`,
> est correcte mais protégée par un contrôle anti-robot : elle répond `202` avec un corps
> vide à tout ce qui n'est pas un navigateur. Elle fonctionne parfaitement pour un
> lecteur humain. L'adresse de l'Office des publications donnée ci-dessus sert le même
> texte et reste accessible aux outils — c'est celle à utiliser dans une chaîne
> automatisée. Les deux ont été vérifiées à la main le 16 septembre 2026.

## Le métier lui-même

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| article | [Forward deployed engineer is AI's hottest job](https://thenewstack.io/forward-deployed-engineer-fde-openai-google/) | The New Stack. Le panorama le plus sobre parmi les articles disponibles sur le rôle | débutant |
| officiel | [roadmap.sh — Forward Deployed Engineer](https://roadmap.sh/forward-deployed-engineer) | la roadmap d'origine. Vingt nœuds : utile pour voir ce que la source couvre, et surtout ce qu'elle ne couvre pas | débutant |

Le dossier complet est dans [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]].

## Écarté, et pourquoi

Cette section est plus longue que d'habitude, parce que le tri l'a été.

- **Les guides « complets » sur le FDE publiés par des éditeurs de logiciel
  d'onboarding client.** Le sujet sert de prétexte au produit ; on y apprend le
  vocabulaire du vendeur, pas le métier.
- **Les guides d'entretien vendus par leur auteur.** Il y en a dans l'amont, et ils ne
  sont pas sans valeur — mais un texte qui prépare à un entretien tout en vendant du
  coaching pour ce même entretien a un conflit d'intérêts qu'il faut signaler à chaque
  citation. Le dossier FDE en cite un en le disant ; cette page ne le reprend pas.
- **Les pages de calcul de retour sur investissement publiées par des vendeurs d'IA.**
  Les catégories de valeur y sont justes, la conclusion est écrite d'avance. Le sujet est
  traité en propre dans [[notions/roi-des-projets-ia]].
- **Les introductions sommaires à la gestion des flux de travail en entreprise**, qui
  n'apprennent rien à quelqu'un qui a déjà ouvert un ERP.
