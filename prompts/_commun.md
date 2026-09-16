# Socle commun à tous les chantiers

> À lire en entier avant de commencer. Chaque prompt de chantier s'appuie dessus et ne
> répète pas ce qui est ici.

## Le projet

On construit un **atlas des métiers de l'IA et de la data science**, en français :
un corpus de notes Markdown navigables, publié en site statique par Quartz 4. C'est
inspiré de roadmap.sh, mais ce n'est pas une traduction — chaque note explique les
notions, dit ce que la source ne dit pas, et renvoie vers des ressources vérifiées.

Le cadrage complet est dans `PROJET.md`. Le lire avant toute chose.

Dépôt : `/home/florianhorellou/Projets/Roadmaps`

## Le socle déjà construit — ne pas le refaire

**Ne recapture jamais roadmap.sh à la main.** Tout est déjà extrait :

| Chemin | Contenu |
|---|---|
| `data/extract/<slug>.md` | le plan complet de la roadmap amont : sections, nœuds dans l'ordre visuel, texte pédagogique, ressources typées |
| `data/extract/<slug>.json` | la même chose, normalisée, pour les scripts |
| `data/raw/<slug>/<date>.json` | la capture brute de l'API, avec les positions des nœuds |
| `data/extract/_rapport-ecart.md` | l'écart entre les notes déjà rédigées et l'état courant de l'amont |
| `tools/roadmap_extract.py` | l'outil d'extraction, si une roadmap manque |

Ta source primaire de travail est `data/extract/<ton-slug>.md`. Pars de là.

## La règle anti-duplication — la contrainte la plus importante

Une notion transverse — RAG, évaluation, SQL, statistiques descriptives, garde-fous —
est expliquée **dans un seul fichier**, sous `content/notions/`, et jamais ailleurs.

Concrètement, dans ta note :

- tu poses un lien `[[notions/<slug>]]` en utilisant **le slug du registre**
  `content/notions/_registre.md`, que tu dois lire avant de commencer ;
- tu n'écris **aucun** fichier dans `content/notions/` — ce n'est pas ton chantier ;
- le fichier cible n'existe probablement pas encore : **c'est normal et voulu**. Un lien
  orphelin est un signal de travail pour la passe de consolidation, pas une erreur ;
- tu ajoutes seulement, en une ou deux phrases, ce que la notion signifie **pour ton
  métier** — l'angle, le piège local, l'usage réel. C'est ton seul droit de spécificité ;
- si une notion te manque dans le registre, tu **ne modifies pas le registre** : tu
  proposes le slug dans ta synthèse, en respectant la convention (français, minuscules,
  tirets, singulier, sans article).

## Ta zone d'écriture

Chaque chantier a une zone d'écriture **exclusive**, précisée dans son prompt. Tu
n'écris nulle part ailleurs. Plusieurs chantiers tournent en parallèle sur le même
dépôt : écrire hors de ta zone écrase le travail d'un autre.

## Le contrat de format

Le format de référence est celui des notes existantes. **Lis
`content/roadmaps/05 - Roadmap — AI Engineer.md` en entier avant d'écrire** : c'est le
gabarit, le niveau de langue et la densité attendus.

En résumé :

- **Frontmatter** : `tags`, `date`, `statut: actif`, `source` (l'URL roadmap.sh d'origine).
- **Un `> [!abstract]`** en ouverture : à qui la note s'adresse, ce qu'elle couvre.
- **Une ligne de provenance** : source, date de capture, date de rédaction.
- **Une vue macro** en Mermaid, puis **une section par grande étape** de la roadmap.
- **Par étape** : un schéma Mermaid, un paragraphe **« À quoi ça sert »** qui explique
  l'intérêt réel et non la définition, une liste **« Ce qu'il faut savoir »** en puces
  courtes et denses, un `> [!tip] Ajout 2026`, un `> [!warning] Piège`.
- **Les nœuds absents de l'amont** apparaissent en vert pointillé :
  `classDef ajout fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px,stroke-dasharray:4 3`
  et le nœud reçoit `:::ajout`.

### Le ton

Le corpus existant a une voix : directe, sans emphase, sans enthousiasme commercial.
Elle dit « à quoi ça sert vraiment » et « voilà l'erreur qu'on voit en vrai ». Elle ne
dit jamais « il est important de noter que ». Écris comme les huit notes existantes,
pas comme une documentation d'éditeur.

### Les sources

Les ressources amont sont dans `data/extract/<slug>.md`, typées `@article`, `@video`,
`@course`, `@official`, `@opensource`, `@feed`. Tu peux les reprendre : elles viennent
de la source officielle.

**Tu n'inventes jamais une URL, un titre d'article, un nom d'auteur ou une date.** Si
tu ajoutes une ressource qui ne vient pas de l'amont, tu l'as vérifiée. Dans le doute,
tu ne la mets pas. Une affirmation technique qui n'est ni sourcée ni évidente est
signalée comme un apport propre dans un encadré `Ajout 2026`.

## Les commits

Commits **granulaires et réguliers**, au fil de l'avancement — un commit par unité
cohérente, pas un gros lot final. Messages en français, à l'impératif ou au substantif.

**Aucune ligne d'attribution.** Pas de `Co-Authored-By`, pas de mention d'un outil ou
d'un assistant dans le message de commit. C'est une règle stricte.

Ne committe que ta zone. Avant de committer, `git add` fichier par fichier, jamais
`git add -A` — un autre chantier travaille peut-être dans le même arbre.

## La restitution

Tu termines par une synthèse à rendre au pilote, **ouverte par la ligne
`SYNTHÈSE DE TÂCHE`** et **fermée par la ligne `FIN DE TÂCHE`**, toutes deux en
majuscules et seules sur leur ligne. Entre les deux, dans cet ordre :

1. **Fichiers créés ou modifiés** — chemin et rôle en une ligne.
2. **Notions appelées** — pour chaque `[[notions/<slug>]]` posé : le slug, et en une
   phrase la définition attendue vue depuis ton métier. Signale ceux absents du registre.
3. **Ressources retenues** — celles que tu juges vraiment utiles, avec leur URL.
4. **Écarts avec l'amont** — ce que tu as ajouté, retiré ou contredit, et pourquoi.
5. **Recouvrements constatés** — ce que ton métier partage avec un autre du lot.
6. **Points ouverts** — ce que tu n'as pas pu trancher et qui demande un arbitrage.

Sois factuel. Si une partie du travail n'a pas abouti, dis-le explicitement plutôt que
de la passer sous silence.
