---
tags: [ressources, index, moc, sources, reference]
date: 2026-09-16
statut: actif
source: https://roadmap.sh
---

# Ressources

> [!abstract] L'entrée unique vers les sources du corpus, classées par **usage** et non par métier. 198 adresses choisies et commentées dans un catalogue amont de 3 216, toutes vérifiées le jour de la publication. Ce qu'on lit pour démarrer, ce qu'on lit pour approfondir, ce qui fait référence, et ce qu'on relit.

**Source** : capture roadmap.sh du 16 septembre 2026 · **Vérification des liens** : 16 septembre 2026 · **Rédaction** : 16 septembre 2026

---

## Pourquoi deux cents et pas trois mille

Le catalogue amont compte 3 216 ressources, soit 2 649 adresses distinctes. Publiées
telles quelles, elles ne servent à personne : un annuaire de cette taille se consulte
comme un moteur de recherche, sauf qu'il est moins bon. Il en reste ici **198**, chacune
vérifiée et assortie d'une ligne qui dit ce qu'elle apporte.

Quatre critères ont servi à trancher.

**La source primaire l'emporte sur le commentaire.** La spécification MCP plutôt qu'un
article qui la résume, l'article de Lewis et al. plutôt qu'un billet « comprendre le
RAG », le texte du règlement plutôt qu'une synthèse de cabinet. Ce n'est pas du purisme :
le commentaire périme, la source se corrige.

**Le daté et maintenu l'emporte sur l'intemporel autoproclamé** — sauf en statistique,
où c'est l'inverse et où c'est expliqué sur [[ressources/statistiques|la page
correspondante]].

**Le gratuit et accessible l'emporte à qualité égale.** Un manuel libre vaut mieux qu'un
cours payant qui couvre le même terrain.

**Le contenu promotionnel déguisé en pédagogie est écarté sans état d'âme.** Il est
identifiable : 76 adresses du catalogue amont portent un marqueur de campagne dans leur
URL. Quand une ressource d'éditeur est malgré tout retenue parce qu'elle est la meilleure
sur son sujet, sa provenance est écrite à côté.

Le détail de la méthode, des outils et de ce qu'ils ne garantissent pas :
[[ressources/sources]].

---

## Pour démarrer

Ce qu'on ouvre quand on ne connaît pas encore le sujet, et qui ne demande rien d'autre
que du temps.

