// refresh-moddate.mjs
// Bumps `modDatetime:` in the frontmatter of articles that were just genuinely
// edited (passed in via stdin or hardcoded list). Honest content update.
// - If `modDatetime:` exists, replace it with TODAY (YYYY-MM-DD form).
// - If `modDatetime:` is missing, insert it right after `pubDatetime:`.
// Pass file paths on argv (relative to repo root). Idempotent.

import { readFile, writeFile } from "node:fs/promises";

const TODAY = new Date().toISOString().slice(0, 10) + "T08:00:00Z";

async function bump(path) {
  const original = await readFile(path, "utf8");
  if (!original.startsWith("---")) {
    console.warn(`SKIP no frontmatter: ${path}`);
    return false;
  }

  const fmEnd = original.indexOf("\n---", 3);
  if (fmEnd === -1) {
    console.warn(`SKIP malformed frontmatter: ${path}`);
    return false;
  }

  const fm = original.slice(0, fmEnd);
  const body = original.slice(fmEnd);

  let newFm;
  if (/^modDatetime:\s*.+$/m.test(fm)) {
    newFm = fm.replace(/^modDatetime:\s*.+$/m, `modDatetime: ${TODAY}`);
  } else if (/^pubDatetime:\s*.+$/m.test(fm)) {
    newFm = fm.replace(
      /^(pubDatetime:\s*.+)$/m,
      `$1\nmodDatetime: ${TODAY}`
    );
  } else {
    console.warn(`SKIP no pubDatetime to anchor against: ${path}`);
    return false;
  }

  if (newFm === fm) return false;
  await writeFile(path, newFm + body, "utf8");
  return true;
}

async function main() {
  const paths = process.argv.slice(2);
  if (paths.length === 0) {
    console.error("Usage: node scripts/refresh-moddate.mjs <file> [<file>...]");
    process.exit(2);
  }
  let bumped = 0;
  for (const p of paths) {
    try {
      if (await bump(p)) {
        bumped++;
        console.log(`  updated  ${p}`);
      }
    } catch (e) {
      console.error(`  ERROR    ${p}: ${e.message}`);
    }
  }
  console.log(`\nDone. ${bumped} / ${paths.length} files updated to ${TODAY}.`);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
