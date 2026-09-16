---
tags: [notion, sql, bases-de-donnees, requete, data]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-product-builder, data-analyst, bi-analyst]
---

# SQL

Langage déclaratif d'interrogation et de manipulation des bases relationnelles : on décrit le résultat voulu, le moteur choisit comment l'obtenir.

## À quoi ça sert

SQL est l'outil le plus rentable de tout le périmètre data, et de loin. La raison est simple : c'est le seul endroit où le calcul se fait à côté de la donnée. Tout ce qu'une requête agrège, filtre ou joint est du volume qui ne transite pas, qui ne tient pas en mémoire ailleurs et qui n'a pas besoin d'être réconcilié. La plupart des problèmes réputés « de volume » sont des problèmes de requête.

Sa seconde utilité est sociale : une requête est lisible par quelqu'un qui n'est pas développeur. C'est ce qui en fait le support naturel d'une définition métier partagée — une mesure écrite en SQL dans un dépôt peut être relue, discutée et amendée par le contrôle de gestion, ce qu'un notebook ne permet pas.

Le fait déclaratif est aussi la source des mauvaises surprises : deux requêtes qui renvoient le même résultat peuvent coûter mille fois plus l'une que l'autre, et rien dans le texte ne le dit. D'où l'importance du plan d'exécution dès qu'une requête est destinée à tourner souvent.

## Ce qu'il faut savoir

- **Le socle** : `SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`. L'ordre logique d'évaluation n'est pas l'ordre d'écriture — `WHERE` filtre avant l'agrégation, `HAVING` après —, et c'est la source d'erreur la plus fréquente chez les débutants.
- **Jointures** : interne, externe gauche et droite, complète, croisée. Une jointure externe suivie d'un filtre sur la table de droite se comporte comme une jointure interne : le filtre annule ce que la jointure préservait. Vérifier systématiquement que le nombre de lignes ne change pas quand ce n'est pas voulu.
- **Sous-requêtes et CTE** (`WITH`) : la CTE nommée est presque toujours préférable à l'imbrication, parce qu'elle se relit et se teste morceau par morceau. Attention aux CTE récursives, utiles pour les hiérarchies mais coûteuses.
- **Fonctions de fenêtrage** : `ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, `SUM(...) OVER (PARTITION BY ... ORDER BY ...)`. C'est le saut qualitatif du métier — cumuls, variations d'une période à l'autre, déduplication par rang, tout ce qui demandait une auto-jointure devient une ligne. Si une seule chose est à apprendre au-delà des bases, c'est celle-là.
- **Valeurs nulles** : `NULL` n'est pas une valeur mais une absence. `NULL = NULL` est faux, une comparaison avec `NULL` est inconnue, et les agrégats l'ignorent silencieusement — une moyenne calculée sur une colonne à moitié vide est une moyenne sur l'autre moitié.
- **Plan d'exécution** : `EXPLAIN` / `EXPLAIN ANALYZE`. Chercher les balayages complets de table sur les grandes tables, les estimations de cardinalité manifestement fausses, et les jointures dans le mauvais sens.
- **Index** : ils accélèrent la lecture et ralentissent l'écriture. Un index sert s'il couvre les colonnes du filtre dans le bon ordre ; une fonction appliquée à la colonne filtrée le neutralise.
- **Dialectes** : le cœur est standard, les fonctions de date, de chaîne et de fenêtrage avancé ne le sont pas. PostgreSQL, BigQuery, Snowflake et SQL Server divergent précisément là où le travail se fait.

## Selon le métier

### Forward Deployed Engineer

La première requête utile en mission n'est pas métier, c'est un inventaire : combien de lignes, depuis quand, combien de valeurs nulles, quelles valeurs distinctes sur les colonnes censées être normalisées. Elle produit souvent le premier résultat qui impressionne le client, avant toute IA — parce qu'elle montre l'état réel de ses données.

### AI Product Builder

Le besoin est modeste mais non nul : savoir lire le schéma généré, comprendre une jointure, et repérer la requête qui lit toute la table à chaque affichage de page. Un générateur produit volontiers du code qui fonctionne sur cent lignes et s'effondre sur cent mille.

### Data Analyst

C'est l'outil le plus rentable du métier, avant tout le reste. L'essentiel tient dans l'agrégation, les jointures, le fenêtrage et les sous-requêtes. L'optimisation fine et l'administration ne sont pas le sujet ; interroger l'entrepôt plutôt que le système de production l'est.

### BI Analyst

Niveau avancé exigé : fenêtrage, CTE, plans d'exécution. La différence tient à la destination — ses requêtes ne sont pas des réponses mais des **définitions**, écrites une fois et exécutées dix mille fois par un outil de restitution. Le coût et le plan comptent donc autant que le résultat.

> [!warning] Piège
> Découvrir la duplication après l'agrégation. Une jointure sur une clé non unique multiplie les lignes, et la somme qui suit est fausse d'un facteur que personne ne remarque parce que le résultat reste plausible. Le réflexe : compter les lignes avant et après chaque jointure, et vérifier l'unicité de la clé du côté censé être unique.

## Pour aller plus loin

- [SQL Tutorial — Essential SQL For The Beginners](https://www.sqltutorial.org/) — le socle, gratuit et sans détour.
- [25 Advanced SQL Query Examples](https://learnsql.com/blog/25-advanced-sql-query-examples/) — fenêtrage, CTE, agrégations conditionnelles sur des cas réels.
- [Roadmap SQL dédiée](https://roadmap.sh/sql) — le parcours amont si le sujet doit être couvert en profondeur.
- [What is Normalization in DBMS (SQL)? 1NF, 2NF, 3NF, BCNF](https://www.guru99.com/database-normalization.html) — la normalisation, utile pour lire un schéma qu'on n'a pas conçu.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]
- [[parcours/ai-product-builder|AI Product Builder]]
- [[parcours/data-analyst|Data Analyst]]
- [[parcours/bi-analyst|BI Analyst]]

Voisines : [[notions/entrepot-de-donnees]], [[notions/modelisation-dimensionnelle]], [[notions/transformation-dbt]], [[notions/traitement-distribue]].
