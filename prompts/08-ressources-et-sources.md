# 08 — Ressources et sources

Lis d'abord `PROJET.md` puis `prompts/_commun.md`. Tu es le chantier
**08 — Ressources et sources**.

> [!warning] Ne démarre pas avant d'avoir reçu les synthèses des chantiers 02 à 06.

## Zone d'écriture exclusive

`content/ressources/` et `tools/verifier_liens.py`.

## Ce que tu reçois

**3 216 ressources** extraites de l'amont, dans `data/extract/*.json`, chacune typée
`@article`, `@video`, `@course`, `@official`, `@opensource`, `@feed`, avec son titre,
son URL et le nœud dont elle provient. Plus les ressources retenues par chaque chantier
métier dans sa synthèse.

## Mission

### 1. Vérifier

Écris `tools/verifier_liens.py` : un script qui teste les URL du corpus et classe les
réponses (2xx, redirection, 404, domaine mort, blocage anti-robot). Exigences :

- **respectueux** — un délai entre requêtes, un `User-Agent` honnête, pas de
  parallélisme agressif. Tu interroges des sites tiers, comporte-toi correctement ;
- **incrémental** — il met en cache ses résultats pour ne pas tout retester à chaque
  passage, et il resservira à chaque veille ;
- il produit un rapport, il ne modifie **jamais** le corpus tout seul.

Une ressource morte n'est pas supprimée en silence : elle est signalée, et remplacée
seulement si tu as trouvé un équivalent vérifié.

### 2. Dédupliquer et classer

La même ressource revient dans plusieurs roadmaps. Construis
`content/ressources/index.md` : l'entrée unique vers les sources du corpus, organisée
par **usage** et non par métier — « pour démarrer », « pour approfondir », « la
référence officielle », « ce qu'on relit ».

Puis une page par grande famille (IA générative, données, statistiques, ingénierie,
conseil et terrain). Chaque ressource porte : son type, son titre, son URL, ce qu'elle
apporte en une ligne, et le niveau attendu du lecteur.

### 3. Trier, vraiment

3 216 ressources publiées telles quelles ne servent à personne. **Tu sélectionnes.** Un
ensemble de deux cents ressources choisies et commentées vaut infiniment mieux qu'un
annuaire exhaustif. Les critères : la source primaire l'emporte sur le commentaire, le
daté et maintenu l'emporte sur l'intemporel autoproclamé, le gratuit et accessible
l'emporte à qualité égale.

Écarte sans état d'âme le contenu promotionnel déguisé en pédagogie — il y en a, en
particulier sur les sujets récents comme le FDE.

### 4. La page des sources

`content/ressources/sources.md` : d'où vient ce corpus, comment il a été extrait, à
quelle date, et comment le rafraîchir. Documente les deux outils existants
(`roadmap_extract.py`, `roadmap_diff.py`) et le tien. C'est la page qui rend le travail
auditable — elle compte autant que le contenu.

## Ne pas faire

Ne réécris pas les ressources dans les notes des parcours : ce n'est pas ta zone. Si
une note cite une ressource morte, signale-la dans ta synthèse pour que le chantier
concerné la corrige.
