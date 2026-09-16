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

Un parcours métier n'explique jamais une notion transverse : il pose un lien vers `notions/<slug>` et ajoute, en une ou deux phrases, ce que cette notion signifie
**pour ce métier-là**. C'est le seul endroit où il a le droit d'être spécifique.

Avant d'inventer un slug, chercher dans ce registre. Si la notion y figure, utiliser
le slug tel quel. S'il faut créer un slug : français, en minuscules, tirets, singulier,
sans article — et le proposer au pilote plutôt que de modifier ce fichier.

**Les soixante-cinq notions du registre ont désormais un fichier.** Un lien vers un slug
de ce registre ne peut donc plus être orphelin ; un lien orphelin signale une faute de
frappe ou un slug inventé.

> [!info] Mise à jour du 16 septembre 2026 — passe du chantier 07
> Les 65 notions ont été rédigées. Bijection vérifiée : 65 slugs au registre, 65 fichiers,
> aucun lien orphelin dans `content/`. Aucun slug n'a été fusionné, scindé ni refusé —
> les arbitrages de fin de lot 1 avaient déjà tranché les recouvrements.
>
> Neuf notions n'ont encore aucun appelant dans le corpus : `controle-d-acces`,
> `modelisation-de-la-menace`, `chaine-d-approvisionnement-logicielle`,
> `collecte-de-donnees`, `traitement-distribue`, `series-temporelles`,
> `analyse-de-cohorte`, `mesure-d-usage-produit`, `plateforme-de-deploiement`. Leurs
> sujets sont encore traités en ligne dans les parcours ; le chantier 09 pose les liens.
>
> La colonne **Appelée par** a été recalculée depuis le corpus : elle liste désormais les
> parcours qui posent réellement le lien. `· attendu :` signale un parcours du corpus qui
> n'est pas encore rédigé, `· à raccorder par le chantier 09` les neuf notions dont les
> appelants sont arbitrés mais pas encore liés.

> [!info] Mise à jour du 16 septembre 2026 — arbitrages
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
| `ab-testing` | protocole, métriques de ratio, sensibilité | Data Analyst, BI Analyst · attendu : Data Engineer |
| `analyse-correlation` | corrélation, causalité, pièges | Data Analyst, BI Analyst |
| `regression-lineaire` | moindres carrés, hypothèses, diagnostic | Data Analyst, BI Analyst · attendu : Machine Learning |
| `regression-logistique` | classification binaire, odds ratio | Data Analyst · attendu : Machine Learning |

## Apprentissage automatique

| Slug | Recouvre | Appelée par |
|---|---|---|
| `apprentissage-supervise` | classification, régression, jeux étiquetés | AI Red Teaming, Data Analyst, BI Analyst |
| `apprentissage-non-supervise` | clustering, réduction de dimension | AI Red Teaming, Data Analyst, BI Analyst |
| `apprentissage-par-renforcement` | politique, récompense, RLHF | AI Red Teaming, Data Analyst, BI Analyst |
| `reseaux-de-neurones` | perceptron, rétropropagation, architectures | AI Red Teaming, Data Analyst |
| `series-temporelles` | tendance, saisonnalité, résidu, effets de calendrier, prévision et sa référence naïve | BI Analyst, Data Analyst · à raccorder par le chantier 09 |
| `analyse-de-cohorte` | regroupement par période d'entrée, fenêtre d'observation, effet de composition | BI Analyst, Data Analyst · à raccorder par le chantier 09 |
| `metriques-evaluation-ml` | exactitude, précision, rappel, F1, AUC | Data Analyst |
| `traitement-langage-naturel` | tokenisation, plongements, tâches classiques | Data Analyst · attendu : Machine Learning |

## Données

| Slug | Recouvre | Appelée par |
|---|---|---|
| `entrepot-de-donnees` | data warehouse, data mart, schéma étoile et flocon | BI Analyst · attendu : Data Engineer |
| `data-lake` | stockage brut, lakehouse | BI Analyst · attendu : Data Engineer |
| `qualite-des-donnees` | complétude, fraîcheur, unicité, tests | FDE, AI Red Teaming, Data Analyst, BI Analyst · attendu : Data Engineer |
| `lignage-des-donnees` | traçabilité, catalogues, impact | BI Analyst · attendu : MLOps |
| `modelisation-dimensionnelle` | faits, dimensions, granularité | BI Analyst |
| `sql` | requêtes, jointures, fenêtrage, optimisation | FDE, AI Product Builder, Data Analyst, BI Analyst |
| `collecte-de-donnees` | base, fichier, API, moissonnage ; fiabilité et métadonnées d'extraction | Data Analyst, BI Analyst · à raccorder par le chantier 09 |
| `traitement-distribue` | Spark, formats colonnes, moteurs embarqués, et le seuil à partir duquel distribuer a un sens | Data Analyst, BI Analyst · à raccorder par le chantier 09 |
| `transformation-dbt` | modèles, tests, documentation | BI Analyst · attendu : Data Engineer |
| `orchestration-de-flux` | Airflow, DAG, ordonnancement, reprise | BI Analyst · attendu : MLOps |

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
| `assistants-de-codage` | Claude Code, Cursor, Codex — usages réels | AI Product Builder, Data Analyst |

