# Cadrage — Atlas des métiers de l'IA et de la data

> Un site de parcours d'apprentissage inspiré de roadmap.sh, en français, centré sur
> le métier de **Forward Deployed Engineer**, adossé à un corpus de notes Markdown
> navigables et à un socle d'extraction rejouable.

**Statut** : cadrage soumis à validation · **Date** : 16 septembre 2026

---

## 1. Ce qu'on a constaté

Trois faits établis en vérifiant roadmap.sh à la source, qui conditionnent tout le reste.

**Le FDE existe en amont, mais à l'état d'ébauche.** La roadmap officielle
`/forward-deployed-engineer` compte 20 nœuds de contenu et 30 ressources — la plus
maigre du catalogue, contre 189 nœuds pour AI Engineer. Son socle technique n'est
qu'un renvoi vers sept autres roadmaps. Sa vraie valeur tient dans un seul bloc,
*Customer Delivery & Field Skills*. C'est donc le métier où l'apport propre est le
plus grand, et non celui où il faut traduire le plus.

**Cinq rôles du périmètre IA/data manquaient au corpus** : Forward Deployed Engineer,
AI Red Teaming, AI Product Builder, Data Analyst, BI Analyst.

**Les huit notes existantes ont mieux vieilli que prévu** : 87 à 99 % des nœuds amont
restent couverts. Une seule lacune de fond, sur AI Engineer — le bloc observabilité et
évaluation ajouté en amont après la capture de mars. Voir `data/extract/_rapport-ecart.md`.

---

## 2. Périmètre retenu

| Chantier | Contenu | Lot |
|---|---|---|
| Forward Deployed Engineer | dossier approfondi, pièce maîtresse | 1 |
| AI Red Teaming · AI Product Builder · Data Analyst · BI Analyst | notes au format du corpus | 1 |
| Site Quartz publié sur GitHub Pages, dépôt public | infrastructure | 1 |
| Rafraîchissement des huit notes existantes | rédaction | 2 |
| Compétences data (SQL, Python for Data Analysis, R, Power BI) | notes | 2 |

**Hors périmètre du lot 1** : traduction exhaustive des 3 216 ressources amont, contenus
vidéo, exercices interactifs, authentification ou suivi de progression.

---

## 3. Le socle, déjà construit

Deux outils, dans `tools/`, qui rendent le corpus rejouable. Aucun agent ne doit les
réécrire ni recapturer roadmap.sh à la main.

`roadmap_extract.py` combine l'API officielle `roadmap.sh/api/v1-official-roadmap/<slug>`
— l'arbre complet avec les positions, donc l'ordre de lecture exact — et le dépôt de
contenu `nilbuild/developer-roadmap`, qui donne un Markdown par nœud avec ses ressources
typées (`@article`, `@video`, `@course`, `@official`, `@opensource`, `@feed`). Il écrit
une capture horodatée dans `data/raw/<slug>/`, un plan lisible dans
`data/extract/<slug>.md` et sa forme normalisée en JSON.

`roadmap_diff.py` compare une note déjà rédigée à l'état courant de l'amont, en lisant
les libellés de ses schémas Mermaid. Il sert à mesurer l'obsolescence, et resservira à
chaque veille.

État à ce jour : **13 roadmaps extraites, 1 387 nœuds documentés, 3 216 ressources**.

> La capture HTML manuelle du 15 mars 2026 est abandonnée. Elle n'était pas rejouable,
> ce qui est précisément la raison pour laquelle l'écart de six mois n'avait pas été vu.

---

## 4. Architecture du contenu

Trois niveaux, et une règle qui les gouverne.

```
content/
├── index.md                      accueil : les métiers, les trajectoires
├── parcours/                     un par métier — la carte et le fil conducteur
│   ├── forward-deployed-engineer/
│   │   ├── index.md              la carte cliquable et les étapes
│   │   ├── cycle-mission.md      audit → rationalisation → industrialisation
│   │   └── ...
│   ├── ai-red-teaming.md
│   └── ...
├── notions/                      une notion = un fichier = écrit une seule fois
│   ├── rag.md
│   ├── evaluation-llm.md
│   ├── bpmn.md
│   └── ...
├── ressources/                   les sources, dédupliquées et classées
└── roadmaps/                     les huit notes historiques
```

**La règle anti-duplication.** Une notion transverse — RAG, embeddings, évaluation,
garde-fous, Docker, CI/CD, SQL — est expliquée **dans un seul fichier**, sous
`notions/`. Un parcours métier ne la réexplique jamais : il y renvoie par un wikilink
et se contente d'ajouter *ce que cette notion veut dire pour ce métier-là*, en une ou
deux phrases. C'est ce qui empêche cinq rédactions parallèles de produire cinq
explications divergentes du RAG.

**Conséquence sur le travail parallèle.** Un agent métier n'écrit **que** dans ses
propres fichiers. Il pose librement des liens `[[notions/xxx]]` même vers des notions
qui n'existent pas encore — un lien orphelin est un signal, pas une erreur — et il
liste ces besoins dans sa synthèse. Une passe de consolidation crée ensuite chaque
notion manquante, une fois, à partir des besoins collectés. Aucun conflit d'écriture
possible, parallélisme réel.

---

## 5. Le site

