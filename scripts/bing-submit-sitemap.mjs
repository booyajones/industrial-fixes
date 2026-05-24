#!/usr/bin/env node
/**
 * bing-submit-sitemap.mjs
 *
 * Pulls every URL from the live sitemap-index.xml and submits them in
 * batches to Bing Webmaster Tools' SubmitUrlBatch API (10k/day cap).
 * Idempotent. Skips URLs already submitted in the last 7 days.
 *
 * USAGE:
 *   BING_API_KEY=... node scripts/bing-submit-sitemap.mjs
 *   node scripts/bing-submit-sitemap.mjs --dry  # preview, don't submit
 */

import { readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, "..");
const STATE_DIR = join(ROOT, "growth-pipeline", "indexing");
const STATE_FILE = join(STATE_DIR, "bing-submitted.json");
const SITE_URL = "https://errorcodefixes.com/";
const SITEMAP_INDEX = "https://errorcodefixes.com/sitemap-index.xml";
const BATCH_SIZE = 500;     // Bing accepts up to 500 per call
// Daily quota is dynamic per site reputation. New sites start at ~50,
// growing as Bing builds trust. We query GetUrlSubmissionQuota live
// and respect whatever Bing currently allows.

const DRY = process.argv.includes("--dry");
const API_KEY = process.env.BING_API_KEY;
if (!API_KEY) {
    console.error("[!] BING_API_KEY env var missing");
    process.exit(1);
}

async function fetchText(url) {
    const r = await fetch(url, { headers: { "user-agent": "Mozilla/5.0 ecf-bot" } });
    if (!r.ok) throw new Error(`${url} -> ${r.status}`);
    return await r.text();
}

async function pullAllUrlsFromSitemapIndex() {
    const idx = await fetchText(SITEMAP_INDEX);
    const sitemapUrls = [...idx.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m => m[1]);
    console.log(`[i] sitemap-index lists ${sitemapUrls.length} sub-sitemaps`);
    const all = new Set();
    for (const sm of sitemapUrls) {
        try {
            const xml = await fetchText(sm);
            const urls = [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m => m[1]);
            urls.forEach(u => all.add(u));
            console.log(`  ${sm.replace("https://errorcodefixes.com", "")}: ${urls.length} URLs`);
        } catch (e) {
            console.warn(`  [!] ${sm}: ${e.message}`);
        }
    }
    return [...all];
}

function loadState() {
    if (!existsSync(STATE_FILE)) return { lastBatch: null, submitted: {} };
    return JSON.parse(readFileSync(STATE_FILE, "utf-8"));
}

function saveState(state) {
    if (!existsSync(STATE_DIR)) mkdirSync(STATE_DIR, { recursive: true });
    writeFileSync(STATE_FILE, JSON.stringify(state, null, 2));
}

async function submitBatch(urls) {
    const body = { siteUrl: SITE_URL, urlList: urls };
    const url = `https://ssl.bing.com/webmaster/api.svc/json/SubmitUrlBatch?apikey=${API_KEY}`;
    const r = await fetch(url, {
        method: "POST",
        headers: { "content-type": "application/json; charset=utf-8" },
        body: JSON.stringify(body),
    });
    const text = await r.text();
    if (!r.ok) throw new Error(`Bing API ${r.status}: ${text.slice(0, 300)}`);
    return JSON.parse(text);
}

async function getQuota() {
    const url = `https://ssl.bing.com/webmaster/api.svc/json/GetUrlSubmissionQuota` +
                `?siteUrl=${encodeURIComponent(SITE_URL)}&apikey=${API_KEY}`;
    const r = await fetch(url);
    const data = await r.json();
    return data.d || {};
}

async function main() {
    const state = loadState();
    const sevenDaysAgo = Date.now() - 7 * 24 * 3600 * 1000;

    const allUrls = await pullAllUrlsFromSitemapIndex();
    console.log(`\n[i] ${allUrls.length} unique URLs in sitemap`);

    // Filter out URLs submitted in the last 7 days
    const queue = allUrls.filter(u => !(state.submitted[u] && state.submitted[u] > sevenDaysAgo));
    console.log(`[i] ${queue.length} URLs need (re-)submission`);

    if (queue.length === 0) {
        console.log("[+] All URLs recently submitted. Nothing to do.");
        return;
    }

    const quota = await getQuota();
    const dailyCap = Math.max(0, quota.DailyQuota || 50);
    console.log(`[i] Bing daily quota: ${dailyCap} (monthly: ${quota.MonthlyQuota || "?"})`);
    const todoToday = queue.slice(0, dailyCap);
    console.log(`[i] Submitting ${todoToday.length} URLs in batches of ${Math.min(BATCH_SIZE, dailyCap)}${DRY ? " (DRY)" : ""}`);

    const now = Date.now();
    let submitted = 0;
    const effectiveBatchSize = Math.min(BATCH_SIZE, dailyCap);
    for (let i = 0; i < todoToday.length; i += effectiveBatchSize) {
        const batch = todoToday.slice(i, i + effectiveBatchSize);
        if (DRY) {
            console.log(`  [dry] would submit batch ${1 + i / BATCH_SIZE}: ${batch.length} URLs`);
        } else {
            try {
                await submitBatch(batch);
                batch.forEach(u => (state.submitted[u] = now));
                submitted += batch.length;
                console.log(`  [+] batch ${1 + i / BATCH_SIZE}: ${batch.length} URLs submitted`);
            } catch (e) {
                console.error(`  [!] batch failed: ${e.message}`);
            }
            // Throttle: 1 batch every 2s to be polite
            await new Promise(r => setTimeout(r, 2000));
        }
    }

    if (!DRY) {
        state.lastBatch = new Date(now).toISOString();
        saveState(state);
        console.log(`\n[+] Done. Submitted ${submitted} URLs to Bing. State: ${STATE_FILE}`);
    }
}

main().catch(e => {
    console.error("FATAL:", e);
    process.exit(1);
});
