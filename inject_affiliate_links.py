#!/usr/bin/env python3
"""
inject_affiliate_links.py

Cleanly injects Amazon affiliate links into the "Where to Buy" column
of the Parts tables across all articles that don't already have links.

Tag: errorcodefixes-20

Strategy:
- Find the "Parts That May Need Replacement" section
- Parse the markdown table cleanly
- Build Amazon search URL from part number + part name
- Replace the "Where to Buy" / vendor cell with an affiliate link
- Preserve all other content untouched
"""

import os
import re
import sys
from pathlib import Path
from urllib.parse import quote_plus

BLOG_DIR = Path(r"C:\Users\Administrator\.openclaw\workspace\industrial-fixes\src\data\blog")
AMAZON_TAG = "errorcodefixes-20"

def make_amazon_url(query: str) -> str:
    encoded = quote_plus(query.strip())
    return f"https://www.amazon.com/s?k={encoded}&tag={AMAZON_TAG}"

def process_table_row(row: str, col_indices: dict, num_cols: int) -> str:
    """
    Process a single table data row.
    col_indices: dict with 'part', 'partnum', 'vendor' -> column index
    Returns the row with affiliate link added to vendor column.
    """
    # Split on | and clean
    cells = row.split('|')
    # Remove leading/trailing empty from outer pipes
    if cells and not cells[0].strip():
        cells = cells[1:]
    if cells and not cells[-1].strip():
        cells = cells[:-1]
    
    if len(cells) < 2:
        return row
    
    # Pad to num_cols
    while len(cells) < num_cols:
        cells.append('')
    cells = cells[:num_cols]
    
    # Clean each cell
    cells = [c.strip() for c in cells]
    
    # Build search query
    search_parts = []
    
    partnum_idx = col_indices.get('partnum', -1)
    part_idx = col_indices.get('part', 0)
    vendor_idx = col_indices.get('vendor', num_cols - 1)
    
    if partnum_idx >= 0 and partnum_idx < len(cells):
        pnum = cells[partnum_idx].strip(' \t"\'')
        if pnum and pnum not in ('-', 'N/A', 'varies', '—', 'n/a', 'varies by model', 'model-specific'):
            search_parts.append(pnum)
    
    if part_idx < len(cells):
        pname = cells[part_idx].strip()
        if pname and len(pname) > 2:
            search_parts.append(pname)
    
    if not search_parts:
        return row
    
    # Limit search query length
    query = ' '.join(search_parts[:2])
    if len(query) > 100:
        query = query[:100]
    
    amazon_url = make_amazon_url(query)
    
    # Update vendor cell
    if vendor_idx < len(cells):
        original_vendor = cells[vendor_idx].strip()
        if original_vendor and original_vendor not in ('', '-', 'N/A', 'n/a'):
            cells[vendor_idx] = f'[Amazon]({amazon_url}) \\| {original_vendor}'
        else:
            cells[vendor_idx] = f'[Amazon]({amazon_url})'
    
    return '| ' + ' | '.join(cells) + ' |'


def inject_links_into_table(table_text: str) -> str:
    """
    Take a clean markdown table and inject affiliate links into the vendor column.
    Returns modified table or original if can't parse.
    """
    lines = table_text.strip().split('\n')
    
    if len(lines) < 3:
        return table_text
    
    # Find header line (first line with |)
    header_line = None
    sep_line_idx = None
    
    for i, line in enumerate(lines):
        if '|' in line and line.strip().startswith('|'):
            if header_line is None:
                header_line = line
            elif all(c in '|-: ' for c in line.replace('|', '')):
                sep_line_idx = i
                break
    
    if header_line is None or sep_line_idx is None:
        return table_text
    
    # Parse header columns
    header_cells = [c.strip() for c in header_line.split('|')]
    header_cells = [c for i, c in enumerate(header_cells) 
                   if not (i == 0 and not c) and not (i == len(header_cells)-1 and not c)]
    
    num_cols = len(header_cells)
    
    # Identify column roles
    col_indices = {'part': 0, 'partnum': -1, 'vendor': num_cols - 1}
    
    for i, h in enumerate(header_cells):
        h_lower = h.lower().strip()
        if any(kw in h_lower for kw in ['part number', 'part #', 'part num', 'model', 'number', '#']):
            if 'part' in h_lower:
                col_indices['partnum'] = i
        elif h_lower in ('part', 'component', 'item', 'description') or h_lower.startswith('part'):
            col_indices['part'] = i
        elif any(kw in h_lower for kw in ['where', 'buy', 'vendor', 'source', 'supplier', 'purchase']):
            col_indices['vendor'] = i
    
    # Process lines
    output_lines = []
    in_data = False
    
    for i, line in enumerate(lines):
        if i < sep_line_idx:
            # Header lines - keep as-is
            output_lines.append(line)
        elif i == sep_line_idx:
            # Separator line - keep as-is
            output_lines.append(line)
            in_data = True
        elif in_data and '|' in line and line.strip():
            # Data row
            processed = process_table_row(line, col_indices, num_cols)
            output_lines.append(processed)
        else:
            output_lines.append(line)
    
    return '\n'.join(output_lines)


