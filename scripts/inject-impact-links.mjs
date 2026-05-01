// inject-impact-links.mjs
// Adds a second affiliate link (Impact partner) alongside the existing
// Amazon link in fix-guide markdown files. Runs ONLY where you already
// have an Amazon link with `tag=errorcodefixes-20`. Skips files that
// already mention any of the configured Impact partner domains.
//
// Wiring:
//   - Edit IMPACT_PARTNERS below to enable a partner once Impact has
//     approved the program. `enabled: false` partners are skipped.
//   - Each partner declares which equipment categories (matched against
//     the post's tags) it should appear on, plus a base shopping URL
//     and the SubID parameter Impact requires for click attribution.
//   - First pass injects the partner link as a "Also from <Partner>"
//     row right after the Amazon row in any pipe-table that already
//     contains `errorcodefixes-20`. Idempotent (re-running is a no-op).
//
// Run a dry preview:
//   node scripts/inject-impact-links.mjs --dry
// Apply changes:
//   node scripts/inject-impact-links.mjs

import { readdir, readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";

const BLOG_DIR = "src/data/blog";
const DRY = process.argv.includes("--dry");

// Edit this once an Impact program is approved. The script will pick it up
// on next run; nothing else to change.
const IMPACT_PARTNERS = [
  {
    key: "repairclinic",
    enabled: false, // flip to true once approved
    name: "Repair Clinic",
    domain: "repairclinic.com",
    base: "https://www.repairclinic.com/Shop-For-Parts",
    // Impact attaches click attribution via the irgwc/irclickid params.
    // Replace SUBID_PLACEHOLDER with the actual Impact SubID once known.
    paramTemplate: "?irgwc=1&irclickid=ecf-{slug}&utm_source=errorcodefixes",
    matchTags: ["hvac", "refrigeration", "appliance", "boiler"],
  },
  {
    key: "supplyhouse",
    enabled: false,
    name: "SupplyHouse",
    domain: "supplyhouse.com",
    base: "https://www.supplyhouse.com/sh/control/search",
    paramTemplate: "?irgwc=1&irclickid=ecf-{slug}&utm_source=errorcodefixes",
    matchTags: ["hvac", "boiler", "refrigeration", "plumbing"],
  },
  {
    key: "grainger",
    enabled: false,
    name: "Grainger",
    domain: "grainger.com",
    base: "https://www.grainger.com/search",
    paramTemplate: "?searchQuery={query}&irgwc=1&irclickid=ecf-{slug}",
    matchTags: ["industrial", "vfd", "compressor", "electrical"],
  },
  {
    key: "jbtools",
    enabled: false,
    name: "JB Tools",
    domain: "jbtools.com",
    base: "https://www.jbtools.com/search",
    paramTemplate: "?q={query}&irgwc=1&irclickid=ecf-{slug}",
    matchTags: ["compressor", "automotive", "industrial"],
  },
  {
    key: "jracenstein",
    enabled: false,
    name: "JRacenstein",
    domain: "jracenstein.com",
    base: "https://www.jracenstein.com/search",
    paramTemplate: "?q={query}&irgwc=1&irclickid=ecf-{slug}",
    matchTags: ["plumbing", "commercial-refrigeration", "ice-machine"],
  },
];

function pickPartner(tags, slug, alreadyMentioned) {
  for (const p of IMPACT_PARTNERS) {
    if (!p.enabled) continue;
    if (alreadyMentioned.has(p.domain)) continue;
    if (!p.matchTags.some(t => tags.includes(t))) continue;
    return p;
  }
  return null;
}

function buildLink(partner, query, slug) {
  const url =
    partner.base +
    partner.paramTemplate
      .replaceAll("{slug}", slug)
      .replaceAll("{query}", encodeURIComponent(query || "replacement parts"));
  return `[${partner.name}](${url})`;
}

function parseFrontmatter(text) {
  if (!text.startsWith("---")) return { tags: [], slug: "" };
  const end = text.indexOf("\n---", 3);
  if (end === -1) return { tags: [], slug: "" };
  const fm = text.slice(0, end);
  const tags = [];
  const tagSection = fm.match(/tags:\s*\n((?:\s+-\s+.+\n?)+)/);
  if (tagSection) {
    for (const line of tagSection[1].split("\n")) {
      const m = line.match(/^\s+-\s+(.+?)\s*$/);
      if (m) tags.push(m[1].toLowerCase());
    }
  }
  const slugMatch = fm.match(/^slug:\s*(.+?)\s*$/m);
  return { tags, slug: slugMatch ? slugMatch[1] : "" };
}

function alreadyHasPartner(text) {
  const found = new Set();
  for (const p of IMPACT_PARTNERS) {
    if (text.includes(p.domain)) found.add(p.domain);
  }
  return found;
}

function injectIntoTables(text, partner, primaryQuery, slug) {
  // Find any pipe-table row that already contains errorcodefixes-20 and
  // append " | <Partner>" link to that cell. Conservative: leave tables
  // that don't mention Amazon alone.
  const lines = text.split("\n");
  let changed = false;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (!line.includes("errorcodefixes-20")) continue;
    if (line.includes(partner.domain)) continue; // safety
    // Append the partner link inside the same cell, separated by `\|`.
    lines[i] = line.replace(
      /errorcodefixes-20\)/,
      `errorcodefixes-20) \\| ${buildLink(partner, primaryQuery, slug)}`
    );
    changed = true;
  }
  return { text: lines.join("\n"), changed };
}

async function main() {
  if (!IMPACT_PARTNERS.some(p => p.enabled)) {
    console.log(
      "No Impact partners are enabled yet. Edit IMPACT_PARTNERS in this " +
        "script (set `enabled: true`) once your programs are approved."
    );
    return;
  }

  const files = (await readdir(BLOG_DIR)).filter(f => f.endsWith(".md"));
  let touched = 0;
  let skipped = 0;
  for (const f of files) {
    const path = join(BLOG_DIR, f);
    const original = await readFile(path, "utf8");
    if (!original.includes("errorcodefixes-20")) {
      skipped++;
      continue;
    }
    const { tags, slug } = parseFrontmatter(original);
    const slugSafe = slug || f.replace(/\.md$/, "");
    const mentioned = alreadyHasPartner(original);
    const partner = pickPartner(tags, slugSafe, mentioned);
    if (!partner) {
      skipped++;
      continue;
    }
    const titleMatch = original.match(/^title:\s*"?([^"\n]+)"?/m);
    const query = titleMatch ? titleMatch[1] : slugSafe;
    const { text: next, changed } = injectIntoTables(
      original,
      partner,
      query,
      slugSafe
    );
    if (!changed) {
      skipped++;
      continue;
    }
    if (!DRY) await writeFile(path, next, "utf8");
    touched++;
    console.log(`  ${DRY ? "[dry] " : ""}${f}  +${partner.name}`);
  }
  console.log(
    `\n${DRY ? "DRY RUN — " : ""}${touched} files would be updated, ${skipped} skipped.`
  );
  if (DRY) console.log("Run without --dry to apply.");
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
