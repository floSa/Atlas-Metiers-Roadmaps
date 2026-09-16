---
title: Les outils de codage assisté
---

Niveau attendu : **autonomie**. On change d'outil selon le travail du jour et on assume ce choix devant une équipe qui en utilise un autre : c'est le raisonnement qui se transmet, jamais l'outil.

Trois catégories stables, un critère de choix en une question, et un facteur de qualité qui ne dépend pas du modèle. Les noms changent tous les six mois ; les cases, non.

```mermaid
flowchart TD
  O["Les trois catégories<br/>terminal, éditeur augmenté, complétion"]
  R["Le retour d'exécution<br/>le seul facteur qui ne dépend pas du modèle"]
  I["La chaîne qui exécute les tests<br/>ce qui rend le retour systématique"]
  C["Le contexte donné à l'outil<br/>conventions, commandes, interdits"]
  M["Brancher l'outil sur le reste<br/>dépôt, base, suivi de tickets"]

  click O "/notions/assistants-de-codage"
  click R "/notions/tests-logiciels"
  click I "/notions/integration-continue"
  click C "/notions/ingenierie-de-prompt"
  click M "/notions/mcp"
```

## Ce qu'il faut savoir faire

- Reconnaître l'**assistant en terminal** : un agent qui lit le dépôt, modifie plusieurs fichiers, exécute les tests et boucle sur le résultat. C'est la catégorie des tâches qui traversent l'application — tracer un bug, renommer un concept partout, ajouter une couche de validation.
- Reconnaître l'**éditeur augmenté** : un environnement qui indexe le dépôt et répond sur la sélection courante. C'est la catégorie du travail d'exploration — ouvrir un fichier inconnu, demander ce qu'il fait, modifier avec la structure sous les yeux.
- Reconnaître la **complétion en ligne** : la prédiction du bloc suivant pendant la frappe. Utile quand on sait déjà ce qu'on écrit, inutile quand on cherche à comprendre.
- Trancher avec une seule question : **je sais ce que je veux écrire, ou je cherche à savoir ce qui existe ?** Première réponse, complétion. Deuxième, éditeur augmenté. Tâche traversante dont le succès est vérifiable par un test, assistant en terminal.
- Brancher systématiquement l'outil sur un **retour d'exécution** — tests, typage, linter. Un agent qui voit le résultat se corrige ; le même agent sans rien produit du code plausible et faux avec une confiance identique.
- Tenir un fichier d'instructions à la racine du dépôt : conventions, commande de test, ce qu'on ne touche pas. Il améliore plus la qualité de sortie qu'un changement d'outil, et il sert à toute la catégorie d'un coup. Quand un assistant refait deux fois la même bêtise, la correction va dans ce fichier, pas dans la conversation.

## Les notions mobilisées

- [[notions/assistants-de-codage]] — les trois catégories et leurs usages réels ; ce qui est propre à ce métier, c'est que le code à modifier n'a pas été écrit par celui qui le modifie.
- [[notions/tests-logiciels]] — le retour d'exécution est le seul facteur de qualité qui ne dépend pas du modèle choisi, donc le seul sur lequel on a prise.
- [[notions/integration-continue]] — ce qui transforme le retour d'exécution en habitude plutôt qu'en intention.
- [[notions/ingenierie-de-prompt]] — le fichier d'instructions de dépôt est du contexte permanent : c'est la forme qui tient, par opposition à la consigne répétée en conversation.
- [[notions/mcp]] — pour ce métier, l'usage courant du protocole n'est pas dans le produit livré mais dans l'atelier : brancher les assistants sur le dépôt, la base et le suivi de tickets.

## Pour apprendre

- [Claude Code](https://code.claude.com/docs/en/overview) et sa [roadmap dédiée](https://roadmap.sh/claude-code) — la catégorie assistant en terminal, documentée de bout en bout.
- [Codex](https://developers.openai.com/codex) et [Gemini CLI](https://geminicli.com/docs/) — les deux autres représentants de la même case, utiles pour voir ce qui est commun à la catégorie.
- [Cursor](https://cursor.com/docs) — l'éditeur augmenté le plus répandu.
- [GitHub Copilot](https://docs.github.com/en/copilot) — la complétion en ligne, et la limite de ce qu'elle sait faire.
