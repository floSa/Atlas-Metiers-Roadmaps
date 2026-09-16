---
title: Cadencer la mission
---

Niveau attendu : **autonomie**. Séquencer par le risque et renégocier un périmètre se conçoivent et se défendent seul, mais la cadence se partage avec la direction de projet du client — ce n'est pas là que le FDE fait autorité.

Le triangle périmètre, vitesse, qualité — et l'ordre dans lequel on attaque, qui compte davantage.

```mermaid
flowchart TD
  R["Séquencer par le risque<br/>d'abord ce qui peut tuer la mission"]
  P["Réduire le périmètre<br/>le seul levier sans dette"]
  D["Démonstration hebdomadaire<br/>le rythme qui fait remonter les objections"]
  U["Observer l'usage réel<br/>les journaux, pas les déclarations"]

  click R "/notions/cadrage-besoin"
  click P "/notions/roi-des-projets-ia"
  click D "/notions/gestion-parties-prenantes"
  click U "/notions/mesure-d-usage-produit"
```

## Ce qu'il faut savoir faire

- Séquencer par le risque et non par la valeur perçue : l'intégration la plus incertaine d'abord, la fonctionnalité la plus démonstrative ensuite. L'ouverture d'un flux réseau vers l'ERP n'impressionne personne en comité, et c'est elle qui décide du sort du projet.
- Répondre à une contrainte de délai par une réduction de périmètre, en faisant comprendre au client ce qu'il abandonne — d'où l'arbitrage écrit.
- Placer les délais organisationnels sur le chemin critique : validation sécurité, accès aux données, avis du délégué à la protection des données. Ils ne s'accélèrent pas avec plus d'ingénieurs.
- Fixer au cadrage une date de mise en service partielle, très en amont de la fin de mission, et la traiter comme intangible : tout ce qui est prêt part, le reste attend.
- Montrer quelque chose chaque semaine, même minuscule. C'est le rythme qui entretient la confiance et fait remonter les objections tant qu'elles coûtent peu.

## Les notions mobilisées

- [[notions/cadrage-besoin]] — l'angle FDE est que le périmètre se renégocie en continu, pas une fois au démarrage.
- [[notions/roi-des-projets-ia]] — ce qu'on abandonne en réduisant le périmètre doit être chiffré, sinon la discussion se fait à l'affect.
- [[notions/gestion-parties-prenantes]] — la démonstration hebdomadaire est d'abord un dispositif relationnel : elle rend les objections bon marché.
- [[notions/mesure-d-usage-produit]] — ce que les gens disent d'un outil et ce que les journaux montrent divergent systématiquement.

> [!warning] Piège
> Accepter chaque demande pour entretenir la relation. C'est le mode d'échec propre au métier : le FDE est sur place, disponible, et chaque ajout paraît minime. Au bout de deux mois le périmètre a doublé, rien n'est en service, et la relation se dégrade bien plus qu'avec un refus argumenté au premier jour.
