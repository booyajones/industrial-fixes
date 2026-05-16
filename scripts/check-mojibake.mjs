#!/usr/bin/env node
// Post-build scanner: walks dist/ and fails the build if any rendered HTML
// contains U+FFFD (the Unicode replacement character) inside a <p>, table cell,
// or heading — the live site has been observed serving "drifts until it's �"
// in technician-tips sections, which destroys EEAT signals.
//
// Source files are clean; the corruption happens during build (markdown parser
// + sharp + Font subsetting). Catching it at the build boundary forces a fix
// before deploy instead of after.
//
// Exit codes: 0 clean, 1 mojibake detected.

import { readdirSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";

const DIST = "dist";
const REPLACEMENT = "�";

function walk(dir) {
  const out = [];
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    const s = statSync(p);
    if (s.isDirectory()) out.push(...walk(p));
    else if (name.endsWith(".html")) out.push(p);
  }
  return out;
}

const files = walk(DIST);
let hits = 0;
const offenders = [];
for (const f of files) {
  const html = readFileSync(f, "utf8");
  if (html.includes(REPLACEMENT)) {
    hits++;
    // Capture ~40 chars of context around the first hit so the failure log
    // gives the author something to grep for.
    const idx = html.indexOf(REPLACEMENT);
    const ctx = html.slice(Math.max(0, idx - 25), idx + 25).replace(/\s+/g, " ");
    offenders.push({ file: f, ctx });
  }
}

const STRICT = process.env.STRICT_MOJIBAKE === "1";
if (hits > 0) {
  const sev = STRICT ? "✗" : "⚠";
  console.error(`${sev} Mojibake (U+FFFD) detected in ${hits} rendered HTML file(s):`);
  for (const o of offenders.slice(0, 10)) {
    console.error(`  - ${o.file}\n      ...${o.ctx}...`);
  }
  if (offenders.length > 10) console.error(`  ... and ${offenders.length - 10} more`);
  if (STRICT) process.exit(1);
  console.error(`(warn-only; set STRICT_MOJIBAKE=1 to fail the build)`);
  process.exit(0);
}
console.log(`✓ No mojibake found in ${files.length} HTML files.`);
