import { chromium } from 'playwright'
const EXE = process.env.CHROMIUM || undefined
const base = 'http://localhost:8100'
const page_carte = '/parcours/forward-deployed-engineer/carte'
const b = await chromium.launch(EXE ? { executablePath: EXE } : {})
const ctx = await b.newContext(); const p = await ctx.newPage()
await p.goto(base + page_carte, { waitUntil: 'networkidle' })

const liens = await p.$$eval('.carte-cadre svg a', els => els.map(e => ({
  href: e.getAttribute('href'), cls: e.getAttribute('class'),
  titre: e.querySelector('title')?.textContent })))
const internes = liens.filter(l => (l.cls||'').includes('internal'))
const resultats = []
for (const l of internes) {
  const url = new URL(l.href.split('#')[0], base + page_carte).toString()
  const r = await p.request.get(url)
  resultats.push({ href: l.href, statut: r.status(), aEcrire: (l.cls||'').includes('a-ecrire') })
}
const existantes = resultats.filter(r => !r.aEcrire)
const aEcrire = resultats.filter(r => r.aEcrire)
console.log(JSON.stringify({
  ancres: liens.length,
  internes: internes.length,
  externes: liens.length - internes.length,
  ciblesExistantes: { total: existantes.length, en200: existantes.filter(r=>r.statut===200).length,
                      cassees: existantes.filter(r=>r.statut!==200) },
  ciblesAEcrire: { total: aEcrire.length, en404: aEcrire.filter(r=>r.statut===404).length },
}, null, 2))

// la carte alimente-t-elle les retroliens d'une note qui existe ?
await p.goto(base + '/roadmaps/05---Roadmap-—-AI-Engineer', { waitUntil: 'networkidle' })
console.log('retroliens de la note AI Engineer :', await p.locator('.backlinks').innerText())

// sans JavaScript
const ctx2 = await b.newContext({ javaScriptEnabled: false })
const p2 = await ctx2.newPage()
await p2.goto(base + page_carte)
console.log('sans JS — ancres de la carte :', await p2.locator('.carte-cadre svg a').count())
console.log('sans JS — liste de secours :', await p2.locator('details.carte-en-liste a').count())
await b.close()
