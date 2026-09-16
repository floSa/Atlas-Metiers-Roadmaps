---
title: Outils décisionnels
tags: [notion, bi, power-bi, tableau, looker, restitution]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst, bi-analyst]
---

Plateformes qui connectent des sources de données, portent des définitions de mesures et publient des tableaux de bord partagés — Power BI, Tableau, Looker et leurs concurrents.

## À quoi ça sert

Ce qu'on achète n'est pas la capacité à faire un graphique : n'importe quelle bibliothèque en fait de meilleurs. On achète la **distribution** — un chiffre calculé une fois, rafraîchi automatiquement, visible par deux cents personnes avec les bons droits, et identique pour tout le monde. C'est la partie qu'un notebook ne fait pas et qu'une organisation ne sait pas faire autrement.

La conséquence est que le choix d'un outil est une décision d'entreprise, pas une préférence personnelle. Il engage un modèle de licence, un mode d'authentification, une façon d'écrire les mesures et une manière de gouverner qui publie quoi. On en change rarement, et jamais sans coût.

## Ce qu'il faut savoir

- **Power BI** — intégration étroite à l'écosystème Microsoft, coût d'entrée bas, langage de mesure DAX puissant et rebutant. La question à instruire est la capacité de service et le mode de licence, qui gouvernent la facture bien plus que le nombre d'utilisateurs affiché.
- **Tableau** — la meilleure expérience d'exploration visuelle, forte culture de conception, coût par utilisateur élevé. À son avantage quand des analystes explorent ; moins pertinent pour distribuer des rapports figés à grande échelle.
- **Looker** — la modélisation est centrale et versionnée dans un dépôt, ce qui en fait l'outil le plus proche des pratiques de développement. L'investissement initial de modélisation est réel et se rentabilise sur la durée.
- **Le vrai critère n'est pas la fonctionnalité** mais la couche de définitions : où vivent les mesures, qui peut les écrire, comment elles sont testées et versionnées. Un outil qui laisse chacun redéfinir le chiffre d'affaires dans son rapport reproduira le problème qu'il devait résoudre.
- **Le mode de connexion compte** : import dans le moteur de l'outil (rapide, décalé, volumineux) ou requête directe sur l'entrepôt (frais, dépendant de la performance et du coût de l'entrepôt). Ce choix détermine l'expérience utilisateur autant que la conception.
- **Les droits d'accès par ligne** sont une fonctionnalité de sécurité qui se teste comme telle. Elle est souvent configurée une fois et jamais vérifiée.
- **Le cycle de vie manque presque toujours** : environnements séparés, revue avant publication, retrait des rapports morts. Un espace non gouverné accumule des centaines de rapports dont personne ne connaît la justesse.
- **L'analyse embarquée** — publier un tableau de bord dans un produit — est un modèle de licence différent, à instruire à part.

## Selon le métier

### Data Analyst

L'analyste les consomme et y publie parfois ; les construire et les gouverner relève du BI Analyst. Ce qu'il faut savoir faire : lire un rapport existant pour comprendre d'où vient un chiffre, et publier une analyse ponctuelle sans créer une définition concurrente de celles qui existent déjà.

### BI Analyst

Un outil maîtrisé en profondeur vaut mieux que trois survolés — c'est vrai des offres d'emploi comme du travail réel. L'angle propre au métier est la maintenance : on juge le BI Analyst sur l'esthétique de ses tableaux de bord et on ne finance jamais leur entretien. Prévoir dès la conception le coût du rafraîchissement, de la correction et du retrait.

> [!warning] Piège
> Traiter l'outil décisionnel comme une couche de transformation. Il est tentant de nettoyer, joindre et corriger directement dans le rapport, parce que c'est immédiat. Six mois plus tard, la logique métier est éparpillée dans quarante rapports, invisible, non testée et non réutilisable. La transformation appartient à l'entrepôt ; l'outil restitue.

## Pour aller plus loin

- [Business intelligence: A complete overview — Tableau](https://www.tableau.com/business-intelligence/what-is-business-intelligence) — le cadrage du domaine, par un éditeur mais honnête sur les principes.
- [Power BI Community](https://community.fabric.microsoft.com/t5/Power-BI-forums/ct-p/powerbi) — où se règlent les problèmes réels de DAX et de modèle.
- [Tableau Community](https://community.tableau.com/s/) — l'équivalent côté Tableau.

## Appelée par

- [[parcours/data-analyst/index|Data Analyst]]
- [[parcours/bi-analyst|BI Analyst]]

Voisines : [[notions/visualisation-de-donnees]], [[notions/modelisation-dimensionnelle]], [[notions/entrepot-de-donnees]], [[notions/tableur]].
