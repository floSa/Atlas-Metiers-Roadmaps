#!/usr/bin/env bash
#
# Construit le site de l'atlas.
#
# Quartz n'est pas verse dans ce depot : on le clone au commit epingle dans
# quartz/VERSION, on y recopie la configuration et les correctifs de ce dossier,
# puis on construit content/ par-dessus. Le depot reste un depot de contenu, et
# la montee de version de Quartz est un changement d'une ligne, visible en revue.
#
# Usage :
#   quartz/build.sh                 construit vers public/
#   quartz/build.sh --preparer      clone et installe seulement, sans construire
#   quartz/build.sh --servir        construit et sert en local, avec rechargement
#   quartz/build.sh --sortie <dir>  ecrit ailleurs que dans public/
#
# Variables :
#   QUARTZ_BASE_URL   l'URL publique du site (l'Action GitHub la renseigne)
set -euo pipefail

RACINE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOCLE="$RACINE/quartz"
CLONE="$SOCLE/.build/quartz"
SORTIE="$RACINE/public"
MODE="construire"

while [ $# -gt 0 ]; do
  case "$1" in
    --preparer) MODE="preparer" ;;
    --servir)   MODE="servir" ;;
    --sortie)   SORTIE="$2"; shift ;;
    *) echo "argument inconnu : $1" >&2; exit 2 ;;
  esac
  shift
done

lire_version() { sed -n "s/^$1=//p" "$SOCLE/VERSION"; }
COMMIT="$(lire_version commit)"
DEPOT="$(lire_version depot)"
[ -n "$COMMIT" ] || { echo "quartz/VERSION : commit absent" >&2; exit 1; }

# --- 1. le clone, au commit epingle ---------------------------------------
if [ ! -d "$CLONE/.git" ]; then
  echo "==> clonage de Quartz"
  mkdir -p "$(dirname "$CLONE")"
  git clone --quiet "$DEPOT" "$CLONE"
fi
if [ "$(git -C "$CLONE" rev-parse HEAD)" != "$COMMIT" ]; then
  echo "==> Quartz au commit $COMMIT"
  git -C "$CLONE" fetch --quiet origin
  git -C "$CLONE" checkout --quiet --force "$COMMIT"
  git -C "$CLONE" clean -qfd -e node_modules
  rm -f "$CLONE/.correctifs-appliques"
fi

# --- 2. les correctifs ----------------------------------------------------
# Ils touchent des fichiers internes de Quartz. Appliques avec git apply, ils
# echouent bruyamment si l'amont a bouge -- c'est le comportement voulu : mieux
# vaut une construction qui s'arrete qu'un correctif silencieusement perdu.
if [ ! -f "$CLONE/.correctifs-appliques" ]; then
  for correctif in "$SOCLE"/correctifs/*.patch; do
    [ -e "$correctif" ] || continue
    echo "==> correctif $(basename "$correctif")"
    if ! git -C "$CLONE" apply "$correctif"; then
      echo "ECHEC : $(basename "$correctif") ne s'applique plus sur Quartz $COMMIT." >&2
      echo "Le fichier vise a change en amont. Refaire le correctif avant d'aller plus loin." >&2
      exit 1
    fi
  done
  touch "$CLONE/.correctifs-appliques"
fi

# --- 3. la configuration --------------------------------------------------
cp "$SOCLE/quartz.config.ts" "$SOCLE/quartz.layout.ts" "$CLONE/"
cp "$SOCLE/styles/custom.scss" "$CLONE/quartz/styles/custom.scss"

# --- 4. les dependances ---------------------------------------------------
if [ ! -d "$CLONE/node_modules" ]; then
  echo "==> npm ci"
  (cd "$CLONE" && npm ci --no-audit --no-fund)
fi

[ "$MODE" = "preparer" ] && { echo "socle pret dans $CLONE"; exit 0; }

# --- 5. la construction ---------------------------------------------------
if [ "$MODE" = "servir" ]; then
  exec env -C "$CLONE" npx quartz build --serve -d "$RACINE/content" -o "$SORTIE"
fi
env -C "$CLONE" npx quartz build -d "$RACINE/content" -o "$SORTIE"
echo "==> site construit dans $SORTIE"
