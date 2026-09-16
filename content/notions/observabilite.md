---
tags: [notion, observabilite, traces, supervision, exploitation]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-product-builder, ai-red-teaming]
---

# Observabilité

Capacité à reconstituer ce qu'un système a fait, à partir de ce qu'il a émis — traces, journaux et métriques — sans avoir à le reproduire ni à le modifier.

## À quoi ça sert

Sur un système classique, un incident se rejoue : mêmes entrées, même code, même résultat. Sur un système à base de modèle, ce n'est pas vrai. La même requête peut produire une autre réponse, le contexte récupéré a changé, le fournisseur a mis à jour le modèle. Si la trace n'a pas été conservée au moment de l'appel, l'incident n'est pas analysable — il est perdu.

L'observabilité sert donc d'abord à rendre reproductible ce qui ne l'est pas. Elle sert ensuite à répondre à trois questions que personne d'autre ne sait trancher : combien ça coûte réellement, où passe le temps, et qu'est-ce qui a changé avant que ça se dégrade.

Il faut la distinguer de l'évaluation. L'évaluation mesure un comportement attendu sur un jeu fixé, avant livraison ; l'observabilité constate le comportement réel en production, sur la population réelle. Les deux se nourrissent : les échecs observés deviennent des cas d'évaluation.

## Ce qu'il faut savoir

- **La trace est l'unité utile** : une requête complète, avec son entrée, le contexte récupéré, les appels d'outils et leurs résultats, la sortie, la latence et le coût. Une trace amputée du contexte envoyé ne permet aucun diagnostic.
- **Trois signaux complémentaires** : les traces (le détail d'une requête), les métriques (l'agrégat dans le temps), les journaux (l'événement daté). Aucun ne remplace les deux autres.
- **Instrumenter le coût dès le premier jour**, par requête et par session, et plafonner le budget **dans le code**. Une boucle d'agent découverte le lendemain matin coûte plus que le reste du projet.
- **Les métriques propres aux systèmes d'IA** : taux de refus, nombre de tours d'agent, taux de récupération vide, longueur du contexte, part des réponses sans source, consommation de jetons par utilisateur. Ce sont elles qui détectent une dérive, pas le taux d'erreur HTTP.
- **Corréler avec les changements** : version de modèle, version de prompt, version d'index. Une dégradation sans ces trois marqueurs est ininterprétable.
- **Les données personnelles passent dans les traces.** Décider dès la conception ce qui est journalisé, masqué ou tronqué, et pour combien de temps — c'est un traitement au sens du [[notions/rgpd]].
- **L'outillage existe** : LangSmith, Langfuse, Helicone et les plateformes généralistes instrumentées via OpenTelemetry. Le choix compte moins que le fait d'avoir une trace complète ; commencer par journaliser soi-même le contexte envoyé vaut mieux qu'attendre d'avoir choisi.
- **Le tableau de bord doit être lisible par l'exploitant**, pas par son auteur. Cinq indicateurs compris valent mieux que trente affichés.

## Selon le métier

### Forward Deployed Engineer

Traces par requête, coût par requête, et un tableau de bord que l'équipe cliente comprend **sans le FDE**. C'est ce qui autorise le passage d'un palier de déploiement au suivant, et c'est ce qui permet de surveiller la dérive après le départ : nouveaux types de documents dans le corpus, usages détournés, volumes en hausse. Sans cela, le système devient une boîte noire le jour de la sortie de mission.

### AI Product Builder

Traces par requête et coût par requête, sans quoi aucun incident sur une fonction à base de modèle n'est reproductible. Le second usage est économique : le budget par utilisateur actif est une contrainte de modèle économique, et il ne se mesure pas sur la facture mensuelle — trop tard, trop agrégée.

### AI Red Teaming

Le red teamer évalue aussi la détection : l'attaque a-t-elle produit une alerte, et une alerte exploitable. La supervision d'un système d'IA doit couvrir des anomalies propres — dérive du taux de refus, explosion du nombre de tours d'un agent, pics de consommation de jetons, changement soudain de la distribution des sorties — en plus de la supervision d'infrastructure habituelle. Un système parfaitement instrumenté côté serveur et aveugle côté modèle est un constat à part entière.

> [!warning] Piège
> Journaliser la réponse sans le contexte. C'est l'erreur la plus fréquente et la plus coûteuse : on conserve ce que le modèle a dit et on perd ce sur quoi il s'appuyait, c'est-à-dire la seule information qui aurait permis de savoir si la faute vient de la récupération, du prompt ou du modèle. Le contexte réellement envoyé fait partie de la trace, pas des détails d'implémentation.

## Pour aller plus loin

- [What is LLM observability? — IBM](https://www.ibm.com/think/topics/llm-observability) — le cadrage conceptuel, court.
- [Langfuse — documentation](https://langfuse.com/docs) — outil open source, utile aussi comme modèle de ce qu'il faut tracer.
- [LangSmith — documentation](https://docs.smith.langchain.com/) — l'alternative la plus répandue, intégrée à l'évaluation.
- [Helicone — démarrage rapide](https://docs.helicone.ai/getting-started/quick-start) — l'approche par passerelle, la moins intrusive à mettre en place.

## Appelée par

- [[parcours/forward-deployed-engineer|Forward Deployed Engineer]]
- [[parcours/ai-product-builder|AI Product Builder]]
- [[parcours/ai-red-teaming|AI Red Teaming]]

Voisines : [[notions/evaluation-llm]], [[notions/cout-et-latence-inference]], [[notions/integration-continue]], [[notions/mesure-d-usage-produit]].
