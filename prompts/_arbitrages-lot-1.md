# Arbitrages du pilote — fin du lot 1

> Rendus le 16 septembre 2026, après lecture des six synthèses et vérification du
> dépôt. Les chantiers 07, 08 et 09 s'y conforment. Ce document fait autorité sur les
> synthèses individuelles en cas de contradiction.

## État vérifié du lot 1

Les six chantiers ont tourné dans des worktrees isolés et sont fusionnés dans `master`.
**5 715 lignes, 23 notes, 41 commits, aucune ligne d'attribution.**

Contrôle du contrat anti-duplication : **56 slugs appelés, 56 au registre, bijection
parfaite** — aucun slug inventé, aucune notion du registre laissée sans appelant. C'est
la vérification la plus importante du lot, et elle passe.

Couverture amont mesurée par `tools/roadmap_diff.py` : Data Analyst 100 %, AI Red
Teaming 98 %, BI Analyst 97 %, AI Product Builder 92 %. Le FDE affiche 75 %, mais c'est
un artefact de mesure et non un manque : ses schémas sont rédigés en français, or le
diff compare des libellés. **Convention retenue pour la suite : un schéma conserve le
libellé amont d'origine et porte la traduction dans le texte**, comme l'a fait le
chantier 05.

## Slugs proposés — 9 retenus, 7 écartés

Critère : une notion entre au registre si **au moins deux parcours** l'appellent. En
dessous, elle appartient au parcours qui la demande et y reste.

### Retenus, ajoutés au registre

| Slug | Origine | Appelants |
|---|---|---|
| `controle-d-acces` | fusion de `controle-d-acces` (03) et `authentification-et-autorisation` (04) | Red Teaming, FDE, Product Builder, BI Analyst |
| `modelisation-de-la-menace` | 03 | Red Teaming, FDE |
| `chaine-d-approvisionnement-logicielle` | 03 | Red Teaming, FDE |
| `collecte-de-donnees` | 05 | Data Analyst, BI Analyst |
| `traitement-distribue` | 05 | Data Analyst, BI Analyst |
| `series-temporelles` | 06 | BI Analyst, Data Analyst |
| `analyse-de-cohorte` | 06 | BI Analyst, Data Analyst |
| `mesure-d-usage-produit` | 04 | Product Builder, Data Analyst |
| `plateforme-de-deploiement` | 04 | Product Builder, FDE |

`authentification-et-autorisation` et `controle-d-acces` désignaient la même chose. Le
second l'emporte : il couvre aussi le moindre privilège et la propagation d'identité,
que les chantiers 02 et 03 appellent tous deux.

### Écartés — le sujet reste dans le parcours qui le porte

`exemple-adverse`, `extraction-de-modele`, `empoisonnement-de-donnees`,
`divulgation-responsable` (chantier 03) et `dorsale-geree` (chantier 04) n'ont qu'un
seul appelant. Les mutualiser créerait des fichiers que personne ne croise.

`couche-semantique` est écarté sur l'argument du chantier 06 lui-même, qui est juste :
c'est le cœur de son parcours, en faire une notion produirait la duplication que le
registre existe pour éviter.

`donnees-manquantes` est **absorbé par `qualite-des-donnees`**, qui lui consacrera une
sous-partie « Selon le métier » côté Data Analyst : mécanismes MCAR, MAR, MNAR,
imputation contre modalité explicite.

## Arbitrages de fond

**`arbitrage-deterministe-probabiliste` — les deux sens de l'erreur.** Les chantiers 02
et 04 ont relevé, séparément, que l'erreur s'inverse selon le métier : le FDE
sous-utilise l'IA sur des processus automatisables, le product builder met un modèle là
où une règle suffisait. C'est le constat le plus utile du lot. La grille de décision à
cinq questions produite par le chantier 02 **remonte dans la notion**, qui porte les
deux sens de l'erreur. Les deux parcours ne gardent que leur angle.

**`evaluation-llm` — trois angles, une notion.** FDE (instrument de négociation),
Product Builder (une fonction à base de modèle n'a pas d'état binaire), Red Teaming
(corpus adverse, critère vérifiable par programme, seuil bloquant en intégration
continue). La notion porte les trois en sous-parties. Le volet adverse **entre dans la
notion** ; le chantier 03 garde la méthode de test, qui est autre chose.

**`modelisation-dimensionnelle` — le partage proposé par le chantier 06 est retenu.**
La notion porte les définitions, le parcours porte les décisions et leurs conséquences.
Sa section de 40 lignes n'est pas une entorse au contrat : le contrat borne l'apport
d'angle sur une notion liée, pas le traitement d'un sujet attribué en propre.

**Convention de lien.** Les deux formes fonctionnent — le chantier 01 a corrigé un
défaut de Quartz qui déclarait morts tous les wikilinks en forme courte. **Aucune
reprise n'est demandée.** Pour tout contenu nouveau : chemin depuis la racine de
`content/`, soit `[[notions/<slug>]]`, `[[parcours/<slug>]]`, `[[roadmaps/<titre>]]`.

**Cartes.** La carte SVG générée depuis les positions amont **complète** le schéma
Mermaid éditorial, elle ne le remplace pas. L'argument du chantier 02 est retenu : une
carte fidèle à une roadmap de 20 nœuds dont 7 sont des renvois serait moins informative
que son schéma en quatre phases. Le Mermaid éditorial reste en tête de page, la carte
fidèle va en fin de page sous un titre « La roadmap d'origine ».

## Défauts d'outillage — corrigés par le pilote

**Le regroupement par section était faux** (signalé par le chantier 03). La cause n'est
pas celle qu'il supposait : les nœuds `section` de roadmap.sh sont de vrais conteneurs
avec une boîte englobante, que l'extraction ignorait au profit d'un simple tri par
ordonnée. Un titre dérivait donc d'une bande à l'autre. Corrigé : appartenance
géométrique à la boîte, repli sur le dernier label au-dessus quand la roadmap n'a pas
de conteneur. `data/extract/` est régénéré.

**Le décompte d'`ai-product-builder` n'est pas faux** (signalé par le chantier 04).
52 nœuds, 52 comptés. En revanche la duplication est réelle **en amont** : `Claude Code`,
`Codex` et `Bit Cloud` apparaissent chacun deux fois dans la roadmap d'origine, avec des
descriptifs différents. À traiter au dédoublonnage.

**`roadmap_diff.py` couvre désormais les treize roadmaps**, y compris un parcours
éclaté en dossier comme le FDE.

## Points laissés ouverts

- **Les 33 cibles orphelines héritées** (146 occurrences : `14 - Évaluation`,
  `16 - Sécurité et gouvernance`, `Pipeline Data`, le dossier RAG complet) pointent vers
  un coffre Obsidian plus large, extérieur à ce dépôt. Arbitrage en attente du
  propriétaire du coffre : importer, ou assumer des liens morts visibles.
- **L'URL EUR-Lex du règlement (UE) 2024/1689** n'a pas pu être confirmée par
  récupération automatique (interstitiel anti-robot). À vérifier par le chantier 08.
- **Les durées de mission FDE** et les efforts en semaines des parcours conseillés sont
  des apports propres non sourcés, signalés comme tels dans les notes. Ils le restent
  tant qu'aucun retour d'expérience chiffré ne vient les corriger.
