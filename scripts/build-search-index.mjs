/**
 * build-search-index.mjs
 * Reads all markdown files in src/data/blog/, extracts metadata,
 * and writes a compact JSON search index to public/search-index.json.
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const REPO_ROOT = path.resolve(__dirname, '..');
const BLOG_DIR = path.join(REPO_ROOT, 'src', 'data', 'blog');
const OUTPUT_PATH = path.join(REPO_ROOT, 'public', 'search-index.json');

/**
 * Parse frontmatter from a markdown string.
 * Returns { data: {}, body: '' }
 * Splits on /^---$/m which handles any line-ending combo.
 */
function parseFrontmatter(content) {
  // Split on lines that are exactly `---`
  const parts = content.split(/^---$/m);
  // parts[0] = '' (before first ---), parts[1] = yaml, parts[2]+ = body
  if (parts.length < 3) return { data: {}, body: content };

  const rawYaml = parts[1];
  const body = parts.slice(2).join('---');

  // Minimal YAML parser — handles key: "value" and key: value lines
  const data = {};
  for (const line of rawYaml.split('\n')) {
    const kv = line.match(/^(\w+):\s*(.+)$/);
    if (kv) {
      let val = kv[2].trim();
      // Strip surrounding quotes
      if ((val.startsWith('"') && val.endsWith('"')) ||
          (val.startsWith("'") && val.endsWith("'"))) {
        val = val.slice(1, -1);
      }
      data[kv[1]] = val;
    }
  }

  return { data, body };
}

/**
 * Strip markdown syntax to get plain text.
 */
function stripMarkdown(text) {
  return text
    .replace(/^#{1,6}\s+/gm, '')            // headings
    .replace(/!\[.*?\]\(.*?\)/g, '')          // images
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') // links → text
    .replace(/[`*_~>]+/g, '')                // inline code, bold, italic, etc.
    .replace(/^\s*[-*+]\s+/gm, '')           // unordered list markers
    .replace(/^\s*\d+\.\s+/gm, '')           // ordered list markers
    .replace(/\|[^\n]+\|/g, '')              // table rows
    .replace(/\r?\n+/g, ' ')                // newlines → spaces
    .replace(/\s+/g, ' ')
    .trim();
}

/**
 * Extract keywords from a string: tokens 3+ chars, lowercased, deduped.
 */
function extractKeywords(text) {
  return [...new Set(
    text
      .toLowerCase()
      .split(/[-_\s\/\.]+/)
      .map(t => t.replace(/[^a-z0-9]/g, ''))
      .filter(t => t.length >= 3)
  )];
}

// --- Main ---
const files = fs.readdirSync(BLOG_DIR).filter(f => f.endsWith('.md'));

const index = [];
let skipped = 0;

for (const file of files) {
  const slug = file.replace(/\.md$/, '');
  const filePath = path.join(BLOG_DIR, file);
  let content;
  try {
    content = fs.readFileSync(filePath, 'utf8').replace(/\r\n/g, '\n').replace(/\r/g, '\n');
  } catch (e) {
    skipped++;
    continue;
  }

  const { data, body } = parseFrontmatter(content);

  // Skip articles with no title
  if (!data.title || !data.title.trim()) {
    skipped++;
    continue;
  }

  // Skip drafts
  if (data.draft === 'true') {
    skipped++;
    continue;
  }

  const title = data.title.trim();
  const url = `/posts/${slug}/`;

  // Excerpt: first 150 chars of plain body text
  const plainBody = stripMarkdown(body);
  const excerpt = plainBody.substring(0, 150);

  // Keywords: words from title + slug tokens
  const titleKeywords = extractKeywords(title);
  const slugKeywords = extractKeywords(slug);
  const keywords = [...new Set([...titleKeywords, ...slugKeywords])];

  index.push({ slug, title, url, excerpt, keywords });
}

// Write minified JSON
fs.writeFileSync(OUTPUT_PATH, JSON.stringify(index), 'utf8');

const sizeKB = (fs.statSync(OUTPUT_PATH).size / 1024).toFixed(1);
console.log(`✅ Search index written to public/search-index.json`);
console.log(`   Articles indexed: ${index.length}`);
console.log(`   Articles skipped: ${skipped}`);
console.log(`   File size: ${sizeKB} KB`);