## IA générative

| Slug | Recouvre | Appelée par |
|---|---|---|
| `rag` | récupération, découpage, reclassement, échecs typiques | FDE, AI Red Teaming, AI Product Builder |
| `embeddings-et-bases-vectorielles` | vecteurs, similarité, index | FDE, AI Product Builder |
| `agents-llm` | boucle agentique, outils, mémoire, multi-agents | FDE, AI Product Builder |
| `mcp` | protocole, serveurs, description d'outils | FDE, AI Red Teaming, AI Product Builder |
| `ingenierie-de-prompt` | ce qui marche encore, ce qui est du folklore | AI Red Teaming, AI Product Builder |
| `injection-de-prompt` | directe, indirecte, exfiltration, atténuations | FDE, AI Red Teaming, AI Product Builder |
| `garde-fous` | filtrage entrée/sortie, politiques, dégradation contrôlée | FDE, AI Red Teaming, AI Product Builder |
| `evaluation-llm` | jeux d'évaluation, évals déterministes, model-based, humaines, régression | FDE, AI Red Teaming, AI Product Builder |
| `cout-et-latence-inference` | facturation, mise en cache, traitement par lots, budget | FDE, AI Product Builder |
| `choix-de-modele` | SLM contre LLM, raisonnement, arbitrage coût-qualité | FDE, AI Product Builder |
| `affinage-de-modele` | quand il sert vraiment, dette de ré-entraînement | FDE, AI Red Teaming |

## Ingénierie et exploitation

| Slug | Recouvre | Appelée par |
|---|---|---|
| `conteneurisation` | Docker, images, Kubernetes | FDE, AI Red Teaming |
| `integration-continue` | CI/CD, tests, livraison | FDE, AI Red Teaming, AI Product Builder |
| `observabilite` | traces, journaux, métriques, LangSmith, Langfuse, Arize | FDE, AI Red Teaming, AI Product Builder |
| `tests-logiciels` | unitaires, intégration, régression | FDE, AI Red Teaming, AI Product Builder |
| `conception-d-api` | REST, contrats, versionnement | FDE, AI Red Teaming, AI Product Builder |
| `controle-d-acces` | authentification, autorisation, moindre privilège, propagation d'identité | Red Teaming, FDE, Product Builder, BI Analyst · à raccorder par le chantier 09 |
| `plateforme-de-deploiement` | périphérie, plateforme applicative, infrastructure brute, chaîne d'entreprise | Product Builder, FDE · à raccorder par le chantier 09 |
| `chaine-d-approvisionnement-logicielle` | poids de modèles, SDK, serveurs d'outils tiers | Red Teaming, FDE · à raccorder par le chantier 09 |
| `mesure-d-usage-produit` | instrumentation d'événements, entonnoir, activation, rétention | Product Builder, Data Analyst · à raccorder par le chantier 09 |
| `systemes-patrimoniaux` | ERP, CRM, bases legacy, stratégies d'interfaçage | FDE |

## Conformité et sécurité

| Slug | Recouvre | Appelée par |
|---|---|---|
| `rgpd` | bases légales, minimisation, transferts | FDE, AI Red Teaming, AI Product Builder, Data Analyst, BI Analyst |
| `modelisation-de-la-menace` | adversaires, surfaces d'attaque, priorisation par impact | Red Teaming, FDE · à raccorder par le chantier 09 |
| `gouvernance-ia` | AI Act, responsabilité, documentation | FDE, AI Red Teaming |
| `donnees-sensibles` | classification, anonymisation, cloisonnement | FDE, AI Red Teaming |

## Conseil et terrain

| Slug | Recouvre | Appelée par |
|---|---|---|
| `cadrage-besoin` | recueil, reformulation, spécification | FDE, AI Product Builder, Data Analyst, BI Analyst |
| `bpmn` | notation, cartographie d'un processus | FDE |
| `reingenierie-de-processus` | BPR, redondances, simplification avant automatisation | FDE |
| `arbitrage-deterministe-probabiliste` | script, webhook, RPA contre IA générative | FDE, AI Product Builder |
| `gestion-parties-prenantes` | intérêts divergents, alignement, arbitrage | FDE, BI Analyst |
| `conduite-du-changement` | résistance, adoption, politique interne | FDE, BI Analyst |
| `roi-des-projets-ia` | valeur, mesure d'impact, coût complet | FDE, AI Product Builder |
| `redaction-technique` | spécification, note de décision, documentation | FDE, AI Red Teaming |
| `transfert-de-competences` | sortie de mission, maintenance, autonomie du client | FDE |
