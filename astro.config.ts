import { defineConfig, envField, fontProviders } from "astro/config";
import tailwindcss from "@tailwindcss/vite";
import sitemap from "@astrojs/sitemap";
import remarkToc from "remark-toc";
import remarkCollapse from "remark-collapse";
import remarkHeadingIds from "./src/utils/remark-heading-ids.mjs";
import rehypeNoskim from "./src/utils/rehype-noskim.mjs";
import {
  transformerNotationDiff,
  transformerNotationHighlight,
  transformerNotationWordHighlight,
} from "@shikijs/transformers";
import { transformerFileName } from "./src/utils/transformers/fileName";
import { SITE } from "./src/config";
import { NOINDEX_SLUGS } from "./src/data/noindex-slugs";

// https://astro.build/config
export default defineConfig({
  site: SITE.website,
  integrations: [
    sitemap({
      // Strip paginated archives (/posts/2/, /posts/3/...) — they're noindexed
      // in Layout.astro and don't belong in the crawl queue. Also strip
      // /archives if disabled in SITE config.
      filter: page => {
        if (!SITE.showArchives && page.endsWith("/archives")) return false;
        // Match https://errorcodefixes.com/posts/<digits>/ but keep /posts/<slug>/
        if (/\/posts\/\d+\/?$/.test(page)) return false;
        // Tag pages are meta-noindexed (Layout.astro) — listing 650 of them in
        // the sitemap sends contradictory crawl signals. Keep them out.
        if (/\/tags\//.test(page)) return false;
        // Quality-consolidation: keep noindexed zero-demand posts OUT of the
        // sitemap so Google crawls the quality core, not the 5,680-page farm.
        const m = page.match(/\/posts\/([^/]+)\/?$/);
        if (m && NOINDEX_SLUGS.has(m[1])) return false;
        return true;
      },
    }),
  ],
  markdown: {
    remarkPlugins: [remarkHeadingIds, remarkToc, [remarkCollapse, { test: "Table of contents" }]],
    rehypePlugins: [rehypeNoskim],
    shikiConfig: {
      // For more themes, visit https://shiki.style/themes
      themes: { light: "min-light", dark: "night-owl" },
      defaultColor: false,
      wrap: false,
      transformers: [
        transformerFileName({ style: "v2", hideDot: false }),
        transformerNotationHighlight(),
        transformerNotationWordHighlight(),
        transformerNotationDiff({ matchAlgorithm: "v3" }),
      ],
    },
  },
  vite: {
    // eslint-disable-next-line
    // @ts-ignore
    // This will be fixed in Astro 6 with Vite 7 support
    // See: https://github.com/withastro/astro/issues/14030
    plugins: [tailwindcss()],
    optimizeDeps: {
      exclude: ["@resvg/resvg-js"],
    },
  },
  image: {
    responsiveStyles: true,
    layout: "constrained",
  },
  env: {
    schema: {
      PUBLIC_GOOGLE_SITE_VERIFICATION: envField.string({
        access: "public",
        context: "client",
        optional: true,
      }),
      PUBLIC_GA4_MEASUREMENT_ID: envField.string({
        access: "public",
        context: "client",
        optional: true,
      }),
      PUBLIC_ADSENSE_CLIENT: envField.string({
        access: "public",
        context: "client",
        optional: true,
      }),
    },
  },
  experimental: {
    preserveScriptOrder: true,
    fonts: [
      {
        name: "Google Sans Code",
        cssVariable: "--font-google-sans-code",
        provider: fontProviders.google(),
        fallbacks: ["monospace"],
        weights: [300, 400, 500, 600, 700],
        styles: ["normal", "italic"],
      },
    ],
  },
});
