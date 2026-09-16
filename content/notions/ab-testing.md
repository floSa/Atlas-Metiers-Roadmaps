---
title: Test A/B
tags: [notion, experimentation, ab-testing, causalite, protocole]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst, bi-analyst, ai-product-builder]
---

Protocole expérimental qui affecte au hasard deux versions d'un traitement à deux groupes comparables, de manière à attribuer l'écart observé à la version et non aux différences entre les groupes.

## À quoi ça sert

C'est la seule méthode simple qui donne accès à la causalité. Toute analyse observationnelle bute sur la même question — les gens qui ont vu la nouvelle version sont-ils comparables à ceux qui ont vu l'ancienne ? — et la randomisation la ferme par construction : en moyenne, les deux groupes se ressemblent sur tout, y compris sur ce qu'on n'a pas mesuré.

Son second apport est organisationnel. Un protocole fixé à l'avance — métrique, effectif, durée, règle d'arrêt — retire à la discussion la possibilité de choisir le résultat après coup. C'est souvent sa contribution la plus utile en entreprise, avant même la statistique.

## Ce qu'il faut savoir

- **Une métrique primaire, décidée avant.** Une seule. Les autres sont des métriques de surveillance, qui servent à détecter les dégâts collatéraux, pas à déclarer la victoire.
- **Effectif et durée se calculent avant** à partir de l'effet minimal qu'on juge intéressant. Un test lancé sans calcul de puissance ne conclura ni dans un sens ni dans l'autre.
- **Durée minimale d'un cycle complet.** Le comportement varie selon le jour de la semaine ; arrêter après trois jours mesure trois jours, pas le régime permanent.
- **Ne pas regarder en continu et arrêter quand ça arrange.** C'est la façon la plus répandue de fabriquer un faux positif. Soit on fixe la règle d'arrêt, soit on utilise une méthode séquentielle prévue pour cela.
- **Randomisation au bon niveau** : l'utilisateur, pas la session, sinon la même personne voit les deux versions. Quand il existe des effets d'entraînement entre utilisateurs, randomiser par groupe ou par zone.
- **Les métriques de ratio demandent de la prudence** : le dénominateur peut lui-même être affecté par le traitement, ce qui rend la variation ininterprétable.
- **Vérifier l'équilibre des groupes** avant d'interpréter. Un écart d'effectif inattendu signale un défaut d'affectation, et invalide le test.
- **La significativité n'est pas la décision.** Un gain significatif de 0,2 % qui coûte trois mois de maintenance est un résultat négatif. La décision se prend sur l'effet et son coût, pas sur la p-value.

## Selon le métier

### Data Analyst

Quand la question porte sur l'effet d'une action qu'on contrôle, le protocole expérimental est la seule réponse propre — c'est ce qui distingue une analyse causale d'une histoire bien racontée. L'analyste est souvent celui qui doit dire que le test n'a pas été conçu pour répondre à la question qu'on lui pose maintenant.

### BI Analyst

Le BI Analyst est rarement celui qui conçoit le test, souvent celui qui produit la mesure sur laquelle il sera tranché. Ce qui compte de son côté : la métrique de décision est définie **avant** le début du test, une seule métrique primaire, et pas de relecture quotidienne avec arrêt dès que l'écart est favorable. Une définition de mesure stable dans la couche sémantique est ce qui empêche la redéfinition opportuniste à l'arrivée des résultats.

> [!warning] Piège
> Conclure d'un test non significatif que les deux versions sont équivalentes. Ne pas rejeter l'hypothèse nulle signifie manquer de preuve, souvent parce que l'effectif était insuffisant. Pour affirmer une équivalence, il faut un test conçu pour cela et une borne d'équivalence définie à l'avance.

## Pour aller plus loin

- [A Refresher on A/B Testing — Harvard Business Review](https://hbr.org/2017/06/a-refresher-on-ab-testing) — le cadrage décisionnel, court et solide.
- [A software engineer's guide to A/B testing — PostHog](https://posthog.com/product-engineers/ab-testing-guide-for-engineers) — le versant implémentation, avec les pièges d'affectation.
- [A/B testing — Wikipédia](https://en.wikipedia.org/wiki/A/B_testing) — les variantes et les références académiques.

## Appelée par

- [[parcours/data-analyst/index|Data Analyst]]
- [[parcours/bi-analyst/index|BI Analyst]]
- [[parcours/ai-product-builder/index|AI Product Builder]]

Voisines : [[notions/tests-hypotheses]], [[notions/analyse-correlation]], [[notions/mesure-d-usage-produit]].
