import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { resolveRelative, simplifySlug, FullSlug } from "../util/path"

/**
 * Navigation de bas de page, pour un corpus organise en arbre.
 *
 *   <- page precedente du meme niveau | ^ niveau superieur | page suivante ->
 *
 * Elle evite de remonter en haut de page pour changer de section. Ce qui n'existe
 * pas ne s'affiche pas : une page sans voisin de gauche n'a pas de fleche gauche.
 *
 * L'ordre des voisins n'est pas alphabetique : c'est celui dans lequel la page
 * parente les enumere, donc l'ordre d'apprentissage voulu par l'auteur. On le lit
 * dans les liens sortants du parent.
 */

const titre = (f: any, secours: string) =>
  (f?.frontmatter?.title as string) ?? secours

export default (() => {
  const NavigationArbre: QuartzComponent = ({ fileData, allFiles }: QuartzComponentProps) => {
    const slug = simplifySlug(fileData.slug!)
    const segments = slug.split("/").filter(Boolean)
    if (segments.length === 0) return null

    // simplifySlug a deja retire le "/index" final : les segments designent donc
    // la page elle-meme, qu'elle soit une feuille ou l'index d'un dossier.
    const parentSegments = segments.slice(0, -1)
    const parentSlug = parentSegments.length ? `${parentSegments.join("/")}/index` : "index"
    const parent = allFiles.find((f) => f.slug === parentSlug)

    let voisins: typeof allFiles = []
    if (parent) {
      const prefixe = parentSegments.length ? `${parentSegments.join("/")}/` : ""
      const candidats = allFiles.filter((f) => {
        const s = f.slug!
        if (s === parentSlug || s === fileData.slug) return false
        if (!s.startsWith(prefixe)) return false
        const reste = s.slice(prefixe.length)
        // Une page du meme niveau : soit une feuille, soit l'index d'un sous-dossier.
        return reste.split("/").length <= 2 && (!reste.includes("/") || reste.endsWith("/index"))
      })
      // L'ordre du parent fait foi ; ce qu'il ne cite pas vient ensuite.
      const ordre = (parent.links ?? []).map((l) => simplifySlug(l as FullSlug))
      const rang = (f: any) => {
        const i = ordre.indexOf(simplifySlug(f.slug))
        return i === -1 ? 9999 : i
      }
      voisins = [...candidats, fileData as any].sort((a, b) => rang(a) - rang(b))
    }

    const position = voisins.findIndex((f) => f.slug === fileData.slug)
    const precedent = position > 0 ? voisins[position - 1] : undefined
    const suivant = position >= 0 && position < voisins.length - 1 ? voisins[position + 1] : undefined

    if (!precedent && !parent && !suivant) return null

    return (
      <nav class="navigation-arbre" aria-label="Navigation dans le parcours">
        <div class="nav-precedent">
          {precedent && (
            <a href={resolveRelative(fileData.slug!, precedent.slug!)} class="internal">
              <span aria-hidden="true">←</span> {titre(precedent, "Précédent")}
            </a>
          )}
        </div>
        <div class="nav-parent">
          {parent && (
            <a href={resolveRelative(fileData.slug!, parent.slug!)} class="internal">
              <span aria-hidden="true">↑</span> {titre(parent, "Niveau supérieur")}
            </a>
          )}
        </div>
        <div class="nav-suivant">
          {suivant && (
            <a href={resolveRelative(fileData.slug!, suivant.slug!)} class="internal">
              {titre(suivant, "Suivant")} <span aria-hidden="true">→</span>
            </a>
          )}
        </div>
      </nav>
    )
  }

  NavigationArbre.css = `
  .navigation-arbre {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    align-items: center;
    gap: 1rem;
    margin: 2.5rem 0 1rem;
    padding-top: 1rem;
    border-top: 1px solid var(--lightgray);
    font-size: 0.92rem;
  }
  .navigation-arbre .nav-precedent { text-align: left; }
  .navigation-arbre .nav-parent { text-align: center; }
  .navigation-arbre .nav-suivant { text-align: right; }
  .navigation-arbre a {
    color: var(--darkgray);
    text-decoration: none;
    background-image: none;
  }
  .navigation-arbre a:hover { color: var(--secondary); }
  .navigation-arbre .nav-parent a { font-weight: 600; }
  @media all and (max-width: 800px) {
    .navigation-arbre {
      grid-template-columns: 1fr;
      gap: 0.5rem;
      text-align: left;
    }
    .navigation-arbre .nav-parent,
    .navigation-arbre .nav-suivant { text-align: left; }
  }
  `

  return NavigationArbre
}) satisfies QuartzComponentConstructor
