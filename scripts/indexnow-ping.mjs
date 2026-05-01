// indexnow-ping.mjs
// Pings IndexNow (Bing/Yandex/etc.) with the URLs that changed in the
// most recent git commit. Runs after a successful build but is safe to
// skip — IndexNow is best-effort signaling, never blocking.
//
// Skip with NO_INDEXNOW=1 in env (CI dry-runs, local builds).
//
// Strategy:
//   1. Ask git which .md / .astro files changed in HEAD vs HEAD~1.
//   2. Map each to its public URL.
//   3. POST the batch to https://api.indexnow.org/indexnow.
//   4. If git is unavailable (e.g. shallow clone), fall back to pinging
//      the homepage and sitemap so something gets indexed.

import { execSync } from "node:child_process";

const KEY = "f5b3c5c081882ae5e934de31784c91fb";
const HOST = "errorcodefixes.com";
const KEY_LOCATION = `https://${HOST}/${KEY}.txt`;
const ENDPOINT = "https://api.indexnow.org/indexnow";

if (process.env.NO_INDEXNOW === "1") {
  console.log("indexnow: skipped (NO_INDEXNOW=1)");
  process.exit(0);
}

function fileToUrl(path) {
  // src/data/blog/<slug>.md -> /posts/<slug>/
  let m = path.match(/^src\/data\/blog\/(.+)\.md$/);
  if (m) return `https://${HOST}/posts/${m[1]}/`;

  // src/pages/<rest>.astro|md  -> /<rest>/  (index files map to /)
  m = path.match(/^src\/pages\/(.+)\.(astro|md)$/);
  if (m) {
    let p = m[1];
    if (p === "index") return `https://${HOST}/`;
    if (p.endsWith("/index")) p = p.slice(0, -"/index".length);
    return `https://${HOST}/${p}/`;
  }

  return null;
}

function getChangedFiles() {
  try {
    const raw = execSync("git diff --name-only HEAD~1 HEAD", {
      stdio: ["ignore", "pipe", "ignore"],
      encoding: "utf8",
    });
    return raw.split("\n").filter(Boolean);
  } catch {
    return null;
  }
}

const changed = getChangedFiles();
let urls;

if (changed) {
  urls = [...new Set(changed.map(fileToUrl).filter(Boolean))];
  if (urls.length === 0) {
    console.log("indexnow: no eligible URLs in last commit; skipping.");
    process.exit(0);
  }
} else {
  console.log("indexnow: git history unavailable, falling back to homepage + sitemap.");
  urls = [`https://${HOST}/`, `https://${HOST}/sitemap-index.xml`];
}

// IndexNow caps a single submit to 10,000 URLs; we'll never approach that.
const payload = {
  host: HOST,
  key: KEY,
  keyLocation: KEY_LOCATION,
  urlList: urls.slice(0, 10000),
};

console.log(`indexnow: submitting ${payload.urlList.length} URLs...`);

try {
  const res = await fetch(ENDPOINT, {
    method: "POST",
    headers: { "Content-Type": "application/json; charset=utf-8" },
    body: JSON.stringify(payload),
  });
  // 200 = accepted, 202 = accepted (queued), 422 = invalid URL list, etc.
  console.log(`indexnow: HTTP ${res.status} ${res.statusText}`);
  if (res.status >= 400) {
    const body = await res.text().catch(() => "");
    console.warn(`indexnow: response body: ${body.slice(0, 400)}`);
  }
} catch (e) {
  // Never fail the build over a ping miss.
  console.warn(`indexnow: ping failed (non-fatal): ${e.message}`);
}
