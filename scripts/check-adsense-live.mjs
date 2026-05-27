/**
 * AdSense live-serving watcher.
 *
 * AdSense approval has no public/no-auth API (the Management API needs user
 * OAuth we don't have), so instead of reading the dashboard we check the thing
 * that actually matters: are paid ads RENDERING on a live page. When Google
 * approves the site, the auto-ads script injects ad iframes; before approval it
 * injects nothing. This headless check loads real article pages, waits for the
 * ad script, and reports whether any ad slot got filled.
 *
 * Exit codes:
 *   0  SERVING  — ads are rendering (AdSense is live)
 *   2  PENDING  — no ads yet (still in review)
 *   1  ERROR    — couldn't run the check
 *
 * Needs Playwright's chromium (cached on this host). NODE_PATH must point at the
 * global @playwright/mcp node_modules so `playwright-core` resolves.
 */

import { createRequire } from "node:module";
import { execSync } from "node:child_process";
import { existsSync } from "node:fs";

// playwright-core lives in the global @playwright/mcp install. Resolve it at
// runtime (ESM `import` ignores NODE_PATH, so we use createRequire).
const require = createRequire(import.meta.url);
const gRoot = execSync("npm root -g").toString().trim().replace(/\\/g, "/");
const { chromium } = require(`${gRoot}/@playwright/mcp/node_modules/playwright-core`);

const PAGES = [
  "https://errorcodefixes.com/posts/weil-mclain-e04-error-code/",
  "https://errorcodefixes.com/posts/carrier-error-code-15/",
  "https://errorcodefixes.com/",
];

// Use whichever cached chromium build exists (Playwright's pinned build may
// differ from what's installed; any recent chromium loads a page fine).
function chromePath() {
  const base = "C:/Users/Administrator/AppData/Local/ms-playwright";
  for (const v of ["chromium-1217", "chromium-1208", "chromium-1222"]) {
    const p = `${base}/${v}/chrome-win64/chrome.exe`;
    if (existsSync(p)) return p;
  }
  return undefined; // let Playwright try its default
}

async function pageHasAds(page) {
  // Before approval the AdSense script still loads and creates 0x0 scaffold
  // iframes (aswift_0, google_esf) with ins.adsbygoogle data-ad-status="unfilled".
  // A real served ad means data-ad-status="filled" OR an ad iframe that actually
  // rendered with non-trivial size. We require one of those — never mere presence.
  return page.evaluate(() => {
    const filled = [...document.querySelectorAll("ins.adsbygoogle")]
      .filter((e) => e.getAttribute("data-ad-status") === "filled").length;
    const renderedIframes = [...document.querySelectorAll(
      'iframe[id^="aswift_"], iframe[id*="google_ads_iframe"], ' +
      'iframe[src*="googleads"], iframe[src*="doubleclick"], iframe[src*="googlesyndication"]'
    )].filter((f) => f.offsetHeight > 30 && f.offsetWidth > 50).length;
    return { filled, renderedIframes, serving: filled > 0 || renderedIframes > 0 };
  });
}

async function main() {
  const exe = chromePath();
  const browser = await chromium.launch({ headless: true, executablePath: exe });
  let serving = false;
  const details = [];
  try {
    const ctx = await browser.newContext({
      userAgent:
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " +
        "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    });
    for (const url of PAGES) {
      const page = await ctx.newPage();
      try {
        await page.goto(url, { waitUntil: "networkidle", timeout: 45000 });
        await page.waitForTimeout(8000); // give auto-ads time to inject
        const r = await pageHasAds(page);
        details.push(`${url} -> filled=${r.filled} renderedIframes=${r.renderedIframes}`);
        if (r.serving) serving = true;
      } catch (e) {
        details.push(`${url} -> error ${String(e).slice(0, 80)}`);
      } finally {
        await page.close();
      }
      if (serving) break;
    }
  } finally {
    await browser.close();
  }
  for (const d of details) console.log("  " + d);
  if (serving) {
    console.log("RESULT: SERVING — AdSense ads are rendering live.");
    process.exit(0);
  }
  console.log("RESULT: PENDING — no ads rendering yet (still in review).");
  process.exit(2);
}

main().catch((e) => {
  console.error("ERROR:", e);
  process.exit(1);
});
