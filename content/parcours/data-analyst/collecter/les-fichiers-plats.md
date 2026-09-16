---
title: Les fichiers plats
---

Niveau attendu : **autonomie**. Un CSV mal lu ne lève aucune erreur, donc aucune documentation ne prévient : il faut déboguer un encodage ou un typage silencieux sans filet.

Le format d'échange universel et la première source d'erreurs silencieuses du métier. Un CSV mal lu ne lève aucune erreur : il produit des données plausibles et fausses.

```mermaid
flowchart LR
  F["Fichier reçu"] --> E["Encodage<br/>UTF-8 ou Latin-1, les accents le disent"]
  E --> S["Séparateur<br/>virgule ou point-virgule, décimal compris"]
  S --> T["Typage imposé<br/>dates, identifiants, montants"]
  T --> C["Contrôle<br/>lignes comptées, colonnes attendues"]
  C --> P["Conversion en Parquet<br/>types conservés pour la suite"]
```

## Ce qu'il faut savoir faire

- Regarder les premières lignes du fichier brut avant de le charger. L'encodage, le séparateur, la présence d'un en-tête et les guillemets se voient en dix secondes et évitent une heure de diagnostic.
- Imposer le type des colonnes à la lecture au lieu de laisser l'inférence décider. L'identifiant client lu comme un entier perd son zéro initial ; la date américaine une ligne sur deux devient un mois.
- Reconnaître les pièges francophones : le point-virgule comme séparateur, la virgule comme séparateur décimal, l'espace insécable comme séparateur de milliers. Un montant sur trois est alors lu comme du texte, et l'agrégat est silencieusement faux.
- Compter les lignes du fichier et les comparer aux lignes chargées. L'écart signale un saut de ligne dans un champ texte non protégé, le mode d'échec le plus courant des exports mal générés.
- Convertir en Parquet dès que le fichier dépasse quelques centaines de milliers de lignes, et travailler sur cette version : types conservés, lecture par colonne, relecture immédiate.
- Conserver le fichier d'origine intact, avec sa date de réception. C'est la seule référence quand un écart apparaît trois semaines plus tard.

## Les notions mobilisées

- [[notions/collecte-de-donnees]] — le fichier reçu est une extraction faite par quelqu'un d'autre : ses métadonnées manquent et se redemandent.
- [[notions/qualite-des-donnees]] — validité et complétude se testent à la lecture, pas après les premières agrégations.
- [[notions/pandas]] — les options de lecture qui évitent la moitié des problèmes : types explicites, format de date, séparateur décimal.
- [[notions/traitement-distribue]] — le format colonne et pourquoi il remplace le CSV comme format de travail intermédiaire.

> [!tip] Le contrôle en trois lignes
> Après tout chargement : le nombre de lignes, le nombre de colonnes, et le type de chacune. Écrits en assertions plutôt que regardés une fois, ils échouent bruyamment le jour où la source change de format — ce qui arrive sans prévenir et sans annonce.

## Pour apprendre

- [RFC 4180](https://www.rfc-editor.org/rfc/rfc4180) — la spécification du CSV, courte, et utile surtout pour comprendre à quel point elle est peu respectée.
- [DuckDB — Import CSV](https://duckdb.org/docs/stable/data/csv/overview) — le lecteur le plus tolérant et le plus explicite sur ce qu'il a deviné.
- [pandas — Lecture et écriture](https://pandas.pydata.org/docs/user_guide/io.html) — la liste complète des options de typage et de format, à garder sous la main.
- [Apache Parquet](https://parquet.apache.org/) — le format qui supprime le problème pour toutes les étapes suivantes.
