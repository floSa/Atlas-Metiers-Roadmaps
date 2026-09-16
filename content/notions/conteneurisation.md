---
tags: [notion, conteneurisation, docker, kubernetes, deploiement]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-red-teaming]
---

# Conteneurisation

Empaquetage d'une application avec ses dépendances dans une image exécutable isolée du système hôte, de manière à ce qu'elle se comporte de la même façon partout où elle tourne.

## À quoi ça sert

Le conteneur résout un problème qui a coûté des décennies d'heures : l'écart entre l'environnement de développement et celui de production. En figeant les dépendances dans l'image, on transforme « ça marche chez moi » en propriété vérifiable.

Son second apport est l'isolation, et elle a une valeur de sécurité directe : un processus qui exécute du code dont on ne maîtrise pas l'origine — code généré par un modèle, outil tiers, traitement d'un fichier reçu — doit tourner dans un conteneur jetable, sans réseau et sans secret. C'est une des rares mesures qui transforme une exécution arbitraire en incident borné.

Le troisième usage est contractuel : l'image est un artefact daté, signé et reproductible. C'est ce qu'on livre, ce qu'on audite et ce qu'on redéploie à l'identique.

## Ce qu'il faut savoir

- **Une image se construit en couches** et se met en cache par couche. Ordonner du plus stable au plus variable — dépendances d'abord, code ensuite — divise les temps de construction.
- **Construction en plusieurs étapes** : compiler dans une image outillée, copier le résultat dans une image minimale. L'image finale ne doit contenir ni compilateur, ni gestionnaire de paquets, ni secret.
- **Épingler les versions**, y compris celle de l'image de base. Une base référencée par un simple `latest` n'est pas reproductible, et ce qui n'est pas reproductible n'est pas auditable.
- **Les secrets ne vont jamais dans l'image.** Ils sont injectés à l'exécution, et une couche qui en a contenu les conserve même si une couche ultérieure les supprime.
- **Ne pas tourner en `root`** dans le conteneur, monter le système de fichiers en lecture seule quand c'est possible, et limiter les capacités. L'isolation par défaut est moins forte qu'on ne le suppose.
- **Analyser les images** pour les vulnérabilités connues, à chaque construction, dans la chaîne d'intégration. Une image construite il y a six mois accumule des failles sans que rien ne change.
- **Kubernetes est une réponse à un problème d'échelle et d'exploitation**, pas une étape obligatoire. Un conteneur sur une plateforme applicative couvre la majorité des besoins réels ; l'orchestrateur se justifie quand il y a une équipe pour l'exploiter.
- **Les charges GPU** ont leurs contraintes propres — pilotes, bibliothèques, taille des images. Elles se traitent séparément.

## Selon le métier

### Forward Deployed Engineer

L'image doit se construire **hors ligne, depuis le registre interne du client**, sans accès direct aux dépôts publics. Les bases d'images imposées par la sécurité du client sont rarement récentes, et c'est une contrainte à découvrir en phase d'audit plutôt qu'au premier déploiement. Corollaire : aucune installation qui suppose un accès Internet non filtré.

### AI Red Teaming

Le conteneur est ici un contrôle à vérifier, pas une commodité. Dès qu'une sortie de modèle atteint un interpréteur — code généré puis exécuté, requête, gabarit —, l'exécution doit se faire dans un conteneur jetable sans réseau ni secret. Les points d'audit habituels : exécution en `root`, socket Docker monté dans le conteneur, secrets en variables d'environnement lisibles, image de base non mise à jour.

> [!warning] Piège
> Traiter le conteneur comme une frontière de sécurité équivalente à une machine virtuelle. Il partage le noyau de l'hôte, et une évasion reste possible via une configuration trop permissive — privilèges étendus, montages hôte, socket du démon exposé. Pour du code réellement non fiable, l'isolation doit être renforcée, pas supposée.

## Pour aller plus loin

- [What is a Container? — Docker](https://www.docker.com/resources/what-container/) — le concept, par la source.
- [What are Containers? — Google Cloud](https://cloud.google.com/learn/what-are-containers) — la même chose sous l'angle exploitation.
- [A Data Scientist's Guide to Docker Containers](https://towardsdatascience.com/a-data-scientists-guide-to-docker-containers/) — l'angle data, avec les pièges de dépendances scientifiques.

## Appelée par

- [[parcours/forward-deployed-engineer|Forward Deployed Engineer]]
- [[parcours/ai-red-teaming|AI Red Teaming]]

Voisines : [[notions/integration-continue]], [[notions/plateforme-de-deploiement]], [[notions/chaine-d-approvisionnement-logicielle]].
