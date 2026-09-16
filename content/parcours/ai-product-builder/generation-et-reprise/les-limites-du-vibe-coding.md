---
title: Les limites du vibe coding
---

Niveau attendu : **référence**. Savoir nommer l'absence silencieuse — ce que le générateur n'a pas écrit et que personne ne réclamera — est ce qu'on attend de ce métier dans une salle où tout le monde a vu la démonstration marcher.

Le débat public oscille entre deux positions également fausses : « ça remplace les développeurs » et « ça ne produit que de la dette ». La position tenable est plus ennuyeuse — le vibe coding est excellent là où se tromper ne coûte rien, mauvais là où l'erreur est silencieuse et durable.

```mermaid
flowchart TD
  A["La route sans autorisation<br/>tout fonctionne, chacun lit les données des autres"]
  J["Le service sans journal<br/>personne ne le demande dans l'énoncé"]
  T["Le test qui ne peut pas échouer<br/>un voyant vert, pas un filet"]
  E["Le tiers supposé toujours disponible<br/>ni délai d'attente, ni repli"]
  G["Ce que devient la compétence<br/>générer ce qu'on saurait écrire"]

  click A "/notions/controle-d-acces"
  click J "/notions/observabilite"
  click T "/notions/tests-logiciels"
  click E "/parcours/ai-product-builder/du-prototype-au-produit/le-comportement-en-erreur"
  click G "/notions/assistants-de-codage"
```

## Ce qu'il faut savoir faire

- Utiliser la génération sans réserve là où elle est bonne : franchir la page blanche, produire un squelette conventionnel, explorer trois directions en une heure au lieu de trois jours, écrire les parties fastidieuses et vérifiables — formulaires, migrations, adaptateurs, scripts internes, tests d'interface.
- Reconnaître le terrain où elle est structurellement mauvaise : tout choix durable pris une fois. Modèle de données, frontières de modules, gestion des droits, comportement en cas d'erreur, limites de charge. Le générateur propose la solution la plus fréquente, qui est souvent la bonne — et quand elle ne l'est pas, rien dans la sortie ne le signale.
- Chercher **l'absence silencieuse** plutôt que le bug : pas de limitation de débit, pas de vérification d'autorisation sur une route, pas de journalisation, pas de gestion du cas où le service externe est indisponible. Le code livré fonctionne ; ce qui manque ne produit aucune erreur jusqu'au jour où.
- Relire en se demandant « qu'est-ce qui devrait être là et n'y est pas », question à laquelle l'écriture de code n'entraîne pas. C'est une compétence de relecture, et elle s'acquiert mal en produisant.
- Appliquer la règle d'usage : **générer ce qu'on saurait écrire, écrire ce qu'on ne saurait pas juger.** Elle s'applique fichier par fichier, sans débat philosophique.
- Accepter que le facteur de réussite le plus discriminant ne soit pas le talent de formulation mais le niveau du lecteur. Le même outil produit un résultat solide entre les mains de quelqu'un qui sait ce qu'il aurait écrit, et un château de cartes entre celles de quelqu'un qui ne peut pas juger.

## Les notions mobilisées

- [[notions/assistants-de-codage]] — le déplacement réel est du débit d'écriture vers la capacité de jugement ; c'est cette dernière qui devient le facteur limitant.
- [[notions/controle-d-acces]] — l'exemple canonique de l'absence silencieuse : rien ne signale qu'une route ne vérifie pas les droits, et tout fonctionne.
- [[notions/observabilite]] — la journalisation fait partie de ce qui n'est jamais généré spontanément, parce que personne ne la demande dans l'énoncé.
- [[notions/tests-logiciels]] — sur du code qu'on n'a pas écrit, les tests sont autant un outil de compréhension qu'une vérification.

> [!warning] Piège
> Traiter la vitesse de production comme la mesure du progrès. Le débit de code n'a jamais été le facteur limitant d'un produit — la compréhension du besoin et la capacité à faire évoluer l'existant le sont. Multiplier par dix la production d'une équipe qui n'a pas augmenté sa capacité de relecture ne la fait pas aller dix fois plus vite : elle accumule un stock qu'elle ne peut plus vérifier.

## Pour apprendre

- [Roadmap vibe-coding](https://roadmap.sh/vibe-coding) — le versant pratique du sujet : la boucle d'itération, ses garde-fous, et les erreurs de débutant.
- [Will AI make us all product builders?](https://www.fundament.design/p/will-ai-make-us-all-product-builders?hide_intro_popup=true) — l'argument de fond sur le déplacement du goulot d'étranglement vers le jugement.
