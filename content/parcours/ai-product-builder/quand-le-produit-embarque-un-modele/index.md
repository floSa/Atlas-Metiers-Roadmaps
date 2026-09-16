---
title: Quand le produit embarque un modèle
aliases:
  - parcours/ai-product-builder/quand-le-produit-embarque-un-modele
---

Jusqu'ici l'IA était l'atelier. À partir du moment où une fonction du produit appelle un modèle, le produit devient aussi un système d'IA — et rien de ce qui suit ne s'explique ici : [[05 - Roadmap — AI Engineer]] le traite une fois pour tout le corpus.

## Les cinq sujets

```mermaid
flowchart TD
  R["Règle ou modèle<br/>la question avant toutes les autres"]
  I["Isoler la fonction à base de modèle<br/>un service, un contrat, un budget"]
  C["Faut-il un corpus<br/>la récupération n'est pas un passage obligé"]
  E["Évaluer ce qui n'est pas binaire<br/>sans jeu de cas, chaque amélioration est un pari"]
  X["Exposer une sortie de modèle<br/>lire un document, déclencher une action"]

  click R "/parcours/ai-product-builder/quand-le-produit-embarque-un-modele/regle-ou-modele"
  click I "/parcours/ai-product-builder/quand-le-produit-embarque-un-modele/isoler-la-fonction-a-base-de-modele"
  click C "/parcours/ai-product-builder/quand-le-produit-embarque-un-modele/faut-il-un-corpus"
  click E "/parcours/ai-product-builder/quand-le-produit-embarque-un-modele/evaluer-ce-qui-n-est-pas-binaire"
  click X "/parcours/ai-product-builder/quand-le-produit-embarque-un-modele/exposer-une-sortie-de-modele"
```

## Ma progression

- [ ] [[parcours/ai-product-builder/quand-le-produit-embarque-un-modele/regle-ou-modele|Règle ou modèle]] — ce qui justifie vraiment un appel probabiliste
- [ ] [[parcours/ai-product-builder/quand-le-produit-embarque-un-modele/isoler-la-fonction-a-base-de-modele|Isoler la fonction à base de modèle]] — changer de fournisseur, dégrader, mesurer
- [ ] [[parcours/ai-product-builder/quand-le-produit-embarque-un-modele/faut-il-un-corpus|Faut-il un corpus]] — le surcoût le plus fréquent est de monter une récupération par réflexe
- [ ] [[parcours/ai-product-builder/quand-le-produit-embarque-un-modele/evaluer-ce-qui-n-est-pas-binaire|Évaluer ce qui n'est pas binaire]] — le point où un product builder échoue le plus souvent
- [ ] [[parcours/ai-product-builder/quand-le-produit-embarque-un-modele/exposer-une-sortie-de-modele|Exposer une sortie de modèle]] — garde-fous, injection indirecte, actions permises
