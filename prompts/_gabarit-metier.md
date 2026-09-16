# Gabarit — l'arbre et ses pages

> Le modèle de référence est `content/parcours/forward-deployed-engineer/`. Ouvre-le,
> ouvre les pages rendues sur `http://localhost:8080`, et copie leur comportement.

## Le principe

Le site est un **arbre à tiroirs**. À chaque étage, le lecteur voit une carte de ce
qu'il y a à apprendre, clique sur une case, descend d'un cran. Il remonte par le fil
d'Ariane. Il descend jusqu'à une page unitaire qui explique une chose et renvoie vers
les ressources pour l'apprendre.

```
Accueil          les métiers
 └── Métier      la roadmap du métier
      └── Domaine        la carte des sous-domaines
           └── Sous-domaine   la carte des notions
                └── Notion    la feuille : explication et ressources
```

Cinq étages au maximum. Une branche peut être moins profonde, jamais plus.

## La règle qui gouverne tout

**Une case dans un schéma mène toujours quelque part.** Si un sujet n'a pas de page, il
n'a pas de case : il est dans le texte.

C'est ce qui rend la navigation prévisible. Un lecteur qui voit une boîte doit pouvoir
cliquer dessus, sans avoir à deviner lesquelles sont actives.

```
  click N1 "/parcours/<metier>/<domaine>/<sous-domaine>"
  click N2 "/notions/<slug>"
```

Le chemin est **absolu**, il commence par `/`. Un chemin relatif casse dès qu'on y
arrive depuis une page imbriquée. **Vérifie chaque cible** :
`curl -o /dev/null -w '%{http_code}\n' http://localhost:8080/<le-chemin>`

Seule exception : sur une page-feuille, un schéma qui montre un **mécanisme** — un
enchaînement, un flux, une boucle — n'est pas une carte et n'a pas à être cliquable.
Une liste de boîtes côte à côte est toujours une carte.

## Une page d'aiguillage — courte

Une page qui aiguille ne contient que trois choses, et **tient en 40 lignes** :

1. **Une phrase.** Ce que couvre cet étage.
2. **La carte.** Un schéma Mermaid dont chaque case est cliquable. Le libellé tient sur
   deux lignes : `"Titre<br/>précision courte"`.
3. **Ma progression.** La même liste, en cases à cocher, que le navigateur retient :

```
- [ ] [[chemin/vers/la/page|Titre]] — ce qu'on y apprend, en une ligne
```

Pas de tableau d'explication, pas d'encadré, pas de préambule. Tout ce qui explique
descend d'un étage. Si une information est déjà dans le libellé d'une case, elle ne se
répète pas en dessous.

## Une page-feuille

Elle explique **une chose** et donne de quoi l'apprendre. Viser 40 à 90 lignes.

1. **Une phrase** qui dit de quoi il s'agit, et le niveau attendu s'il y a lieu.
2. **Un schéma de mécanisme**, seulement s'il montre comment ça marche.
3. **Ce qu'il faut savoir faire** — des puces formulées en capacités
   (« déboguer un service sans accès graphique »), pas en connaissances.
4. **Les notions mobilisées** — des liens `[[notions/<slug>]]` avec une ligne d'angle
   métier chacun. On n'explique jamais une notion ici : elle a sa propre page.
5. **Pour apprendre** — trois à six ressources gratuites et vérifiées, avec ce qu'elles
   apportent en une ligne.

Un ou deux encadrés `> [!warning]` ou `> [!tip]` sont permis s'ils portent une vraie
mise en garde de terrain.

## Proscrit, partout

- Les lignes de provenance, dates de capture, mentions de chantier ou de roadmap amont.
- Les sections « Comment lire », « Ce que c'est et ce que ce n'est pas », « En un coup
  d'œil », « Le métier en une page ».
- Les encadrés `> [!abstract]` qui répètent le paragraphe suivant.
- Les comparaisons entre métiers : elles vivent toutes dans `content/ne-pas-confondre.md`.
- Les couleurs de remplissage écrites en dur dans un `classDef` : elles cassent en thème
  sombre. Le contour suffit — `classDef ajout stroke:#2e7d32,stroke-dasharray:4 3`.
- Toute page de plus de 120 lignes.
