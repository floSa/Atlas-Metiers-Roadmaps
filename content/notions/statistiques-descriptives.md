---
title: Statistiques descriptives
tags: [notion, statistiques, description, distribution, data]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst, bi-analyst]
---

Ensemble des mesures qui résument un jeu de données observé — position, dispersion, forme — sans prétendre généraliser à une population plus large.

## À quoi ça sert

Décrire avant d'expliquer. Avant tout test, tout modèle et toute conclusion, il faut savoir ce que la donnée contient réellement, par opposition à ce que le dictionnaire de données prétend. Quinze minutes de description font apparaître ce qu'aucune modélisation ne rattrapera : une colonne à moitié vide, une distribution bimodale qui trahit deux populations mélangées, des valeurs négatives dans un montant, une date en 1970 qui est un zéro mal converti.

Le second usage est la restitution. Une moyenne publiée sans dispersion est une information incomplète — le délai de livraison moyen de trois jours cache mal 20 % de livraisons à dix jours, et ce sont elles qui produisent les réclamations. Savoir quel résumé publier est un choix éditorial autant que statistique.

## Ce qu'il faut savoir

- **Position** : moyenne (sensible aux valeurs extrêmes), médiane (robuste, à préférer sur toute distribution asymétrique), mode (utile sur les variables catégorielles, souvent oublié).
- **Dispersion** : étendue, variance, écart-type, écart interquartile. L'écart-type parle dans l'unité de la variable ; l'écart interquartile résiste aux valeurs extrêmes. La dispersion est presque toujours l'information qui manque.
- **Forme** : asymétrie (le poids d'une queue de distribution) et aplatissement (la fréquence des valeurs extrêmes). Deux distributions de même moyenne et même écart-type peuvent se comporter très différemment.
- **Les quantiles sont plus parlants que les moments.** Médiane, 9e décile et maximum décrivent une distribution de délais mieux que moyenne et écart-type, et sont compris sans formation.
- **Toujours regarder la distribution, pas seulement ses résumés.** Un histogramme ou une boîte à moustaches révèle ce qu'aucun indicateur ne dit : bimodalité, effet de plancher, valeurs agglutinées sur un arrondi.
- **Les valeurs extrêmes ne sont pas des erreurs par défaut.** Écarter les 1 % supérieurs d'un chiffre d'affaires revient à écarter les plus gros clients. Décider au cas par cas, et le documenter.
- **Le quartet d'Anscombe et le datasaurus** restent la meilleure démonstration du sujet : des jeux aux statistiques identiques et aux formes radicalement différentes.

## Selon le métier

### Data Analyst

Le contenu statistique de l'exploration. Ce qui est propre à l'analyste, c'est **l'ordre dans lequel on regarde** : d'abord le volume et la période, ensuite le taux de valeurs absentes par colonne, puis la distribution des variables clés, enfin les croisements. L'exploration sert à vérifier que les données supportent la question et à produire les hypothèses à tester — pas à trouver la réponse. Si une exploration livre directement la conclusion, on a généralement regardé jusqu'à ce qu'elle apparaisse.

### BI Analyst

L'angle est la publication. Un indicateur affiché sans dispersion ni référence de comparaison fabrique de la réaction là où il n'y a rien à décider. Sur toute distribution asymétrique — délais, paniers, durées de traitement — publier la médiane et un quantile haut plutôt que la moyenne seule, et indiquer ce qu'est la variation habituelle.

> [!warning] Piège
> Publier une variation sans indiquer si elle sort du bruit habituel. « Les ventes ont baissé de 4 % » ne veut rien dire tant qu'on ne sait pas que la variation hebdomadaire courante est de plus ou moins 6 %. Un tableau de bord couvert de flèches vertes et rouges sur des variations non significatives finit par être ignoré — y compris le jour où la variation compte vraiment.

## Pour aller plus loin

- [Descriptive Statistics — Definitions, Types, Examples (Scribbr)](https://www.scribbr.com/statistics/descriptive-statistics/) — le cours d'entrée, propre et complet.
- [Measures of central tendency — Australian Bureau of Statistics](https://www.abs.gov.au/statistics/understanding-statistics/statistical-terms-and-concepts/measures-central-tendency) — quand utiliser moyenne, médiane ou mode, par un institut statistique.
- [What is dispersion? — Investopedia](https://www.investopedia.com/terms/d/dispersion.asp) — le versant dispersion, avec les usages financiers.

## Appelée par

- [[parcours/data-analyst|Data Analyst]]
- [[parcours/bi-analyst/index|BI Analyst]]

Voisines : [[notions/visualisation-de-donnees]], [[notions/tests-hypotheses]], [[notions/qualite-des-donnees]], [[notions/series-temporelles]].
