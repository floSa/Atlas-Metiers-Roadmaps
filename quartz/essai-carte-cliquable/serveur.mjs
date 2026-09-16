// Serveur statique minimal pour l'essai : sert le repertoire construit par Quartz.
// Usage : node serveur.mjs <racine> [port]
import http from "node:http"
import fs from "node:fs"
import path from "node:path"

const racine = process.argv[2]
const port = Number(process.argv[3] ?? 8099)
const types = {
  ".html": "text/html",
  ".css": "text/css",
  ".js": "text/javascript",
  ".mjs": "text/javascript",
  ".json": "application/json",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".woff2": "font/woff2",
  ".ttf": "font/ttf",
  ".xml": "application/xml",
}

http
  .createServer((req, res) => {
    const chemin = decodeURIComponent(req.url.split("?")[0])
    let fichier = path.join(racine, chemin)
    try {
      if (fs.statSync(fichier).isDirectory()) fichier = path.join(fichier, "index.html")
    } catch {
      if (fs.existsSync(fichier + ".html")) fichier = fichier + ".html"
    }
    if (!fs.existsSync(fichier)) {
      res.writeHead(404)
      return res.end("404 " + chemin)
    }
    res.writeHead(200, { "Content-Type": types[path.extname(fichier)] ?? "application/octet-stream" })
    fs.createReadStream(fichier).pipe(res)
  })
  .listen(port, () => console.error(`essai servi depuis ${racine} sur le port ${port}`))
