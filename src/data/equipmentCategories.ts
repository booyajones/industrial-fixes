// Equipment category metadata. Drives the /equipment/[slug]/ hub pages,
// the /equipment/ index, and the homepage equipment-card grid. One source of
// truth so the three views stay in sync.

export type EquipmentCategory = {
  slug: string;          // URL slug, e.g. "hvac"
  name: string;          // display name, e.g. "HVAC"
  emoji: string;         // homepage card icon
  tagline: string;       // short subtitle for cards + meta description
  intro: string;         // 2-3 sentence intro paragraph for the hub page
  // Posts whose `tags` field contains ANY of these strings are included.
  tags: string[];
  // Featured brands to surface at the top of the hub. Slugs match /brands/[brand]/.
  brands: string[];
  // The author key (matches src/data/authors.ts) who owns this category.
  ownerAuthorKey?: string;
};

export const equipmentCategories: EquipmentCategory[] = [
  {
    slug: "hvac",
    name: "HVAC",
    emoji: "❄️",
    tagline: "Carrier, Daikin, Mitsubishi, Trane",
    intro:
      "Heating, ventilation, and air-conditioning fault diagnostics for residential and commercial systems. Coverage spans furnaces, heat pumps, mini-splits, communicating thermostats, and packaged rooftop units across the major OEMs.",
    tags: [
      "hvac",
      "furnace",
      "heat-pump",
      "mini-split",
      "thermostat",
      "rooftop-unit",
      "air-handler",
    ],
    brands: ["carrier", "trane", "lennox", "daikin", "mitsubishi", "goodman"],
    ownerAuthorKey: "Marcus Webb",
  },
  {
    slug: "cnc",
    name: "CNC Machines",
    emoji: "⚙️",
    tagline: "Fanuc, Haas, Mazak, Siemens",
    intro:
      "Alarm and fault code troubleshooting for CNC machine tools. Servo alarms, spindle faults, axis errors, and control-system issues across Fanuc, Haas, Mazak, Okuma, Siemens, and Heidenhain controllers.",
    tags: ["cnc", "fanuc", "haas", "mazak", "okuma", "siemens-cnc"],
    brands: ["fanuc", "haas", "mazak"],
    ownerAuthorKey: "Dana Kowalski",
  },
  {
    slug: "refrigeration",
    name: "Refrigeration",
    emoji: "🧊",
    tagline: "Walk-in coolers, reach-in, ice machines",
    intro:
      "Commercial refrigeration error codes and diagnostics. Ice machines, walk-in cooler controllers, reach-in display cases, and refrigeration system faults — including Hoshizaki, Manitowoc, Scotsman, True, and Heatcraft equipment.",
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
    emoji: "🔥",
    tagline: "Burnham, Weil-McLain, Carrier, gas & condensing",
    intro:
      "Gas and condensing boiler error codes. Lockout faults, ignition failures, pressure switch errors, and combustion safety codes for residential and commercial boilers including Navien, Rinnai, Noritz, Burnham, and Weil-McLain.",
    tags: ["boiler", "tankless", "water-heater", "hydronic"],
    brands: [],
    ownerAuthorKey: "James Rutherford",
  },
  {
    slug: "compressors",
    name: "Compressors",
    emoji: "🔧",
    tagline: "Rotary screw, reciprocating, centrifugal",
    intro:
      "Industrial air and refrigeration compressor fault codes. Trip causes, oil pressure faults, motor protection alarms, and control-board diagnostics across reciprocating, rotary screw, and centrifugal designs.",
    tags: ["compressor", "air-compressor"],
    brands: [],
    ownerAuthorKey: "Dana Kowalski",
  },
  {
    slug: "electrical",
    name: "Electrical",
    emoji: "⚡",
    tagline: "MCC, VFD, switchgear, UPS",
    intro:
      "Industrial electrical equipment fault codes. Variable frequency drive trips (OC, OV, UV, OL), UPS faults, switchgear alarms, transfer switch faults, and motor control center diagnostics.",
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

export const equipmentBySlug: Record<string, EquipmentCategory> =
  Object.fromEntries(equipmentCategories.map(c => [c.slug, c]));
