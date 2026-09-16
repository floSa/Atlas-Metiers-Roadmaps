# 07 — Notions mutualisées

Lis d'abord `PROJET.md` puis `prompts/_commun.md`. Tu es le chantier
**07 — Notions mutualisées**.

> [!warning] Ne démarre pas avant d'avoir reçu les synthèses des chantiers 02 à 06.
> Ton travail consiste précisément à traiter ce qu'ils ont demandé. Démarrer trop tôt
> revient à écrire des notions dont personne n'a besoin et à en manquer d'autres.

## Zone d'écriture exclusive

`content/notions/`, à l'exclusion de `_registre.md` que tu peux en revanche mettre à
jour — tu es le seul chantier autorisé à y toucher.

## Ce que tu reçois

- `content/notions/_registre.md` — les 52 slugs canoniques figés au cadrage.
- Les synthèses des chantiers 02 à 06, chacune listant les notions appelées, la
  définition attendue vue de son métier, et les slugs manquants proposés.
- Le corpus lui-même : `grep -ro "\[\[notions/[^]]*\]\]" content/ | sort | uniq -c`
  donne les liens réellement posés et leur fréquence. **C'est ta source de vérité**,
  plus fiable que les synthèses.

## Mission

Écrire un fichier par notion réellement appelée, et rien de plus.

### L'ordre de traitement

Trie par nombre de parcours appelants, décroissant. Une notion appelée par quatre
parcours est quatre fois plus rentable qu'une notion appelée par un seul. Si tu ne peux
pas tout traiter, il vaut mieux vingt notions solides que cinquante ébauches — dis-le
dans ta synthèse et laisse les liens orphelins visibles.

Une notion appelée par **un seul** parcours n'a probablement pas sa place ici : soit
elle appartient à ce parcours et tu le signales, soit elle est réellement transverse et
d'autres parcours auraient dû l'appeler.

### Le format d'une notion

Plus court et plus dense qu'une note de parcours. Une notion n'est pas un cours :

- **Frontmatter** : `tags`, `date`, `statut`, et `appelee-par` listant les parcours.
- **Une phrase de définition** en ouverture, autonome et non circulaire.
- **« À quoi ça sert »** — l'intérêt réel, le problème que ça résout.
- **« Ce qu'il faut savoir »** — l'essentiel en puces denses.
- **« Selon le métier »** — une sous-partie courte par parcours appelant, reprenant
  l'angle que ce parcours a demandé dans sa synthèse. C'est ce qui rend la mutualisation
  acceptable : le lecteur retrouve son point de vue sans que la notion soit dupliquée.
- **« Piège »** — l'erreur classique, `> [!warning]`.
- **« Pour aller plus loin »** — deux à cinq ressources vérifiées, pas davantage.
- **Les rétroliens** vers les parcours appelants.

Un schéma Mermaid seulement quand il montre un mécanisme. Pas de schéma décoratif.

### Arbitrages attendus

- **Fusionner** deux slugs qui recouvrent la même chose, en mettant à jour le registre
  et en signalant la redirection.
- **Scinder** une notion devenue fourre-tout.
- **Refuser** une notion demandée qui n'en est pas une, en disant pourquoi.

Toute modification du registre est tracée dans ta synthèse, ligne par ligne.

### Après écriture

Vérifie qu'il ne reste aucun lien orphelin non assumé :

```
grep -ro "\[\[notions/[^]]*\]\]" content/ | sed 's/.*\[\[notions\///;s/\]\]//' \
  | sort -u | while read s; do [ -f "content/notions/$s.md" ] || echo "ORPHELIN: $s"; done
```

Les orphelins restants doivent être listés dans ta synthèse avec la raison.

---

## Arbitrages du pilote — à lire avant de commencer

`prompts/_arbitrages-lot-1.md` contient les décisions rendues après les six synthèses
du lot 1. **Il fait autorité sur les synthèses individuelles en cas de contradiction.**
Le registre a déjà été mis à jour en conséquence : 65 notions.
