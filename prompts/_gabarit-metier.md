# Gabarit d'une fiche métier

> Le modèle de référence est `content/parcours/forward-deployed-engineer/index.md`.
> Ouvre-le, ouvre la page rendue, et copie sa structure. Ce document en explique les
> règles ; le fichier en est la preuve qu'elles fonctionnent.

## La page d'entrée d'un métier

Quatre blocs, dans cet ordre, et rien d'autre.

**1. Une phrase.** Ce qu'est le métier. Pas d'encadré, pas de `> [!abstract]`, pas de
ligne de provenance, pas de date. Le lecteur doit savoir en cinq secondes s'il est au
bon endroit.

**2. `## La roadmap`** — un schéma Mermaid dont **chaque nœud est cliquable** :

```
  click S "/parcours/<metier>/<section>"
```

Le chemin est **absolu**, il commence par `/`. Un chemin relatif casse dès qu'on arrive
depuis une page imbriquée. Le nœud porte un libellé court sur deux lignes :
`"Titre<br/>précision courte"`.

**3. `## Ma progression`** — la même liste, en cases à cocher :

```
- [ ] [[parcours/<metier>/<section>|Titre de la section]] — ce qu'on y apprend, en une ligne
```

Quartz retient l'état des cases dans le navigateur, par page. C'est le suivi de
progression : le lecteur coche ce qu'il maîtrise.

**4. Un tableau de positionnement**, facultatif — ce qui distingue ce métier des rôles
voisins. Trois à cinq lignes, pas plus.

## Les pages de section

Une section = une page = **un sujet**. Courte : viser 60 à 120 lignes, jamais 250.
Si une section dépasse, elle se coupe en sous-sections, chacune avec sa page, et la
page de section devient à son tour une petite roadmap avec sa liste à cocher.

Chaque page de section suit le même ordre :

1. **Une phrase** qui dit de quoi il s'agit.
2. **Un schéma Mermaid** — seulement s'il montre un mécanisme. Pas de schéma décoratif.
3. **Ce qu'il faut savoir faire** — des puces courtes, formulées en capacités
   (« déboguer un service sans accès graphique »), pas en connaissances.
4. **Les notions mobilisées** — des liens `[[notions/<slug>]]`, avec une ligne d'angle
   métier chacun. On n'explique jamais une notion ici.
5. **Pour apprendre** — trois à six ressources gratuites, vérifiées, avec ce qu'elles
   apportent en une ligne.

## Ce qui est proscrit

- Les lignes de provenance, les dates de capture, les mentions de chantier.
- Les sections « Comment lire », « Ce que c'est et ce que ce n'est pas », « Lire la
  provenance ». Le lecteur vient pour le métier.
- Les encadrés `> [!abstract]` qui répètent le paragraphe suivant.
- Les titres vides de sens : « Le métier en une page », « En un coup d'œil ».
- Les pages de plus de 250 lignes.
