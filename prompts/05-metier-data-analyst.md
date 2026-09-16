# 05 — Métier : Data Analyst

Lis d'abord `PROJET.md` puis `prompts/_commun.md`. Tu es le chantier
**05 — Métier : Data Analyst**.

## Zone d'écriture exclusive

`content/parcours/data-analyst.md`. Un seul fichier.

## Source

`data/extract/data-analyst.md` — 99 nœuds documentés, 192 ressources.
Amont : `roadmap.sh/data-analyst`, dernière modification 4 septembre 2026.

## Le partage avec le chantier 06 — lis ceci avant d'écrire

L'analyse du corpus a mesuré le recouvrement : **Data Analyst et BI Analyst partagent
une quarantaine de nœuds identiques** — statistiques descriptives, tests d'hypothèses,
corrélation, SQL, visualisation, Pandas, outils décisionnels. C'est de loin le plus
gros risque de doublon du lot.

Le chantier 06 travaille en parallèle sur BI Analyst. La répartition est la suivante,
et elle n'est pas négociable unilatéralement :

| Sujet | Qui le traite en propre |
|---|---|
| Statistiques, tests, corrélation, régression | **notion mutualisée** — aucun des deux ne l'explique |
| SQL, Pandas, tableur, visualisation | **notion mutualisée** — aucun des deux ne l'explique |
| Exploration, nettoyage, analyse ad hoc, restitution d'un résultat | **toi** |
| Entrepôt, modélisation dimensionnelle, dbt, sémantique, gouvernance | **06** |

Autrement dit : tu es le parcours de **celui qui répond à une question avec des
données**. Le 06 est celui qui **construit l'infrastructure décisionnelle** dont
d'autres se serviront. Écris ta note depuis cet angle, et pour tout le reste, pose le
lien vers le slug canonique.

Si tu constates que la frontière est mal placée sur un sujet précis, ne la déplace pas
tout seul : signale-le dans **Points ouverts**, le pilote arbitrera.

## Ce qui compte particulièrement

- **Ce qui sépare vraiment le Data Analyst du Data Scientist**, au-delà du titre. La
  note `content/roadmaps/02 - Roadmap — AI and Data Scientist.md` existe : positionne
  les deux explicitement.
- **La question avant la donnée.** L'amont est très outil ; le métier est d'abord de
  reformuler une question floue en quelque chose de mesurable.
- **Ce que l'IA générative a changé au métier depuis un an** — et ce qu'elle n'a pas
  changé. L'amont n'en dit presque rien. C'est un `Ajout 2026` important.
- **Corrélation et causalité.** Le piège structurant du métier.

## Slugs canoniques à utiliser

`statistiques-descriptives`, `tests-hypotheses`, `analyse-correlation`,
`regression-logistique`, `metriques-evaluation-ml`, `apprentissage-supervise`,
`apprentissage-non-supervise`, `apprentissage-par-renforcement`, `reseaux-de-neurones`,
`traitement-langage-naturel`, `sql`, `pandas`, `python-pour-la-data`, `r-et-tidyverse`,
`visualisation-de-donnees`, `outils-decisionnels`, `tableur`, `qualite-des-donnees`.
