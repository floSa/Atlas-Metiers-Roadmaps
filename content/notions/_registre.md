---
tags: [registre, notions, convention]
date: 2026-09-16
statut: actif
---

# Registre des notions

> [!abstract] Le contrat qui empêche cinq rédactions parallèles de produire cinq
> explications divergentes de la même chose. Une notion transverse porte **un slug et
> un seul**, quel que soit le parcours métier qui l'appelle.

## Comment s'en servir

Un parcours métier n'explique jamais une notion transverse : il pose un lien
`[[notions/<slug>]]` et ajoute, en une ou deux phrases, ce que cette notion signifie
**pour ce métier-là**. C'est le seul endroit où il a le droit d'être spécifique.

Avant d'inventer un slug, chercher dans ce registre. Si la notion y figure, utiliser
le slug tel quel, **même si le fichier n'existe pas encore** — un lien orphelin est un
signal de travail, pas une erreur. S'il faut créer un slug : français, en minuscules,
tirets, singulier, sans article.

Une ligne en `italique` signale une notion dont le fichier reste à écrire.

> [!info] Mise à jour du 16 septembre 2026
> Neuf notions ajoutées après les arbitrages de fin de lot 1 — voir
> `prompts/_arbitrages-lot-1.md` pour les slugs retenus, ceux écartés et pourquoi.
> `donnees-manquantes` a été absorbé par `qualite-des-donnees`, qui lui consacre une
> sous-partie côté Data Analyst.

---

## Statistiques et analyse

| Slug | Recouvre | Appelée par |
|---|---|---|
| `statistiques-descriptives` | moyenne, médiane, mode, étendue, variance, dispersion, asymétrie, aplatissement | Data Analyst, BI Analyst |
| `tests-hypotheses` | hypothèse nulle, p-value, puissance, sensibilité | Data Analyst, BI Analyst |
| `ab-testing` | protocole, métriques de ratio, sensibilité | BI Analyst, Data Engineer |
| `analyse-correlation` | corrélation, causalité, pièges | Data Analyst, BI Analyst |
| `regression-lineaire` | moindres carrés, hypothèses, diagnostic | BI Analyst, Machine Learning |
| `regression-logistique` | classification binaire, odds ratio | Data Analyst, Machine Learning |

## Apprentissage automatique

| Slug | Recouvre | Appelée par |
|---|---|---|
| `apprentissage-supervise` | classification, régression, jeux étiquetés | Data Analyst, BI Analyst, AI Red Teaming |
| `apprentissage-non-supervise` | clustering, réduction de dimension | Data Analyst, BI Analyst, AI Red Teaming |
| `apprentissage-par-renforcement` | politique, récompense, RLHF | Data Analyst, BI Analyst, AI Red Teaming |
| `reseaux-de-neurones` | perceptron, rétropropagation, architectures | Data Analyst, AI Red Teaming |
| `series-temporelles` | tendance, saisonnalité, résidu, effets de calendrier, prévision et sa référence naïve | BI Analyst, Data Analyst |
| `analyse-de-cohorte` | regroupement par période d'entrée, fenêtre d'observation, effet de composition | BI Analyst, Data Analyst |
| `metriques-evaluation-ml` | exactitude, précision, rappel, F1, AUC | Data Analyst, BI Analyst |
| `traitement-langage-naturel` | tokenisation, plongements, tâches classiques | Data Analyst, Machine Learning |

## Données

| Slug | Recouvre | Appelée par |
|---|---|---|
| `entrepot-de-donnees` | data warehouse, data mart, schéma étoile et flocon | BI Analyst, Data Engineer |
| `data-lake` | stockage brut, lakehouse | BI Analyst, Data Engineer |
| `qualite-des-donnees` | complétude, fraîcheur, unicité, tests | BI Analyst, Data Engineer |
| `lignage-des-donnees` | traçabilité, catalogues, impact | BI Analyst, MLOps |
| `modelisation-dimensionnelle` | faits, dimensions, granularité | BI Analyst |
| `sql` | requêtes, jointures, fenêtrage, optimisation | BI Analyst, Data Analyst |
| `collecte-de-donnees` | base, fichier, API, moissonnage ; fiabilité et métadonnées d'extraction | Data Analyst, BI Analyst |
| `traitement-distribue` | Spark, formats colonnes, moteurs embarqués, et le seuil à partir duquel distribuer a un sens | Data Analyst, BI Analyst |
| `transformation-dbt` | modèles, tests, documentation | BI Analyst, Data Engineer |
| `orchestration-de-flux` | Airflow, DAG, ordonnancement, reprise | BI Analyst, MLOps |

## Restitution

