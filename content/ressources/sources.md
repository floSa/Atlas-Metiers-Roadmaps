---
tags: [ressources, sources, methode, extraction, verification, reference]
date: 2026-09-16
statut: actif
source: https://roadmap.sh
---

# D'où vient ce corpus

> [!abstract] La page qui rend le reste auditable. D'où viennent les 3 216 ressources amont, comment elles ont été extraites, à quelle date, avec quels outils, et comment tout rejouer. Si une affirmation de ce corpus vous paraît douteuse, c'est ici qu'on trouve de quoi la vérifier soi-même.

**Sources** : roadmap.sh (API officielle et dépôt de contenu) · **Capture** : 16 septembre 2026 · **Rédaction** : 16 septembre 2026

---

## La règle

Une ressource non vérifiée n'est pas publiée. Une URL, un titre, un nom d'auteur ou une
date ne s'inventent pas — et quand la source amont en donne un faux, c'est la source
amont qui a tort, pas la vérification. Cette page existe pour qu'on puisse le constater
sans nous croire sur parole.

## Les deux sources amont

L'atlas ne recopie pas les pages web de roadmap.sh. Il lit deux points d'accès stables,
ce qui rend la capture reproductible à l'identique :

| Source | Adresse | Ce qu'elle donne |
|---|---|---|
| L'API officielle | `roadmap.sh/api/v1-official-roadmap/<slug>` | l'arbre complet : nœuds, arêtes, **positions (x, y)** — donc l'ordre de lecture exact et la disposition visuelle |
| Le dépôt de contenu | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | un fichier Markdown par nœud : le texte pédagogique et les ressources typées |

Les positions sont ce qui permet de régénérer une carte cliquable fidèle à l'originale
plutôt qu'un schéma approximatif. Les types de ressources — `@article`, `@video`,
`@course`, `@official`, `@opensource`, `@feed`, `@book`, `@roadmap` — viennent du dépôt
de contenu et sont repris tels quels.

> [!warning] Piège
> La capture HTML manuelle du 15 mars 2026, qui a servi aux huit premières notes, est
> abandonnée. Elle n'était pas rejouable — c'est précisément pour ça qu'un écart de six
> mois avec l'amont a pu passer inaperçu. Tout ce qui n'est pas rejouable finit par
> mentir sans qu'on le sache.

## Ce qui a été capturé

Treize roadmaps, le 16 septembre 2026. La colonne « amont modifié » est la date que
roadmap.sh déclare pour sa propre dernière mise à jour : c'est elle qui dit si une
roadmap bouge encore.

