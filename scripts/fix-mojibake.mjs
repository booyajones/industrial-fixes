// fix-mojibake.mjs
// Bulk-repair UTF-8 articles that were saved as CP1252-misinterpreted UTF-8.
// Replaces the most common mojibake sequences (em-dash, en-dash, smart quotes,
// degree sign, etc.) and reports how many files / replacements changed.
// Idempotent — safe to re-run.

import { readdir, readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";

const BLOG_DIR = "src/data/blog";

// CP1252-misread-as-Latin1 mojibake sequences -> correct UTF-8 character.
// Order matters: longer sequences first so they match before shorter prefixes.
const REPLACEMENTS = [
  ["ΓÇö", "—"],   // em dash
  ["ΓÇô", "–"],   // en dash
  ["ΓÇ¥", "”"], // right double quote
  ["ΓÇ£", "“"], // left double quote
  ["ΓÇÖ", "’"], // right single quote / apostrophe
  ["ΓÇÿ", "‘"], // left single quote
  ["ΓÇª", "…"],   // ellipsis
  ["ΓÇó", "•"],   // bullet
  ["┬░", "°"],    // degree
  ["┬±", "±"],    // plus-minus
  ["┬®", "©"],    // copyright
  ["┬«", "®"],    // registered
  ["┬á", " "],    // non-breaking space -> regular space
  ["├ñ", "ä"], ["├ú", "ã"], ["├Ñ", "å"],
  ["├⌐", "é"], ["├¿", "è"], ["├¬", "ê"], ["├½", "ë"],
  ["├¡", "í"], ["├«", "î"], ["├»", "ï"],
  ["├│", "ó"], ["├┤", "ô"], ["├╢", "ö"],
  ["├║", "ú"], ["├╗", "û"], ["├╝", "ü"],
  ["├▒", "ñ"],
];

async function main() {
  const files = (await readdir(BLOG_DIR)).filter(f => f.endsWith(".md"));
  let touched = 0;
  let totalSubs = 0;

  for (const f of files) {
    const path = join(BLOG_DIR, f);
    const original = await readFile(path, "utf8");
    let next = original;
    let subsThisFile = 0;

    for (const [bad, good] of REPLACEMENTS) {
      const occ = next.split(bad).length - 1;
      if (occ > 0) {
        next = next.split(bad).join(good);
        subsThisFile += occ;
      }
    }

    if (subsThisFile > 0) {
      await writeFile(path, next, "utf8");
      touched++;
      totalSubs += subsThisFile;
      console.log(`  ${f.padEnd(60)} ${subsThisFile} subs`);
    }
  }

  console.log("");
  console.log(`Done: ${touched} files updated, ${totalSubs} total replacements.`);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
