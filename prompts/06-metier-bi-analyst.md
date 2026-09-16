# 06 — Métier : BI Analyst

Lis d'abord `PROJET.md` puis `prompts/_commun.md`. Tu es le chantier
**06 — Métier : BI Analyst**.

## Zone d'écriture exclusive

`content/parcours/bi-analyst.md`. Un seul fichier.

## Source

`data/extract/bi-analyst.md` — **200 nœuds documentés**, 275 ressources. C'est la
roadmap la plus volumineuse du lot, et de loin.

Amont : `roadmap.sh/bi-analyst`, dernière modification 4 septembre 2026.

## Le partage avec le chantier 05 — lis ceci avant d'écrire

L'analyse du corpus a mesuré le recouvrement : **BI Analyst et Data Analyst partagent
une quarantaine de nœuds identiques**. C'est le plus gros risque de doublon du lot.

Le chantier 05 travaille en parallèle sur Data Analyst. La répartition est la suivante,
et elle n'est pas négociable unilatéralement :

| Sujet | Qui le traite en propre |
|---|---|
| Statistiques, tests, corrélation, régression | **notion mutualisée** — aucun des deux ne l'explique |
| SQL, Pandas, tableur, visualisation | **notion mutualisée** — aucun des deux ne l'explique |
| Exploration, nettoyage, analyse ad hoc, restitution d'un résultat | **05** |
| Entrepôt, modélisation dimensionnelle, dbt, sémantique, gouvernance | **toi** |

Tu es le parcours de celui qui **construit l'infrastructure décisionnelle** dont
d'autres se serviront : modèles, couche sémantique, définitions partagées, qualité,
lignage. Le 05 est celui qui répond à une question ponctuelle.

Si la frontière te paraît mal placée sur un sujet précis, ne la déplace pas seul :
signale-le dans **Points ouverts**.

## Attention au volume

200 nœuds, c'est plus que ce qu'une note lisible peut absorber sans devenir un annuaire.
L'amont énumère beaucoup de produits interchangeables — bases, outils de restitution,
formats. **Regroupe par catégorie et traite la catégorie**, en citant les produits comme
exemples. Une note dense de trente pages vaut mieux qu'un catalogue de cent.

Si tu juges qu'un découpage en plusieurs fichiers est nécessaire, tu peux créer
`content/parcours/bi-analyst/` avec un `index.md` — mais argumente-le dans ta synthèse.

## Ce qui compte particulièrement

- **La couche sémantique et les définitions partagées.** Ce qui fait qu'un même
  indicateur ne vaut pas trois choses différentes selon le service. C'est le vrai
  travail du métier, et l'amont le sous-traite.
- **La frontière avec le Data Engineer.** La note
  `content/roadmaps/03 - Roadmap — Data Engineer.md` existe : positionne explicitement.
- **La gouvernance et le lignage**, pas comme de la conformité mais comme ce qui rend un
  chiffre défendable en réunion.
- **Ce que la BI conversationnelle a changé** — et ce qu'elle casse quand la couche
  sémantique est mauvaise. `Ajout 2026`.

## Slugs canoniques à utiliser

`entrepot-de-donnees`, `data-lake`, `modelisation-dimensionnelle`, `transformation-dbt`,
`orchestration-de-flux`, `qualite-des-donnees`, `lignage-des-donnees`, `sql`, `pandas`,
`r-et-tidyverse`, `visualisation-de-donnees`, `outils-decisionnels`, `tableur`,
`statistiques-descriptives`, `tests-hypotheses`, `ab-testing`, `analyse-correlation`,
`regression-lineaire`, `apprentissage-supervise`, `apprentissage-non-supervise`,
`apprentissage-par-renforcement`, `rgpd`, `cadrage-besoin`, `gestion-parties-prenantes`.
