---
tags: [socle, quartz, carte, essai]
date: 2026-09-16
statut: actif
---

# Essai — la carte cliquable : `click` Mermaid contre SVG généré

> [!abstract] Le cadrage suspectait la politique de sécurité des générateurs de sites de
> neutraliser le `click` natif de Mermaid. **C'est faux pour Quartz 4.5.2** : le `click`
> fonctionne. Mais il perd sur trois autres points, mesurés, et c'est le SVG généré qui
> l'emporte.

**Verdict : SVG généré.** Mesuré le 16 septembre 2026, Quartz 4.5.2 (`d25a6ea`),
Chrome for Testing 151, sur une page d'essai réduite aux deux approches.

---

## Le protocole

Un site Quartz construit avec deux pages :

- `parcours/fde` — **une page imbriquée**, qui porte les deux approches côte à côte et
  vise la même cible, `notions/cadrage-besoin` ;
- `notions/cadrage-besoin` — la cible, qui existe.

Le choix d'une page imbriquée n'est pas cosmétique : c'est lui qui départage. Les cartes
vivront sous `content/parcours/<metier>/`, jamais à la racine.

Trois mesures, dans un vrai navigateur : où atterrit le clic, que reste-t-il sans
JavaScript, et le lien alimente-t-il le graphe de Quartz.

Rejouable : voir `README.md` de ce dossier.

---

## Le résultat brut

```json
{
  "mermaidClick": {
    "url": "http://localhost:8099/parcours/notions/cadrage-besoin",
    "corps": "",
    "echecs": [["/parcours/notions/cadrage-besoin", 404]]
  },
  "svgGenere": {
    "url": "http://localhost:8099/notions/cadrage-besoin",
    "corps": "Cible existante.",
    "echecs": []
  },
  "sansJavaScript": {
    "mermaidRendu": false,
    "ancresSvgGenere": 1
  },
  "retroliensDeLaCible": "Backlinks\nParcours FDE (page imbriquee)\nEssai SVG lien"
}
```

---

## Ce que ça dit

### Le `click` Mermaid n'est pas bloqué — il est hors circuit

Quartz initialise Mermaid avec `securityLevel: "loose"`
(`quartz/components/scripts/mermaid.inline.ts`), ce qui active les `click`. Le clic
navigue bel et bien. Le problème est ailleurs : **l'URL n'est jamais réécrite**.

Mermaid produit son SVG dans le navigateur, longtemps après que Quartz a fini de
résoudre les liens. Le `click A "notions/cadrage-besoin"` reste une chaîne littérale que
le navigateur résout contre l'URL courante. Depuis `/parcours/fde`, elle donne
`/parcours/notions/cadrage-besoin` — **404**.

Écrire un chemin absolu ne sauve pas l'affaire : GitHub Pages sert un dépôt de projet
sous `/<depot>/`, alors que l'aperçu local sert sous `/`. Un chemin absolu est juste
faux à l'un des deux endroits. Il faudrait générer les cartes en injectant l'URL de
déploiement — c'est-à-dire produire le Markdown par script, donc payer déjà le coût de
la seconde approche, sans en toucher les bénéfices.

### Sans JavaScript, la carte Mermaid n'existe pas

`mermaidRendu: false`. Mermaid est importé depuis `cdnjs.cloudflare.com` au moment de
l'affichage. Pas de JavaScript, pas de CDN joignable, pas de carte — sur un poste
d'entreprise filtré, la pièce maîtresse du site est une page blanche. Le SVG généré,
lui, est dans le HTML : il s'affiche et ses liens fonctionnent.

### Le SVG généré compte pour le graphe, le Mermaid non

C'est le point qu'on n'attendait pas. Quartz passe son résolveur de liens sur le HTML
brut du Markdown, **y compris à l'intérieur d'un `<svg>`** :

```html
<!-- écrit dans la note -->
<a href="notions/cadrage-besoin">…</a>
<!-- émis par Quartz depuis une page imbriquée -->
<a href="../notions/cadrage-besoin" class="internal" data-slug="notions/cadrage-besoin">…</a>
```

Conséquence : chaque nœud de la carte devient un lien interne de plein droit. Il apparaît
dans les **rétroliens** de la notion visée (`retroliensDeLaCible` liste bien la page
imbriquée), dans le **graphe de liens**, et il est pris en charge par la navigation SPA
et les aperçus au survol. La carte n'est plus une image posée à côté du corpus : elle en
fait partie.

Un `click` Mermaid ne produit rien de tout ça. La notion visée ne saura jamais qu'une
carte pointe vers elle.

---

## Le tableau

| Critère | `click` Mermaid | SVG généré |
|---|---|---|
| Le clic atteint la cible depuis une page imbriquée | non — 404 | oui |
| Survit à un déploiement sous un sous-chemin | non | oui |
| Fonctionne sans JavaScript | non | oui |
| Fonctionne sans CDN externe | non | oui |
| Alimente rétroliens et graphe | non | oui |
| Reproduit la disposition exacte de roadmap.sh | non | oui |
| Coût de mise en œuvre | nul | un script |

---

## Ce que ça engage

Le SVG est généré par `tools/roadmap_render.py` à partir de la capture brute
`data/raw/<slug>/<date>.json`, qui porte la position, la largeur et la hauteur de chaque
nœud — la disposition de roadmap.sh est donc reproduite au pixel, pas réinventée.

Deux limites acceptées :

- **Quartz injecte une icône « lien externe » dans les ancres externes**, y compris à
  l'intérieur d'un SVG, où elle se pose de travers. Le rendu n'émet donc que des liens
  internes ; les renvois vers roadmap.sh restent dans le texte de la note.
- **Le SVG est du HTML brut dans du Markdown.** Il s'affiche dans Obsidian comme dans
  Quartz, mais il n'est pas lisible à la source. C'est un fichier généré : on le
  régénère, on ne l'édite pas.

Mermaid reste utilisé partout ailleurs — les schémas d'étape des notes, qui n'ont pas
besoin d'être cliquables.
