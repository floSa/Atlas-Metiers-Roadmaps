# 10 — Mise au gabarit d'un métier

Lis `prompts/_gabarit-metier.md`, puis ouvre le modèle de référence
`content/parcours/forward-deployed-engineer/index.md` et sa page rendue sur
`http://localhost:8080/parcours/forward-deployed-engineer/`.

Ta mission : mettre **ton métier** à ce gabarit. Le métier t'est donné dans le message
qui t'envoie ici.

## Le problème à résoudre

Les fiches métier actuelles sont des notes d'une seule traite, de 450 à 750 lignes. On
les lit mal et on ne peut pas s'y repérer. Il faut les transformer en **une page
d'entrée courte avec une roadmap cliquable**, plus **une page par section**, chacune
courte et bâtie pareil.

Le contenu existe déjà et il est bon : tu **découpes et réorganises**, tu ne réécris pas
de zéro. Tu as le droit de couper ce qui est du remplissage.

## Marche à suivre

1. **Lis ta note actuelle en entier** et repère ses grandes sections — il y en a
   généralement entre 5 et 15.
2. **Regroupe-les** en 5 à 8 sections de premier niveau. Une section = un sujet qu'on
   peut apprendre séparément. Si un regroupement dépasse 250 lignes, coupe-le en
   sous-sections avec leurs propres pages.
3. **Crée un dossier** `content/parcours/<ton-slug>/` et écris :
   - `index.md` — la page d'entrée : une phrase, la roadmap Mermaid cliquable, la liste
     à cocher, le tableau de positionnement.
   - une page par section, au gabarit.
4. **Supprime l'ancien fichier** `content/parcours/<ton-slug>.md` s'il existe, ou
   déplace la note historique `content/roadmaps/<numéro> - Roadmap — <nom>.md` dans le
   nouveau dossier en la découpant. Dans les deux cas, `git mv` puis découpage.
5. **Vérifie** que chaque `click` du Mermaid et chaque lien de la liste pointent vers
   une page qui existe, en interrogeant le serveur local :
   `curl -o /dev/null -w '%{http_code}\n' http://localhost:8080/parcours/<slug>/<section>`

## Règles

**Les liens Mermaid sont absolus** : `click X "/parcours/<slug>/<section>"`. Un chemin
relatif casse depuis une page imbriquée.

**Les notions ne sont jamais réexpliquées.** Le corpus a 65 fiches sous
`content/notions/`, avec leur registre dans `content/notions/_registre.md`. Une page de
section pose des liens `[[notions/<slug>]]` et ajoute une ligne d'angle métier. Tu
n'écris rien dans `content/notions/`.

**Les liens qui pointaient vers l'ancien fichier doivent suivre.** Après ton découpage,
cherche qui citait ta note et corrige la cible :
`grep -rn "<ton-ancien-nom>" content --include='*.md'`. Ne corrige que les liens qui
pointent vers toi ; le reste n'est pas ta zone.

**Zone d'écriture exclusive** : `content/parcours/<ton-slug>/`, l'ancien fichier de ta
note, et les liens vers toi dans les autres fichiers. **Rien d'autre.** Plusieurs
métiers sont traités en parallèle dans le même dépôt : `git add` fichier par fichier,
jamais `git add -A`.

**Commits** granulaires, en français, **sans aucune ligne d'attribution**.

## Ce qu'on ne veut plus voir

Relis la section « Ce qui est proscrit » du gabarit. En particulier : plus de ligne de
provenance, plus de date de capture, plus de section « Comment lire », plus d'encadré
qui répète le paragraphe suivant, plus de titre creux type « En un coup d'œil ».

## Restitution

Termine par une synthèse ouverte par `SYNTHÈSE DE TÂCHE` et fermée par `FIN DE TÂCHE`,
donnant : l'arborescence produite, le nombre de lignes par page, les liens vérifiés avec
leur code de réponse, ce que tu as coupé et pourquoi, et les points restés ouverts.
