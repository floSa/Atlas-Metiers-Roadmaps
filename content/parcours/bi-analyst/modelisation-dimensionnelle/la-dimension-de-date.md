---
title: La dimension de date
---

Toujours une table réelle, jamais un calcul à la volée. Elle porte le calendrier de l'entreprise, qui n'est presque jamais le calendrier civil — et c'est la table la plus rentable de tout l'entrepôt.

```mermaid
flowchart TD
  SE["Séries temporelles<br/>tendance, saisonnalité, effets de calendrier"]
  MD["Modélisation dimensionnelle<br/>la dimension conformée par excellence"]
  SQ["SQL<br/>le partitionnement qui en découle"]
  AC["Analyse de cohorte<br/>les fenêtres d'observation s'y appuient"]

  click SE "/notions/series-temporelles"
  click MD "/notions/modelisation-dimensionnelle"
  click SQ "/notions/sql"
  click AC "/notions/analyse-de-cohorte"
```

## Ce qu'il faut savoir faire

- Construire la table avec une ligne par jour et, pour chacun, son mois, son trimestre, son exercice fiscal, ses semaines, ses jours ouvrés, ses jours fériés et ses périodes comparables. Elle se génère en une requête et sert tous les jours.
- Y inscrire le calendrier **fiscal** de l'entreprise, pas seulement le civil. Beaucoup d'exercices ne commencent pas en janvier, et une comparaison annuelle calculée sur le calendrier civil est simplement fausse pour la finance.
- Y porter les périodes comparables explicitement — « même période l'an dernier », « à date », « cumul depuis le début de l'exercice ». Recalculer ces bornes dans chaque rapport garantit qu'elles divergeront.
- Marquer les jours ouvrés et les jours fériés, et les exposer au métier. La position d'un jour férié et le décalage des semaines d'une année sur l'autre expliquent une grande part des variations qu'on attribue à une action commerciale.
- Prévoir les cas particuliers de l'entreprise : périodes de clôture, saisons commerciales, semaines de campagne. C'est ce qui fait la différence entre une dimension générique et une dimension utile.
- Utiliser la clé de date comme axe de partitionnement de la table de faits. La même décision sert à la fois la lisibilité du modèle et la facture du moteur.

## Les notions mobilisées

- [[notions/series-temporelles]] — les effets de calendrier, que seule une vraie table de date permet d'isoler proprement.
- [[notions/modelisation-dimensionnelle]] — la dimension de date est le cas d'école de la dimension conformée.
- [[notions/sql]] — le partitionnement et les fonctions de fenêtre s'appuient sur cette clé.
- [[notions/analyse-de-cohorte]] — les fenêtres d'observation se définissent en jours ouvrés aussi souvent qu'en jours calendaires.

> [!tip] Ce qu'on regrette de ne pas y avoir mis
> Une colonne « jour comparable de l'an dernier », calculée selon la règle retenue par l'entreprise — même date, ou même position dans la semaine. C'est la règle qui change d'un service à l'autre, et la porter dans la table plutôt que dans les rapports règle le débat une fois.

## Pour apprendre

- [Engineering Statistics Handbook, séries temporelles — NIST](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm) — la décomposition tendance-saisonnalité, qui suppose un calendrier propre.
- [Star Schema vs Snowflake Schema](https://www.thoughtspot.com/data-trends/data-modeling/star-schema-vs-snowflake-schema) — la place de la dimension de date dans le modèle.
- [SQL Window Functions](https://www.thoughtspot.com/sql-tutorial/sql-window-functions) — les comparaisons de périodes, une fois la dimension en place.
