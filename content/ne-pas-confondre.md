---
title: Ne pas confondre ces métiers
---

Les titres se ressemblent et se recouvrent. Ce qui les sépare n'est pas la liste des technologies, c'est **ce qu'ils produisent** et **où s'arrête leur responsabilité**.

## Autour du déploiement chez le client

| Rôle | Ce qu'il produit | Où s'arrête sa responsabilité |
|---|---|---|
| AI Engineer | le système et ses garde-fous | à la frontière de son dépôt |
| Consultant | une recommandation argumentée | au livrable écrit |
| Solutions Architect | une cible cohérente | au schéma d'architecture |
| **Forward Deployed Engineer** | un système adopté en production chez le client | quand le client s'en sert sans lui |

## Autour de la sécurité des systèmes d'IA

| Rôle | Ce qu'il produit | Où s'arrête sa responsabilité |
|---|---|---|
| Pentesteur applicatif | des faiblesses connues, énumérées contre un référentiel | au périmètre technique convenu |
| AI Engineer | le système et ses garde-fous | à la qualité de ce qu'il construit |
| Auditeur de conformité | la preuve documentaire qu'un cadre est suivi | au dossier |
| **AI Red Teamer** | le chemin complet qu'un adversaire emprunterait, et l'atténuation qui tient | quand la posture est mesurée et rejouée à chaque changement |

## Autour de la donnée

| Rôle | Ce qu'il produit | Où s'arrête sa responsabilité |
|---|---|---|
| Data Analyst | une réponse chiffrée à une question posée | à la restitution du résultat |
| BI Analyst | des définitions partagées et les tableaux de bord qui les portent | quand l'indicateur veut dire la même chose pour tout le monde |
| Data Engineer | des données disponibles, fraîches et fiables | aux tables de l'entrepôt |
| Data Scientist | un modèle qui généralise au-delà du cas observé | à la performance mesurée |

## Autour de la fabrication d'un produit

| Rôle | Ce qu'il produit | Où s'arrête sa responsabilité |
|---|---|---|
| **AI Product Builder** | un produit en ligne, utilisé, fabriqué avec des outils de génération | quand l'usage est mesuré et que le produit tient sans son auteur |
| AI Engineer | un système à base de modèle, fiable et évalué | à la qualité de réponse, au coût et à la latence du système |
| Product Manager | une décision de périmètre argumentée | à l'arbitrage, pas à la livraison |
| Développeur d'application | du code qui répond à une spécification | au code livré et testé |

La confusion la plus coûteuse est la première ligne contre la deuxième, et elle se tranche en une question : **quelle est votre métrique de succès ?** Si la réponse parle d'utilisateurs actifs et de délai de mise en ligne, c'est un product builder. Si elle parle de taux de réponse correcte et de coût par appel, c'est un AI engineer. Le mot « AI » désigne l'atelier dans un cas, le composant dans l'autre.

Le glissement de carrière le plus fréquent va du produit vers le système, parce que le premier produit livré finit toujours par demander une fonction intelligente — c'est ce que traite [[parcours/ai-product-builder/quand-le-produit-embarque-un-modele/index|Quand le produit embarque un modèle]]. L'inverse est plus rare.
