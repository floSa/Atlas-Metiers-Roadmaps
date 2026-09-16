---
title: Séries temporelles
tags: [notion, series-temporelles, saisonnalite, prevision, calendrier]
date: 2026-09-16
statut: actif
appelee-par: [bi-analyst, data-analyst]
---

Suites de valeurs indexées par le temps, dont l'analyse consiste d'abord à séparer ce qui relève de la tendance de fond, de la récurrence saisonnière et du résidu.

## À quoi ça sert

L'essentiel des « alertes » d'un tableau de bord sont de la saisonnalité mal interprétée. Séparer les trois composantes permet de répondre à la seule question qui compte devant une variation : **est-ce que cela sort de ce qui se passe habituellement à cette période ?**

Une règle simple élimine une grande partie des faux signaux : un indicateur d'exploitation se compare à la même période de l'année précédente, pas au mois précédent. Comparer décembre à novembre mesure principalement le calendrier.

Le second usage est la prévision, et son intérêt réel est souvent modeste. Ce qui est utile n'est pas le modèle mais la référence : savoir de combien on se trompe habituellement dit s'il y a lieu de réagir aujourd'hui.

## Ce qu'il faut savoir

- **Trois composantes** : tendance de fond, saisonnalité récurrente, résidu. La décomposition est le premier geste, avant tout modèle.
- **Plusieurs saisonnalités coexistent** : hebdomadaire (jour de la semaine), mensuelle, annuelle. Une série d'activité en porte souvent deux ou trois simultanément.
- **Les effets de calendrier expliquent beaucoup** de ce qu'on attribue à une action commerciale : nombre de jours ouvrés, position des jours fériés, décalage des semaines d'une année sur l'autre, Pâques mobile. Ils sont portés par la dimension de date, ce qui est la raison pour laquelle elle mérite une vraie table — voir [[notions/modelisation-dimensionnelle]].
- **La référence à battre est toujours la prévision naïve** : la même valeur que la même période l'an dernier, ou la dernière valeur connue. Publier l'erreur de sa prévision **contre cette référence** ; beaucoup de modèles sophistiqués ne la battent pas, et le savoir évite de porter une dette de maintenance pour rien.
- **Les modèles usuels**, par ordre de complexité : moyennes mobiles, lissage exponentiel, décomposition saisonnière, modèles à composantes, et méthodes d'apprentissage sur données tabulaires enrichies de variables de calendrier. Commencer par le plus simple qui batte la référence.
- **La validation est chronologique.** Un découpage aléatoire entraîne sur le futur et évalue sur le passé, ce qui produit des scores magnifiques et faux.
- **Les ruptures structurelles** — changement de périmètre, migration d'outil, changement de définition — invalident l'historique. Les repérer avant de modéliser, et documenter la date de rupture.
- **Publier un intervalle, pas un point.** Une prévision sans incertitude sera lue comme un engagement.

## Selon le métier

### BI Analyst

Le déplacement propre au métier : là où un analyste calcule une analyse, lui la **modélise pour qu'elle se recalcule seule**. Cela passe par trois objets concrets — la dimension de date, les définitions de fenêtre, et les mesures de variation inscrites dans la couche sémantique. La prévision qui sert vraiment en BI est celle des séries d'activité, pas un modèle de classification.

### Data Analyst

L'angle est diagnostique plutôt que prédictif : décomposer avant de conclure, et vérifier qu'une variation n'est pas un effet de calendrier avant de chercher une cause métier. C'est aussi le domaine où l'erreur de validation chronologique est la plus fréquente et la plus difficile à repérer après coup.

> [!warning] Piège
> Publier une variation sans indiquer si elle sort du bruit habituel. « Les ventes ont baissé de 4 % » ne veut rien dire tant qu'on ne sait pas que la variation hebdomadaire courante est de plus ou moins 6 %. Un tableau de bord qui affiche des flèches sur des variations non significatives fabrique de la réaction là où il n'y a rien à décider, et finit par être ignoré — y compris le jour où la variation compte vraiment.

## Pour aller plus loin

- [Introduction to Time Series Analysis — NIST](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm) — la référence méthodologique, rigoureuse et gratuite.
- [Time Series Analysis: Definition, Types & Techniques — Tableau](https://www.tableau.com/analytics/what-is-time-series-analysis) — l'entrée en matière, orientée usage décisionnel.
- [Forecasting: Principles and Practice](https://otexts.com/fpp3/) — l'ouvrage de référence en libre accès sur la prévision et son évaluation.

## Appelée par

- [[parcours/bi-analyst|BI Analyst]]
- [[parcours/data-analyst/index|Data Analyst]]

Voisines : [[notions/analyse-de-cohorte]], [[notions/statistiques-descriptives]], [[notions/modelisation-dimensionnelle]], [[notions/visualisation-de-donnees]].
