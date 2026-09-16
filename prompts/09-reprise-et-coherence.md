# 09 — Reprise et cohérence

Lis d'abord `PROJET.md`, `prompts/_commun.md`, puis `prompts/_arbitrages-lot-1.md`.
Tu es le chantier **09 — Reprise et cohérence**.

> [!warning] Ne démarre pas avant que les chantiers 07 et 08 soient livrés.
> Ton travail consiste à raccorder les parcours aux notions et aux ressources qu'ils
> auront produites.

## Zone d'écriture exclusive

`content/parcours/` (les cinq parcours du lot 1), `content/index.md`,
`content/roadmaps/00 - Index — Roadmaps.md`.

**Tu ne touches pas** à `content/notions/`, `content/ressources/`, `tools/`, `quartz/`.

## Mission

### 1. Convertir en liens les sujets devenus des notions

Neuf notions ont été créées après coup. Les parcours qui les ont demandées ont traité
ces sujets **en ligne**, faute de cible à l'époque. Il faut maintenant remplacer ces
passages par un renvoi plus une ou deux phrases d'angle, conformément à la règle
anti-duplication.

| Parcours | Passages à convertir |
|---|---|
| `ai-red-teaming.md` | `controle-d-acces`, `modelisation-de-la-menace`, `chaine-d-approvisionnement-logicielle` |
| `ai-product-builder.md` | `controle-d-acces` (écrit sous « authentification et autorisation »), `mesure-d-usage-produit`, `plateforme-de-deploiement` |
| `data-analyst.md` | `collecte-de-donnees`, `traitement-distribue` |
| `bi-analyst.md` | `series-temporelles`, `analyse-de-cohorte` |

Lis d'abord la notion écrite par le chantier 07, puis coupe dans le parcours ce qu'elle
dit déjà. **Ne coupe pas l'angle métier** : c'est ce qui reste, et c'est le plus utile.

Quatre sujets sont restés volontairement dans leur parcours — `exemple-adverse`,
`extraction-de-modele`, `empoisonnement-de-donnees`, `divulgation-responsable` côté Red
Teaming, `dorsale-geree` côté Product Builder, `couche-semantique` côté BI Analyst.
**N'y touche pas.**

### 2. Poser les cartes fidèles

`tools/roadmap_render.py` génère une carte SVG cliquable depuis les positions amont.
Pour chacun des cinq parcours :

```
python3 tools/roadmap_render.py <slug> --verifier
python3 tools/roadmap_render.py <slug> --sortie <la page du parcours>
```

La carte va **en fin de page**, sous un titre « La roadmap d'origine », et ne remplace
pas le schéma Mermaid éditorial en tête. Vérifie avec `--verifier` que les cibles
existent maintenant que les notions sont écrites, et fournis le fichier `--liens` quand
un libellé amont doit tomber sur une ancre française plutôt que sur une notion.

### 3. Rétablir la mesure d'obsolescence

`tools/roadmap_diff.py` donne 75 % au FDE alors que sa couverture est réelle : ses
schémas sont en français, et le diff compare des libellés amont. La convention retenue
est de **conserver le libellé amont dans le nœud** et de porter la traduction dans le
texte, comme l'a fait le chantier 05 qui mesure 100 %.

Applique-la au dossier FDE, puis relance `python3 tools/roadmap_diff.py` et vise une
couverture qui reflète le contenu réel. Si un nœud amont est réellement absent, ajoute-le
plutôt que de maquiller la mesure — c'est tout l'intérêt de l'indicateur.

### 4. Raccorder les index

`content/index.md` et `content/roadmaps/00 - Index — Roadmaps.md` ne référencent pas
encore les cinq parcours du lot 1, ni les notions, ni les pages de `content/ressources/`
— `index.md` mentionne le répertoire dans son schéma sans pointer vers une seule page. Mets-les à jour : les métiers, les
trajectoires, et la façon dont parcours, notions et ressources s'articulent.

### 5. Reprendre les liens qui redirigent

Le chantier 08 a mesuré **16 redirections** dans le corpus rédigé et les a listées dans
`data/liens/rapport-corpus.md`. Une redirection n'est pas toujours anodine : `mode.com`
part chez ThoughtSpot (2 liens dans BI Analyst), `research.nccgroup.com` retombe sur sa
racine — un 404 déguisé — et `gandalf.lakera.ai` mène désormais à un autre produit.

**Juge sur le contenu servi, pas sur le code HTTP.** Un lien qui répond 200 après
redirection peut très bien ne plus servir l'article cité. Le cas `hevodata.com` sur
l'analyse de cohorte en est l'exemple : il répond, mais vers autre chose.

Cinq liens franchement faux ont déjà été corrigés par le pilote, dont deux URL arXiv qui
pointaient vers des articles sans aucun rapport — voir l'addendum des arbitrages. Ne les
retouche pas.

### 6. Contrôle final

```
grep -rhoE '\[\[notions/[^]|#]+' content | sed 's|\[\[notions/||' | sort -u \
  | while read s; do [ -f "content/notions/$s.md" ] || echo "ORPHELIN: $s"; done
python3 tools/roadmap_diff.py
bash quartz/build.sh
```

Les trois doivent passer. Tout orphelin restant est listé dans ta synthèse avec sa raison.

## Ce que tu ne fais pas

Tu ne réécris pas les parcours. Tu coupes ce qui a migré vers une notion, tu ajoutes les
cartes, tu corriges les libellés de schéma et tu raccordes les index. Si tu constates un
défaut de fond dans un parcours, **signale-le dans ta synthèse** au lieu de le corriger :
ce n'est pas ton mandat et l'auteur du parcours est mieux placé.
