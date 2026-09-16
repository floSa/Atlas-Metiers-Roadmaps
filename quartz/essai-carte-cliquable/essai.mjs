// Essai comparatif : carte cliquable par `click` Mermaid contre SVG genere.
//
// Mesure, dans un vrai navigateur, sur un site Quartz construit :
//   1. le lien part-il vers la bonne URL depuis une page imbriquee ;
//   2. la carte survit-elle sans JavaScript ;
//   3. le lien alimente-t-il le graphe et les retroliens de Quartz.
//
// Prerequis : un site construit et servi (voir README.md), playwright installe,
// et un binaire Chromium accessible.
//
// Usage :
//   BASE=http://localhost:8099 CHROMIUM=/chemin/vers/chrome node essai.mjs
import { chromium } from "playwright"

const base = process.env.BASE ?? "http://localhost:8099"
const executablePath = process.env.CHROMIUM || undefined
const navigateur = await chromium.launch(executablePath ? { executablePath } : {})
const rapport = {}

// Clique une cible sur la page imbriquee /parcours/fde et rapporte ou l'on atterrit.
async function clique(selecteur, attendre) {
  const ctx = await navigateur.newContext()
  const page = await ctx.newPage()
  const echecs = []
  page.on("response", (r) => {
    if (r.status() >= 400) echecs.push([r.url().replace(base, ""), r.status()])
  })
  await page.goto(base + "/parcours/fde", { waitUntil: "networkidle" })
  if (attendre) await page.waitForSelector(attendre, { timeout: 20000 })
  await page.locator(selecteur).first().click({ timeout: 8000 })
  await page.waitForTimeout(1500)
  const resultat = {
    url: page.url(),
    corps: (await page.locator("article").first().innerText().catch(() => "")).slice(0, 60),
    echecs,
  }
  await ctx.close()
  return resultat
}

rapport.mermaidClick = await clique("code.mermaid svg g.node", "code.mermaid svg")
rapport.svgGenere = await clique("article svg a[data-slug]")

// Sans JavaScript : que reste-t-il a l'ecran ?
{
  const ctx = await navigateur.newContext({ javaScriptEnabled: false })
  const page = await ctx.newPage()
  await page.goto(base + "/parcours/fde")
  rapport.sansJavaScript = {
    mermaidRendu: (await page.locator("code.mermaid svg").count()) > 0,
    ancresSvgGenere: await page.locator("article svg a").count(),
  }
  await ctx.close()
}

// Le lien compte-t-il pour Quartz ? La cible doit lister la page imbriquee en retrolien.
{
  const ctx = await navigateur.newContext()
  const page = await ctx.newPage()
  await page.goto(base + "/notions/cadrage-besoin", { waitUntil: "networkidle" })
  rapport.retroliensDeLaCible = await page
    .locator(".backlinks")
    .innerText()
    .catch(() => "(composant absent)")
  await ctx.close()
}

await navigateur.close()
console.log(JSON.stringify(rapport, null, 2))