| Slug | Recouvre | Appelée par |
|---|---|---|
| `visualisation-de-donnees` | choix du graphique, lisibilité, erreurs classiques | Data Analyst, BI Analyst |
| `outils-decisionnels` | Power BI, Tableau, Looker — ce qui les distingue | Data Analyst, BI Analyst |
| `tableur` | Excel, limites, quand il suffit | Data Analyst, BI Analyst |

## Outillage

| Slug | Recouvre | Appelée par |
|---|---|---|
| `pandas` | DataFrame, opérations, pièges de performance | Data Analyst, BI Analyst |
| `python-pour-la-data` | environnement, bibliothèques, notebooks | Data Analyst |
| `r-et-tidyverse` | dplyr, ggplot2, quand R plutôt que Python | Data Analyst, BI Analyst |
| `assistants-de-codage` | Claude Code, Cursor, Codex — usages réels | AI Product Builder |

## IA générative

| Slug | Recouvre | Appelée par |
|---|---|---|
| `rag` | récupération, découpage, reclassement, échecs typiques | FDE, AI Product Builder |
| `embeddings-et-bases-vectorielles` | vecteurs, similarité, index | FDE, AI Product Builder |
| `agents-llm` | boucle agentique, outils, mémoire, multi-agents | FDE, AI Product Builder |
| `mcp` | protocole, serveurs, description d'outils | FDE, AI Product Builder |
| `ingenierie-de-prompt` | ce qui marche encore, ce qui est du folklore | AI Red Teaming, AI Product Builder |
| `injection-de-prompt` | directe, indirecte, exfiltration, atténuations | FDE, AI Red Teaming |
| `garde-fous` | filtrage entrée/sortie, politiques, dégradation contrôlée | FDE, AI Red Teaming |
| `evaluation-llm` | jeux d'évaluation, évals déterministes, model-based, humaines, régression | FDE, AI Product Builder, AI Red Teaming |
| `cout-et-latence-inference` | facturation, mise en cache, traitement par lots, budget | FDE, AI Product Builder |
| `choix-de-modele` | SLM contre LLM, raisonnement, arbitrage coût-qualité | FDE, AI Product Builder |
| `affinage-de-modele` | quand il sert vraiment, dette de ré-entraînement | FDE |

## Ingénierie et exploitation

| Slug | Recouvre | Appelée par |
|---|---|---|
| `conteneurisation` | Docker, images, Kubernetes | FDE |
| `integration-continue` | CI/CD, tests, livraison | FDE, AI Product Builder |
| `observabilite` | traces, journaux, métriques, LangSmith, Langfuse, Arize | FDE, AI Product Builder |
| `tests-logiciels` | unitaires, intégration, régression | FDE, AI Product Builder |
| `conception-d-api` | REST, contrats, versionnement | FDE, AI Product Builder |
| `controle-d-acces` | authentification, autorisation, moindre privilège, propagation d'identité | Red Teaming, FDE, Product Builder, BI Analyst |
| `plateforme-de-deploiement` | périphérie, plateforme applicative, infrastructure brute, chaîne d'entreprise | Product Builder, FDE |
| `chaine-d-approvisionnement-logicielle` | poids de modèles, SDK, serveurs d'outils tiers | Red Teaming, FDE |
| `mesure-d-usage-produit` | instrumentation d'événements, entonnoir, activation, rétention | Product Builder, Data Analyst |
| `systemes-patrimoniaux` | ERP, CRM, bases legacy, stratégies d'interfaçage | FDE |

## Conformité et sécurité

| Slug | Recouvre | Appelée par |
|---|---|---|
| `rgpd` | bases légales, minimisation, transferts | BI Analyst, FDE |
| `modelisation-de-la-menace` | adversaires, surfaces d'attaque, priorisation par impact | Red Teaming, FDE |
| `gouvernance-ia` | AI Act, responsabilité, documentation | FDE, AI Red Teaming |
| `donnees-sensibles` | classification, anonymisation, cloisonnement | FDE, AI Red Teaming |

## Conseil et terrain

| Slug | Recouvre | Appelée par |
|---|---|---|
| `cadrage-besoin` | recueil, reformulation, spécification | FDE, BI Analyst |
| `bpmn` | notation, cartographie d'un processus | FDE |
| `reingenierie-de-processus` | BPR, redondances, simplification avant automatisation | FDE |
| `arbitrage-deterministe-probabiliste` | script, webhook, RPA contre IA générative | FDE, AI Product Builder |
| `gestion-parties-prenantes` | intérêts divergents, alignement, arbitrage | FDE, BI Analyst |
| `conduite-du-changement` | résistance, adoption, politique interne | FDE |
| `roi-des-projets-ia` | valeur, mesure d'impact, coût complet | FDE, AI Product Builder |
| `redaction-technique` | spécification, note de décision, documentation | FDE |
| `transfert-de-competences` | sortie de mission, maintenance, autonomie du client | FDE |
