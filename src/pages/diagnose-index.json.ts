import type { APIRoute } from "astro";
import { getCollection } from "astro:content";
import getListablePosts from "@/utils/getListablePosts";

export const prerender = true;

// Compact client-side index for the /diagnose tool: every live quality-core
// CODE page — industrial (fault/alarm codes) AND consumer (error codes) — as
// { a:equipment, b:brand, c:code, t:title, s:slug, m:most-likely-cause,
//   d:diy|pro }. Prerendered to a static JSON file at build.
//
// Industrial-first (2026-07 strategy, see CLAUDE.md): the site's real human
// traffic is industrial techs, so the index now includes -fault-code(s),
// -alarm-code(s), -alarm-N and code-token slugs, not just consumer
// "-error-code" pages. Listability (draft + NOINDEX_SLUGS) is enforced via
// getListablePosts — the same gate every other listing surface uses.
//
// Equipment tokens (a) — the /diagnose picker groups these into families:
//   industrial: cnc | vfd | chvac | ice | kitchen | power
//   consumer:   washer dryer refrigerator dishwasher range oven cooktop
//               freezer microwave

const CONSUMER_APPLIANCES = [
  "washer", "dryer", "refrigerator", "dishwasher", "range",
  "oven", "microwave", "cooktop", "freezer",
];

// Brand vocabulary, matched against frontmatter tags first, then a
// delimiter-bounded slug match (verified against src/data/blog tag usage
// 2026-07-27: every industrial brand below exists as a tag on listable posts;
// "mitsubishi" is the tag in use, not "mitsubishi-electric"). Industrial
// brands are listed first and multi-word brands before their fragments so
// e.g. "fanuc-alarm-300-apc-battery" resolves to fanuc, not apc.
const INDUSTRIAL_BRANDS = [
  "allen-bradley", "sew-eurodrive", "ice-o-matic", "weil-mclain",
  "fanuc", "haas", "mazak", "okuma", "heidenhain",
  "siemens", "abb", "yaskawa", "danfoss", "schneider", "mitsubishi",
  "york", "trane", "carrier", "daikin",
  "hoshizaki", "manitowoc", "scotsman",
  "rational", "hobart", "meiko",
  "apc", "generac",
];
const CONSUMER_BRANDS = [
  "samsung", "lg", "whirlpool", "ge", "maytag", "frigidaire",
  "bosch", "kitchenaid", "kenmore", "electrolux", "amana",
];
const ALL_BRANDS = [...INDUSTRIAL_BRANDS, ...CONSUMER_BRANDS];

const CNC_BRANDS = new Set(["fanuc", "haas", "mazak", "okuma", "heidenhain"]);
const VFD_BRANDS = new Set(["abb", "yaskawa", "danfoss", "allen-bradley", "schneider", "sew-eurodrive"]);
const HVAC_BRANDS = new Set(["york", "trane", "carrier", "daikin", "mitsubishi", "weil-mclain"]);
const ICE_BRANDS = new Set(["hoshizaki", "manitowoc", "scotsman", "ice-o-matic"]);
const KITCHEN_BRANDS = new Set(["rational", "hobart", "meiko"]);
const POWER_BRANDS = new Set(["apc", "generac"]);

// A "code page" is anything whose slug marks it as a fault/alarm/error-code
// reference: consumer -error-code, list pages -error-codes / -fault-codes /
// -alarm-codes, and industrial single-code slugs like -alarm-300, -fault-f07,
// -a0-fault-code, -error-1-1.
const isCodePage = (slug: string) =>
  /-error-codes?(-|$)/.test(slug) || // "…-error-code", "…-error-code-13"
  /(^|-)(fault|alarm)s?(-|$)/.test(slug) ||
  /-error-\d/.test(slug);

// Best-effort single-code token for the result chip. List pages (…-codes)
// intentionally get none. A candidate only counts if it looks like a code
// (has a digit, or is a short all-caps mnemonic like OC / OBF / FA81) and is
// not an equipment word ("VFD Fault" must not yield "VFD").
const NOT_CODES = new Set([
  "vfd", "cnc", "ups", "plc", "hvac", "drive", "servo",
  "code", "codes", "fault", "alarm", "error",
  // model/equipment words that precede "… Error Code N" in titles
  "rtu", "nxt", "ac", "loss",
]);
const looksLikeCode = (t: string) =>
  !NOT_CODES.has(t.toLowerCase()) &&
  (/\d/.test(t) || (t.length <= 5 && t === t.toUpperCase()));

