---
title: Choisir sa plateforme
---

Quatre familles suffisent à s'orienter. Le critère qui départage en pratique n'est presque jamais la richesse fonctionnelle : c'est le modèle de licence rapporté au nombre de consultants occasionnels.

```mermaid
flowchart TD
  OD["Outils décisionnels<br/>ce qui distingue vraiment les plateformes"]
  TB["Tableur<br/>le poste de travail réel du métier"]
  VD["Visualisation de données<br/>ce que la plateforme ne fera pas à votre place"]
  PD["Plateforme de déploiement<br/>ce que l'équipe devra exploiter"]

  click OD "/notions/outils-decisionnels"
  click TB "/notions/tableur"
  click VD "/notions/visualisation-de-donnees"
  click PD "/notions/plateforme-de-deploiement"
```

## Ce qu'il faut savoir faire

- Situer les quatre familles. Les **plateformes intégrées à un écosystème** gagnent par l'existant : licences déjà là, authentification en place, tableur de l'autre côté. Les outils d'**exploration visuelle** restent supérieurs quand l'usage est de creuser librement plutôt que de suivre des indicateurs. Les outils à **sémantique en code** ont défendu le plus tôt l'idée que les définitions se versionnent, et c'est leur intérêt principal bien avant leurs graphiques. Les outils **libres** sont un choix sérieux quand le budget de licences est contraint ou que l'outil doit être embarqué.
- Compter les consultants occasionnels avant tout. L'existence d'un mode d'accès pour ceux qui ne se connecteront que trois fois par an décide plus souvent du choix que n'importe quelle fonctionnalité.
- Vérifier ce que la plateforme sait porter en propre : agrégations non additives, droits à la ligne, périodes comparables. C'est là que les écarts entre outils sont réels, et c'est rarement ce que les démonstrations montrent.
- Maîtriser un outil en profondeur plutôt que trois en surface. Connaître ses droits d'accès, ses modes de rafraîchissement et son instrumentation d'usage vaut plus qu'une familiarité avec le catalogue de graphiques de trois plateformes.
- Organiser l'export vers le tableur au lieu de le combattre. La moitié des consultations finissent par un export, parce que le métier veut recalculer à sa façon ; ce qui doit être combattu, c'est le classeur qui devient une source de vérité parallèle.
- Déployer un outil libre soi-même au moins une fois. On y voit comment sont gérés le cache, les droits et la couche sémantique, ce qu'aucune documentation commerciale n'explique.

## Les notions mobilisées

- [[notions/outils-decisionnels]] — ce qui distingue réellement les plateformes, au-delà du catalogue de visuels.
- [[notions/tableur]] — la destination finale d'une grande part des consultations, à cadrer plutôt qu'à interdire.
- [[notions/visualisation-de-donnees]] — la grammaire du graphique, que la plateforme n'impose ni ne corrige.
- [[notions/plateforme-de-deploiement]] — un outil décisionnel est aussi un système à exploiter, sauvegarder et mettre à jour.

> [!tip] La question à poser en démonstration
> « Montrez-moi comment vous calculez un taux de marge correct au niveau national à partir de données régionales, et comment vous restreignez chaque directeur régional à sa région. » Les deux réponses départagent les plateformes plus sûrement que n'importe quelle comparaison de fonctionnalités.

## Pour apprendre

- [Metabase — dépôt](https://github.com/metabase/metabase) — l'outil libre le plus simple à déployer pour comprendre le fonctionnement interne.
- [Superset — dépôt](https://github.com/apache/superset) — l'autre option libre, plus complète et plus exigeante à exploiter.
- [Visual Best Practices — Tableau](https://help.tableau.com/current/blueprint/en-us/bp_visual_best_practices.htm) — les principes d'un éditeur majeur, applicables ailleurs.