**Quartz 4**, qui publie un vault Obsidian sans rien réécrire : wikilinks, callouts
`> [!tip]`, Mermaid, graphe de liens et rétroliens fonctionnent nativement. Le Markdown
reste la source unique ; le site en est le rendu. Déploiement GitHub Pages par Action,
dépôt public.

**La carte cliquable.** C'est ce qui fait la différence avec un simple site de notes.
Les captures contiennent la position `(x, y)` de chaque nœud : on peut donc régénérer
la disposition visuelle de roadmap.sh en SVG, avec un vrai lien par nœud vers la page
de la notion correspondante. Sans JavaScript, sans dépendance, et reproductible par
script depuis `data/extract/<slug>.json`.

> [!warning] Point à lever par un essai avant de s'engager
> Le `click` natif de Mermaid est souvent neutralisé par la politique de sécurité des
> générateurs de sites. Le rendu SVG maison contourne le problème par construction,
> mais il reste à vérifier sur une carte réelle — celle du FDE, la plus petite — avant
> de généraliser. C'est la première tâche du chantier 01.

---

## 6. Le dossier Forward Deployed Engineer

La roadmap amont sert de squelette, pas de plan. Elle couvre le socle technique et le
bloc *Customer Delivery*. Le brief de commande va plus loin sur cinq points qu'elle
n'aborde pas du tout, et ce sont eux qui font l'intérêt du dossier :

1. **Business Process Re-engineering** — décortiquer un processus, repérer les
   redondances, simplifier *avant* d'écrire la moindre ligne de code ; modélisation BPMN.
2. **L'arbitrage déterministe / probabiliste** — quand un script, un webhook ou du RPA
   suffit, et quand l'IA générative est réellement nécessaire. L'erreur de cadrage la
   plus coûteuse du métier.
3. **L'interfaçage avec l'existant** — ERP, CRM, bases legacy, systèmes patrimoniaux.
4. **La dimension politique** — parties prenantes aux intérêts divergents, résistance au
   changement, vulgarisation d'arbitrages techniques devant une direction exécutive.
5. **La sortie de mission** — transfert de compétences, maintenance, ce qui reste quand
   le FDE part.

S'y ajoutent, repris de l'amont et approfondis : LLMOps et garde-fous (injection de
prompt, filtrage des données sensibles), protocoles d'évaluation, coût d'inférence et
latence, architectures RAG et agents.

---

## 7. Découpage en chantiers

Chaque chantier est une conversation distincte, numérotée et nommée.

| N° | Nom | Dépend de | Écrit dans |
|---|---|---|---|
| 00 | Pilote | — | `PROJET.md`, coordination |
| 01 | Socle et site | — | `quartz/`, `tools/roadmap_render.py`, CI |
| 02 | Métier — Forward Deployed Engineer | — | `content/parcours/forward-deployed-engineer/` |
| 03 | Métier — AI Red Teaming | — | `content/parcours/ai-red-teaming.md` |
| 04 | Métier — AI Product Builder | — | `content/parcours/ai-product-builder.md` |
| 05 | Métier — Data Analyst | — | `content/parcours/data-analyst.md` |
| 06 | Métier — BI Analyst | — | `content/parcours/bi-analyst.md` |
| 07 | Notions mutualisées | 02→06 | `content/notions/` |
| 08 | Ressources et sources | 02→06 | `content/ressources/` |

Les chantiers 01 à 06 tournent en parallèle : leurs zones d'écriture sont disjointes.
Les chantiers 07 et 08 sont des passes de consolidation, lancées une fois les besoins
en notions et en ressources remontés par les synthèses.

**Protocole de restitution.** Chaque chantier termine par une synthèse ouverte par
`SYNTHÈSE DE TÂCHE` et fermée par `FIN DE TÂCHE`, contenant : les fichiers créés, les
notions appelées en lien et leur définition attendue en une ligne, les ressources
retenues, les points de désaccord avec l'amont, et ce qui reste ouvert.

---

## 8. Contrat de format

Toute note produite respecte le format des huit notes existantes, qui fait déjà
référence dans le corpus :

- **Frontmatter** : `tags`, `date`, `statut`, `source` (l'URL roadmap.sh d'origine).
- **Un encadré `> [!abstract]`** en ouverture, qui dit à qui la note s'adresse.
- **Une vue macro** en Mermaid, puis une section par grande étape.
- **Par étape** : un schéma Mermaid, un paragraphe « À quoi ça sert » qui explique
  l'intérêt réel, une liste « Ce qu'il faut savoir », un encadré `> [!tip] Ajout 2026`
  et un encadré `> [!warning] Piège` tiré du terrain.
- **Les nœuds absents de l'amont** apparaissent en vert pointillé dans les schémas
  (`classDef ajout fill:#e8f5e9,stroke:#2e7d32,stroke-dasharray:4 3`).
- **Les sources sont citées**, jamais inventées. Une ressource non vérifiée n'est pas
  publiée.

---

## 9. Critères de validation du lot 1

- Le site se construit et se déploie sur GitHub Pages sans erreur.
- La carte du FDE est cliquable et chaque nœud mène à une page qui existe.
- Aucune notion transverse n'est expliquée deux fois dans deux parcours différents.
- Aucun lien orphelin ne subsiste après la passe 07.
- Chaque affirmation technique est soit sourcée, soit signalée comme un apport propre.
