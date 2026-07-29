export const SITE = {
  website: "https://errorcodefixes.com/",
  author: "Error Code Fixes",
  profile: "https://errorcodefixes.com/",
  desc: "Look up equipment fault codes: CNC controls, VFDs, chillers, ice machines, commercial kitchen equipment, and home appliances. What the code means, what causes it, and how to fix it.",
  title: "Error Code Fixes — Industrial & Appliance Fault Code Lookup",
  ogImage: "og-industrial.jpg",
  lightAndDarkMode: true,
  postPerIndex: 4,
  postPerPage: 24,
  scheduledPostMargin: 15 * 60 * 1000, // 15 minutes
  showArchives: false,
  showBackButton: true,
  editPost: {
    enabled: false,
    text: "Edit page",
    url: "",
  },
  dynamicOgImage: false,
  dir: "ltr",
  lang: "en",
  timezone: "America/Chicago",
} as const;

// Buy URL for the Industrial Fault-Code Field Reference (/field-reference/).
// Empty string = not on sale yet: the landing page renders the email-gated
// free-sample flow with "full edition launching soon" framing. Set this to the
// payment link (Gumroad/Lemon Squeezy/etc.) once the FULL edition is uploaded,
// and the page switches to a Buy button automatically.
export const FIELD_REFERENCE_BUY_URL = "";