| Pour | Ressource | Pourquoi celle-là |
|---|---|---|
| Comprendre les statistiques | [OpenIntro Statistics](https://www.openintro.org/book/os/) | le manuel libre le mieux fait, exercices corrigés, sans prérequis |
| Voir *pourquoi* une formule statistique est celle-là | [StatQuest](https://www.youtube.com/@statquest) | la meilleure vulgarisation du domaine, et elle ne triche pas |
| Apprendre Python sérieusement | [Le tutoriel Python](https://docs.python.org/3/tutorial/) | officiel, en français, meilleur que la plupart des cours payants |
| Apprendre l'analyse de données en Python | [Python for Data Analysis](https://wesmckinney.com/book/) | par l'auteur de pandas, libre en ligne |
| Apprendre R | [R for Data Science](https://r4ds.hadley.nz/) | la 2ᵉ édition libre, celle qui couvre le tidyverse actuel |
| Apprendre Git | [Git — Documentation](https://git-scm.com/doc) | contient *Pro Git* en entier, gratuitement, en français |
| Découvrir le machine learning | [scikit-learn](https://scikit-learn.org/stable/) | le guide utilisateur est un cours de ML déguisé |
| Commencer à construire sur des LLM | [OpenAI Cookbook](https://github.com/openai/openai-cookbook) | des exemples qui tournent, maintenus par l'éditeur |
| Comprendre les agents sans cadre propriétaire | [Hugging Face — Agents Course](https://huggingface.co/learn/agents-course/en/unit1/tools) | gratuit, progressif, avec des exercices |
| Choisir un graphique | [The Data Visualisation Catalogue](https://datavizcatalogue.com/) | on part de la question posée, pas du catalogue d'esthétiques |

## Pour approfondir

Ce qu'on ouvre quand on a déjà livré quelque chose et qu'on veut savoir pourquoi ça
tient — ou pourquoi ça ne tient pas.

| Pour | Ressource | Pourquoi celle-là |
|---|---|---|
| Comprendre le RAG à la source | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | l'article fondateur (Lewis et al., 2020) |
| Comprendre pourquoi l'alignement échoue | [Jailbroken: How Does LLM Safety Training Fail?](https://arxiv.org/abs/2307.02483) | explique le mécanisme, au lieu de lister des contournements périssables |
| Évaluer la robustesse d'un modèle | [Towards Evaluating the Robustness of Neural Networks](https://arxiv.org/abs/1608.04644) | Carlini et Wagner, et leur démolition des fausses défenses |
| Évaluer un système RAG | [Ragas](https://docs.ragas.io/en/stable/) | des métriques définies et calculables, pas des impressions |
| Mettre l'évaluation en intégration continue | [DeepEval](https://www.deepeval.com/) | l'évaluation écrite comme des tests |
| Instrumenter un système en production | [OpenTelemetry](https://opentelemetry.io/docs/) | le standard à adopter avant de choisir un outil |
| Exposer des outils à un agent sans ouvrir une porte | [MCP — Spécification d'autorisation](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) | la partie du protocole qui décide de la surface d'attaque |
| Valider un modèle sans se mentir | [scikit-learn — Recherche d'hyperparamètres](https://scikit-learn.org/stable/modules/grid_search.html) | la validation croisée imbriquée, expliquée correctement |
| Comprendre l'entrepôt de données | [Apache Parquet](https://parquet.apache.org/) | comprendre pourquoi le format colonne est rapide change les choix d'architecture |
| Traiter un gros fichier sans cluster | [DuckDB](https://duckdb.org/docs/) | la réponse à la plupart des « il faut du distribué » |

## La référence officielle

Ce qu'on cite quand quelqu'un demande sur quoi on s'appuie. Ces adresses ne se
paraphrasent pas : elles se lisent.

| Domaine | Référence |
|---|---|
| Règlement européen sur l'IA | [Règlement (UE) 2024/1689, texte intégral](https://publications.europa.eu/resource/celex/32024R1689) |
| Gestion du risque IA | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) |
| Management de l'IA, certifiable | [ISO/IEC 42001](https://www.iso.org/standard/81230.html) — payante |
| Risques des applications LLM | [OWASP GenAI Security Project](https://genai.owasp.org/) |
| Protection des données | [Texte du RGPD](https://gdpr-info.eu/) |
| Protocole d'accès aux outils | [Model Context Protocol](https://modelcontextprotocol.io/) |
| Modélisation de processus | [Spécification BPMN 2.0 (OMG)](https://www.omg.org/spec/BPMN/2.0/) |
| Méthodes statistiques | [NIST/SEMATECH e-Handbook](https://www.itl.nist.gov/div898/handbook/) |
| Le langage Python | [docs.python.org](https://docs.python.org/3/tutorial/) |
| Le moteur SQL le mieux documenté | [PostgreSQL](https://www.postgresql.org/docs/) |
| Format colonne | [Apache Parquet](https://parquet.apache.org/) |
| Instrumentation | [OpenTelemetry](https://opentelemetry.io/docs/) |

## Ce qu'on relit

Les quelques pages qu'on rouvre pour de bon, souvent juste avant une réunion ou une mise
en production. Elles ne s'apprennent pas : elles se vérifient.

| Avant de | Relire |
|---|---|
| Affirmer qu'un lien existe entre deux séries | [Correlation vs. Causation](https://www.scribbr.com/methodology/correlation-vs-causation/) |
| Lancer un test A/B | [A Refresher on A/B Testing](https://hbr.org/2017/06/a-refresher-on-ab-testing) |
| Choisir un test statistique | [Choosing the Right Statistical Test](https://www.scribbr.com/statistics/statistical-tests/) |
| Commenter un coefficient de régression | [A Refresher on Regression Analysis](https://hbr.org/2015/11/a-refresher-on-regression-analysis) |
| Publier un graphique | [10 Guidelines for DataViz Accessibility](https://www.highcharts.com/blog/best-practices/10-guidelines-for-dataviz-accessibility/) et [How To Spot Misleading Charts](https://www.tableau.com/blog/how-spot-misleading-charts-check-axes) |
| Ouvrir un système à un agent | [OWASP LLM01 — Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) |
| Présenter un arbitrage de périmètre | [Project management triangle](https://asana.com/resources/project-management-triangle) |
| Écrire une requête qui doit tenir | [SQL Window Functions](https://www.thoughtspot.com/sql-tutorial/sql-window-functions) |

---

## Les cinq familles

Chaque page donne, pour chaque ressource : son type, son titre, son URL, ce qu'elle
apporte en une ligne, et le niveau attendu du lecteur. Chacune se termine par ce qui a
été écarté, et pourquoi.

- [[ressources/ia-generative|IA générative]] — API de modèles, prompt et context
  engineering, RAG, agents et MCP, évaluation, sécurité, red teaming, régulation.
- [[ressources/donnees|Données]] — SQL, entrepôt, modélisation, transformation,
  orchestration, restitution, qualité et gouvernance.
- [[ressources/statistiques|Statistiques et méthode]] — manuels de fond, causalité,
  protocole de test, apprentissage automatique, interprétabilité.
- [[ressources/ingenierie|Ingénierie]] — versionnement, intégration continue,
  conteneurs, plateformes de déploiement, API, supervision, outils de génération de code.
- [[ressources/conseil-et-terrain|Conseil et terrain]] — cadrage du besoin, modélisation
  de processus, parties prenantes, conformité en mission.

Et la page qui rend tout ça auditable : [[ressources/sources|d'où vient ce corpus]].

---

## Ce que cette sélection ne prétend pas être

Elle n'est ni neutre ni exhaustive. Cent quatre-vingt-dix-huit ressources commentées,
c'est autant de jugements, et ils sont discutables un par un — ce qui est précisément
pourquoi chaque entrée dit ce qu'elle apporte plutôt que de se contenter d'exister.

Elle n'est pas non plus stable. Sur les 133 adresses citées par les parcours et les huit
notes historiques, vérifiées le 16 septembre 2026 : **3 étaient déjà mortes** et **13
avaient changé de place**, en quelques semaines d'existence du corpus. La vérification est
rejouable en une commande, et elle doit l'être régulièrement :

```bash
python3 tools/verifier_liens.py --selection
```

Enfin, elle ne remplace pas les parcours. Une ressource répond à une question qu'on se
pose déjà ; c'est le rôle des [[index|parcours métier]] de dire quelle question se poser,
et dans quel ordre.
