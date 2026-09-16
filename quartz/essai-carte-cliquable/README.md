# Essai — carte cliquable

Ce dossier garde la trace de la décision prise à l'ouverture du chantier 01 : comment
rendre une carte de roadmap cliquable dans un site Quartz. Le résultat est dans
[`VERDICT.md`](VERDICT.md). Ce qui suit dit comment le rejouer.

## Rejouer l'essai

```sh
# 1. le socle Quartz, construit une fois
./quartz/build.sh --preparer
CLONE=.quartz-build/quartz

# 2. le contenu de l'essai, isolé du corpus
mkdir -p /tmp/essai-carte && cp -r quartz/essai-carte-cliquable/contenu/. /tmp/essai-carte/
(cd "$CLONE" && npx quartz build -d /tmp/essai-carte -o /tmp/essai-carte-public)

# 3. servir et mesurer
node quartz/essai-carte-cliquable/serveur.mjs /tmp/essai-carte-public 8099 &
npm i playwright   # une fois
CHROMIUM=/chemin/vers/chrome node quartz/essai-carte-cliquable/essai.mjs
```

`CHROMIUM` est facultatif si `npx playwright install chromium` a déjà été lancé.

## Ce qu'il y a dedans

| Fichier | Rôle |
|---|---|
| `VERDICT.md` | la décision, les mesures et ce qu'elles engagent |
| `contenu/parcours/fde.md` | la page d'essai : les deux approches côte à côte, **imbriquée** — c'est ce qui départage |
| `contenu/notions/cadrage-besoin.md` | la cible du clic, qui existe |
| `essai.mjs` | les trois mesures : où atterrit le clic, survie sans JavaScript, rétroliens |
| `serveur.mjs` | serveur statique minimal, sans dépendance |
| `captures/` | le rendu des deux approches, pour mémoire |

## Quand le rejouer

À chaque montée de version de Quartz. Le verdict tient à deux détails d'implémentation
amont qui peuvent bouger : le résolveur de liens de Quartz passe-t-il toujours dans le
HTML brut d'un `<svg>`, et Mermaid est-il toujours chargé depuis un CDN au moment de
l'affichage. Si l'un des deux change, la comparaison est à refaire.
