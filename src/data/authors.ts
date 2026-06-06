// Honest editorial attribution.
//
// The site previously credited fabricated named "technicians" with fabricated
// licenses (EPA 608, NATE, Master Plumber, CAP, CFESA) on safety-adjacent
// content — an E-E-A-T and honesty risk. All bylines now resolve to one
// transparent editorial-team identity. The original frontmatter author keys are
// preserved here so no content files need editing; every key maps to the same
// honest values, and slug is empty so no per-person profile is implied.
const TEAM = {
  name: "Error Code Fixes Editorial Team",
  slug: "",
  title: "Editorial Team",
  credentials: "",
};

export const authors: Record<string, {
  name: string;
  slug: string;
  title: string;
  credentials: string;
}> = {
  "Marcus Webb": { ...TEAM },
  "Dana Kowalski": { ...TEAM },
  "James Rutherford": { ...TEAM },
  "Industrial Error Code Fixes": { ...TEAM },
};
