#!/usr/bin/env node
/**
 * build-field-reference.mjs
 *
 * Builds the "Industrial Fault-Code Field Reference" — a sellable, offline,
 * print-optimized HTML compilation of the site's industrial quality-core
 * content (code tables + condensed field diagnostics), with a per-section
 * citation back to the source page on errorcodefixes.com.
 *
 * STRICT compilation rules:
 *  - Source of truth is src/data/blog/*.md ONLY. No new facts are authored
 *    here; every table row and every entry is extracted from a published page
 *    and cites that page's URL.
 *  - Quality core only: draft:true pages and NOINDEX_SLUGS pages are skipped.
 *  - Deterministic: output depends only on the source markdown (the "content
 *    updated" stamp is the max modDatetime of the included pages, not the
 *    build clock).
 *
 * Outputs:
 *  - product/field-reference-full.html        FULL edition (gitignored — the
 *    paid artifact must never land in this public repo; it is uploaded to the
 *    payment platform out-of-band)
 *  - public/resources/field-reference-sample.html   SAMPLE edition (2 brands)
 *  - matching .pdf files when a local Chrome/Chromium is available
 *    (headless --print-to-pdf; the HTML is the PDF master)
 *  - src/data/field-reference-stats.json      counts consumed by
 *    src/pages/field-reference.astro and the PostDetails promo card
 *
 * Run:  node scripts/build-field-reference.mjs [--stats-only] [--no-pdf]
 */

