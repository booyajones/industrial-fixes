// Category metadata. Drives the /equipment/[slug]/ hub pages, the /equipment/
// index, and the homepage category grid. One source of truth so the views stay
// in sync.
//
// CONSUMER PIVOT (2026-06-02, council 1ed58c): consumer appliance categories lead;
// industrial categories carry audience:"industrial" so the homepage/nav can filter
// to consumer while industrial hubs stay generable (quarantined + noindexed in P2).

export type EquipmentCategory = {
  slug: string;          // URL slug, e.g. "washers"
  name: string;          // display name, e.g. "Washers"
  emoji: string;         // homepage card icon
  tagline: string;       // short subtitle for cards + meta description
  intro: string;         // 2-3 sentence intro paragraph for the hub page
  audience: "consumer" | "industrial";
  // Posts whose `tags` field contains ANY of these strings are included.
  tags: string[];
  // Featured brands to surface at the top of the hub. Slugs match /brands/[brand]/.
  brands: string[];
  // The author key (matches src/data/authors.ts) who owns this category.
  ownerAuthorKey?: string;
};

export const equipmentCategories: EquipmentCategory[] = [
  // ---------------------------------------------------------------- CONSUMER
  {
    slug: "washers",
    name: "Washers",
    emoji: "🧺",
    tagline: "Samsung, LG, Whirlpool, Maytag, GE",
    intro:
      "Washing machine error codes for top-load and front-load models. Find what your code means, the most likely cause, and the exact replacement part. Coverage spans Samsung, LG, Whirlpool, Maytag, GE, Frigidaire and more, with common faults like drain pump, water inlet valve, door lock and control board.",
    audience: "consumer",
    tags: ["washer"],
    brands: ["samsung", "lg", "whirlpool", "maytag", "ge", "frigidaire"],
    ownerAuthorKey: "Marcus Webb",
  },
  {
    slug: "dryers",
    name: "Dryers",
    emoji: "🌀",
    tagline: "Samsung, LG, Whirlpool, Maytag, GE",
    intro:
      "Clothes dryer error codes for electric and gas models. Heating problems, airflow faults, thermistor and thermal-fuse errors, and the OEM parts that fix them. Coverage across Samsung, LG, Whirlpool, Maytag, GE and Frigidaire.",
    audience: "consumer",
    tags: ["dryer"],
    brands: ["samsung", "lg", "whirlpool", "maytag", "ge"],
    ownerAuthorKey: "Marcus Webb",
  },
  {
    slug: "refrigerators",
    name: "Refrigerators",
    emoji: "🧊",
    tagline: "Samsung, LG, Whirlpool, GE, Frigidaire",
    intro:
      "Refrigerator error codes for french-door, side-by-side and top-freezer models. Cooling faults, evaporator-fan and defrost errors, thermistor and control-board codes, and the exact parts to fix them across Samsung, LG, Whirlpool, GE and Frigidaire.",
    audience: "consumer",
    tags: ["refrigerator"],
    brands: ["samsung", "lg", "whirlpool", "ge", "frigidaire"],
    ownerAuthorKey: "Marcus Webb",
  },
  {
    slug: "dishwashers",
    name: "Dishwashers",
    emoji: "🍽️",
    tagline: "Bosch, Samsung, LG, Whirlpool, KitchenAid",
    intro:
      "Dishwasher error codes and fault diagnostics. Drain and fill faults, heating errors, leak detection and control-board codes, plus the OEM parts that resolve them. Coverage across Bosch, Samsung, LG, Whirlpool, KitchenAid and GE.",
    audience: "consumer",
    tags: ["dishwasher"],
    brands: ["bosch", "samsung", "lg", "whirlpool", "kitchenaid", "ge"],
    ownerAuthorKey: "Marcus Webb",
  },
  {
    slug: "ranges-ovens",
    name: "Ranges & Ovens",
    emoji: "🍳",
    tagline: "Samsung, LG, Whirlpool, GE, Frigidaire",
    intro:
      "Range, oven and cooktop error codes for electric and gas models. Temperature-sensor faults, control (ERC) errors, igniter and relay codes, and the parts that fix them across Samsung, LG, Whirlpool, GE, Frigidaire and KitchenAid. Gas work is flagged pro-recommended.",
    audience: "consumer",
    tags: ["oven", "range"],
    brands: ["samsung", "lg", "whirlpool", "ge", "frigidaire", "kitchenaid"],
    ownerAuthorKey: "James Rutherford",
  },
  {
    slug: "microwaves",
    name: "Microwaves",
    emoji: "📡",
    tagline: "Samsung, LG, GE, Whirlpool",
    intro:
      "Microwave error codes for over-the-range and countertop models. Touchpad, sensor and control-board faults, and the parts that fix them across Samsung, LG, GE and Whirlpool.",
    audience: "consumer",
    tags: ["microwave"],
    brands: ["samsung", "lg", "ge", "whirlpool"],
    ownerAuthorKey: "Dana Kowalski",
  },
  {
    slug: "furnaces",
    name: "Furnaces",
    emoji: "🔥",
    tagline: "Carrier, Goodman, Lennox, Trane, Rheem",
    intro:
      "Residential gas and electric furnace error and flash codes. Ignition lockouts, flame-sensor faults, pressure-switch and limit errors, and the parts that fix them across Carrier, Goodman, Lennox, Trane, Rheem and York. Gas and combustion work is flagged pro-recommended.",
    audience: "consumer",
    tags: ["furnace"],
    brands: ["carrier", "goodman", "lennox", "trane", "rheem", "york"],
    ownerAuthorKey: "James Rutherford",
  },
  {
    slug: "mini-splits",
    name: "Mini-Splits & Heat Pumps",
    emoji: "❄️",
    tagline: "Mitsubishi, Daikin, LG, Fujitsu",
    intro:
      "Ductless mini-split and heat-pump error codes for residential systems. Communication, sensor and fan-motor faults, and the parts that fix them across Mitsubishi, Daikin, LG, Fujitsu, MRCOOL and Senville. Refrigerant work is flagged pro-recommended.",
    audience: "consumer",
    tags: ["mini-split", "heat-pump"],
    brands: ["mitsubishi", "daikin", "lg", "fujitsu"],
    ownerAuthorKey: "Marcus Webb",
  },
  {
    slug: "water-heaters",
    name: "Water Heaters",
    emoji: "♨️",
    tagline: "Rheem, Navien, Rinnai, Bosch",
    intro:
      "Tankless and tank water-heater error codes. Ignition, flame-rod, flow-sensor and venting faults, and the parts that fix them across Rheem, Navien, Rinnai, A.O. Smith, Bosch and Noritz. Gas and venting work is flagged pro-recommended.",
    audience: "consumer",
    tags: ["water-heater", "tankless"],
    brands: ["rheem", "navien", "rinnai", "bosch"],
    ownerAuthorKey: "James Rutherford",
  },

  // -------------------------------------------------------------- INDUSTRIAL
  // Kept generable for /equipment/[slug] but filtered out of the consumer
  // homepage/nav and noindexed in P2 (quarantine). Do not surface to homeowners.
  {
    slug: "hvac",
    name: "Commercial HVAC",
    emoji: "🏢",
    tagline: "Rooftop units, air handlers, controls",
    intro:
      "Commercial HVAC fault diagnostics for rooftop units, air handlers and building controls across the major OEMs.",
    audience: "industrial",
    tags: ["hvac", "rooftop-unit", "air-handler"],
    brands: ["carrier", "trane", "lennox"],
    ownerAuthorKey: "Marcus Webb",
  },
  {
    slug: "cnc",
    name: "CNC Machines",
    emoji: "⚙️",
    tagline: "Fanuc, Haas, Mazak, Siemens",
    intro:
      "Alarm and fault code troubleshooting for CNC machine tools. Servo alarms, spindle faults, axis errors, and control-system issues across Fanuc, Haas, Mazak, Okuma, Siemens, and Heidenhain controllers.",
    audience: "industrial",
    tags: ["cnc", "fanuc", "haas", "mazak", "okuma", "siemens-cnc"],
    brands: ["fanuc", "haas", "mazak"],
    ownerAuthorKey: "Dana Kowalski",
  },
  {
    slug: "refrigeration",
    name: "Commercial Refrigeration",
    emoji: "🏪",
    tagline: "Walk-in coolers, reach-in, ice machines",
    intro:
      "Commercial refrigeration error codes and diagnostics. Ice machines, walk-in cooler controllers, reach-in display cases, and refrigeration system faults including Hoshizaki, Manitowoc, Scotsman, True, and Heatcraft equipment.",
    audience: "industrial",
    tags: [
      "refrigeration",
      "commercial-refrigeration",
      "ice-machine",
      "commercial-refrigerator",
      "walk-in",
    ],
    brands: ["hoshizaki", "manitowoc"],
    ownerAuthorKey: "Marcus Webb",
  },
  {
    slug: "boilers",
    name: "Boilers",
    emoji: "🔧",
    tagline: "Burnham, Weil-McLain, condensing",
    intro:
      "Gas and condensing boiler error codes. Lockout faults, ignition failures, pressure switch errors, and combustion safety codes for residential and commercial boilers including Burnham and Weil-McLain.",
    audience: "industrial",
    tags: ["boiler", "hydronic"],
    brands: [],
    ownerAuthorKey: "James Rutherford",
  },
  {
    slug: "compressors",
    name: "Compressors",
    emoji: "🛠️",
    tagline: "Rotary screw, reciprocating, centrifugal",
    intro:
      "Industrial air and refrigeration compressor fault codes. Trip causes, oil pressure faults, motor protection alarms, and control-board diagnostics across reciprocating, rotary screw, and centrifugal designs.",
    audience: "industrial",
    tags: ["compressor", "air-compressor"],
    brands: [],
    ownerAuthorKey: "Dana Kowalski",
  },
  {
    slug: "electrical",
    name: "Industrial Electrical",
    emoji: "⚡",
    tagline: "MCC, VFD, switchgear, UPS",
    intro:
      "Industrial electrical equipment fault codes. Variable frequency drive trips (OC, OV, UV, OL), UPS faults, switchgear alarms, transfer switch faults, and motor control center diagnostics.",
    audience: "industrial",
    tags: [
      "vfd",
      "variable-frequency-drive",
      "ups",
      "switchgear",
      "mcc",
      "transfer-switch",
      "industrial",
    ],
    brands: [],
    ownerAuthorKey: "Dana Kowalski",
  },
];

// Consumer-only view (homepage grid, /equipment/ index lead, nav).
export const consumerCategories: EquipmentCategory[] = equipmentCategories.filter(
  c => c.audience === "consumer"
);
export const industrialCategories: EquipmentCategory[] = equipmentCategories.filter(
  c => c.audience === "industrial"
);

export const equipmentBySlug: Record<string, EquipmentCategory> =
  Object.fromEntries(equipmentCategories.map(c => [c.slug, c]));
