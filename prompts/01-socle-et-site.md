# 01 — Socle et site

Lis d'abord `PROJET.md` puis `prompts/_commun.md`. Tu es le chantier **01 — Socle et site**.

Tu es le seul chantier à ne pas produire de contenu rédactionnel. Tu produis
l'infrastructure sur laquelle les cinq chantiers métier viendront poser leurs notes.

## Zone d'écriture exclusive

`quartz/`, `tools/roadmap_render.py`, `.github/workflows/`, `content/index.md`,
`content/.gitignore`. **Rien dans `content/parcours/`, `content/notions/`,
`content/ressources/` ni `content/roadmaps/`.**

## Mission

### 1. Lever le point de risque, avant tout le reste

Le cadrage identifie un risque non levé : le `click` natif de Mermaid est souvent
neutralisé par la politique de sécurité des générateurs de sites, ce qui casserait
l'idée même de carte cliquable.

Commence par un essai sur la plus petite carte, celle du FDE (20 nœuds). Compare deux
approches et tranche **sur preuve**, pas sur intuition :

- `click <id> "<url>"` dans un bloc Mermaid rendu par Quartz ;
- un SVG généré depuis `data/extract/forward-deployed-engineer.json`, où chaque nœud
  devient un `<a href>` réel.

Les captures brutes `data/raw/<slug>/<date>.json` contiennent la position `(x, y)`, la
largeur et la hauteur de chaque nœud : la disposition visuelle de roadmap.sh est donc
reproductible exactement. C'est ce qui rend la seconde approche crédible.

Rends ton verdict avec la preuve (capture, page de test, ou sortie de build) dans ta
synthèse. Si les deux échouent, propose une troisième voie plutôt que de forcer.

### 2. `tools/roadmap_render.py`

Un script qui transforme `data/extract/<slug>.json` en carte navigable, selon
l'approche retenue à l'étape 1. Exigences :

- **déterministe** — même entrée, même sortie, pour que le rendu soit diffable ;
- **sans JavaScript** si l'approche SVG l'emporte, et sans dépendance hors bibliothèque
  standard Python ;
- **lisible en thème clair et en thème sombre** — Quartz propose les deux ;
- **utilisable au téléphone** — une carte roadmap.sh est large, prévois le défilement
  horizontal ou une bascule en liste ;
- chaque nœud pointe vers `notions/<slug>` quand le registre
  `content/notions/_registre.md` contient une correspondance, et sinon vers l'ancre de
  la section correspondante dans la note du parcours ;
- un nœud dont la cible n'existe pas encore reste cliquable et visiblement distinct
  (les chantiers métier travaillent en parallèle, beaucoup de cibles manqueront au début).

Documente l'usage en tête du script, comme les deux outils existants.

### 3. Quartz 4

Installe et configure Quartz pour publier `content/` :

- wikilinks `[[...]]`, callouts `> [!tip]`, Mermaid et graphe de liens fonctionnels ;
- recherche en français ;
- rétroliens visibles — c'est ce qui rend le maillage notions/parcours lisible ;
- thème sobre, lisible, clair et sombre ;
- les liens orphelins doivent rester visibles et distincts, pas silencieux.

Vérifie le rendu réel des huit notes de `content/roadmaps/` : elles utilisent
intensivement Mermaid et les callouts Obsidian. Si quelque chose casse, dis-le dans ta
synthèse — **ne réécris pas les notes pour contourner**, ce n'est pas ta zone.

### 4. `content/index.md`

La page d'accueil : les métiers couverts, les trajectoires possibles, comment lire le
corpus. Prends `content/roadmaps/00 - Index — Roadmaps.md` comme modèle de ton et de
structure. Pose des liens vers les parcours du lot 1 même s'ils n'existent pas encore.

### 5. Déploiement

Une GitHub Action qui construit et publie sur GitHub Pages, dépôt public. Le dépôt n'a
pas encore de remote : prépare le workflow et documente la marche à suivre pour le
brancher, sans créer le dépôt distant toi-même.

## Attention

`data/_upstream/` est un clone de 50 Mo, ignoré par git. Ne le committe pas, ne le
publie pas.