import { readFileSync, readdirSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { spawnSync } from "node:child_process";
import path from "node:path";
import { fileURLToPath } from "node:url";

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const BLOG_DIR = path.join(REPO, "src", "data", "blog");
const SITE_URL = "https://errorcodefixes.com";

const STATS_ONLY = process.argv.includes("--stats-only");
const NO_PDF = process.argv.includes("--no-pdf");

/* ------------------------------------------------------------------ *
 * Section / brand curation
 * ------------------------------------------------------------------ */

// Ordered. First matcher that hits a page claims it. Matchers see
// { slug, tags } with lowercase tags.
const SECTIONS = [
  {
    id: "fanuc", brand: "Fanuc", group: "CNC Machine Tools",
    title: "Fanuc CNC Controls",
    match: p => p.slug.startsWith("fanuc-"),
  },
  {
    id: "haas", brand: "Haas", group: "CNC Machine Tools",
    title: "Haas CNC Machines",
    match: p => p.slug.startsWith("haas-"),
  },
  {
    id: "abb", brand: "ABB", group: "VFDs & Industrial Drives",
    title: "ABB Drives (ACS / ACH)",
    // Breakers/switchgear are out of scope — this is the VFD section.
    match: p => (p.slug.startsWith("abb-") || p.tags.includes("abb")) &&
      !/circuit-breaker|tmax|emax/.test(p.slug),
  },
  {
    id: "siemens", brand: "Siemens", group: "VFDs & Industrial Drives",
    title: "Siemens Drives, CNC & PLC",
    match: p =>
      (p.slug.startsWith("siemens-") || p.slug.startsWith("sinamics") || p.slug.startsWith("micromaster")) &&
      !/circuit-breaker|desigo|fire-alarm|sentron|siprotec/.test(p.slug),
  },
  {
    id: "yaskawa", brand: "Yaskawa", group: "VFDs & Industrial Drives",
    title: "Yaskawa Drives (A1000 / GA500 / GA700 / GA800 / V1000)",
    match: p => p.slug.startsWith("yaskawa-") || p.tags.includes("yaskawa"),
  },
  {
    id: "danfoss", brand: "Danfoss", group: "VFDs & Industrial Drives",
    title: "Danfoss Drives (VLT FC-Series)",
    match: p => p.slug.startsWith("danfoss-") || p.tags.includes("danfoss"),
  },
  {
    id: "mitsubishi", brand: "Mitsubishi", group: "VFDs & Industrial Drives",
    title: "Mitsubishi Drives & Servo (FR / MR-J)",
    match: p =>
      p.slug.startsWith("mitsubishi-") &&
      (p.tags.includes("vfd") || p.tags.includes("servo") || p.tags.includes("plc") ||
        p.tags.includes("cnc") || p.tags.includes("industrial")) &&
      !p.tags.includes("mini-split") && !p.tags.includes("heat-pump"),
  },
  {
    id: "sew", brand: "SEW-Eurodrive", group: "VFDs & Industrial Drives",
    title: "SEW-Eurodrive (Movitrac / Movidrive)",
    match: p => p.slug.startsWith("sew-") || p.tags.includes("sew-eurodrive"),
  },
  {
    id: "york", brand: "York", group: "Chillers",
    title: "York Chillers (OptiView)",
    match: p =>
      (p.slug.startsWith("york-") || p.tags.includes("york")) &&
      (p.tags.includes("chiller") || /chiller|ycal|ylaa|yvaa/.test(p.slug)),
  },
  {
    id: "trane", brand: "Trane", group: "Chillers",
    title: "Trane Chillers (Tracer CH530)",
    match: p =>
      (p.slug.startsWith("trane-") || p.tags.includes("trane")) &&
      (p.tags.includes("chiller") || /chiller|cvhf|cgam|rtac|rthd/.test(p.slug)),
  },
  {
    id: "hoshizaki", brand: "Hoshizaki", group: "Ice Machines & Refrigeration",
    title: "Hoshizaki Ice Machines",
    match: p => p.slug.startsWith("hoshizaki-") || p.tags.includes("hoshizaki"),
  },
  {
    id: "manitowoc", brand: "Manitowoc", group: "Ice Machines & Refrigeration",
    title: "Manitowoc Ice Machines",
    match: p => p.slug.startsWith("manitowoc-") || p.tags.includes("manitowoc"),
  },
  {
    id: "scotsman", brand: "Scotsman", group: "Ice Machines & Refrigeration",
    title: "Scotsman Ice Machines",
    match: p => p.slug.startsWith("scotsman-") || p.tags.includes("scotsman"),
  },
  {
    id: "rational", brand: "Rational", group: "Commercial Kitchen",
    title: "Rational Combi Ovens",
    match: p => p.slug.startsWith("rational-") || p.tags.includes("rational"),
  },
  {
    id: "hobart", brand: "Hobart", group: "Commercial Kitchen",
    title: "Hobart Dish Machines",
    match: p => p.slug.startsWith("hobart-") || p.tags.includes("hobart"),
  },
  {
    id: "apc", brand: "APC", group: "Power & Backup",
    title: "APC UPS Systems",
    match: p => p.slug.startsWith("apc-") || p.tags.includes("apc"),
  },
  {
    id: "generac", brand: "Generac", group: "Power & Backup",
    title: "Generac Generators",
    match: p => p.slug.startsWith("generac-") || p.tags.includes("generac"),
  },
];

// SAMPLE edition: two brands, one drives + one refrigeration — a cross-trade
// taste of the full edition.
const SAMPLE_SECTION_IDS = ["abb", "hoshizaki"];

/* ------------------------------------------------------------------ *
 * Markdown parsing helpers
 * ------------------------------------------------------------------ */

function parseFrontmatter(text) {
  if (!text.startsWith("---")) return null;
  const end = text.indexOf("\n---", 3);
  if (end === -1) return null;
  const fmBlock = text.slice(3, end);
  const body = text.slice(end + 4).replace(/^-*\n/, "");
  const fm = {};
  let listKey = null;
  for (const line of fmBlock.split("\n")) {
    if (/^\s+-\s+/.test(line) && listKey) {
      fm[listKey].push(line.replace(/^\s+-\s+/, "").trim().replace(/^["']|["']$/g, ""));
      continue;
    }
    const m = line.match(/^([A-Za-z_]+):\s*(.*)$/);
    if (!m) continue;
    const [, key, raw] = m;
    const val = raw.trim();
    if (val === "") {
      fm[key] = [];
      listKey = key;
    } else if (val.startsWith("[") && val.endsWith("]")) {
      // Inline YAML flow array: `tags: [vfd, danfoss]`. Already used by ~10
      // live posts. Parsing this as a plain string silently yielded an empty
      // tag list downstream, which could drop a real page out of a PAID
      // product with no warning.
      fm[key] = val.slice(1, -1).split(",")
        .map(v => v.trim().replace(/^["']|["']$/g, ""))
        .filter(Boolean);
      listKey = null;
    } else {
      fm[key] = val.replace(/^["']|["']$/g, "");
      listKey = null;
    }
  }
  return { fm, body };
}

// Strip inline markdown down to plain text.
function cleanInline(s) {
  return String(s ?? "")
    .replace(/\[([^\]]*)\]\([^)]*\)/g, "$1") // links -> text
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/\*([^*]+)\*/g, "$1")
    .replace(/`([^`]*)`/g, "$1")
    .replace(/<br\s*\/?>/gi, " ")
    .replace(/<[^>]+>/g, "")
    .replace(/\s+/g, " ")
    .trim();
}

function esc(s) {
  return String(s ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

// Table-caption cosmetics: source headings occasionally lowercase acronyms
// ("More Abb Vfd fault codes"). Display-only normalization, data untouched.
const ACRONYMS = ["ABB", "VFD", "CNC", "PLC", "UPS", "LED", "STO", "HVAC", "VLT", "EFB", "APC", "CPF", "IGBT"];
function fixAcronyms(s) {
  let out = String(s ?? "");
  for (const a of ACRONYMS) {
    out = out.replace(new RegExp(`\\b${a}\\b`, "gi"), a);
  }
  return out;
}

function firstSentence(s, cap = 220) {
  const t = cleanInline(s);
  if (!t) return "";
  const m = t.match(/^.{20,}?[.!?](?=\s|$)/);
  const out = m ? m[0] : t;
  return out.length > cap ? out.slice(0, cap - 1).replace(/\s+\S*$/, "") + "…" : out;
}

// Markdown tables whose header looks like a code column. Returns
// [{ label, header:[], rows:[[]] }]
function extractCodeTables(body) {
  const lines = body.split("\n");
  const tables = [];
  let lastHeading = "";
  for (let i = 0; i < lines.length; i++) {
    const hm = lines[i].match(/^#{2,4}\s+(.*)$/);
    if (hm) {
      lastHeading = cleanInline(hm[1].replace(/\{#[^}]*\}\s*$/, ""));
      continue;
    }
    if (!/^\s*\|/.test(lines[i]) || !/^\s*\|[\s:|-]+\|\s*$/.test(lines[i + 1] ?? "")) continue;
    const splitRow = line =>
      line.trim().replace(/^\|/, "").replace(/\|\s*$/, "").split("|").map(c => cleanInline(c));
    const header = splitRow(lines[i]);
    const rows = [];
    let j = i + 2;
    while (j < lines.length && /^\s*\|/.test(lines[j])) {
      const cells = splitRow(lines[j]);
      while (cells.length < header.length) cells.push("");
      rows.push(cells.slice(0, Math.min(header.length, 5)));
      j++;
    }
    const codeHeaded = /code|fault|alarm|error|display|flash/i.test(
      (header[0] ?? "") + " " + (header[1] ?? "")
    );
    // Parts/pricing tables are NOT reference content (prices go stale, and the
    // product's positioning is "we don't sell parts"). "Order Code" headers
    // would otherwise sneak them past the code-column check.
    const isPartsTable = /\bparts?\b|price|cost|where to buy|order/i.test(header.join(" "));
    if (codeHeaded && !isPartsTable && rows.length >= 3) {
      tables.push({ label: lastHeading, header: header.slice(0, 5), rows });
    }
    i = j - 1;
  }
  return tables;
}

// Chiller-style pages: H3 fault sections carrying **Trigger:** blocks
// (york-chiller-fault-codes / trane-chiller-fault-codes structure).
function extractFaultSections(body) {
  if ((body.match(/\*\*Trigger:\*\*/g) || []).length < 4) return [];
  const out = [];
  const chunks = body.split(/^###\s+/m).slice(1);
  for (const chunk of chunks) {
    const nl = chunk.indexOf("\n");
    const name = cleanInline(chunk.slice(0, nl)).replace(/^System Fault:\s*/i, "");
    const rest = chunk.slice(nl + 1);
    const trigger = rest.match(/\*\*Trigger:\*\*\s*(.+)/);
    if (!trigger) continue;
    const code =
      rest.match(/\*\*Fault code:\*\*\s*(.+)/i)?.[1] ??
      rest.match(/\*\*CH530 Text:\*\*\s*(.+)/i)?.[1] ?? "";
    const diag = rest.match(/\*\*Diagnosis:\*\*[^\n]*\n1\.\s*(.+)/);
    const reset = rest.match(/\*\*Reset:\*\*\s*(.+)/);
    out.push({
      name,
      code: cleanInline(code).replace(/\s*[—–-]\s*$/, ""),
      trigger: firstSentence(trigger[1], 180),
      firstCheck: diag ? firstSentence(diag[1], 160) : "",
      reset: reset ? firstSentence(reset[1], 110) : "",
    });
  }
  return out;
}

// Extract the code token from a single-code guide title. Mirrors the
// PostDetails hero-code heuristics (site-verified title grammar).
const CODE_STOPWORDS = new Set(["CODE", "CODES", "LIST", "GUIDE", "FIX", "FIXES"]);
// Model-series tokens (ACS580, GA700, KM1301…) must never be read as codes.
const looksLikeModel = tok => tok.length >= 6 || /^[A-Z]{2,3}\d{3,}$/.test(tok);
const validCode = tok =>
  !!tok && !CODE_STOPWORDS.has(tok.toUpperCase()) && !looksLikeModel(tok.toUpperCase());

function codeFromTitle(title) {
  const t = String(title);
  // "3 Flashes", "1 Flash Code" (blink-code equipment)
  let m = t.match(/\b(\d{1,2})\s+flash(?:es)?\b/i);
  if (m) return `${m[1]} FLASH`;
  // "E1 Error Code", "AL-29 Fault Code", "AI1 LOSS Fault Code"
  m = t.match(/\b([A-Za-z0-9.-]{1,8}(?:\s+[A-Z]{2,6})?)\s+(?:error|fault|flash)\s+code\b/i);
  if (m && /\d/.test(m[1]) && validCode(m[1].split(/\s/)[0])) return m[1].toUpperCase();
  // "Alarm 300", "Fault 3130", "Error Code 10", "Fault F07"
  m = t.match(/\b(?:alarm|fault|error|code)\s+#?([A-Z]{0,4}-?\d{1,5}(?:[.-]\d{1,4})?)\b/i);
  if (m && /\d/.test(m[1]) && validCode(m[1])) return m[1].toUpperCase();
  // "Fault OC", "Fault UV1", "Alarm AL 29", "Fault E.OC1", "Fault E-Trip" —
  // keyword-first letter codes, with optional . / - / space separator. MUST
  // run before the token-first pattern, or "GA700 Fault OC" reads the model
  // as the code.
  m = t.match(/\b(?:fault|alarm|error)\s+#?([A-Z]{1,4}(?:[.\s-][A-Z0-9]{1,4})?\d{0,4})\b(?!\s*codes?\b)/i);
  if (m && validCode(m[1].split(/[.\s-]/)[0])) return m[1].toUpperCase();
  // "F0001 Fault", "A2B3 Fault", "FA81 Fault", "F0001 Overcurrent"
  m = t.match(/\b([A-Z][A-Z0-9]{1,5}(?:[.-]\d{1,4})?)\s+(?:fault|alarm|error|overcurrent|overvoltage|undervoltage|overtemp)\b(?!\s*codes?\b)/i);
  if (m && /\d/.test(m[1]) && validCode(m[1])) return m[1].toUpperCase();
  // "2310 Fault"
  m = t.match(/\b(\d{3,5})\s+fault\b/i);
  if (m) return m[1];
  return null;
}

// "ABB ACS580 Fault Codes — Complete Guide" -> "ABB ACS580"
function modelFromTitle(title) {
  const t = cleanInline(title).replace(/\s*[—:|-].*$/, "");
  const m = t.match(/^(.*?)\s+(?:fault|error|alarm|flash)\b/i);
  return (m ? m[1] : t).trim();
}

/* ------------------------------------------------------------------ *
 * Collection
 * ------------------------------------------------------------------ */

function loadNoindex() {
  const src = readFileSync(path.join(REPO, "src", "data", "noindex-slugs.ts"), "utf8");
  return new Set([...src.matchAll(/"([^"]+)"/g)].map(m => m[1]));
}

function collect() {
  const noindex = loadNoindex();
  const bySection = new Map(SECTIONS.map(s => [s.id, []]));
  let latestMod = "";

  for (const file of readdirSync(BLOG_DIR).sort()) {
    if (!file.endsWith(".md")) continue;
    const parsed = parseFrontmatter(readFileSync(path.join(BLOG_DIR, file), "utf8"));
    if (!parsed) continue;
    const { fm, body } = parsed;
    if (String(fm.draft).toLowerCase() === "true") continue;
    const slug = fm.slug || file.replace(/\.md$/, "");
    if (noindex.has(slug)) continue;
    const page = {
      slug,
      tags: (Array.isArray(fm.tags) ? fm.tags : []).map(t => t.toLowerCase()),
      title: cleanInline(fm.title || slug),
      description: fm.description || "",
      cause: fm.most_likely_cause || "",
      diyOrPro: (fm.diy_or_pro || "").toLowerCase(),
      freeChecks: Array.isArray(fm.free_checks) ? fm.free_checks : [],
      mod: fm.modDatetime || fm.pubDatetime || "",
      body,
    };
    const section = SECTIONS.find(s => s.match(page));
    if (!section) continue;
    bySection.get(section.id).push(page);
    if (page.mod > latestMod) latestMod = page.mod;
  }
  return { bySection, latestMod };
}

// Dedupe key: "Hoshizaki E1" and "Hoshizaki Ice Machine E1" are the same code
// entry; filler words don't distinguish models.
function normModel(model) {
  return model.toLowerCase()
    .replace(/\b(ice machine|machine|vfd|drive|drives|servo|inverter|combi oven|generator|ups)\b/g, "")
    .replace(/\s+/g, " ").trim();
}

// Strip templated title suffixes ("— Causes & Fix", "- What It Means and How
// to Fix It", …) so entries read as reference lines, not SEO headlines.
function cleanGuideTitle(title) {
  const parts = String(title).split(/\s*(?:—|\||:)\s+|\s+-\s+/);
  let out = parts[0];
  for (const p of parts.slice(1)) {
    if (/fix|guide|diagnos|what it means|means|causes|troubleshoot|step[- ]by[- ]step|explained/i.test(p)) break;
    out += " — " + p;
  }
  return out.trim();
}

function buildSectionData(section, pages) {
  const tables = [];   // { model, label, header, rows, url }
  const faults = [];   // chiller-style { model, entries, url }
  const guides = [];   // { code, title, model, meaning, cause, checks, pro, url }
  const codeKeys = new Set();

  const isListPage = (page, pageTables) =>
    /(?:fault|error|alarm|flash)-codes?$|complete-guide$|-alarms$|common-alarms$/.test(page.slug) ||
    pageTables.reduce((n, t) => n + t.rows.length, 0) >= 8;

  for (const page of pages.sort((a, b) => a.slug.localeCompare(b.slug))) {
    // Comparison / opinion pieces are site content, not reference content.
    if (/-vs-/.test(page.slug)) continue;

    const url = `${SITE_URL}/posts/${page.slug}/`;
    const model = modelFromTitle(page.title);
    const nm = normModel(model);
    const pageTables = extractCodeTables(page.body);
    const faultSections = extractFaultSections(page.body);

    if (faultSections.length) {
      faults.push({ model, entries: faultSections, url, title: page.title });
      for (const f of faultSections) if (f.code) codeKeys.add(`${nm}::${f.code}`);
      continue;
    }

    if (pageTables.length && isListPage(page, pageTables)) {
      for (const t of pageTables) {
        tables.push({ model, label: t.label, header: t.header, rows: t.rows, url });
        for (const r of t.rows) {
          const c = (r[0] || "").trim();
          if (c && c.length <= 24) codeKeys.add(`${nm}::${c.toUpperCase()}`);
        }
      }
      continue;
    }

    // Single-code deep guide -> condensed field entry.
    const code = codeFromTitle(page.title);
    const guide = {
      code,
      title: cleanGuideTitle(page.title),
      model,
      nm,
      meaning: firstSentence(page.description, 230),
      cause: cleanInline(page.cause),
      checks: page.freeChecks.slice(0, 3).map(c => cleanInline(c)),
      pro: page.diyOrPro,
      url,
      // Occasional sub-code tables inside deep guides — carry the guide's
      // model + source URL so they render with full attribution.
      subTables: pageTables.map(t => ({ ...t, model, url })),
    };
    // Drop pure-teaser entries (no code, no cause, no checks) unless they are
    // series overview pages worth pointing at.
    const isOverview = /-codes?$|-guide$/.test(page.slug);
    if (!guide.code && !guide.cause && !guide.checks.length && !guide.subTables.length && !isOverview) continue;

    guides.push(guide);
    if (code) codeKeys.add(`${nm}::${code}`);
    for (const t of pageTables) {
      for (const r of t.rows) {
        const c = (r[0] || "").trim();
        if (c && c.length <= 24) codeKeys.add(`${nm}::${c.toUpperCase()}`);
      }
    }
  }

  // Same code documented by two pages (e.g. "...-fault-2310" and
  // "...-fault-2310-overcurrent"): keep the richer entry.
  const richness = g =>
    g.checks.length * 4 + (g.cause ? 2 : 0) + g.subTables.length * 3 + Math.min(g.meaning.length / 100, 2);
  const byKey = new Map();
  for (const g of guides) {
    const key = g.code ? `${g.nm}::${g.code}` : `uniq::${g.url}`;
    const prev = byKey.get(key);
    if (!prev || richness(g) > richness(prev)) byKey.set(key, g);
  }
  const dedupedGuides = [...byKey.values()];

  // Sort guides by model then natural code order.
  const natural = s => String(s ?? "").replace(/(\d+)/g, m => m.padStart(6, "0"));
  dedupedGuides.sort((a, b) =>
    natural(`${a.model} ${a.code ?? a.title}`).localeCompare(natural(`${b.model} ${b.code ?? b.title}`)));
  tables.sort((a, b) => natural(a.model + a.label).localeCompare(natural(b.model + b.label)));

  const models = [...new Set([...tables.map(t => t.model), ...faults.map(f => f.model), ...dedupedGuides.map(g => g.model)])];
  return {
    ...section,
    tables, faults, guides: dedupedGuides, models,
    pageCount: pages.length,
    codeCount: codeKeys.size,
  };
}

/* ------------------------------------------------------------------ *
 * HTML rendering
 * ------------------------------------------------------------------ */

const PRO_LABELS = { pro: "PRO SERVICE", diy: "DIY-OK" };

function renderTable(t) {
  const head = t.header.map((h, i) =>
    `<th class="${i === 0 ? "c-code" : ""}">${esc(h)}</th>`).join("");
  const body = t.rows.map(r =>
    `<tr>${r.map((c, i) => `<td class="${i === 0 ? "c-code" : ""}">${esc(c)}</td>`).join("")}</tr>`
  ).join("\n");
  const label = t.label && !/quick reference/i.test(t.label) ? ` — ${esc(fixAcronyms(t.label))}` : "";
  return `
<div class="tblock">
  <p class="tcap"><span class="tmodel">${esc(t.model)}</span>${label}</p>
  <table class="codes">
    <thead><tr>${head}</tr></thead>
    <tbody>
${body}
    </tbody>
  </table>
  <p class="src">Full diagnostics: ${esc(t.url)}</p>
</div>`;
}

function renderFaultTable(f) {
  const rows = f.entries.map(e => `
    <tr>
      <td class="c-code">${esc(e.code || e.name)}</td>
      <td>${e.code ? `<strong>${esc(e.name)}.</strong> ` : ""}${esc(e.trigger)}</td>
      <td>${esc(e.firstCheck || "—")}</td>
      <td>${esc(e.reset || "—")}</td>
    </tr>`).join("\n");
  return `
<div class="tblock">
  <p class="tcap"><span class="tmodel">${esc(f.model)}</span> — fault index</p>
  <table class="codes faults">
    <thead><tr><th class="c-code">Fault</th><th>Trigger</th><th>First check</th><th>Reset</th></tr></thead>
    <tbody>${rows}
    </tbody>
  </table>
  <p class="src">Full diagnostics: ${esc(f.url)}</p>
</div>`;
}

function renderGuide(g) {
  const badge = PRO_LABELS[g.pro] ? `<span class="badge ${g.pro === "pro" ? "b-pro" : "b-diy"}">${PRO_LABELS[g.pro]}</span>` : "";
  const checks = g.checks.length
    ? `<div class="gchecks"><span class="glabel">Check first</span><ol>${g.checks.map(c => `<li>${esc(c)}</li>`).join("")}</ol></div>`
    : "";
  const cause = g.cause ? `<p class="gcause"><span class="glabel">Most likely</span> ${esc(g.cause)}</p>` : "";
  const subTables = g.subTables.map(renderTable).join("\n");
  return `
<article class="entry">
  <div class="ehead">
    <span class="ecode">${esc(g.code ?? "•")}</span>
    <span class="etitle">${esc(g.title)}</span>
    ${badge}
  </div>
  ${g.meaning ? `<p class="emean">${esc(g.meaning)}</p>` : ""}
  ${cause}
  ${checks}
  <p class="src">Full guide: ${esc(g.url)}</p>
  ${subTables}
</article>`;
}

function renderSection(s, num) {
  const parts = [];
  parts.push(`
<section class="brand" id="s-${s.id}">
  <div class="band"><span class="bnum">${String(num).padStart(2, "0")}</span><span class="bname">${esc(s.title)}</span><span class="bgroup">${esc(s.group)}</span></div>
  <p class="bmeta">${s.codeCount} code entries · ${s.pageCount} source guides · Series: ${esc(s.models.slice(0, 8).join(" · "))}${s.models.length > 8 ? " · …" : ""}</p>`);
  for (const t of s.tables) parts.push(renderTable(t));
  for (const f of s.faults) parts.push(renderFaultTable(f));
  if (s.guides.length) {
    parts.push(`<h3 class="gsubhead">Field diagnostics — code by code</h3>`);
    for (const g of s.guides) parts.push(renderGuide(g));
  }
  parts.push(`</section>`);
  return parts.join("\n");
}

function renderDocument({ edition, sections, updatedLabel, totalCodes, totalGuides, fullStats }) {
  const isSample = edition === "SAMPLE";
  const groups = [...new Set(sections.map(s => s.group))];

  const toc = groups.map(g => {
    const rows = sections.filter(s => s.group === g).map((s, i) => `
      <tr>
        <td class="c-code"><a href="#s-${s.id}">${String(sections.indexOf(s) + 1).padStart(2, "0")}</a></td>
        <td><a href="#s-${s.id}">${esc(s.title)}</a></td>
        <td class="tnum">${s.codeCount}</td>
      </tr>`).join("");
    return `<p class="tocgroup">${esc(g)}</p>
      <table class="toc"><thead><tr><th class="c-code">§</th><th>Brand section</th><th class="tnum">Codes</th></tr></thead><tbody>${rows}</tbody></table>`;
  }).join("\n");

  const sampleStrip = isSample ? `
  <div class="sample-strip">SAMPLE EDITION — ${sections.map(s => esc(s.brand)).join(" + ")} sections only. The full edition covers ${fullStats.brands} brands and ${fullStats.codes} code entries: ${SITE_URL}/field-reference/</div>` : "";

  const upsell = isSample ? `
<section class="brand upsell">
  <div class="band"><span class="bnum">→</span><span class="bname">Get the full Field Reference</span><span class="bgroup">${fullStats.brands} brands</span></div>
  <p class="upsell-copy">This sample covers ${sections.map(s => esc(s.brand)).join(" and ")}. The full edition adds every industrial brand section on errorcodefixes.com — ${fullStats.brandList} — ${fullStats.codes} code entries compiled the same way, one file, works offline.</p>
  <p class="upsell-cta">${SITE_URL}/field-reference/</p>
</section>` : "";

  const body = sections.map((s, i) => renderSection(s, i + 1)).join("\n");

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Industrial Fault-Code Field Reference${isSample ? " — Free Sample" : ""} | errorcodefixes.com</title>
<style>
  :root {
    --navy: #15233F; --paper: #FFFFFF; --offpaper: #FAFAF8; --ink: #10182A;
    --rule: #D8D6CE; --accent: #C2410C; --dim: #5A6472; --safe: #0E7C5A; --danger: #B91C1C;
    --mono: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
    --sans: -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  html { background: #E8E6E0; }
  body { font-family: var(--sans); color: var(--ink); font-size: 10.5px; line-height: 1.42; }
  .sheet { max-width: 8.5in; margin: 0 auto; background: var(--paper); }
  a { color: inherit; }

  /* Running header: table thead repeats on every printed page. */
  .pagetable { width: 100%; border-collapse: collapse; }
  .pagetable > thead .runhead {
    display: flex; justify-content: space-between; align-items: baseline;
    padding: 6px 28px; background: var(--navy); color: #E8ECF4;
    font-size: 7.5px; letter-spacing: 0.14em; text-transform: uppercase; font-weight: 600;
  }
  .runhead .rh-site { color: #F0B27E; }
  .pagetable > tbody > tr > td { padding: 0; }
  .inner { padding: 0 28px 28px; }

  /* Cover */
  .cover { padding: 64px 0 40px; }
  .cover-rule { height: 6px; background: var(--accent); width: 88px; margin-bottom: 26px; }
  .cover h1 { font-size: 34px; line-height: 1.08; letter-spacing: -0.01em; color: var(--navy); text-transform: uppercase; }
  .cover .ed { display: inline-block; margin-top: 14px; padding: 4px 10px; border: 2px solid var(--navy);
    font-family: var(--mono); font-size: 11px; font-weight: 700; letter-spacing: 0.12em; }
  .cover .ed.sample { border-color: var(--accent); color: var(--accent); }
  .cover-sub { margin-top: 18px; font-size: 13px; max-width: 5.6in; color: var(--ink); }
  .cover-stats { display: flex; gap: 0; margin-top: 30px; border: 1px solid var(--rule); }
  .cover-stats div { flex: 1; padding: 10px 14px; border-right: 1px solid var(--rule); }
  .cover-stats div:last-child { border-right: 0; }
  .cover-stats .n { font-family: var(--mono); font-size: 20px; font-weight: 700; color: var(--navy); display: block; }
  .cover-stats .l { font-size: 8px; text-transform: uppercase; letter-spacing: 0.12em; color: var(--dim); }
  .cover-note { margin-top: 26px; font-size: 9.5px; color: var(--dim); max-width: 5.8in; }
  .cover-note p + p { margin-top: 6px; }
  .cover-note strong { color: var(--ink); }

  .sample-strip { margin: 0 0 4px; padding: 7px 28px; background: var(--accent); color: #fff;
    font-size: 8.5px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; }

  /* TOC */
  .tocwrap { padding-top: 26px; }
  .tocwrap h2, .gsubhead { font-size: 12px; text-transform: uppercase; letter-spacing: 0.14em; color: var(--navy);
    border-bottom: 2px solid var(--navy); padding-bottom: 4px; margin-bottom: 12px; }
  .tocgroup { font-size: 8.5px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em;
    color: var(--accent); margin: 12px 0 4px; }
  table.toc { width: 100%; border-collapse: collapse; }
  table.toc th, table.toc td { text-align: left; padding: 3px 8px; border-bottom: 1px solid var(--rule); font-size: 10px; }
  table.toc th { font-size: 7.5px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--dim); }
  table.toc a { text-decoration: none; }
  .tnum { text-align: right; font-family: var(--mono); }

  /* Brand sections */
  .brand { padding-top: 18px; }
  .band { display: flex; align-items: baseline; gap: 10px; background: var(--navy); color: #fff;
    padding: 7px 12px; }
  .bnum { font-family: var(--mono); font-size: 13px; font-weight: 700; color: #F0B27E; }
  .bname { font-size: 13.5px; font-weight: 700; letter-spacing: 0.02em; text-transform: uppercase; }
  .bgroup { margin-left: auto; font-size: 8px; letter-spacing: 0.12em; text-transform: uppercase; color: #AAB6CC; }
  .bmeta { font-size: 9px; color: var(--dim); padding: 5px 2px 2px; font-family: var(--mono); }

  .tblock { margin-top: 12px; break-inside: auto; }
  .tcap { font-size: 10px; font-weight: 700; color: var(--navy); margin-bottom: 3px; }
  .tcap .tmodel { font-family: var(--mono); background: var(--offpaper); border: 1px solid var(--rule); padding: 1px 5px; }
  table.codes { width: 100%; border-collapse: collapse; border: 1px solid var(--rule); }
  table.codes th { background: var(--offpaper); text-align: left; font-size: 7.5px; text-transform: uppercase;
    letter-spacing: 0.1em; color: var(--dim); padding: 3px 7px; border-bottom: 1.5px solid var(--navy); }
  table.codes td { padding: 3px 7px; border-bottom: 1px solid var(--rule); vertical-align: top; font-size: 9.5px; }
  table.codes tbody tr:nth-child(even) td { background: #FBFAF7; }
  td.c-code, th.c-code { font-family: var(--mono); font-weight: 700; white-space: nowrap; width: 1%; color: var(--navy); }
  table.faults td.c-code { white-space: normal; min-width: 0.9in; }
  .src { font-size: 8px; color: var(--dim); font-family: var(--mono); margin: 3px 0 0; }

  /* Guide entries */
  .gsubhead { margin-top: 18px; }
  .entry { border: 1px solid var(--rule); border-left: 3px solid var(--navy); padding: 7px 10px 8px; margin-top: 8px;
    break-inside: avoid; }
  .ehead { display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap; }
  .ecode { font-family: var(--mono); font-weight: 700; font-size: 12px; color: #fff; background: var(--navy); padding: 1px 7px; }
  .etitle { font-weight: 700; font-size: 10.5px; }
  .badge { font-size: 7px; font-weight: 700; letter-spacing: 0.1em; padding: 2px 6px; border: 1px solid; margin-left: auto; }
  .b-pro { color: var(--danger); border-color: var(--danger); }
  .b-diy { color: var(--safe); border-color: var(--safe); }
  .emean { margin-top: 4px; }
  .gcause { margin-top: 3px; }
  .glabel { font-size: 7px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); margin-right: 5px; }
  .gchecks { margin-top: 3px; display: flex; gap: 5px; align-items: baseline; }
  .gchecks ol { margin: 0 0 0 14px; }
  .gchecks li { margin: 0; }

  /* Upsell (sample only) */
  .upsell-copy { margin-top: 10px; font-size: 11px; max-width: 6in; }
  .upsell-cta { margin-top: 8px; font-family: var(--mono); font-weight: 700; font-size: 12px; color: var(--accent); }

  /* End matter */
  .endnote { margin-top: 26px; border-top: 2px solid var(--navy); padding-top: 8px; font-size: 8.5px; color: var(--dim); }
  .endnote p + p { margin-top: 4px; }

  @media screen { .sheet { box-shadow: 0 2px 24px rgba(16,24,42,0.18); margin: 24px auto; } }
  @page { size: letter; margin: 0.42in 0.42in 0.5in; }
  @media print {
    html { background: #fff; }
    body { font-size: 9.5px; }
    .sheet { max-width: none; box-shadow: none; margin: 0; }
    .cover, .tocwrap { break-after: page; }
    .brand { break-before: page; padding-top: 0; margin-top: 10px; }
    .brand.upsell { break-before: auto; }
    .entry { break-inside: avoid; }
    tr { break-inside: avoid; }
    .pagetable > thead { display: table-header-group; }
    a { text-decoration: none; }
  }
</style>
</head>
<body>
<div class="sheet">
<table class="pagetable">
<thead><tr><td>
  <div class="runhead">
    <span>Industrial Fault-Code Field Reference — ${edition} EDITION</span>
    <span class="rh-site">errorcodefixes.com</span>
  </div>
</td></tr></thead>
<tbody><tr><td>
${sampleStrip}
<div class="inner">

<section class="cover">
  <div class="cover-rule"></div>
  <h1>Industrial<br>Fault-Code<br>Field Reference</h1>
  <span class="ed${isSample ? " sample" : ""}">${edition} EDITION</span>
  <p class="cover-sub">The offline fault-code reference for industrial and facilities technicians:
  ${sections.length} brand section${sections.length === 1 ? "" : "s"} of code tables, meanings, first checks,
  and when-to-call-a-pro flags — compiled from the published, source-checked diagnostic guides at errorcodefixes.com.</p>
  <div class="cover-stats">
    <div><span class="n">${sections.length}</span><span class="l">Brand sections</span></div>
    <div><span class="n">${totalCodes}</span><span class="l">Code entries</span></div>
    <div><span class="n">${totalGuides}</span><span class="l">Source guides</span></div>
    <div><span class="n">${esc(updatedLabel)}</span><span class="l">Content updated</span></div>
  </div>
  <div class="cover-note">
    <p><strong>How to use it:</strong> keep this file on your phone or print it into the shop binder.
    Each brand section opens with its code tables, then condensed per-code field notes. Every table and
    entry cites the full step-by-step guide on errorcodefixes.com for when you are back on the network.</p>
    <p><strong>Independence:</strong> errorcodefixes.com is an independent reference. It is not affiliated
    with or endorsed by any equipment manufacturer named in this document, and it does not sell parts or
    repair services. Brand names are used for identification only.</p>
    <p><strong>Safety:</strong> industrial equipment can injure or kill. Follow your site's lockout/tagout
    procedure and the manufacturer's service documentation. Entries flagged PRO SERVICE involve work that
    should be left to qualified technicians.</p>
  </div>
</section>

<section class="tocwrap">
  <h2>Contents</h2>
  ${toc}
</section>

${body}
${upsell}

<div class="endnote">
  <p>Industrial Fault-Code Field Reference — ${edition} edition. Compiled from ${totalGuides} published
  diagnostic guides at errorcodefixes.com. Content updated ${esc(updatedLabel)}.</p>
  <p>© errorcodefixes.com. Independent reference — not affiliated with any equipment manufacturer.
  Codes, thresholds, and procedures vary by model, firmware, and installation: always confirm against the
  unit's own service documentation before acting.</p>
</div>

</div>
</td></tr></tbody>
</table>
</div>
</body>
</html>
`;
}

/* ------------------------------------------------------------------ *
 * PDF (headless Chrome — the HTML is the PDF master)
 * ------------------------------------------------------------------ */

function findChrome() {
  const candidates = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium-browser",
  ];
  return candidates.find(existsSync) ?? null;
}

function htmlToPdf(chrome, htmlPath, pdfPath) {
  const res = spawnSync(chrome, [
    "--headless",
    "--no-sandbox", // headless Chrome crashes under most CI sandbox profiles without this
    "--disable-gpu",
    "--no-first-run",
    "--no-default-browser-check",
    "--hide-scrollbars",
    "--no-pdf-header-footer",
    "--virtual-time-budget=10000",
    `--print-to-pdf=${pdfPath}`,
    `file://${htmlPath}`,
  ], { timeout: 120000, encoding: "utf8" });
  return res.status === 0 && existsSync(pdfPath);
}

/* ------------------------------------------------------------------ *
 * Main
 * ------------------------------------------------------------------ */

function main() {
  const { bySection, latestMod } = collect();
  const updatedLabel = latestMod
    ? new Date(latestMod).toLocaleDateString("en-US", { month: "short", year: "numeric", timeZone: "UTC" })
    : "—";

  const built = SECTIONS
    .map(s => buildSectionData(s, bySection.get(s.id)))
    .filter(s => s.pageCount > 0);

  const sum = (arr, f) => arr.reduce((n, x) => n + f(x), 0);
  const fullCodes = sum(built, s => s.codeCount);
  const fullGuides = sum(built, s => s.pageCount);
  const sampleSections = built.filter(s => SAMPLE_SECTION_IDS.includes(s.id));
  const sampleCodes = sum(sampleSections, s => s.codeCount);

  console.log("Industrial Fault-Code Field Reference — build");
  console.log("-".repeat(60));
  for (const s of built) {
    console.log(
      `${s.brand.padEnd(14)} pages=${String(s.pageCount).padStart(3)} ` +
      `codes=${String(s.codeCount).padStart(4)} tables=${String(s.tables.length).padStart(2)} ` +
      `faultIdx=${s.faults.length} guides=${String(s.guides.length).padStart(3)}`
    );
  }
  console.log("-".repeat(60));
  console.log(`FULL:   ${built.length} brands, ${fullCodes} code entries, ${fullGuides} source guides`);
  console.log(`SAMPLE: ${sampleSections.map(s => s.brand).join(" + ")}, ${sampleCodes} code entries`);
  console.log(`Content updated: ${updatedLabel}`);

  // Stats JSON — consumed by the landing page + promo card. Counts only; no
  // paid content, safe for the public repo.
  const stats = {
    updated: updatedLabel,
    full: { brands: built.length, codes: fullCodes, guides: fullGuides },
    sample: {
      brands: sampleSections.map(s => s.brand),
      codes: sampleCodes,
      html: "/resources/field-reference-sample.html",
      pdf: "/resources/field-reference-sample.pdf",
    },
    groups: [...new Set(built.map(s => s.group))].map(g => ({
      group: g,
      sections: built.filter(s => s.group === g).map(s => ({
        brand: s.brand, title: s.title, codes: s.codeCount, guides: s.pageCount,
        models: s.models.slice(0, 6),
      })),
    })),
  };

  // Write stats BEFORE the --stats-only early return, otherwise the flag that
  // exists to refresh stats is the one path that never writes them.
  writeFileSync(path.join(REPO, "src", "data", "field-reference-stats.json"), JSON.stringify(stats, null, 2) + "\n");
  if (STATS_ONLY) return;

  const fullStatsForUpsell = {
    brands: built.length,
    codes: fullCodes,
    brandList: built.map(s => s.brand).join(", "),
  };

  const fullHtml = renderDocument({
    edition: "FULL", sections: built, updatedLabel,
    totalCodes: fullCodes, totalGuides: fullGuides, fullStats: fullStatsForUpsell,
  });
  const sampleHtml = renderDocument({
    edition: "SAMPLE", sections: sampleSections, updatedLabel,
    totalCodes: sampleCodes, totalGuides: sum(sampleSections, s => s.pageCount),
    fullStats: fullStatsForUpsell,
  });

  const productDir = path.join(REPO, "product");
  const resourcesDir = path.join(REPO, "public", "resources");
  mkdirSync(productDir, { recursive: true });
  mkdirSync(resourcesDir, { recursive: true });

  const fullHtmlPath = path.join(productDir, "field-reference-full.html");
  const sampleHtmlPath = path.join(resourcesDir, "field-reference-sample.html");
  writeFileSync(fullHtmlPath, fullHtml);
  writeFileSync(sampleHtmlPath, sampleHtml);
  console.log(`\nWrote ${path.relative(REPO, fullHtmlPath)} (${(fullHtml.length / 1024).toFixed(0)} KB)`);
  console.log(`Wrote ${path.relative(REPO, sampleHtmlPath)} (${(sampleHtml.length / 1024).toFixed(0)} KB)`);
  console.log(`Wrote src/data/field-reference-stats.json`);

  if (NO_PDF) return;
  const chrome = findChrome();
  if (!chrome) {
    console.log("PDF: no local Chrome/Chromium found — HTML-only build (the HTML is print-ready; PDF can be produced later via File > Print).");
    return;
  }
  const fullPdf = path.join(productDir, "field-reference-full.pdf");
  const samplePdf = path.join(resourcesDir, "field-reference-sample.pdf");
  for (const [src, dst] of [[sampleHtmlPath, samplePdf], [fullHtmlPath, fullPdf]]) {
    const ok = htmlToPdf(chrome, src, dst);
    console.log(ok
      ? `PDF: wrote ${path.relative(REPO, dst)}`
      : `PDF: FAILED for ${path.relative(REPO, dst)} — HTML remains the master.`);
  }
}

// This runs from `prebuild`, i.e. on every push-to-main production deploy with
// no human gate. A throw here aborts `npm run build` before astro ever starts,
// so a missing input file would take the whole site's deploy down to ship a
// side artifact. Never let that trade happen: log loudly, exit 0, deploy the
// site. A stale Field Reference is a bad day; a failed deploy is a bad week.
try {
  main();
} catch (err) {
  console.error("\n" + "!".repeat(70));
  console.error("FIELD REFERENCE BUILD FAILED — continuing so the site still deploys.");
  console.error("The product artifacts and stats JSON may be stale. Fix this:");
  console.error(err?.stack || err);
  console.error("!".repeat(70) + "\n");
}
