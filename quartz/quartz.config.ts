import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Atlas des metiers de l'IA et de la data -- configuration Quartz.
 *
 * Ce fichier vit dans quartz/ du depot de contenu ; quartz/build.sh le recopie
 * a la racine du clone Quartz epingle avant de construire. Ne pas l'editer dans
 * le clone : il y est ecrase a chaque construction.
 *
 * L'URL publique se regle par la variable d'environnement QUARTZ_BASE_URL, que
 * l'Action GitHub renseigne depuis l'URL reelle des Pages. Le defaut ne sert
 * qu'a l'apercu local.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Atlas des métiers de l'IA",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "fr-FR",
    baseUrl: process.env.QUARTZ_BASE_URL ?? "localhost:8080",
    // data/, tools/ et prompts/ ne sont pas dans content/ : rien a exclure de ce
    // cote. On ecarte les repertoires de travail Obsidian et les brouillons.
    ignorePatterns: ["private", "templates", ".obsidian", ".trash"],
    // Les notes portent leur date en frontmatter. Sans cela, git ou le systeme
    // de fichiers afficheraient la date du dernier passage d'un agent.
    defaultDateType: "created",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#fbfaf9",
          lightgray: "#e8e5e1",
          gray: "#9b968f",
          darkgray: "#43403c",
          dark: "#22201e",
          secondary: "#2f5d62",
          tertiary: "#7f9c8f",
          highlight: "rgba(47, 93, 98, 0.08)",
          textHighlight: "#f3d98a88",
        },
        darkMode: {
          light: "#17181a",
          lightgray: "#2f3134",
          gray: "#6d6f73",
          darkgray: "#cfd0d2",
          dark: "#eceded",
          secondary: "#8fb3b5",
          tertiary: "#7f9c8f",
          highlight: "rgba(143, 179, 181, 0.10)",
          textHighlight: "#b3aa0288",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({ priority: ["frontmatter", "git", "filesystem"] }),
      Plugin.SyntaxHighlighting({
        theme: { light: "github-light", dark: "github-dark" },
        keepBackground: false,
      }),
      // disableBrokenWikilinks : un lien vers une note pas encore ecrite devient
      // un <a class="internal broken"> inerte au lieu d'un lien qui part en 404.
      // Le corpus s'ecrit en parallele, ces liens sont nombreux et voulus ; ils
      // doivent se voir. La mise en forme est dans styles/custom.scss.
      Plugin.ObsidianFlavoredMarkdown({
        enableInHtmlEmbed: false,
        disableBrokenWikilinks: true,
        // Les cases a cocher servent de suivi de progression : Quartz retient
        // leur etat dans le navigateur, par page.
        enableCheckbox: true,
      }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({ enableSiteMap: true, enableRSS: true }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // CustomOgImages est desactive : il rend une image par page avec satori et
      // telecharge ses polices a la construction. Cout et fragilite reseau sans
      // contrepartie pour un corpus de notes.
    ],
  },
}

export default config
