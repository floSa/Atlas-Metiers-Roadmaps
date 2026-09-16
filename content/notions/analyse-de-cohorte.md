---
tags: [notion, cohorte, retention, composition, analyse]
date: 2026-09-16
statut: actif
appelee-par: [bi-analyst, data-analyst]
---

# Analyse de cohorte

Méthode qui regroupe les individus par période d'entrée puis suit leur comportement dans le temps, de manière à comparer des groupes ayant le même âge plutôt que la même date.

## À quoi ça sert

C'est le seul moyen simple de distinguer une amélioration réelle d'un **effet de composition**. Un taux de rétention global qui monte parce que le recrutement a ralenti n'est pas une amélioration : la population a vieilli, et les anciens restent plus que les nouveaux. L'indicateur agrégé bouge, le comportement n'a pas changé.

Le second usage est le diagnostic dans le temps : en comparant des cohortes successives au même âge, on voit si ce qui a été changé en mars a produit un effet — les entrants d'avril se comportent-ils différemment de ceux de février au même stade.

Le troisième est la projection : une cohorte suivie sur six mois donne une base pour estimer ce que vaudra une cohorte nouvelle, à condition d'assumer que le contexte n'a pas changé.

## Ce qu'il faut savoir

- **La définition de la cohorte est une décision métier** : quel événement fait entrer (première visite, premier achat, signature), et quelle fenêtre d'observation. Elle a donc un propriétaire, et elle se documente.
- **Comparer à âge égal**, pas à date égale. C'est toute l'astuce : l'axe horizontal est le nombre de périodes depuis l'entrée, pas le calendrier.
- **Les cohortes récentes sont incomplètes.** Une cohorte entrée il y a deux mois n'a pas de valeur à six mois ; l'afficher comme un zéro ou l'inclure dans une moyenne fabrique une fausse dégradation.
- **La taille compte** : une cohorte de trente personnes produit des courbes spectaculaires et non significatives. Regrouper les périodes quand les effectifs sont faibles.
- **Le tableau triangulaire** — cohortes en lignes, âge en colonnes — est la forme de restitution standard, et il se lit en diagonale pour retrouver le calendrier.
- **La rétention n'est pas la seule mesure** : chiffre d'affaires cumulé par cohorte, fréquence d'usage, taux de passage à une étape. La méthode s'applique à toute mesure qui évolue avec l'ancienneté.
- **Segmenter les cohortes par canal d'acquisition** est souvent plus instructif que la cohorte temporelle seule : deux canaux produisent des courbes de rétention très différentes, et leur mélange masque les deux.
- **Une cohorte n'établit pas de causalité.** Un changement de comportement entre deux cohortes peut venir de ce qui a été modifié, ou de qui a été recruté. Voir [[notions/ab-testing]] quand la question porte sur l'effet d'une action.

## Selon le métier

### BI Analyst

Une analyse de cohorte produite une fois dans un carnet est une réponse ; la même analyse adossée à une définition de cohorte dans la couche sémantique est un indicateur que le métier suivra tous les mois sans le redemander. C'est la différence entre répondre et outiller, et elle repose sur trois objets : la dimension de date, la définition de cohorte et de fenêtre, et les mesures de variation.

### Data Analyst

L'usage est diagnostique et ponctuel : c'est l'outil à sortir dès qu'un indicateur agrégé bouge sans explication, parce que l'effet de composition est la première hypothèse à écarter. Le réflexe utile est de produire la vue par cohorte **avant** de chercher une cause métier à une variation globale.

> [!warning] Piège
> Comparer des cohortes de tailles très différentes sans le dire. Une campagne d'acquisition massive produit une cohorte énorme et moins engagée ; sa courbe de rétention plus basse n'indique pas une dégradation du produit mais un changement de recrutement. Afficher l'effectif de chaque cohorte à côté de sa courbe suffit à éviter la conclusion inverse.

## Pour aller plus loin

- [Cohort analysis — Wikipédia](https://en.wikipedia.org/wiki/Cohort_analysis) — la définition et les variantes.
- [Understanding Cohort Analysis: A Comprehensive Guide](https://hevodata.com/learn/understanding-cohort-analysis-a-guide/) — la mise en œuvre, avec les formes de tableau.
- [What is a Funnel Chart? — Atlassian](https://www.atlassian.com/data/charts/funnel-chart-complete-guide) — la restitution complémentaire, quand la question porte sur les étapes plutôt que sur le temps.

## Appelée par

- [[parcours/bi-analyst|BI Analyst]]
- [[parcours/data-analyst|Data Analyst]]

Voisines : [[notions/series-temporelles]], [[notions/mesure-d-usage-produit]], [[notions/ab-testing]], [[notions/apprentissage-non-supervise]].
