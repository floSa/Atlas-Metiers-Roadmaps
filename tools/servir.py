#!/usr/bin/env python3
"""Sert le site construit, en resolvant les adresses sans extension.

Quartz ecrit `parcours/data-analyst.html` mais lie vers `parcours/data-analyst`.
GitHub Pages resout cela tout seul ; `python -m http.server` non, et toutes les
pages repondent alors 404 en local. Ce serveur reproduit le comportement de
GitHub Pages pour que la previsualisation soit fidele a la publication.

  python3 tools/servir.py [port]
"""
import functools
import http.server
import os
import pathlib
import socketserver
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent / "public"


class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        chemin = pathlib.Path(super().translate_path(path))
        if chemin.is_dir() and (chemin / "index.html").is_file():
            return str(chemin / "index.html")
        if not chemin.exists() and chemin.with_suffix(".html").is_file():
            return str(chemin.with_suffix(".html"))
        return str(chemin)

    def log_message(self, fmt, *args):  # une ligne par requete suffit
        if not str(args[1] if len(args) > 1 else "").startswith("2"):
            super().log_message(fmt, *args)


def main() -> int:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    if not RACINE.is_dir():
        print("Site non construit : lancer d'abord bash quartz/build.sh", file=sys.stderr)
        return 1
    os.chdir(RACINE)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", port), functools.partial(Handler, directory=str(RACINE))) as srv:
        print(f"http://localhost:{port}")
        srv.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
