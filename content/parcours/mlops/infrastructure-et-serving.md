---
title: Infrastructure et serving
tags: [parcours, mlops, cloud, docker, kubernetes, gpu, terraform, edge]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/mlops
---

Où le modèle s'exécute réellement : le cloud pour l'élasticité par à-coups, le conteneur pour la reproductibilité, l'ordonnanceur pour partager des GPU rares — et l'embarqué quand la donnée ne doit pas sortir.

```mermaid
flowchart TD
  CT["Conteneurisation<br/>l'image d'inférence et son coût de démarrage"]
  PL["Plateforme de déploiement<br/>machine, cluster, service géré, périphérie"]
  CO["Coût et latence d'inférence<br/>ce qui décide de la viabilité"]
  AC["Contrôle d'accès<br/>secrets, identités éphémères, moindre privilège"]
  CH["Chaîne d'approvisionnement logicielle<br/>images de base et poids téléchargés"]

  click CT "/notions/conteneurisation"
  click PL "/notions/plateforme-de-deploiement"
  click CO "/notions/cout-et-latence-inference"
  click AC "/notions/controle-d-acces"
  click CH "/notions/chaine-d-approvisionnement-logicielle"
```

## Entraîner et servir ne demandent pas la même chose

L'entraînement tolère la latence et déteste le coût : il tourne par à-coups, sur des ressources chères, et gagne à utiliser des instances interruptibles avec des points de reprise réguliers. Le service tolère le coût et déteste la latence : il tourne en permanence, et son ennemi est le démarrage à froid.

Les faire cohabiter dans le même code est la première source d'écart entraînement-service. Les séparer proprement, avec une bibliothèque de transformation partagée mais deux chemins d'exécution, est l'une des rares décisions d'architecture qu'on ne regrette jamais.

## Ce qu'il faut savoir faire

- **Réduire une image d'inférence.** Construction à étapes multiples, base mince, roues pour processeur uniquement quand il n'y a pas de GPU. Une image de huit gigaoctets multiplie le démarrage à froid par dix, ce qui interdit la mise à l'échelle rapide.
- **Partager un GPU** : greffon matériel du fournisseur, ressource déclarée, et une stratégie de partage — partitionnement matériel ou découpage temporel — quand plusieurs modèles se disputent une carte.
- **Décrire l'infrastructure de façon déclarative**, avec état distant verrouillé : deux applications concurrentes sans verrou corrompent l'état, et la préproduction qui ne ressemble pas à la production ne teste rien.
- **Ne jamais stocker un secret en clair** dans un état d'infrastructure ou une variable d'environnement : coffre dédié, rôles à durée limitée, authentification fédérée entre la chaîne d'intégration et le fournisseur.
- **Arbitrer entre service géré et infrastructure propre.** Les plateformes ML des fournisseurs accélèrent le démarrage et enferment durablement ; le compromis est acceptable pour l'entraînement, plus discutable pour le service, où le verrouillage est le plus coûteux à défaire.
- **Évaluer un modèle quantifié sur le jeu complet et par segment** avant de l'embarquer : la quantification dégrade rarement la métrique globale et souvent lourdement certaines classes rares.

> [!tip] Ajout 2026
> Deux pratiques ont fortement baissé la facture. **L'autoscaling à zéro** sur les modèles peu sollicités : on ne paie le GPU que pendant les requêtes, au prix d'un démarrage à froid qu'on atténue en préchargeant les poids sur un volume rapide. Et les **instances interruptibles** pour l'entraînement avec points de reprise réguliers, qui divisent le coût des travaux longs à condition que le travail sache reprendre. Côté embarqué, **ONNX Runtime** s'est imposé comme cible portable intermédiaire : on exporte une fois et on vise plusieurs environnements matériels sans réécrire le pipeline.

> [!warning] Piège
> Mettre un ordonnanceur de conteneurs complet sous un seul modèle à faible trafic. Le coût d'exploitation du cluster dépasse largement celui d'un conteneur sur une machine, et il se paie en temps d'ingénieur, pas en facture — donc il ne se voit pas. Surveiller aussi la dérive de configuration : un correctif appliqué à la main dans une console, jamais reporté dans le code, casse la production au déploiement suivant.

## Les notions mobilisées

- [[notions/conteneurisation]] — l'image est le livrable ; sa taille est un paramètre de latence, pas un détail d'esthétique.
- [[notions/plateforme-de-deploiement]] — machine, ordonnanceur, service géré ou périphérie : quatre modèles de coût et quatre profils de verrouillage.
- [[notions/cout-et-latence-inference]] — ce qui décide de la viabilité économique d'un modèle servi, et se mesure par prédiction.
- [[notions/controle-d-acces]] — secrets, identités à durée limitée, moindre privilège sur les ressources d'entraînement comme de service.
- [[notions/chaine-d-approvisionnement-logicielle]] — images de base et poids de modèles téléchargés : à épingler par empreinte, comme n'importe quelle dépendance.

## Pour apprendre

- [Docker Documentation](https://docs.docker.com/) — les constructions à étapes multiples et l'ordre des couches, d'où vient l'essentiel du gain.
- [Kubernetes Documentation](https://kubernetes.io/docs/home/) — objets de base, requêtes et limites, et l'ordonnancement de ressources rares.
- [KServe — Documentation](https://kserve.github.io/website/latest/) — le service de modèles sur cluster, avec mise à l'échelle jusqu'à zéro.
- [Terraform Tutorials](https://learn.hashicorp.com/terraform) — l'infrastructure déclarative, état distant et modules compris.
- [ExecuTorch — Documentation](https://docs.pytorch.org/executorch/stable/index.html) — la voie PyTorch vers les cibles embarquées contraintes.
- [TensorFlow Lite Guide](https://www.tensorflow.org/lite/guide) — quantification et délégués matériels pour mobile et microcontrôleurs.
