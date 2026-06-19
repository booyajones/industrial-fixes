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

export const MERCHANTS: Record<string, Merchant> = {
  repairclinic: { name: "RepairClinic", url: q => `https://www.repairclinic.com/Shop-For-Parts?query=${encodeURIComponent(q)}` },
  partselect: { name: "PartSelect", url: q => `https://www.partselect.com/Search.aspx?SearchTerm=${encodeURIComponent(q)}` },
  partstown: { name: "Parts Town", url: q => `https://www.partstown.com/search?q=${encodeURIComponent(q)}` },
  supplyhouse: { name: "SupplyHouse", url: q => `https://www.supplyhouse.com/sh/control/search/_/Ntt=${encodeURIComponent(q)}` },
  grainger: { name: "Grainger", url: q => `https://www.grainger.com/search?searchQuery=${encodeURIComponent(q)}` },
};

interface Rule { match: string[]; merchant: Merchant; }

// First matching tag wins (preserves tag order). Order matters: specific before broad.
const RULES: Rule[] = [
  { match: ["washer", "dryer", "dishwasher", "refrigerator", "oven", "range", "cooktop", "microwave", "freezer", "appliance"], merchant: MERCHANTS.repairclinic },
  { match: ["commercial-refrigeration", "ice-machine", "ice-maker"], merchant: MERCHANTS.partstown },
  { match: ["boiler", "water-heater", "tankless", "plumbing"], merchant: MERCHANTS.supplyhouse },
  { match: ["vfd", "cnc", "plc", "industrial-controls", "compressor", "drive", "inverter", "servo", "robot", "ups", "generator", "industrial"], merchant: MERCHANTS.grainger },
  { match: ["hvac", "furnace", "heat-pump", "mini-split", "refrigeration", "ac", "thermostat", "chiller"], merchant: MERCHANTS.supplyhouse },
];

// Pick the merchant that stocks parts for this equipment class. Defaults to
// RepairClinic (broad consumer coverage) only when nothing else matches.
export function pickMerchant(tags: readonly string[] = []): Merchant {
  const lower = tags.map(t => t.toLowerCase());
  for (const tag of lower) {
    const rule = RULES.find(r => r.match.includes(tag));
    if (rule) return rule.merchant;
  }
  return MERCHANTS.repairclinic;
}

export function merchantUrl(tags: readonly string[], query: string): string {
  return pickMerchant(tags).url(query);
}
