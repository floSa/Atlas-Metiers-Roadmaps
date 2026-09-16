# Le site

Le corpus est un ensemble de notes Markdown dans `content/`. Ce dossier contient de
quoi en faire un site : la configuration de Quartz, le thème, les correctifs, et le
script qui assemble le tout.

**Le Markdown reste la source unique.** Le site en est le rendu — jamais l'inverse.

---

## Construire

```sh
./quartz/build.sh            # construit dans public/
./quartz/build.sh --servir   # aperçu local avec rechargement, sur http://localhost:8080
```

La première exécution clone Quartz et installe ses dépendances : comptez deux à trois
minutes. Les suivantes prennent moins d'une seconde.

Il faut Node 22 ou plus, et git.

---

## Pourquoi Quartz n'est pas dans le dépôt

L'installation habituelle de Quartz consiste à forker son dépôt et à y déposer son
contenu. Ici c'est l'inverse : le dépôt est un dépôt de contenu, et Quartz est un outil
qu'on va chercher.

`build.sh` clone Quartz au commit épinglé dans [`VERSION`](VERSION), y applique les
correctifs de `correctifs/`, y recopie `quartz.config.ts`, `quartz.layout.ts` et
`styles/custom.scss`, puis construit `content/` par-dessus. Le clone vit dans
`quartz/.build/`, qui n'est pas versionné.

Ce que ça coûte : la construction a besoin du réseau pour son premier clone.
Ce que ça rapporte : le dépôt garde 289 fichiers amont hors de ses diffs, la
configuration du site tient en trois fichiers lisibles, et monter de version de Quartz
est un changement d'une ligne, visible en revue.

---

## Ce qu'il y a dedans

| Chemin | Rôle |
|---|---|
| `VERSION` | le commit Quartz épinglé |
| `build.sh` | clone, correctifs, configuration, construction |
| `quartz.config.ts` | greffons, thème, URL publique, résolution des liens |
| `quartz.layout.ts` | disposition des pages — rétroliens et graphe partout |
| `styles/custom.scss` | liens orphelins, cadres de carte, lisibilité |
| `correctifs/` | les rustines appliquées à Quartz, une par fichier |
| `essai-carte-cliquable/` | l'essai qui a tranché la carte cliquable — [le verdict](essai-carte-cliquable/VERDICT.md) |

---

## Les correctifs

Deux rustines sur des fichiers internes de Quartz. Elles s'appliquent avec `git apply`,
donc **elles échouent bruyamment** si l'amont a bougé : mieux vaut une construction qui
s'arrête qu'un correctif silencieusement perdu.

### `recherche-francaise.patch`

L'index de recherche de Quartz ne coupe que sur les blancs et conserve les accents. Sur
un corpus français, « cout » ne trouve pas « coût », et « évaluation » ne trouve pas
« l'évaluation » — le jeton indexé est `l'évaluation` en entier, et la recherche par
préfixe cale sur l'apostrophe.

Le correctif replie les diacritiques et coupe sur l'apostrophe et la ponctuation, des
deux côtés — documents et requête. Mesuré sur les huit notes :

| Requête | Sans le correctif | Avec |
|---|---|---|
| `coût` | 8 notes | 8 |
| `cout` | 1 | 8 |
| `donnees` | 1 | 8 |
| `deploiement` | 1 | 8 |

### `liens-orphelins-forme-courte.patch`

`disableBrokenWikilinks` compare le slug de la cible à la racine du vault. Il ignore donc
la stratégie `shortest` de `CrawlLinks`, sous laquelle `[[05 - Roadmap — AI Engineer]]`
désigne bien `content/roadmaps/05 - Roadmap — AI Engineer`. Sans correctif, tout wikilink
écrit sous sa forme courte — c'est-à-dire tout le maillage des notes existantes — était
grisé comme un lien mort.

Le correctif reprend le critère de `transformLink` : le dernier segment du slug, s'il est
unique.

---

## Les liens orphelins, et pourquoi ils se voient

Le corpus s'écrit par chantiers parallèles : un parcours métier pose `[[notions/rag]]`
avant que la notion existe. C'est un signal de travail, pas une erreur.

`disableBrokenWikilinks` rend ces liens inertes plutôt que de les laisser partir en 404,
et `custom.scss` les marque — gris, souligné en pointillé, suivi d'un `◦`. Un lien
orphelin doit se voir sans être cliqué.

À ce jour le site compte **38 cibles orphelines distinctes**, dont 33 viennent des huit
notes historiques et pointent vers des notes d'un coffre Obsidian plus large qui n'ont
jamais été versées ici. Ce n'est pas un défaut du site : c'est un arbitrage à rendre —
les importer, ou les laisser en liens morts assumés.

---

## Monter de version de Quartz

1. Changer la ligne `commit=` de [`VERSION`](VERSION).
2. `rm -rf quartz/.build && ./quartz/build.sh`. Si un correctif ne s'applique plus, la
   construction s'arrête et le nomme : le refaire avant d'aller plus loin.
3. **Rejouer l'essai de la carte cliquable** — voir
   [`essai-carte-cliquable/README.md`](essai-carte-cliquable/README.md). Le choix du SVG
   tient à deux détails d'implémentation amont qui peuvent bouger : le résolveur de liens
   de Quartz passe-t-il toujours dans le HTML brut d'un `<svg>`, et Mermaid est-il
   toujours chargé depuis un CDN au moment de l'affichage.
4. Vérifier le rendu des huit notes : elles utilisent intensivement Mermaid et les
   encadrés Obsidian.

---

## Brancher le dépôt distant

Le workflow [`.github/workflows/deploiement.yml`](../.github/workflows/deploiement.yml)
est prêt et n'attend qu'un dépôt. Le dépôt distant n'est pas créé ici : c'est une action
publique, elle revient au pilote.

1. **Créer le dépôt public** sur GitHub, sans README ni `.gitignore` — le dépôt local en
   a déjà.

2. **Le brancher et pousser.**

   ```sh
   git remote add origin git@github.com:<compte>/<depot>.git
   git push -u origin main
   ```

3. **Activer Pages** : *Settings → Pages → Build and deployment → Source* →
   **GitHub Actions**. Pas « Deploy from a branch » : le workflow dépose un artefact, il
   ne pousse rien sur une branche `gh-pages`.

4. **Laisser tourner.** Le premier `push` sur `main` déclenche la construction.
   `actions/configure-pages` renvoie l'URL réelle du site, y compris le sous-chemin
   `/<depot>/` d'un site de projet, et `quartz.config.ts` la lit dans `QUARTZ_BASE_URL`.
   Il n'y a donc **rien à écrire en dur** : le même dépôt se publie sous n'importe quel
   compte.

5. **Vérifier.** L'onglet *Actions* doit afficher « Construire et publier l'atlas » en
   vert, et l'étape *Verifier que le site n'est pas vide* le nombre de pages produites.

> [!note] Si le site doit vivre sous un domaine propre
> Ajouter `content/CNAME` contenant le domaine, et le déclarer dans *Settings → Pages*.
> `Plugin.Assets` recopie tel quel tout fichier non Markdown de `content/`.
