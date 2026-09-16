import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

/**
 * Atlas des metiers de l'IA -- disposition des pages.
 *
 * Recopie a la racine du clone Quartz par quartz/build.sh. Voir quartz.config.ts.
 *
 * Le parti pris : les retroliens et le graphe restent visibles sur toutes les
 * pages. C'est ce qui rend lisible le maillage entre un parcours metier et les
 * notions qu'il appelle -- une notion doit montrer qui la cite.
 */
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      "Les roadmaps d'origine": "https://roadmap.sh",
      "Le registre des notions": "notions/_registre",
    },
  }),
}

export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    // Ni date, ni temps de lecture, ni tags en tete de page : le lecteur doit voir
    // le contenu sans avoir a defiler.
    Component.ConditionalRender({
      component: Component.ContentMeta(),
      condition: (page) => page.fileData.slug !== "index",
    }),
  ],
  left: [
    // Le graphe prend la place du titre de site : il sert de reperage permanent,
    // et le liberer de la colonne de droite rend sa largeur au contenu.
    Component.Graph(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        { Component: Component.Search(), grow: true },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer(),
  ],
  right: [
    // L'accueil n'a ni sommaire ni retroliens utiles : la colonne disparait et le
    // tableau des metiers occupe toute la largeur.
    Component.ConditionalRender({
      component: Component.DesktopOnly(Component.TableOfContents()),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ConditionalRender({
      component: Component.Backlinks(),
      condition: (page) => page.fileData.slug !== "index",
    }),
  ],
}

export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        { Component: Component.Search(), grow: true },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer(),
  ],
  right: [],
}
