---
title: Chaîne d'approvisionnement logicielle
tags: [notion, supply-chain, dependances, poids-de-modele, provenance]
date: 2026-09-16
statut: actif
appelee-par: [ai-red-teaming, forward-deployed-engineer]
---

Ensemble de ce qu'un système exécute sans l'avoir écrit : bibliothèques, images de base, poids de modèles, serveurs d'outils, extensions — et les mécanismes qui permettent de savoir d'où cela vient et si cela a été altéré.

## À quoi ça sert

Un système d'IA est une application avec des dépendances lourdes : des paquets, des conteneurs, des fichiers de poids téléchargés, des serveurs d'outils installés en quelques minutes. Chacun exécute du code avec les droits de son hôte, et le fait que l'application invoque un modèle n'efface aucune des vulnérabilités habituelles.

Ce qui a changé récemment est structurel : les agents partagent désormais des couches de protocole et des outillages communs au lieu d'exécuter chacun du code sur mesure. **Une faille dans cette couche partagée se propage d'un coup à tout l'écosystème**, ce qui est un mode de défaillance différent d'une vulnérabilité cantonnée au produit d'un éditeur.

L'objectif n'est donc pas de tout auditer — c'est impossible — mais de savoir ce qui tourne, d'où cela vient, et de pouvoir répondre vite le jour où une version précise est déclarée vulnérable.

## Ce qu'il faut savoir

- **L'inventaire est le prérequis.** Un système dont on ne peut pas lister les dépendances directes et transitives ne peut pas être corrigé en urgence. La nomenclature logicielle (SBOM) est la forme normalisée de cet inventaire.
- **Épingler les versions**, y compris celles des images de base et des serveurs d'outils. Une référence flottante rend l'exécution non reproductible, donc non auditable.
- **Les formats de sérialisation de modèles historiques exécutent du code à la lecture.** Charger un fichier de poids depuis un dépôt public revient à exécuter du code d'origine inconnue ; les formats de tenseurs sans exécution sont la parade standard, et le contrôle porte sur la provenance et l'intégrité du fichier.
- **Les serveurs d'outils sont une dépendance à part entière** : installés vite, mis à jour rarement, dotés d'identifiants. À inventorier comme les bibliothèques, avec leur origine et leur version.
- **La confiance entre serveurs est une décision**, pas un état de fait. Un serveur qui en appelle un autre transporte des privilèges ; la chaîne complète doit être connue.
- **L'analyse automatisée dans la chaîne d'intégration** détecte les vulnérabilités connues à chaque construction. Une image construite il y a six mois accumule des failles sans qu'aucun code n'ait changé.
- **Attention aux paquets d'origine incertaine** : noms proches de paquets légitimes, dépendances internes résolues depuis un dépôt public, et paquets suggérés par un assistant de codage — un nom plausible n'est pas un nom vérifié.
- **La provenance se vérifie** : signature, attestation de construction, référentiels de niveaux de garantie comme SLSA.

## Selon le métier

### AI Red Teaming

C'est un vecteur à intégrer aux priorités de test, avec quatre points concrets : inventaire des serveurs d'outils, origine des poids, versions des SDK, et confiance accordée entre serveurs. L'incident d'avril 2026 sur les SDK officiels du Model Context Protocol — une faille d'architecture permettant l'exécution de code à distance, touchant environ 200 000 serveurs déployés — illustre le mode de propagation propre à cette couche partagée.

### Forward Deployed Engineer

La contrainte se présente à l'envers : chez un client, l'accès aux dépôts publics est souvent filtré, et les images de base imposées par sa sécurité sont rarement récentes. C'est une contrainte à découvrir en phase d'audit, pas au premier déploiement. L'image doit se construire hors ligne depuis le registre interne, et toute dépendance ajoutée doit passer par le circuit d'homologation du client — ce qui prend du temps et se planifie.

> [!warning] Piège
> Considérer qu'un serveur d'outils installé localement est sans risque parce qu'il ne tourne pas en production. Il s'exécute sur un poste de développement qui contient des identifiants, des accès au dépôt et parfois des extraits de données clients. C'est l'un des environnements les mieux dotés de l'organisation, et l'un des moins surveillés.

## Pour aller plus loin

- [Insecure Deserialization — OWASP](https://owasp.org/www-community/vulnerabilities/Insecure_Deserialization) — le mécanisme qui rend un fichier de poids exécutable.
- [MCP Supply Chain Advisory: RCE Vulnerabilities Across the AI Ecosystem — OX Security](https://www.ox.security/blog/mcp-supply-chain-advisory-rce-vulnerabilities-across-the-ai-ecosystem/) — l'analyse de l'incident sur la couche de protocole partagée.
- [How Hugging Face Was Ethically Hacked](https://www.aiblade.net/p/how-hugging-face-was-ethically-hacked) — un cas réel côté distribution de modèles.
- [SLSA — niveaux de garantie de la chaîne d'approvisionnement](https://slsa.dev/) — le référentiel de provenance et d'intégrité.

## Appelée par

- [[parcours/ai-red-teaming/index|AI Red Teaming]]
- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]

Voisines : [[notions/conteneurisation]], [[notions/mcp]], [[notions/integration-continue]], [[notions/modelisation-de-la-menace]].