def fix_article(filepath: Path) -> tuple[bool, str]:
    """
    Inject affiliate links into a single article.
    Returns (was_changed, status)
    """
    try:
        content = filepath.read_text(encoding='utf-8', errors='replace')
    except Exception as e:
        return False, f"read_error: {e}"
    
    # Skip if already has correct links
    if 'errorcodefixes-20' in content:
        return False, "already_done"
    
    # Skip if has any amazon links (shouldn't happen after cleanup, but be safe)
    if 'amazon.com' in content:
        return False, "has_amazon_already"
    
    # Find the parts section - multiple heading variants used across the site
    # Main variants: "Parts Often Needed", "Parts That May Need Replacement",
    # "Replacement Parts", "Parts Commonly Needed", "Parts and Tools Often Needed", etc.
    pattern = re.compile(
        r'(##\s*(?:Parts(?:\s+(?:Often|Commonly|That May Be?|and Tools(?:\s+Often)?|You May|to Have|Reference|/\s*Actions(?:\s+Often)?))?\s*(?:Needed|Replacement|Ready)?|Replacement\s+Parts)[^\n]*\n)'  # heading
        r'(\{[^\}]*\}\s*\n)?'                               # optional anchor like {#parts-...}
        r'(\s*\n)?'                                          # optional blank line
        r'((?:\|[^\n]*\n?)+)',                              # table rows
        re.IGNORECASE
    )
    
    match = pattern.search(content)
    if not match:
        return False, "no_parts_table"
    
    heading = match.group(1)
    anchor = match.group(2) or ''
    blank = match.group(3) or ''
    table_text = match.group(4)
    
    if '|' not in table_text:
        return False, "no_pipe_table"
    
    new_table = inject_links_into_table(table_text)
    
    if new_table == table_text:
        return False, "table_unchanged"
    
    # Verify the new table has at least one amazon link
    if 'amazon.com' not in new_table:
        return False, "injection_failed"
    
    # Reconstruct content
    new_section = heading + anchor + blank + new_table
    new_content = content[:match.start()] + new_section + content[match.end():]
    
    if new_content == content:
        return False, "no_change"
    
    filepath.write_text(new_content, encoding='utf-8')
    return True, "fixed"


def main():
    files = sorted(BLOG_DIR.glob("*.md"))
    print(f"Total articles: {len(files)}")
    
    # Only process articles without existing amazon links
    to_process = [f for f in files if 'amazon' not in f.read_text(encoding='utf-8', errors='replace')]
    print(f"Articles to process (no existing links): {len(to_process)}")
    
    stats = {}
    changed = []
    
    for i, filepath in enumerate(to_process):
        was_changed, status = fix_article(filepath)
        stats[status] = stats.get(status, 0) + 1
        if was_changed:
            changed.append(filepath.name)
        
        if (i + 1) % 100 == 0:
            done = stats.get('fixed', 0)
            print(f"  {i+1}/{len(to_process)} processed | Fixed: {done}")
            sys.stdout.flush()
    
    print("\n=== RESULTS ===")
    for k, v in sorted(stats.items()):
        print(f"  {k}: {v}")
    
    print(f"\nTotal fixed: {len(changed)}")
    
    # Final verification
    total = len(list(BLOG_DIR.glob("*.md")))
    with_correct = sum(1 for f in BLOG_DIR.glob("*.md") if 'errorcodefixes-20' in f.read_text(encoding='utf-8', errors='replace'))
    print(f"\nFinal state: {with_correct}/{total} articles have errorcodefixes-20 tag")
    
    # Write progress file
    progress = Path(r"C:\Users\Administrator\.openclaw\workspace\industrial-fixes\AFFILIATE_PROGRESS.md")
    with open(progress, 'w', encoding='utf-8') as f:
        f.write("# Affiliate Link Injection Progress\n\n")
        f.write(f"## Amazon Associates Tag: `errorcodefixes-20`\n\n")
        f.write(f"## Results\n\n")
        for k, v in sorted(stats.items()):
            f.write(f"- {k}: {v}\n")
        f.write(f"\n## Articles with affiliate links: {with_correct} / {total}\n\n")
        f.write(f"## Next Steps\n\n")
        f.write("1. Verify a sample of articles look correct\n")
        f.write("2. Deploy to Vercel (git push)\n")
        f.write("3. Apply for J.Racenstein on Impact (8% commission)\n")
        f.write("4. Apply for JB Tools on Impact (5% commission)\n")
        f.write("5. Apply for RepairClinic on ShareASale (6% commission)\n")

if __name__ == "__main__":
    main()
