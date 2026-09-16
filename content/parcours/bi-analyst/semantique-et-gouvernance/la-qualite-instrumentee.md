---
title: La qualité instrumentée
---

Niveau attendu : **autonomie**. Les tests de qualité se conçoivent et se calibrent, mais la réconciliation suppose un interlocuteur métier qui reste propriétaire de son chiffre.

Une dimension de qualité qui n'est pas un test automatisé n'est pas gérée : elle est espérée. L'enjeu n'est pas la conformité, c'est de savoir qu'un chiffre est valide **avant** que quelqu'un le découvre faux.

```mermaid
flowchart TD
  QD["Qualité des données<br/>les six dimensions et leurs tests"]
  OB["Observabilité<br/>volumes, distributions, pannes silencieuses"]
  TL["Tests logiciels<br/>la discipline, appliquée aux données"]
  GO["Gouvernance de l'IA<br/>ce qui tient quand personne ne maintient"]

  click QD "/notions/qualite-des-donnees"
  click OB "/notions/observabilite"
  click TL "/notions/tests-logiciels"
  click GO "/notions/gouvernance-ia"
```

## Ce qu'il faut savoir faire

- Traduire les six dimensions en tests exécutables : exactitude (comparaison à une source de référence), complétude (aucune valeur manquante sur les colonnes structurantes), unicité (clé sans doublon), fraîcheur (dernière donnée à moins de N heures), validité (valeurs dans la liste autorisée), cohérence (les totaux se réconcilient entre deux tables).
- Mettre la **réconciliation avec la source métier** en tête de liste. C'est le contrôle le plus rentable : il attrape les pannes d'ingestion, les doublons et les erreurs de grain d'un seul coup, et c'est le seul que le métier comprend immédiatement.
- Afficher la date et l'heure du dernier rafraîchissement **sur** le tableau de bord, visible. Un chiffre périmé qui se présente comme à jour cause plus de dégâts qu'un chiffre absent, et c'est la correction la moins chère de tout le sujet.
- Négocier un **contrat de données** avec les équipes sources : une entente écrite et courte où l'équipe applicative s'engage sur un schéma, une fraîcheur et un préavis. Cela transforme une rupture de schéma d'accident subi en engagement rompu.
- Traiter l'accessibilité et l'interprétabilité comme des dimensions de qualité, pas comme du confort. Une donnée juste que personne ne trouve ou dont personne ne comprend le libellé ne sert à rien ; un nom de colonne compréhensible fait plus pour la qualité perçue que trois tests supplémentaires.
- Se demander devant toute initiative de gouvernance : qu'est-ce qui se passe si personne ne la maintient ? Si la réponse est « rien ne casse, ça se périme », elle ne sera pas maintenue.

## Les notions mobilisées

- [[notions/qualite-des-donnees]] — les six dimensions ; l'angle BI est leur traduction en tests bloquants.
- [[notions/observabilite]] — la détection d'anomalie sur les volumes et les distributions, qui attrape ce que les tests de schéma laissent passer.
- [[notions/tests-logiciels]] — la discipline du test, y compris la règle « un incident donne un test avant sa correction ».
- [[notions/gouvernance-ia]] — ce qui distingue une gouvernance qui tient d'un catalogue périmé avant d'être terminé.

> [!warning] Piège
> Faire de la gouvernance un projet documentaire. Un catalogue rempli à la main par une équipe dédiée est périmé avant d'être terminé, parce que rien ne force sa mise à jour. Ce qui tient dans le temps est ce qui est **généré depuis le code** — lignage, documentation, tests — et ce qui bloque la chaîne quand c'est faux.

## Pour apprendre

- [What Is Data Quality? — IBM](https://www.ibm.com/think/topics/data-quality) — les définitions de référence des six dimensions.
- [Documentation dbt](https://docs.getdbt.com/docs/build/documentation) — les tests attachés aux modèles, et la documentation générée depuis eux.
- [Documentation Grafana](https://grafana.com/docs/) — pour surveiller volumes et distributions hors de l'outil décisionnel.