| Roadmap | Nœuds | Sujets | Ressources | Amont modifié |
|---|---:|---:|---:|---|
| [`ai-engineer`](https://roadmap.sh/ai-engineer) | 279 | 189 | 474 | 11 sept. 2026 |
| [`data-engineer`](https://roadmap.sh/data-engineer) | 268 | 186 | 398 | 7 août 2026 |
| [`bi-analyst`](https://roadmap.sh/bi-analyst) | 255 | 200 | 275 | 4 sept. 2026 |
| [`computer-science`](https://roadmap.sh/computer-science) | 244 | 188 | 498 | 7 sept. 2026 |
| [`machine-learning`](https://roadmap.sh/machine-learning) | 201 | 150 | 330 | 17 juin 2026 |
| [`ai-agents`](https://roadmap.sh/ai-agents) | 189 | 101 | 305 | 9 mars 2026 |
| [`data-analyst`](https://roadmap.sh/data-analyst) | 161 | 99 | 192 | 4 sept. 2026 |
| [`ai-data-scientist`](https://roadmap.sh/ai-data-scientist) | 130 | 29 | 20 | 4 sept. 2026 |
| [`ai-red-teaming`](https://roadmap.sh/ai-red-teaming) | 105 | 64 | 209 | 20 mars 2026 |
| [`mlops`](https://roadmap.sh/mlops) | 95 | 62 | 275 | 24 janv. 2026 |
| [`prompt-engineering`](https://roadmap.sh/prompt-engineering) | 94 | 47 | 90 | 29 avr. 2026 |
| [`ai-product-builder`](https://roadmap.sh/ai-product-builder) | 93 | 52 | 120 | 25 juin 2026 |
| [`forward-deployed-engineer`](https://roadmap.sh/forward-deployed-engineer) | 44 | 20 | 30 | 30 juin 2026 |
| **Total** | **2 158** | **1 387** | **3 216** | |

Deux lectures utiles de ce tableau. `mlops` n'a pas bougé depuis janvier et
`ai-agents` depuis mars, sur des sujets qui, eux, bougent tous les mois : l'amont y est
en retard, et la note correspondante doit compenser. À l'inverse,
`forward-deployed-engineer` — 44 nœuds, 30 ressources, dont sept sont de simples renvois
vers d'autres roadmaps — n'est pas en retard, il est vide. C'est ce qui justifie que le
dossier FDE de cet atlas soit d'abord un apport propre.

## Les trois outils

Tous dans `tools/`, tous en Python de la bibliothèque standard, sans dépendance à
installer.

### `roadmap_extract.py` — capturer

Combine les deux sources amont et écrit, pour chaque slug :

| Fichier | Contenu |
|---|---|
| `data/raw/<slug>/<date>.json` | la capture brute de l'API, horodatée et versionnée |
| `data/extract/<slug>.md` | le plan lisible : sections, nœuds dans l'ordre visuel, texte, ressources |
| `data/extract/<slug>.json` | la même chose normalisée, pour les scripts |

```bash
python3 tools/roadmap_extract.py --sync
python3 tools/roadmap_extract.py --all-known
```

Le regroupement par section suit la **boîte englobante** du nœud conteneur de
roadmap.sh, et non un simple tri par ordonnée. Le tri par ordonnée faisait dériver les
titres d'une bande à l'autre : un nœud se retrouvait rangé sous la section du dessus.
Le repli sur le dernier label au-dessus ne sert que pour les roadmaps sans conteneur.

### `roadmap_diff.py` — mesurer l'obsolescence

Compare une note déjà rédigée à l'état courant de l'amont, en lisant les libellés de ses
schémas Mermaid. Trois verdicts par nœud : **amont seul** (candidat à l'ajout, c'est la
mesure de l'obsolescence), **note seule** (ajout volontaire, ou nœud retiré en amont),
**couvert**.

```bash
python3 tools/roadmap_diff.py              # tout le corpus rédigé
python3 tools/roadmap_diff.py ai-engineer  # une roadmap
```

> [!warning] Piège
> L'outil compare des libellés. Une note dont les schémas sont rédigés en français
> affiche donc une couverture artificiellement basse — c'est arrivé au dossier FDE, mesuré
> à 75 % sans qu'il lui manque quoi que ce soit. La convention du corpus est pour cette
> raison de **conserver le libellé amont dans le schéma et de porter la traduction dans
> le texte**. Un chiffre de couverture se lit en sachant ça, ou ne se lit pas.

### `verifier_liens.py` — vérifier que ça répond encore

Teste les URL et classe les réponses. Il ne modifie jamais le corpus : il produit un
rapport, et la décision de remplacer ou de retirer reste humaine.

```bash
python3 tools/verifier_liens.py --selection  # les URL de content/ressources/
python3 tools/verifier_liens.py --corpus     # toutes les URL citées dans content/
python3 tools/verifier_liens.py --amont      # les 2 649 URL uniques de l'amont
python3 tools/verifier_liens.py --url https://exemple.org/page
```

Les rapports sont versionnés sous `data/liens/` — `rapport-corpus.md` pour les liens
cités par les notes, `rapport-selection.md` pour ceux de la sélection commentée. Le
cache, lui, ne l'est pas : il dépend du réseau depuis lequel on lance l'outil.

Les statuts :

| Statut | Ce que ça veut dire | Ce qu'on en fait |
|---|---|---|
| `ok` | 2xx à l'URL citée | rien |
| `redirection` | atteignable, mais l'URL réelle a changé | mettre l'URL à jour |
| `introuvable` | 404 ou 410 | remplacer par un équivalent vérifié, ou retirer |
| `erreur` | 5xx ou défaut TLS | revérifier avant de conclure |
| `domaine-mort` | DNS introuvable, connexion refusée | retirer |
| `delai` | pas de réponse dans le temps imparti | revérifier |
| `bloque` | 401, 403, 429 ou interstitiel anti-robot | **ne veut pas dire mort** — vérification humaine |

Trois choix de conception méritent d'être explicités, parce qu'ils changent les
résultats :

- **Respectueux.** Un délai entre deux requêtes, un délai plus long entre deux requêtes
  vers le même domaine, aucun parallélisme, et un `User-Agent` qui dit qui appelle et
  pourquoi. On interroge des serveurs qui ne nous doivent rien. Se déguiser en
  navigateur serait à la fois inutile et malpoli.
- **Incrémental.** Chaque résultat est mis en cache avec sa date dans
  `data/liens/cache.json`. Une URL vue il y a moins de trente jours n'est pas retestée —
  sauf si son statut était instable (`erreur`, `delai`, `bloque`), auquel cas le délai
  tombe à sept jours. C'est ce qui rend la veille tenable au lieu de coûter deux heures
  à chaque passage.
- **Deux pièges traités explicitement.** Une redirection de langue n'est pas un
  déplacement de ressource et n'est pas signalée — qu'elle passe par le chemin
  (`/fr/`, `/en-us/`) ou par la requête (`?hl=fr`, les drapeaux de bannière de
  consentement). En revanche, une redirection vers une page générique — la racine du
  site, l'index de la rubrique, le domaine de celui qui a racheté le site — **est**
  signalée comme telle : c'est un 404 déguisé, et c'est le cas le plus perfide parce
  qu'il répond 200. Une redirection qui conserve le dernier segment du chemin est au
  contraire tenue pour un simple déménagement : c'est ce qui distingue un site racheté
  qui republie ses pages d'un site racheté qui les a jetées.

> [!tip] Ajout 2026
> Le statut `bloque` n'est pas un échec de l'outil, c'est une information. EUR-Lex
> répond `202` avec un corps vide à tout ce qui n'est pas un navigateur : le règlement
> sur l'IA est parfaitement en ligne, mais aucun robot ne peut le constater. Confondre
> « je ne peux pas lire » et « ça n'existe plus » est la principale façon de casser un
> corpus en croyant l'entretenir.

## Rafraîchir le corpus

Dans cet ordre.

```bash
python3 tools/roadmap_extract.py --sync
python3 tools/roadmap_extract.py --all-known
python3 tools/roadmap_diff.py
python3 tools/verifier_liens.py --selection
python3 tools/verifier_liens.py --corpus
```

L'extraction dit ce que l'amont contient aujourd'hui, le diff dit ce que les notes ont
raté, la vérification dit ce qui est mort depuis la dernière fois. Les trois rapports se
lisent ensemble : une note peut être à jour sur le fond et ne plus pointer nulle part.

Les captures brutes sont versionnées par date sous `data/raw/<slug>/`. On peut donc
toujours rejouer une extraction passée, ou comparer deux états de l'amont sans dépendre
de ce que roadmap.sh sert aujourd'hui.

## Ce que la chaîne ne garantit pas

Quatre limites connues, mesurées sur cette capture. Les taire donnerait une fausse idée
de la fiabilité de l'amont.

**Les titres amont ne sont pas fiables.** Neuf titres de cette capture ont perdu leur
première lettre — « laude Code Tutorial », « tatistics - A Full University Course ». Six
autres ont pour titre leur propre URL. Ces ressources sont écartées de la sélection
plutôt que réparées : deviner ce qu'un titre tronqué voulait dire, c'est inventer.

**Une URL vivante peut désigner autre chose que ce qu'annonce son titre.** Vérifié sur
les articles de recherche de cette capture, par l'API arXiv : `arxiv.org/abs/2310.12818`
est annoncé comme « Poisoning Web-Scale Training Data » et renvoie en réalité un article
sur l'efficacité d'inférence ; `arxiv.org/abs/2311.05544`, annoncé « SoK: Prompt Hacking
of LLMs », renvoie un article de calcul quantique adiabatique. Un vérificateur de liens
ne voit rien : les deux répondent 200. Seule la confrontation du titre au document le
révèle.

**Une part du catalogue amont est un placement commercial.** 76 URL de cette capture
portent un marqueur de campagne — `utm_campaign=TDS+roadmap+integration` sur 53 des 83
articles d'un même éditeur, `ref=roadmapsh` sur quinze flux d'agrégateur, `?c=rsh-a` et
`utm_campaign=ai-engineer-roadmap` sur des pages produit. Ce n'est pas illégitime de la
part de roadmap.sh, mais ça n'a pas le même statut qu'une source choisie pour sa qualité,
et ça se voit dans l'URL.

**Le blocage anti-robot est structurel.** EUR-Lex, ISO, Medium et plusieurs autres
refusent les requêtes automatiques. Leurs liens ne peuvent être validés qu'à la main. Le
rapport les isole sous `bloque` précisément pour qu'ils ne soient jamais confondus avec
des liens morts.

## Réutilisation

Les captures sous `data/raw/` et `data/extract/` sont dérivées de roadmap.sh et de son
dépôt de contenu, et restent soumises aux conditions de leurs auteurs. Ce qui est propre
à cet atlas, ce sont les notes de `content/`, la sélection de
[[ressources/index|ressources commentées]] et les trois outils de `tools/`.
