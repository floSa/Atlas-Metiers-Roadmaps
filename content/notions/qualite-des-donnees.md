---
title: Qualité des données
tags: [notion, qualite-des-donnees, gouvernance, data, nettoyage]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-red-teaming, data-analyst, bi-analyst]
---

Ensemble des propriétés mesurables qui déterminent si une donnée peut porter la décision qu'on lui demande de porter — et des tests qui vérifient ces propriétés en continu plutôt qu'à la découverte d'un écart.

## À quoi ça sert

La qualité des données n'est pas un idéal, c'est un seuil relatif à un usage. La même table peut être excellente pour un ordre de grandeur et inutilisable pour une facturation. Poser la question sous la forme « ces données sont-elles bonnes ? » ne mène nulle part ; la poser sous la forme « quelle propriété doit tenir pour que ce chiffre soit défendable ? » donne une liste de tests exécutables.

L'intérêt réel est de déplacer le moment de la découverte. Sans tests, un défaut de qualité se découvre en réunion, par quelqu'un qui connaît le métier et voit un chiffre impossible — au pire moment, avec le maximum de dégâts sur la confiance. Avec des tests, il se découvre à l'exécution du flux, par une alerte, avant publication.

Une donnée d'entreprise porte l'histoire de ses systèmes : une migration qui a laissé deux conventions de statut, un champ libre rempli par vingt commerciaux avec vingt orthographes, une réplication qui duplique certaines lignes. Nettoyer n'est pas appliquer une recette, c'est comprendre pourquoi la donnée est dans cet état, puis décider — en le documentant — ce qu'on en fait.

## Ce qu'il faut savoir

- **Les dimensions usuelles** : complétude (les champs attendus sont remplis), unicité (pas de doublon sur la clé), validité (la valeur appartient au domaine autorisé), cohérence (les tables se recoupent), fraîcheur (la donnée date de moins de X), exactitude (elle correspond au réel — la seule qui ne se teste pas sans référence externe).
- **Un test de qualité est du code**, versionné, exécuté à chaque passage du flux, avec un seuil et une conduite à tenir en cas d'échec : bloquer la publication, ou alerter et laisser passer. Choisir lequel est une décision métier.
- **Le contrôle de volume** est le test le moins cher et le plus rentable : un nombre de lignes qui s'écarte de son historique signale une jointure fautive, un filtre implicite ou un droit d'accès partiel bien avant que quiconque regarde le contenu.
- **La distinction défaut / caractéristique** : une valeur absente peut être une erreur de saisie ou une information (« pas de date de résiliation » signifie « client actif »). Les confondre fabrique des faux positifs et des corrections destructrices.
- **Corriger à la source ou en aval** : corriger en aval est plus rapide et crée une divergence permanente entre les systèmes. Le faire est parfois la seule option, mais cela se documente comme une dette, avec la règle appliquée et son propriétaire.
- **Le profilage** précède le nettoyage : distribution de chaque colonne, valeurs distinctes, taux de nulls, valeurs extrêmes, longueur des chaînes. Dix minutes de profilage évitent des heures de correction mal ciblée.
- **Le nettoyage est un script rejouable depuis la donnée brute**, jamais une suite de corrections manuelles sur une copie. C'est la règle qui distingue un résultat reproductible d'une anecdote.

## Selon le métier

### Forward Deployed Engineer

Le diagnostic qualité est un livrable de la phase d'audit, et souvent le premier résultat qui impressionne le client — avant toute IA. Il a aussi une fonction politique : il déplace la discussion de « votre IA se trompe » vers « votre référentiel produit contient trois orthographes du même fournisseur », ce qui est vérifiable et corrigeable.

### AI Red Teaming

La qualité des données est la parade au piège empoisonné, et elle agit en amont. L'empoisonnement — introduire des données manipulées dans un corpus d'entraînement, d'affinage ou d'index pour dégrader la justesse ou installer une porte dérobée — se traite par la validation et la traçabilité des données entrantes, pas par un contrôle du modèle en aval. La question à poser est toujours la provenance : corpus collecté sur le web, contributions utilisateurs, jeu de données public repris tel quel.

### Data Analyst

L'analyste nettoie **pour une question précise**, et il n'a ni le mandat ni les moyens de corriger la source. Cela change tout : la règle appliquée est locale, documentée dans le script, et n'engage pas l'entreprise.

C'est aussi ici que se traitent les **données manquantes**, qui n'ont pas de notion propre parce qu'elles n'ont de sens qu'à l'intérieur de celle-ci. Trois mécanismes, et ils n'appellent pas la même réponse :

- **MCAR** — l'absence est indépendante de tout. Rare en entreprise. Supprimer les lignes concernées ne biaise que la puissance statistique.
- **MAR** — l'absence dépend d'autres variables observées : le revenu est plus souvent absent chez les jeunes répondants. L'imputation conditionnée sur ces variables est légitime.
- **MNAR** — l'absence dépend de la valeur elle-même : les hauts revenus ne répondent pas. Aucune imputation ne répare cela, et toute analyse qui l'ignore est biaisée dans une direction connue. Le dire vaut mieux que le combler.

La règle de terrain : quand l'absence porte de l'information métier, en faire une **modalité explicite** (« non renseigné ») plutôt qu'une imputation. On perd en élégance statistique et on gagne en honnêteté du résultat.

### BI Analyst

L'angle est celui de la charge de la preuve. Un chiffre défendable est un chiffre dont on peut dire, en réunion et sans préparation, d'où il vient, ce qu'il inclut, quand il a été calculé et ce qui se passerait s'il était faux. Les tests de qualité sont ce qui permet de répondre à la quatrième question sans hausser le ton.

> [!warning] Piège
> Nettoyer avant de comprendre. Supprimer les doublons, remplacer les nulls par zéro et écarter les valeurs extrêmes donne un jeu propre et un résultat faux : les doublons venaient d'une jointure, les nulls signifiaient « en cours » et les valeurs extrêmes étaient les gros clients. Le profilage vient avant le nettoyage, toujours.

## Pour aller plus loin

- [What Is Data Quality? — IBM](https://www.ibm.com/think/topics/data-quality) — le cadre des dimensions, court et clair.
- [What is data cleaning? — Tableau](https://www.tableau.com/learn/articles/what-is-data-cleaning) — le versant pratique du nettoyage.
- [Missing data — Wikipédia](https://en.wikipedia.org/wiki/Missing_data) — MCAR, MAR, MNAR et les méthodes d'imputation, avec les références statistiques.
- [Building a Robust Data Observability Framework](https://towardsdatascience.com/building-a-robust-data-observability-framework-to-ensure-data-quality-and-integrity-07ff6cffdf69/) — quand la qualité devient une supervision continue plutôt qu'un contrôle ponctuel.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]
- [[parcours/ai-red-teaming/index|AI Red Teaming]]
- [[parcours/data-analyst|Data Analyst]]
- [[parcours/bi-analyst|BI Analyst]]

Voisines : [[notions/lignage-des-donnees]], [[notions/collecte-de-donnees]], [[notions/transformation-dbt]], [[notions/statistiques-descriptives]].
