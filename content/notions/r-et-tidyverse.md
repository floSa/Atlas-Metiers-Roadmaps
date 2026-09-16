---
title: R et le tidyverse
tags: [notion, r, tidyverse, dplyr, ggplot2, statistiques]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst, bi-analyst]
---

Langage conçu pour la statistique, et l'ensemble cohérent de bibliothèques — dplyr, tidyr, ggplot2 — qui en font un outil d'analyse de données à part entière.

## À quoi ça sert

R n'est pas un langage généraliste dans lequel on a ajouté des statistiques : il a été conçu pour elles, et cela se voit à deux endroits. La **modélisation statistique** y est native — modèles linéaires et mixtes, séries temporelles, tests, diagnostics, sorties lisibles par un statisticien — là où l'écosystème Python la traite comme une bibliothèque parmi d'autres. Et **ggplot2** implémente une grammaire des graphiques cohérente qui reste, après quinze ans, ce qui se fait de mieux pour produire un graphique juste sans négocier avec l'outil.

Le tidyverse a ajouté ce qui manquait : un enchaînement de verbes lisible, `filter`, `mutate`, `group_by`, `summarise`, reliés par un opérateur de pipeline. Un script dplyr se lit à voix haute, ce qui en fait un bon support de discussion avec quelqu'un qui ne code pas.

## Ce qu'il faut savoir

- **dplyr** pour la manipulation, **tidyr** pour le passage large/long, **ggplot2** pour les graphiques, **readr** pour l'import, **purrr** pour l'itération fonctionnelle. Les cinq forment le socle.
- **Le format long ("tidy")** — une observation par ligne, une variable par colonne — est ce qui rend l'enchaînement et la visualisation naturels. La moitié du travail d'un script R est d'y amener les données.
- **ggplot2 repose sur une grammaire** : des données, une correspondance entre variables et propriétés visuelles, des géométries, des échelles, des facettes. Une fois comprise, elle produit des graphiques corrects par construction.
- **Les formules** (`y ~ x + z`) sont un objet de première classe : la même écriture sert au test, au modèle linéaire et au graphique.
- **R Markdown et Quarto** produisent un document reproductible mêlant code, résultat et texte. C'est un avantage réel pour un livrable d'analyse destiné à être relu.
- **Ce qui manque** : l'interfaçage avec un système d'information et la mise en production. Un modèle R s'industrialise mal en dehors de contextes qui y sont déjà préparés.
- **Choisir un langage et aller au fond.** Python si l'on doit s'interfacer avec le reste du système d'information, R si l'environnement est statistique ou académique. Savoir bricoler dans les deux ne vaut rien ; maîtriser un des deux vaut beaucoup.

## Selon le métier

### Data Analyst

Le choix entre R et Python se fait sur l'environnement, pas sur les mérites du langage. Pour le nettoyage, dplyr et pandas se valent ; la règle d'écriture compte plus que l'outil — un script rejouable depuis la donnée brute, dans les deux cas.

### BI Analyst

R reste utile pour ce que SQL fait mal : appeler une API, lire un format exotique, calculer une prévision. Dans la chaîne de transformation, préférer le SQL pour tout ce qu'il sait faire, parce qu'il est testable, lisible par l'équipe métier et exécuté par l'entrepôt. R intervient en bout de chaîne, sur l'analyse ponctuelle.

> [!warning] Piège
> Traduire du pandas en dplyr ligne à ligne. Les deux ont des modèles différents — évaluation non standard des noms de colonnes, format long par défaut, recyclage des vecteurs — et le code obtenu est illisible dans les deux cultures. Apprendre les verbes du tidyverse pour eux-mêmes prend deux jours et évite des mois de code hybride.

## Pour aller plus loin

- [dplyr — documentation](https://dplyr.tidyverse.org/) — les verbes de manipulation, avec des exemples courts.
- [ggplot2 — site officiel](https://ggplot2.tidyverse.org/) — la grammaire des graphiques et sa référence complète.
- [Exploratory Data Analysis with dplyr](https://www.gastonsanchez.com/intro2cwd/eda-dplyr.html) — une exploration complète menée bout en bout.

## Appelée par

- [[parcours/data-analyst/index|Data Analyst]]
- [[parcours/bi-analyst/index|BI Analyst]]

Voisines : [[notions/python-pour-la-data]], [[notions/pandas]], [[notions/visualisation-de-donnees]].
