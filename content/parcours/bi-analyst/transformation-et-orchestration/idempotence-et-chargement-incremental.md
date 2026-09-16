---
title: Idempotence et chargement incrémental
---

Rejouer un traitement deux fois doit donner le même résultat. Sans cette propriété, aucune reprise sur incident n'est sûre — et un incident finit toujours par arriver un soir de clôture.

```mermaid
flowchart LR
  P["Date de référence<br/>passée en paramètre"] --> D["Suppression de la fenêtre traitée"]
  D --> I["Réinsertion de la fenêtre"]
  I --> R["Résultat identique<br/>quel que soit le nombre de rejeux"]
```

## Ce qu'il faut savoir faire

- Supprimer puis réinsérer la fenêtre traitée, plutôt qu'ajouter. L'ajout est plus rapide et rend chaque reprise dangereuse ; la suppression-réinsertion est la seule forme qui supporte d'être rejouée sans réfléchir.
- Faire dépendre le traitement d'une date de référence **passée en paramètre**, jamais de la date du jour. C'est ce qui permet de rattraper une journée manquante trois semaines plus tard sans réécrire le code.
- Recourir à l'incrémental dès que le volume dépasse ce qu'un rechargement complet peut absorber dans la fenêtre nocturne — et pas avant. Le rechargement complet est plus simple, plus sûr, et suffit bien plus longtemps qu'on ne le croit.
- Prévoir le rattrapage de la donnée en retard : un rechargement complet périodique, ou une fenêtre de reprise glissante sur quelques jours. L'incrémental strict laisse des trous silencieux que rien ne signale.
- Isoler la clé de rejeu dans le modèle — la partition, la fenêtre, le lot. Si on ne sait pas nommer ce qu'on rejoue, le traitement n'est pas idempotent, quelle que soit la façon dont il est écrit.
- Mesurer le coût du rechargement complet avant de le remplacer. Beaucoup de chaînes passent à l'incrémental pour économiser une ressource qui n'était pas le goulet, et achètent une classe de bugs en échange.

## Les notions mobilisées

- [[notions/orchestration-de-flux]] — la reprise, le rattrapage et les fenêtres d'exécution sont des propriétés de l'ordonnanceur autant que du code.
- [[notions/transformation-dbt]] — les matérialisations incrémentales et leurs stratégies de fusion, avec leurs pièges propres.
- [[notions/qualite-des-donnees]] — un trou d'incrémental ne se voit que par un test de complétude sur la période.
- [[notions/tests-logiciels]] — l'idempotence est une propriété qui se teste, en rejouant deux fois et en comparant.

> [!warning] Piège
> L'incrémental fondé sur une colonne de dernière modification que la source met à jour de façon incomplète. Le traitement ne voit jamais les lignes modifiées par un traitement batch côté applicatif, l'écart s'accumule sans aucun signal, et il se découvre lors d'une réconciliation annuelle. Vérifier cette colonne sur un échantillon avant de s'y fier.

## Pour apprendre

- [Documentation Airflow](https://airflow.apache.org/docs) — rattrapage, exécutions datées et reprise, expliqués par l'ordonnanceur de référence.
- [Documentation Prefect](https://docs.prefect.io/v3/get-started) — le même problème avec un modèle d'exécution plus souple, utile en comparaison.
- [Documentation dbt](https://docs.getdbt.com/docs/build/documentation) — les matérialisations incrémentales et ce qu'elles supposent du modèle.
