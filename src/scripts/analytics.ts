/**
 * GA4 Key Event tracking for errorcodefixes.com
 * Tracks: affiliate_click, lead_submit, chatbot_query, scroll_depth
 */

declare function gtag(...args: unknown[]): void;

// Listeners attach to document/window which persist across Astro view-transition
// navigations. Guard so initAnalytics() wires them exactly ONCE per page session;
// otherwise every 'astro:page-load' stacks another click listener and affiliate_click
// events double/triple-fire on SPA nav, corrupting mC/1000.
let listenersAttached = false;

// Resolve the destination hostname for a link. Returns "" if the href can't be parsed.
function destDomain(href: string): string {
  try {
    return new URL(href, window.location.href).hostname;
  } catch {
    return "";
  }
}

function trackAffiliateClicks() {
  document.addEventListener("click", (e: MouseEvent) => {
    const target = (e.target as HTMLElement).closest("a");
    if (!target) return;

    const href = target.href || "";
    const part = target.dataset?.affiliatePart || "";
    const brand = target.dataset?.affiliateBrand || "";
    const kind = target.dataset?.affiliateKind || ""; // "asin" | "search" when AmazonPartLink
    const placement = target.dataset?.affiliatePlacement || ""; // "at_a_glance" | "parts_table" | ...
    const dest = destDomain(href);

    // Amazon Associates links
    if (href.includes("amazon.com") && href.includes("tag=errorcodefixes")) {
      if (typeof gtag !== "undefined") {
        gtag("event", "affiliate_click", {
          affiliate_network: "amazon",
          link_kind: kind || (href.includes("/dp/") ? "asin" : "search"),
          part_number: part,
          brand,
          link_url: href,
          placement,
          dest_domain: dest,
          page_location: window.location.pathname,
        });
      }
    }

    // Angi (lead-gen) — separate event so we can compare RPM by channel
    if (href.includes("angi.com")) {
      if (typeof gtag !== "undefined") {
        gtag("event", "lead_click", {
          partner: "angi",
          link_url: href,
          placement,
          dest_domain: dest,
          page_location: window.location.pathname,
        });
      }
    }

    // Parts-specialist / general supplier links. These are monetized by
    // Skimlinks (rewrites the outbound link at click time — no per-merchant
    // signup), NOT Impact, so they report affiliate_network: "skimlinks".
    // The raw impact.com tracking domain stays on the Impact branch below.
    if (
      href.includes("repairclinic.com") ||
      href.includes("partselect.com") ||
      href.includes("supplyhouse.com") ||
      href.includes("partstown.com") ||
      href.includes("grainger.com") ||
      href.includes("ebay.com") ||
      href.includes("johnstonesupply.com") ||
      href.includes("homedepot.com") ||
      href.includes("jbtools.com") ||
      href.includes("jracenstein.com")
    ) {
      if (typeof gtag !== "undefined") {
        gtag("event", "affiliate_click", {
          affiliate_network: "skimlinks",
          link_kind: kind,
          brand,
          link_url: href,
          placement,
          dest_domain: dest,
          page_location: window.location.pathname,
        });
      }
    }

    // Raw Impact.com tracking links (impact.com radius/click URLs).
    if (href.includes("impact.com")) {
      if (typeof gtag !== "undefined") {
        gtag("event", "affiliate_click", {
          affiliate_network: "impact",
          link_url: href,
          placement,
          dest_domain: dest,
          page_location: window.location.pathname,
        });
      }
    }
  });
}

// QuoteRequest lead capture (QuoteRequest.astro). The form script dispatches
// ecf:lead-submit only after the /api/quote response is CONFIRMED OK (a raw
// submit listener would count leads that the backend then dropped), and
// ecf:lead-error on any failure — so a dead RESEND_API_KEY is discoverable
// in GA4 instead of silently zeroing the channel. Document-level listeners
// survive view-transition navigations, same as the click tracker above.
function trackLeadSubmits() {
  document.addEventListener("ecf:lead-submit", () => {
    if (typeof gtag !== "undefined") {
      gtag("event", "lead_submit", {
        method: "quote_request",
        page_location: window.location.pathname,
      });
    }
  });
  document.addEventListener("ecf:lead-error", () => {
    if (typeof gtag !== "undefined") {
      gtag("event", "lead_error", {
        method: "quote_request",
        page_location: window.location.pathname,
      });
    }
  });
}

function trackScrollDepth() {
  const milestones = [25, 50, 75, 90];
  // Reset the fired set on each view-transition navigation so scroll milestones
  // re-fire for the newly loaded page, even though the listener attaches once.
  let fired = new Set<number>();
  document.addEventListener("astro:page-load", () => {
    fired = new Set<number>();
  });

  window.addEventListener("scroll", () => {
    const scrollPct = Math.round(
      (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100
    );

    for (const milestone of milestones) {
      if (scrollPct >= milestone && !fired.has(milestone)) {
        fired.add(milestone);
        if (typeof gtag !== "undefined") {
          gtag("event", "scroll_depth", {
            percent_scrolled: milestone,
            page_location: window.location.pathname,
          });
        }
      }
    }
  }, { passive: true });
}

function initAnalytics() {
  if (listenersAttached) return;
  listenersAttached = true;
  trackAffiliateClicks();
  trackLeadSubmits();
  trackScrollDepth();
}

initAnalytics();
document.addEventListener("astro:page-load", initAnalytics);