const extractCode = (title: string, slug: string): string => {
  if (/-codes$/.test(slug)) return "";
  const patterns = [
    /\b([A-Za-z0-9-]{1,8})\s+(?:error|fault|alarm)\s+code/i, // "5E Error Code"
    /(?:error|fault|alarm)\s+code[:\s]+([A-Za-z0-9.-]{1,8})/i, // "Error Code 5E"
    /\balarm\s+(\d[A-Za-z0-9.-]{0,7})\b/i, // "Alarm 300"
    /\berror[:\s]+(\d[A-Za-z0-9-]{0,7})\b/i, // "Error 1-1"
    /\b([A-Za-z0-9][A-Za-z0-9-]{0,7})\s+[-—–]\s/, // "F122 - Causes & Fix"
    /\bfault[:\s-]+([A-Za-z0-9]{1,8})\b/i, // "Fault OC"
    /\b([A-Za-z0-9-]{1,8})\s+fault\b/i, // "F30001 Fault", "PF Fault"
    /\bcode[:\s]+([A-Za-z0-9-]{1,8})\b/i, // "Weil-McLain Code 1"
  ];
  for (const re of patterns) {
    const m = title.match(re);
    if (m && looksLikeCode(m[1])) return m[1];
  }
  // Slug fallback: "…-fault-f07", "…-error-code-13", "…-f122-fault-code"
  const sm =
    slug.match(/-(?:error|fault|alarm)-codes?-([a-z0-9-]{1,8})$/) ||
    slug.match(/-(?:fault|alarm|error)-([a-z]{0,2}\d[a-z0-9-]{0,6})/) ||
    slug.match(/-([a-z]{1,3}\d[a-z0-9]{0,5}|[a-z]{1,3})-(?:fault|alarm|error)-code$/);
  return sm && looksLikeCode(sm[1].toUpperCase()) ? sm[1].toUpperCase() : "";
};

export const GET: APIRoute = async () => {
  const posts = getListablePosts(await getCollection("blog"));
  const items: Array<Record<string, string>> = [];
  for (const p of posts) {
    const slug = p.id.replace(/\.md$/, "");
    if (!/^[a-z0-9-]+$/.test(slug)) continue; // clean slugs only (safe in hrefs)
    if (!isCodePage(slug)) continue;
    const tags = (p.data.tags || []).map(t => t.toLowerCase());
    // Exact tag match first; fall back to a delimiter-bounded slug match so
    // "dishwasher" is never read as "washer" and "generac" never as "ge".
    const slugHas = (w: string) =>
      new RegExp(`(^|-)${w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}(-|$)`).test(slug);
    const has = (...names: string[]) => names.some(n => tags.includes(n));
    const brand = ALL_BRANDS.find(b => tags.includes(b)) || ALL_BRANDS.find(b => slugHas(b));
    if (!brand) continue;

    // Equipment classification, industrial signals first (a Hobart commercial
    // dishwasher must land in "kitchen", not consumer "dishwasher"). Fire
    // alarm panels and elevators are out of scope for the tool's families —
    // without this gate the brand-only fallbacks would misfile them (e.g.
    // mitsubishi-elevator-fault-codes under commercial HVAC).
    let equipment = "";
    if (has("fire-alarm", "elevator", "lift")) continue;
    if (has("cnc", "machining") || slugHas("cnc") || slugHas("sinumerik") || CNC_BRANDS.has(brand)) {
      equipment = "cnc";
    } else if (ICE_BRANDS.has(brand)) {
      // Ice-machine brands are unambiguous — checked before kitchen tags so a
      // Manitowoc ice machine tagged commercial-kitchen still lands in "ice".
      equipment = "ice";
    } else if (has("commercial-kitchen", "foodservice") || slugHas("combi-oven") || KITCHEN_BRANDS.has(brand)) {
      equipment = "kitchen";
    } else if (has("ice-machine", "commercial-refrigeration", "refrigeration")) {
      // "refrigeration" (not "refrigerator") is the commercial HVAC-R tag —
      // it routes reefer/refrigeration-controls posts from multi-product
      // brands (Carrier Transicold, Danfoss AKC/RX) here instead of the
      // HVAC/VFD brand-defaults below.
      equipment = "ice";
    } else if (has("ups", "generator") || POWER_BRANDS.has(brand)) {
      equipment = "power";
    } else if (
      has("vfd", "drives", "servo", "motor-control", "powerflex") ||
      slugHas("vfd") || slugHas("powerflex") || slugHas("sinamics") || slugHas("altivar") ||
      VFD_BRANDS.has(brand)
    ) {
      equipment = "vfd";
    } else if (HVAC_BRANDS.has(brand)) {
      equipment = "chvac";
    } else {
      // Consumer appliance path (unchanged logic from the consumer-only index).
      const appliance =
        CONSUMER_APPLIANCES.find(a => tags.includes(a)) ||
        CONSUMER_APPLIANCES.find(a => slugHas(a));
      if (!appliance || !CONSUMER_BRANDS.includes(brand)) continue;
      equipment = appliance;
    }

    items.push({
      a: equipment,
      b: brand,
      c: extractCode(p.data.title, slug),
      // Strip subtitle after a SPACED dash only, so hyphenated brands
      // ("SEW-Eurodrive", "Allen-Bradley") survive intact.
      t: p.data.title.replace(/\s[-—–]\s.*$/, "").trim(),
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
