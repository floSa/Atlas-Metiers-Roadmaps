---
tags: [notion, api, rest, contrat, integration]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-product-builder, ai-red-teaming]
---

# Conception d'API

Définition du contrat par lequel un système expose ses capacités à un autre : les ressources, les opérations, les formats, les erreurs et les règles d'évolution.

## À quoi ça sert

Une API est une promesse faite à des gens qu'on ne rencontrera pas. C'est ce qui la distingue d'une fonction interne : on ne peut pas prévenir ses consommateurs, on ne peut pas les corriger, et on ne peut plus revenir en arrière une fois qu'ils dépendent d'un comportement — y compris d'un comportement non documenté.

L'essentiel de la conception consiste donc à rendre le contrat explicite et à se laisser une marge d'évolution. Une API bien conçue n'est pas celle qui est élégante, c'est celle qui permet d'ajouter une fonctionnalité dans six mois sans casser ce qui existe.

Le second enjeu est la surface d'attaque. Une API est le point où l'extérieur touche le système : chaque route est une décision d'exposition, et l'autorisation y est plus souvent fausse que l'authentification.

## Ce qu'il faut savoir

- **Les ressources avant les verbes.** Un chemin nomme une chose, la méthode HTTP dit ce qu'on en fait. `POST /commandes/42/annulation` reste préférable à `POST /annulerCommande` dès qu'un tiers doit deviner le reste de l'API à partir d'une route.
- **Les codes d'erreur sont une fonctionnalité.** Distinguer 400 (la requête est fausse), 401 (non authentifié), 403 (authentifié mais pas autorisé), 404, 409 (conflit d'état), 422, 429 (débit dépassé), 500. Un service qui renvoie 200 avec un message d'erreur dans le corps fait porter tout le travail à ses appelants.
- **Versionner dès qu'un tiers consomme**, dans l'URL ou par en-tête. Le coût est nul au départ et prohibitif après.
- **Idempotence** : une opération rejouée ne doit pas créer un doublon. Une clé d'idempotence sur les écritures est ce qui rend les reprises sur incident inoffensives.
- **Pagination, filtrage, tri** : à prévoir avant que la collection grossisse. Une route qui renvoie tout fonctionne jusqu'au jour où.
- **Limitation de débit et quotas.** Sur un service qui appelle un modèle, l'absence de quota est une facture ouverte autant qu'une porte ouverte.
- **Autorisation au niveau de l'objet**, pas seulement de la route. Vérifier que l'appelant a le droit d'accéder **à cette ressource-là** est le contrôle le plus souvent absent. Voir [[notions/controle-d-acces]].
- **Le contrat est un document exécutable** — OpenAPI ou équivalent —, généré ou vérifié par les tests, jamais rédigé à part et laissé vieillir.
- **Le référentiel de sécurité applicable est l'OWASP API Security Top 10**, sans adaptation particulière pour l'IA.

## Selon le métier

### Forward Deployed Engineer

L'angle est le contrat : l'API exposée sera consommée par des équipes qu'on ne verra jamais et qui ne liront pas la documentation. Le connecteur vers le système patrimonial est le composant qui survivra le plus longtemps et sera repris par l'équipe du client ; il mérite plus de soin que la partie IA, et c'est rarement ainsi que le temps est réparti.

### AI Product Builder

Le contrat d'API est la couture la plus fragile d'une application générée. Le besoin est modeste et précis : des routes stables, des codes d'erreur justes, une version dans l'URL dès qu'un tiers consomme. Le défaut typique n'est pas un bug mais une **absence silencieuse** — pas de limitation de débit, pas de vérification d'autorisation sur une route, pas de gestion du cas où le service externe est indisponible.

### AI Red Teaming

Dès qu'une sortie de modèle atteint un interpréteur — SQL, shell, gabarit, code généré puis exécuté —, les règles habituelles s'appliquent intégralement : requêtes paramétrées, exécution en conteneur jetable sans réseau ni secret, validation côté serveur de toute action proposée. Le constat le plus fréquent reste l'autorisation au niveau objet absente, qui laisse un utilisateur authentifié lire les données d'un autre.

> [!warning] Piège
> Confondre authentification et autorisation. Une route qui vérifie l'identité mais pas les droits laisse n'importe quel utilisateur connecté lire les données des autres — c'est la faille la plus banale, la plus facile à introduire et la plus visible quand elle se déclenche. Elle se vérifie à la main, route par route, sur tout ce qui renvoie des données d'utilisateur.

## Pour aller plus loin

- [OWASP API Security Project (Top 10)](https://owasp.org/www-project-api-security/) — la liste des défaillances réelles, classées par fréquence.
- [What is a REST API? — Red Hat](https://www.redhat.com/en/topics/api/what-is-a-rest-api) — les principes, sans dogmatisme.
- [Roadmap API Design](https://roadmap.sh/api-design) — le parcours amont dédié, si le sujet doit être couvert en profondeur.

## Appelée par

- [[parcours/forward-deployed-engineer|Forward Deployed Engineer]]
- [[parcours/ai-product-builder|AI Product Builder]]
- [[parcours/ai-red-teaming|AI Red Teaming]]

Voisines : [[notions/controle-d-acces]], [[notions/systemes-patrimoniaux]], [[notions/mcp]], [[notions/tests-logiciels]].
