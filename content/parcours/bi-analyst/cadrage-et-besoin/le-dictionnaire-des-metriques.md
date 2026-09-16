---
title: Le dictionnaire des métriques
---

Niveau attendu : **référence**. L'artefact qui transforme un désaccord en diff appartient à ce poste, et il ne vaut que si quelqu'un en fait autorité.

Un fichier par domaine, une entrée par métrique, cinq lignes chacune, dans le dépôt. Ça coûte deux jours et ça supprime la moitié des désaccords ultérieurs, parce que le désaccord devient un diff au lieu d'une discussion de couloir.

Les cinq lignes d'une entrée complète :

```mermaid
flowchart TD
  L["Libellé métier<br/>le nom que le métier emploie"]
  F["Formule<br/>le calcul, sans ambiguïté"]
  G["Grain<br/>par jour, par client, par commande"]
  S["Source de vérité<br/>la table qui fait foi"]
  P["Propriétaire<br/>la personne qui tranche"]

  click L "/notions/redaction-technique"
  click F "/parcours/bi-analyst/semantique-et-gouvernance/definir-une-mesure"
  click G "/parcours/bi-analyst/modelisation-dimensionnelle/declarer-le-grain"
  click S "/notions/lignage-des-donnees"
  click P "/notions/gouvernance-ia"
```

## Ce qu'il faut savoir faire

- Écrire le dictionnaire **avant le premier modèle**, en Markdown, versionné au même endroit que le code de transformation. Un dictionnaire qui vit dans un tableur partagé diverge du code en trois mois.
- Ne jamais omettre la cinquième ligne. Sans le nom d'une personne — pas d'une direction — les quatre premières seront rediscutées tous les six mois, et personne ne saura qui a le mandat de clore le débat.
- Nommer distinctement deux mesures proches plutôt que de choisir entre elles. « Chiffre d'affaires facturé » et « chiffre d'affaires commandé » cohabitent sans dommage ; « chiffre d'affaires » tout court, employé pour les deux, produit le désaccord permanent.
- Traiter le dictionnaire comme la source de la couche sémantique, pas comme sa documentation. Ce qui s'écrit ici doit se convertir en définitions exécutables — c'est la seule documentation qui ne se périme pas, parce qu'elle est le code.
- Tenir en regard un **journal des décisions** : une entrée par arbitrage, avec la date, les deux positions, ce qui a été tranché et par qui. Cinq minutes par décision, et la réouverture du débat six mois plus tard est réglée d'avance.
- Publier le dictionnaire là où le métier le lit — pas seulement dans le dépôt. Un dictionnaire que seuls les analystes consultent n'arbitre rien.

## Les notions mobilisées

- [[notions/redaction-technique]] — un format court, stable et contraint vaut mieux qu'une documentation riche que personne ne tient à jour.
- [[notions/cadrage-besoin]] — chaque entrée du dictionnaire est le produit fini d'un cadrage, et rien d'autre ne doit y entrer.
- [[notions/lignage-des-donnees]] — la ligne « source de vérité » n'a de valeur que si elle est vérifiable par le lignage réel.
- [[notions/gouvernance-ia]] — le dictionnaire est le premier objet de gouvernance qui survit, parce qu'il est utilisé quotidiennement plutôt que rempli une fois.

> [!tip] Le format qui tient
> Une entrée par fichier ou une par section, jamais un tableau unique. Le tableau devient illisible passé trente lignes, et surtout il produit des conflits de fusion sur chaque modification. Un fichier par métrique rend chaque changement lisible en revue, ce qui est précisément l'effet recherché.

## Pour apprendre

- [Documentation dbt](https://docs.getdbt.com/docs/build/documentation) — comment la description d'un modèle et d'une colonne devient de la documentation générée et versionnée.
- [Roadmap Technical Writer](https://roadmap.sh/technical-writer) — les principes de rédaction qui font qu'une définition est lue et comprise du premier coup.
- [5 Principles of Data Ethics for Business](https://online.hbs.edu/blog/post/data-ethics) — utile sur la documentation du périmètre, qui appartient à la définition d'une métrique.
