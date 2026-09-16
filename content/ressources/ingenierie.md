---
tags: [ressources, ingenierie, git, ci-cd, conteneurisation, cloud, api, observabilite, reference]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/mlops
---

# Ressources — Ingénierie

> [!abstract] Le socle qui ne change pas de nom tous les six mois : versionnement, intégration continue, conteneurs, API, déploiement, supervision. Presque tout ici est de la documentation officielle, parce que c'est le domaine où elle est bonne et où les intermédiaires n'ajoutent rien.

## Versionnement et intégration continue

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| officiel | [Git — Documentation](https://git-scm.com/doc) | inclut *Pro Git* en intégralité et gratuitement, en français. La seule ressource Git nécessaire | débutant |
| officiel | [GitHub Actions](https://docs.github.com/en/actions) | la chaîne d'intégration la plus répandue ; la référence des déclencheurs et des secrets | intermédiaire |
| officiel | [GitLab CI — Prise en main](https://docs.gitlab.com/ee/ci/quick_start/) | l'équivalent côté GitLab, majoritaire dans les DSI françaises | intermédiaire |

Voir [[notions/integration-continue]] et [[notions/tests-logiciels]].

> [!tip] Ajout 2026
> Le choix entre les deux chaînes se fait rarement sur leurs mérites techniques : il se
> fait sur où le code est déjà hébergé, et sur ce que la direction des systèmes
> d'information autorise à sortir du réseau. Arriver chez un client avec une préférence
> est le meilleur moyen de perdre trois semaines.

## Conteneurs et infrastructure

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| officiel | [Docker — Documentation](https://docs.docker.com/) | la référence. Le guide sur les images multi-étapes est celui qui fait gagner le plus de temps | débutant |
| officiel | [Kubernetes — Documentation](https://kubernetes.io/docs/home/) | complète et bien organisée. À ouvrir quand l'orchestration est vraiment nécessaire, pas avant | confirmé |
| officiel | [Terraform](https://developer.hashicorp.com/terraform) | l'infrastructure décrite en fichiers, versionnée comme du code | intermédiaire |
| officiel | [OpenTofu](https://opentofu.org/docs/) | le fork libre de Terraform, pertinent dès que la licence devient un sujet en comité | intermédiaire |
| officiel | [AWS Cloud Essentials](https://aws.amazon.com/getting-started/cloud-essentials/) | le vocabulaire commun du nuage, sans engagement sur un fournisseur | débutant |

Voir [[notions/conteneurisation]] et [[notions/plateforme-de-deploiement]].

## Plateformes de déploiement

L'arbitrage se fait sur trois niveaux, et la plupart des projets choisissent le mauvais
en visant trop haut.

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| officiel | [Vercel](https://vercel.com/docs) | plateforme applicative, déploiement depuis un dépôt en quelques minutes | débutant |
| officiel | [Render](https://render.com/docs) | l'équivalent, avec des services persistants et des bases gérées | débutant |
| officiel | [Railway](https://docs.railway.com/quick-start) | le plus rapide pour un prototype qui doit être vu par quelqu'un demain | débutant |
| officiel | [Cloudflare Pages](https://developers.cloudflare.com/pages/get-started/) | la périphérie : latence faible, modèle d'exécution contraint | intermédiaire |
| officiel | [Supabase](https://supabase.com/docs) | PostgreSQL géré, authentification et stockage — la dorsale la plus rapide à mettre debout | débutant |

## API, protocoles et interfaces

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| officiel | [gRPC — Introduction](https://grpc.io/docs/what-is-grpc/introduction/) | le contrat typé et le streaming, quand REST ne suffit plus | intermédiaire |
| officiel | [GraphQL — Learn](https://graphql.org/learn/) | le modèle de requête côté client, et les problèmes qu'il déplace plutôt qu'il ne résout | intermédiaire |
| officiel | [MDN — Les outils de développement du navigateur](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/What_are_browser_developer_tools) | le premier outil de diagnostic, et le seul vraiment indispensable de cette section | débutant |
| officiel | [React — Référence](https://react.dev/reference/react) | ce que les générateurs d'application produisent par défaut côté interface | intermédiaire |
| officiel | [Node.js — Introduction](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs) | le même besoin côté serveur | débutant |

Voir [[notions/conception-d-api]] et [[notions/controle-d-acces]].

## Supervision

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| officiel | [OpenTelemetry](https://opentelemetry.io/docs/) | le standard d'instrumentation traces-métriques-journaux. À adopter avant de choisir un outil, pas après | intermédiaire |
| officiel | [Prometheus](https://prometheus.io/docs/introduction/overview/) | la collecte de métriques de référence, et son modèle de données | intermédiaire |
| officiel | [Grafana](https://grafana.com/docs/) | la restitution qui va avec, et les alertes | intermédiaire |
| officiel | [Sentry](https://docs.sentry.io/) | le suivi d'erreurs applicatives ; le plus rentable des quatre sur un petit projet | débutant |

Voir [[notions/observabilite]].

## Langages et fondations

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| officiel | [Le tutoriel Python](https://docs.python.org/3/tutorial/) | la référence officielle, disponible en français, meilleure que la plupart des cours payants | débutant |
| officiel | [Go — Documentation](https://go.dev/doc/) | le langage qu'on croise partout dans l'outillage d'infrastructure | intermédiaire |
| officiel | [The Rust Programming Language](https://doc.rust-lang.org/book/) | le manuel libre, exemplaire de ce qu'une documentation de langage peut être | confirmé |
| officiel | [Redis](https://redis.io/docs/latest/) | cache, file, verrou distribué : trois usages, un seul outil | intermédiaire |
| officiel | [Elasticsearch](https://www.elastic.co/guide/index.html) | la recherche plein texte, et ce qu'elle fait mieux qu'une base vectorielle sur du terme exact | intermédiaire |

## Outils de génération de code

Sujet récent, donc terrain favorable au contenu promotionnel. Seules les documentations
officielles sont retenues : elles décrivent le comportement réel de l'outil, là où les
articles décrivent l'enthousiasme de leur auteur.

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| officiel | [Claude Code](https://code.claude.com/docs/en/overview) | assistant en terminal, orienté compréhension d'une base de code existante | intermédiaire |
| officiel | [Cursor](https://cursor.com/docs) | éditeur augmenté ; la documentation sur l'indexation du dépôt est la partie utile | intermédiaire |
| officiel | [GitHub Copilot](https://docs.github.com/en/copilot) | complétion intégrée, et les réglages d'entreprise qui décident de ce qui sort du réseau | débutant |
| officiel | [v0](https://v0.app/docs) | génération d'interface à partir d'une description | débutant |
| officiel | [Lovable](https://docs.lovable.dev/introduction/welcome) | génération d'application complète, prototype compris | débutant |
| officiel | [E2E Testing — Code With Engineering Playbook](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/e2e-testing/) | ce qu'il faut tester quand le code a été généré et non écrit | intermédiaire |

Voir [[notions/assistants-de-codage]].

## Écarté, et pourquoi

- **Les pages d'accueil de fournisseurs de nuage.** L'amont en cite des dizaines —
  `aws.amazon.com/rds/`, `azure.microsoft.com/...`, une par service. Une page produit
  n'apprend rien ; seules les pages de documentation sont retenues.
- **Deux tutoriels d'intégration continue** publiés par un éditeur d'outil de
  déploiement, arrivés avec `utm_source=roadmap`. Le sujet est couvert par les
  documentations officielles ci-dessus.
- **Bit Cloud**, qui apparaît deux fois dans la roadmap amont AI Product Builder, dont
  une fois sur un nœud vide, avec des URL portant `?c=rsh-a` et dont l'une est malformée.
  C'est un placement, pas une ressource.
