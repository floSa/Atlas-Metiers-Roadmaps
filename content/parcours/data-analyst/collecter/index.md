---
title: Collecter
aliases:
  - parcours/data-analyst/collecter
---

L'analyste ne construit pas les flux de données, il en dépend entièrement et il est le premier à en constater les défauts. Collecter, ici, veut dire rapatrier le bon sous-ensemble en sachant d'où il vient, de quand il date et ce qu'il exclut.

## Les cinq sujets

```mermaid
flowchart TD
  S["Choisir la source<br/>entrepôt, production, export"]
  F["Les fichiers plats<br/>encodage, séparateur, typage"]
  A["Les API<br/>pagination, quotas, réponse brute"]
  W["Le moissonnage et son cadre<br/>ce qui est légal, pas seulement possible"]
  T["Tracer l'extraction<br/>requête, horodatage, volume"]

  click S "/parcours/data-analyst/collecter/choisir-la-source"
  click F "/parcours/data-analyst/collecter/les-fichiers-plats"
  click A "/parcours/data-analyst/collecter/les-api"
  click W "/parcours/data-analyst/collecter/le-moissonnage-et-son-cadre"
  click T "/parcours/data-analyst/collecter/tracer-l-extraction"
```

**Porte de sortie** : l'extraction se rejoue par script et rend le même nombre de lignes.

## Ma progression

- [ ] [[parcours/data-analyst/collecter/choisir-la-source|Choisir la source]] — l'entrepôt plutôt que la production, et pourquoi le volume se vérifie tout de suite
- [ ] [[parcours/data-analyst/collecter/les-fichiers-plats|Les fichiers plats]] — la première source d'erreurs silencieuses du métier
- [ ] [[parcours/data-analyst/collecter/les-api|Les API]] — lire les quotas avant d'écrire la boucle, garder la réponse brute
- [ ] [[parcours/data-analyst/collecter/le-moissonnage-et-son-cadre|Le moissonnage et son cadre]] — conditions d'utilisation, droit des bases, données personnelles
- [ ] [[parcours/data-analyst/collecter/tracer-l-extraction|Tracer l'extraction]] — les trois métadonnées qui permettent d'expliquer un écart
