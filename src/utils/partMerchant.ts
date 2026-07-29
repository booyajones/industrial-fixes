// Shared part-merchant routing: send the buyer to a merchant that actually
// STOCKS the part for their equipment class. Industrial pages (VFD/CNC/PLC/
// drives) routed to RepairClinic — a residential appliance-parts shop — was a
// dead link for the site's real (industrial) buyers. PartsSpecialist already had
// this logic; PartCallout + StickyPartsBar (the dominant CTAs, and the source the
// chatbot extracts) hardcoded RepairClinic. This is the single source of truth.

export interface Merchant {
  name: string;
  url: (q: string) => string;
}

// eBay Partner Network campaign ID. Empty = plain eBay links, which Skimlinks
// (already installed sitewide, and eBay is in its network) monetizes at the
// network cut. Once an EPN account exists, set the campid here and links
// switch to direct EPN tracking (higher cut). ALSO add class="noskim" to eBay
// links at that point so Skimlinks doesn't double-wrap them.
export const EBAY_CAMPAIGN_ID = "";

function ebayUrl(q: string): string {
  const base = `https://www.ebay.com/sch/i.html?_nkw=${encodeURIComponent(q)}`;
  if (!EBAY_CAMPAIGN_ID) return base;
  return `${base}&mkcid=1&mkrid=711-53200-19255-0&siteid=0&campid=${EBAY_CAMPAIGN_ID}&toolid=10001&mkevt=1`;
}

export const MERCHANTS: Record<string, Merchant> = {
  repairclinic: { name: "RepairClinic", url: q => `https://www.repairclinic.com/Shop-For-Parts?query=${encodeURIComponent(q)}` },
  partselect: { name: "PartSelect", url: q => `https://www.partselect.com/Search.aspx?SearchTerm=${encodeURIComponent(q)}` },
  partstown: { name: "Parts Town", url: q => `https://www.partstown.com/search?q=${encodeURIComponent(q)}` },
  supplyhouse: { name: "SupplyHouse", url: q => `https://www.supplyhouse.com/sh/control/search/_/Ntt=${encodeURIComponent(q)}` },
  grainger: { name: "Grainger", url: q => `https://www.grainger.com/search?searchQuery=${encodeURIComponent(q)}` },
  ebay: { name: "eBay (new & refurb)", url: ebayUrl },
};

interface Rule { match: string[]; merchant: Merchant; }

// First matching tag wins (preserves tag order). Order matters: specific before broad.
// Commissions verified 2026-06-17 (see .planning/affiliate-research-raw): Grainger
// 5% / RS 5% / Zoro 4% / SupplyHouse ~2% — all payable via Skimlinks today (CJ/Awin),
// zero signup. RepairClinic via Skimlinks for residential. Parts Town / Galco /
// AutomationDirect / Mouser / DigiKey have NO affiliate program ($0) — never route
// buy-intent there. So commercial-refrigeration -> Grainger (5%), not Parts Town ($0).
const RULES: Rule[] = [
  { match: ["washer", "dryer", "dishwasher", "refrigerator", "oven", "range", "cooktop", "microwave", "freezer", "appliance"], merchant: MERCHANTS.repairclinic },
  { match: ["commercial-refrigeration", "ice-machine", "ice-maker"], merchant: MERCHANTS.grainger },
  { match: ["boiler", "water-heater", "tankless", "plumbing"], merchant: MERCHANTS.supplyhouse },
  // Board-level industrial electronics are handled by BOARD_LEVEL below, which
  // takes precedence over this table. Grainger keeps the industrial
  // consumables (contactors, fuses, batteries, compressors).
  { match: ["compressor", "ups", "generator", "industrial"], merchant: MERCHANTS.grainger },
  // "inverter" lives HERE, not in BOARD_LEVEL: on this site it means an
  // inverter-driven mini-split far more often than an industrial inverter
  // drive (the only live post carrying it is mitsubishi-u7-error-code). Every
  // genuine board-level page also carries vfd/drive/cnc/plc/servo, so it is
  // never load-bearing for eBay routing.
  { match: ["hvac", "furnace", "heat-pump", "mini-split", "refrigeration", "ac", "thermostat", "chiller", "inverter"], merchant: MERCHANTS.supplyhouse },
];

// Pick the merchant that stocks parts for this equipment class. Defaults to
// RepairClinic (broad consumer coverage) only when nothing else matches.
// Board-level electronics (drive/servo/CNC/PLC boards) are not stocked by ANY
// of the general suppliers below, so this tag class wins regardless of tag
// order. Without this, a page tagged ["industrial", "servo"] matches the
// generic "industrial" tag first and sends a dead servo-amp buyer to a
// Grainger keyword search. Verified 2026-07-28: affects plc-fault-codes-guide
// and servo-motor-fault-codes; every other page routes identically.
const BOARD_LEVEL = new Set([
  "vfd", "cnc", "plc", "industrial-controls", "drive", "servo", "robot",
]);

// BOARD_LEVEL is checked BEFORE the ordered RULES loop, so any tag appearing in
// both makes its RULES entry silently unreachable. That is exactly how
// "inverter" once hijacked mini-split pages to eBay. Fail loudly in dev instead
// of shipping a silent misroute; tree-shaken out of the production build.
if (import.meta.env?.DEV) {
  const overlap = RULES.flatMap(r => r.match).filter(t => BOARD_LEVEL.has(t));
  if (overlap.length) {
    throw new Error(
      `partMerchant: tag(s) [${overlap.join(", ")}] are in BOARD_LEVEL and in RULES. ` +
      `BOARD_LEVEL wins unconditionally, so those RULES entries are dead. Pick one.`
    );
  }
}

export function pickMerchant(tags: readonly string[] = []): Merchant {
  const lower = tags.map(t => t.toLowerCase());
  if (lower.some(t => BOARD_LEVEL.has(t))) return MERCHANTS.ebay;
  for (const tag of lower) {
    const rule = RULES.find(r => r.match.includes(tag));
    if (rule) return rule.merchant;
  }
  return MERCHANTS.repairclinic;
}

export function merchantUrl(tags: readonly string[], query: string): string {
  return pickMerchant(tags).url(query);
}
