---
title: Nettoyer
aliases:
  - parcours/data-analyst/nettoyer
---

La moitié du temps d'une mission, et la partie que personne ne voit. Nettoyer n'est pas appliquer une recette : c'est comprendre pourquoi la donnée est dans cet état, puis décider — en le documentant — ce qu'on en fait.

## Les cinq sujets

```mermaid
flowchart TD
  M["Les valeurs manquantes<br/>le mécanisme, pas le taux"]
  D["Les doublons<br/>définir la clé métier d'abord"]
  A["Les valeurs aberrantes<br/>saisie, unité, ou extrême légitime"]
  T["Transformer et documenter<br/>chaque regroupement est un choix d'analyse"]
  R["Un nettoyage rejouable<br/>brut intact, script par-dessus, assertions"]

  click M "/parcours/data-analyst/nettoyer/les-valeurs-manquantes"
  click D "/parcours/data-analyst/nettoyer/les-doublons"
  click A "/parcours/data-analyst/nettoyer/les-valeurs-aberrantes"
  click T "/parcours/data-analyst/nettoyer/transformer-et-documenter"
  click R "/parcours/data-analyst/nettoyer/un-nettoyage-rejouable"
```

**Porte de sortie** : rien n'a été fait à la main, et le volume de chaque exclusion est écrit.

## Ma progression

- [ ] [[parcours/data-analyst/nettoyer/les-valeurs-manquantes|Les valeurs manquantes]] — trois mécanismes d'absence, trois traitements différents
- [ ] [[parcours/data-analyst/nettoyer/les-doublons|Les doublons]] — dédoublonner sans clé explicite supprime des faits
- [ ] [[parcours/data-analyst/nettoyer/les-valeurs-aberrantes|Les valeurs aberrantes]] — celle qu'on corrige, celle qu'on convertit, celle qu'on garde
- [ ] [[parcours/data-analyst/nettoyer/transformer-et-documenter|Transformer et documenter]] — typage, libellés, regroupements, et la trace de chacun
- [ ] [[parcours/data-analyst/nettoyer/un-nettoyage-rejouable|Un nettoyage rejouable]] — le script depuis la donnée brute et les assertions qui échouent bruyamment
