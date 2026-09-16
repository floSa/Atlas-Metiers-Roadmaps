# Cadrage — Atlas Métiers Roadmaps

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

## 4. Architecture du contenu — l'arbre à tiroirs

Le site est un arbre. À chaque étage, le lecteur voit une carte cliquable de ce qu'il y
a à apprendre, descend d'un cran, et remonte par le fil d'Ariane ou par la barre de
navigation en bas de page.

```
Accueil          les métiers
 └── Métier      la roadmap du métier
      └── Domaine        la carte des sous-domaines
           └── Sous-domaine   la carte des notions
                └── Notion    la feuille : explication et ressources
```

Cinq étages au maximum ; une branche peut être moins profonde.

**La règle qui gouverne tout** : une case dans un schéma mène toujours quelque part. Si
un sujet n'a pas de page, il n'a pas de case — il est dans le texte. C'est ce qui rend
la navigation prévisible.

**La règle anti-duplication** : une notion transverse est expliquée dans un seul
fichier, sous `notions/`. Un parcours métier n'en redonne jamais l'explication ; il y
renvoie et ajoute ce que la notion signifie pour ce métier-là. Les slugs sont figés dans
`content/notions/_registre.md`.

Le détail des deux formes de page — aiguillage et feuille — est dans
`prompts/_gabarit-metier.md`, qui fait foi.

## 5. État au 16 septembre 2026

| | |
|---|---|
| Pages | 363 |
| Métiers | 13, tous en arbre à tiroirs |
| Notions | 65, avec leur index |
| Schémas | 292, dont 220 cliquables |
| Liens morts | 0 |

Ce qui reste : 72 schémas muets sur Data Analyst, BI Analyst et AI Product Builder, et
la grille de séniorité par section, qui n'est encore faite que pour le FDE.

## 6. Le site

**Quartz 4**, cloné au commit épinglé dans `quartz/VERSION` par `quartz/build.sh`, avec
la configuration et les correctifs de `quartz/`. Le Markdown reste la source unique.

Prévisualisation : `bash quartz/build.sh` puis `python3 tools/servir.py`, qui résout les
adresses sans extension comme le fait GitHub Pages — `python -m http.server` ne le fait
pas et renvoie 404 sur toutes les pages.

Un composant maison, `quartz/composants/NavigationArbre.tsx`, ajoute en bas de chaque
page la navigation précédent / niveau supérieur / suivant. L'ordre des voisins est celui
dans lequel la page parente les énumère, pas l'ordre alphabétique.

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
