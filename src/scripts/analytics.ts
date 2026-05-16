/**
 * GA4 Key Event tracking for errorcodefixes.com
 * Tracks: affiliate_click, chatbot_query, scroll_depth
 */

declare function gtag(...args: unknown[]): void;

function trackAffiliateClicks() {
  document.addEventListener("click", (e: MouseEvent) => {
    const target = (e.target as HTMLElement).closest("a");
    if (!target) return;

    const href = target.href || "";
    const part = target.dataset?.affiliatePart || "";
    const brand = target.dataset?.affiliateBrand || "";
    const kind = target.dataset?.affiliateKind || ""; // "asin" | "search" when AmazonPartLink

    // Amazon Associates links
    if (href.includes("amazon.com") && href.includes("tag=errorcodefixes")) {
      if (typeof gtag !== "undefined") {
        gtag("event", "affiliate_click", {
          affiliate_network: "amazon",
          link_kind: kind || (href.includes("/dp/") ? "asin" : "search"),
          part_number: part,
          brand,
          link_url: href,
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
          page_location: window.location.pathname,
        });
      }
    }

    // Impact.com / general parts supplier links
    if (
      href.includes("impact.com") ||
      href.includes("repairclinic.com") ||
      href.includes("supplyhouse.com") ||
      href.includes("grainger.com") ||
      href.includes("jbtools.com") ||
      href.includes("jracenstein.com")
    ) {
      if (typeof gtag !== "undefined") {
        gtag("event", "affiliate_click", {
          affiliate_network: "impact",
          link_url: href,
          page_location: window.location.pathname,
        });
      }
    }
  });
}

function trackScrollDepth() {
  const milestones = [25, 50, 75, 90];
  const fired = new Set<number>();

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
  trackAffiliateClicks();
  trackScrollDepth();
}

initAnalytics();
document.addEventListener("astro:page-load", initAnalytics);
