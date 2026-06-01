/**
 * Post-build step: inline above-the-fold critical CSS and async-load the rest.
 *
 * The compiled CSS bundle (~60KB about.*.css) was render-blocking in <head>,
 * pinning FCP/LCP at ~2.7s on a zero-TTFB CDN. beasties extracts each page's
 * critical rules, inlines them, and rewrites the bundle <link>s to load async
 * (preload: 'swap' + <noscript> fallback).
 *
 * Runs as a standalone Node step in `npm run build` (after astro build +
 * pagefind) rather than an Astro integration: the astro:build:done hook tears
 * down Vite's module runner, which broke dynamically importing beasties.
 *
 * SAFETY:
 *  - pruneSource:false -> the full stylesheet is kept and still loads (async),
 *    so an imperfect critical extraction can at worst cause a brief flash,
 *    never permanently-broken styling.
 *  - per-file try/catch -> any page beasties cannot parse is left exactly as
 *    built (no-op), so the build can never be made worse than baseline.
 *  - fully reversible: drop this step from package.json "build".
 */
import Beasties from "beasties";
import { readdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";

const dist = path.resolve("dist");

const beasties = new Beasties({
  path: dist,
  publicPath: "/",
  preload: "swap",
  pruneSource: false,
  reduceInlineStyles: false,
  logLevel: "silent",
});

let entries = [];
try {
  entries = await readdir(dist, { recursive: true });
} catch (e) {
  console.warn(`beasties-run: cannot read ${dist} (${e.message}); skipping.`);
  process.exit(0);
}

const htmls = entries.filter(e => typeof e === "string" && e.endsWith(".html"));
let ok = 0,
  skipped = 0;
for (const rel of htmls) {
  const fp = path.join(dist, rel);
  try {
    const html = await readFile(fp, "utf8");
    const out = await beasties.process(html);
    if (out && out !== html) {
      await writeFile(fp, out);
      ok++;
    } else {
      skipped++;
    }
  } catch {
    skipped++; // leave the page exactly as built — never break it
  }
}
console.log(`beasties-run: critical CSS inlined on ${ok} pages (${skipped} unchanged) of ${htmls.length}`);
