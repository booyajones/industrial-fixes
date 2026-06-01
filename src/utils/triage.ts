/**
 * At-a-glance triage inference.
 *
 * Maps a post's tags to a conservative, SAFETY-FIRST difficulty / time / tools
 * estimate so a DIYer can triage a repair before reading the full guide.
 *
 * These values render as guidance to real technicians working on gas,
 * electrical, and refrigerant equipment. When the signal is ambiguous we lean
 * toward the more cautious bucket (Pro recommended), never away from it.
 *
 * Precedence is strict: Pro > Advanced > Intermediate (DIY) > Intermediate.
 * The first bucket whose tag set overlaps the post wins, so a furnace post that
 * also carries a "sensor" tag still resolves to "Pro recommended".
 */

export type TriageLevel =
  | "Pro recommended"
  | "Advanced"
  | "Intermediate (DIY)"
  | "Intermediate";

export interface Triage {
  difficulty: TriageLevel;
  /** Generic range, e.g. "1-3 hrs". Never a single false-precision number. */
  time: string;
  /** Short, safe, generic tool list for this category. */
  tools: string;
}

// Tags that signal a hazardous repair a DIYer should hand to a licensed
// technician — combustion, refrigerant under pressure, or high-voltage work.
const PRO_TAGS = new Set([
  "gas",
  "boiler",
  "furnace",
  "combustion",
  "refrigerant",
  "refrigeration",
  "commercial-refrigeration",
  "commercial-refrigerator",
  "compressor",
  "high-voltage",
  "ignition",
  "water-heater",
  "tankless",
  "tankless-water-heater",
  "ice-machine",
]);

// Industrial automation: not life-safety hazardous in the same way, but
// requires service-manual literacy, ESD discipline, and drive/PLC knowledge.
const ADVANCED_TAGS = new Set([
  "cnc",
  "vfd",
  "plc",
  "servo",
  "industrial-controls",
  "drive",
  "drives",
  "inverter",
  "motor-control",
  "machining",
]);

// Approachable HVAC/appliance work for a confident DIYer.
const INTERMEDIATE_DIY_TAGS = new Set([
  "mini-split",
  "heat-pump",
  "thermostat",
  "sensor",
  "filter",
  "capacitor",
]);

// Tool kits by category. Keep them short, generic, and safe. A multimeter is
// always present for anything electrical.
const TOOLS_REFRIGERATION = "Thermometer, multimeter, gauges, PPE";
const TOOLS_GAS = "Multimeter, manometer, combustion analyzer, PPE";
const TOOLS_INDUSTRIAL = "Multimeter, service manual, ESD strap";
const TOOLS_HVAC = "Multimeter, screwdrivers, PPE";

/**
 * Resolve a triage card from a post's tags.
 * @param tags Raw frontmatter tags (any case). May be undefined.
 */
export function getTriage(tags?: readonly string[]): Triage {
  const set = new Set((tags ?? []).map(t => t.toLowerCase()));
  const has = (group: Set<string>) => {
    for (const t of set) if (group.has(t)) return true;
    return false;
  };

  // Refrigerant / combustion / high-voltage -> Pro recommended.
  if (has(PRO_TAGS)) {
    // Pick the most specific tool kit for the hazard present.
    const refrigerationSignals = new Set([
      "refrigerant",
      "refrigeration",
      "commercial-refrigeration",
      "compressor",
      "ice-machine",
    ]);
    const tools = has(refrigerationSignals) ? TOOLS_REFRIGERATION : TOOLS_GAS;
    return { difficulty: "Pro recommended", time: "1-3 hrs", tools };
  }

  // Industrial automation -> Advanced.
  if (has(ADVANCED_TAGS)) {
    return { difficulty: "Advanced", time: "1-3 hrs", tools: TOOLS_INDUSTRIAL };
  }

  // Approachable HVAC/appliance work -> Intermediate (DIY).
  if (has(INTERMEDIATE_DIY_TAGS)) {
    return {
      difficulty: "Intermediate (DIY)",
      time: "15-60 min",
      tools: TOOLS_HVAC,
    };
  }

  // Fallback: treat unknown equipment as general HVAC-grade work.
  return { difficulty: "Intermediate", time: "15-60 min", tools: TOOLS_HVAC };
}
