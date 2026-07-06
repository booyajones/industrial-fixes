import type { APIRoute } from "astro";
import { getCollection } from "astro:content";
import { NOINDEX_SLUGS } from "@/data/noindex-slugs";

export const prerender = true;

// Compact client-side index for the /diagnose tool: every live consumer
// error-code page as { a:appliance, b:brand, c:code, t:title, s:slug,
// m:most-likely-cause, d:diy|pro }. Prerendered to a static JSON file at build.
const APPLIANCES = [
  "washer", "dryer", "refrigerator", "dishwasher", "range",
  "oven", "microwave", "cooktop", "freezer",
];
const BRANDS = [
  "samsung", "lg", "whirlpool", "ge", "maytag", "frigidaire",
  "bosch", "kitchenaid", "kenmore", "electrolux", "amana",
];

export const GET: APIRoute = async () => {
  const posts = await getCollection("blog", ({ data }) => !data.draft);
  const items: Array<Record<string, string>> = [];
  for (const p of posts) {
    const slug = p.id.replace(/\.md$/, "");
    if (NOINDEX_SLUGS.has(p.id) || NOINDEX_SLUGS.has(slug)) continue; // de-linked: quality core only
    if (!/^[a-z0-9-]+$/.test(slug)) continue; // clean slugs only (safe in hrefs)
    if (!slug.endsWith("-error-code")) continue;
    const tags = (p.data.tags || []).map(t => t.toLowerCase());
    // Exact tag match first; fall back to a delimiter-bounded slug match so
    // "dishwasher" is never read as "washer" and "range" is never read as "ge".
    const slugHas = (w: string) => new RegExp(`(^|-)${w}(-|$)`).test(slug);
    const appliance = APPLIANCES.find(a => tags.includes(a)) || APPLIANCES.find(a => slugHas(a));
    const brand = BRANDS.find(b => tags.includes(b)) || BRANDS.find(b => slugHas(b));
    if (!appliance || !brand) continue;
    // Code can appear before ("5E Error Code") or after ("Error Code 5E") the phrase.
    const m = p.data.title.match(/\b([A-Za-z0-9-]{1,8})\s+(?:error|fault)\s+code/i)
      || p.data.title.match(/(?:error|fault)\s+code[:\s]+([A-Za-z0-9-]{1,8})/i);
    const code = m ? m[1] : "";
    items.push({
      a: appliance,
      b: brand,
      c: code,
      t: p.data.title.replace(/\s*[-—].*$/, "").trim(),
      s: slug,
      m: p.data.most_likely_cause || "",
      d: p.data.diy_or_pro || "",
    });
  }
  return new Response(JSON.stringify(items), {
    headers: {
      "Content-Type": "application/json",
      "Cache-Control": "public, max-age=3600",
    },
  });
};
