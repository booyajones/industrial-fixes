#!/usr/bin/env python3
"""
fix_affiliate_links.py

Fixes all 804 articles with the broken affiliate link injection.
The broken pass:
1. Used wrong tag "errorcodefixe-20" (missing 's') 
2. Linked column headers, part names, costs — instead of just "Where to Buy" column
3. Collapsed table rows into a single mangled line

This script:
1. Detects articles with the broken tag
2. Extracts the parts data from the mangled table
3. Reconstructs a clean table with correct affiliate links ONLY in the "Where to Buy" column
4. Writes the fixed file back

Strategy for affiliate links in "Where to Buy" column:
- Extract part name + part number from the row
- Build an Amazon search URL using those as keywords
- Use correct tag: errorcodefixes-20
"""

import os
import re
import sys
from pathlib import Path

BLOG_DIR = Path(r"C:\Users\Administrator\.openclaw\workspace\industrial-fixes\src\data\blog")
AMAZON_TAG = "errorcodefixes-20"
BACKUP_DIR = Path(r"C:\Users\Administrator\.openclaw\workspace\industrial-fixes\_affiliate_backup")

def make_amazon_url(search_query: str) -> str:
    """Build an Amazon search URL with the affiliate tag."""
    clean = search_query.strip()
    # URL-encode spaces as +
    encoded = clean.replace(" ", "+").replace("/", "%2F").replace("&", "%26").replace("(", "%28").replace(")", "%29")
    return f"https://www.amazon.com/s?k={encoded}&tag={AMAZON_TAG}"

def make_repairclinic_url(search_term: str) -> str:
    """Build a RepairClinic search URL."""
    encoded = search_term.strip().replace(" ", "+")
    return f"https://www.repairclinic.com/Search/SearchResult?searchterm={encoded}"

def strip_links(text: str) -> str:
    """Remove any markdown links, returning just the text content."""
    # Remove [text](url) -> text
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    return text.strip()

def strip_all_amazon(text: str) -> str:
    """Remove all Amazon affiliate link markup from text."""
    # Remove markdown links pointing to amazon
    text = re.sub(r'\[([^\]]*)\]\(https://www\.amazon\.com[^)]*\)', r'\1', text)
    return text

def rebuild_parts_table_from_mangled(mangled: str, article_slug: str) -> str:
    """
    Parse the mangled table block and reconstruct a clean one.
    
    The mangled format looks like:
    | Part | Part Number | Typical Cost | [Where to Buy](amazon_url) |  |------|...|
    | [Part name](amazon_url) | part_num | [$cost](amazon_url) | vendor |
    
    We need to:
    1. Identify columns from the header
    2. Extract rows and clean all amazon links from non-"Where to Buy" cells
    3. Add proper amazon links ONLY to the last column (Where to Buy / vendor)
    """
    # Clean the mangled text - strip all existing amazon links first
    clean = strip_all_amazon(mangled)
    
    # Split into pipe-separated tokens and reconstruct rows
    # The mangled format has everything on one line or split weirdly
    # Normalize: replace newlines within the block with spaces first, then split on |
    normalized = re.sub(r'\n\s*\|', ' |', clean)
    normalized = re.sub(r'\|\s*\n', '| ', normalized)
    
    # Now split the whole thing by | 
    parts = [p.strip() for p in normalized.split('|')]
    parts = [p for p in parts if p]  # remove empty
    
    # Try to identify the header row and separator row
    # Header typically: Part, Part Number, Typical Cost, Where to Buy (or similar)
    # Find column count from header
    header_cols = []
    sep_found = False
    rows = []
    current_row = []
    
    # More robust approach: reconstruct from lines
    lines = mangled.split('\n')
    table_lines = [l for l in lines if l.strip().startswith('|') or (l.strip() and '|' in l)]
    
    if not table_lines:
        return mangled  # can't parse, return as-is
    
    # Parse each line as a table row
    parsed_rows = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if '|' in line:
            # Check if it's a separator row (---)
            cells = [c.strip() for c in line.split('|')]
            cells = [c for c in cells if c]  # remove empty from leading/trailing |
            if all(re.match(r'^[-:]+$', c.replace(' ','')) for c in cells if c):
                parsed_rows.append(('sep', cells))
            else:
                # Clean amazon links from cells
                cleaned_cells = [strip_all_amazon(c).strip() for c in cells]
                # Further clean: remove errorcodefixe (broken tag) artifacts
                cleaned_cells = [re.sub(r'errorcodefixe-20', '', c) for c in cleaned_cells]
                parsed_rows.append(('data', cleaned_cells))
    
    if not parsed_rows:
        return mangled
    
    # Identify header
    header_row = None
    sep_row_idx = None
    for i, (rtype, cells) in enumerate(parsed_rows):
        if rtype == 'sep':
            sep_row_idx = i
            if i > 0:
                header_row = parsed_rows[i-1][1]
            break
    
    if header_row is None and parsed_rows:
        header_row = parsed_rows[0][1]
    
    # Determine column structure
    # Find which column is "Where to Buy" / vendor
    vendor_col_idx = -1
    part_col_idx = 0
    partnum_col_idx = -1
    
    if header_row:
        for i, h in enumerate(header_row):
            h_lower = h.lower().strip()
            if 'where' in h_lower or 'buy' in h_lower or 'vendor' in h_lower or 'source' in h_lower:
                vendor_col_idx = i
            if 'part number' in h_lower or 'part #' in h_lower or 'part num' in h_lower or 'number' in h_lower:
                partnum_col_idx = i
            if h_lower in ('part', 'component', 'item', 'description') or h_lower.startswith('part'):
                part_col_idx = i
    
    # If we couldn't find vendor column, assume it's the last one
    if vendor_col_idx == -1 and header_row:
        vendor_col_idx = len(header_row) - 1
    
    # Rebuild clean table
    if not header_row:
        return mangled
    
    num_cols = len(header_row)
    
    # Clean header (no links in headers)
    clean_header = [strip_all_amazon(h).strip() for h in header_row]
    # Remove "Where to Buy" from being a link
    if vendor_col_idx >= 0 and vendor_col_idx < len(clean_header):
        clean_header[vendor_col_idx] = strip_links(clean_header[vendor_col_idx])
    
    # Build output lines
    out_lines = []
    out_lines.append('| ' + ' | '.join(clean_header) + ' |')
    out_lines.append('|' + '|'.join(['------'] * num_cols) + '|')
    
    # Data rows (skip header and sep rows)
    data_start = (sep_row_idx + 1) if sep_row_idx is not None else 1
    
    for i, (rtype, cells) in enumerate(parsed_rows):
        if rtype == 'sep':
            continue
        if i == (sep_row_idx - 1 if sep_row_idx else 0):
            continue  # skip header row
        if rtype == 'data' and i > (sep_row_idx if sep_row_idx else 0):
            # This is a data row
            # Pad/trim to num_cols
            while len(cells) < num_cols:
                cells.append('')
            cells = cells[:num_cols]
            
            # Clean all cells
            clean_cells = [strip_links(strip_all_amazon(c)).strip() for c in cells]
            
            # Skip rows that are all empty (artifact rows)
            if not any(c for c in clean_cells):
                continue
            
            # Build search query for Amazon: prefer part number, fallback to part name
            search_parts = []
            if partnum_col_idx >= 0 and partnum_col_idx < len(clean_cells):
                pnum = clean_cells[partnum_col_idx].strip().strip('"').strip("'")
                if pnum and pnum not in ('-', 'N/A', 'varies', '—'):
                    search_parts.append(pnum)
            if part_col_idx < len(clean_cells):
                pname = clean_cells[part_col_idx].strip()
                if pname:
                    search_parts.append(pname)
            
            if not search_parts and vendor_col_idx < len(clean_cells):
                search_parts = [clean_cells[vendor_col_idx]]
            
            search_query = ' '.join(search_parts[:2])  # Part number + part name
            
            # Build affiliate "Where to Buy" cell
            if vendor_col_idx >= 0 and vendor_col_idx < len(clean_cells) and search_query:
                amazon_url = make_amazon_url(search_query)
                # Keep original vendor info but add Amazon link
                original_vendor = clean_cells[vendor_col_idx]
                if original_vendor and original_vendor not in ('', '-', 'N/A'):
                    # Add Amazon link alongside existing vendor
                    new_vendor = f'[Amazon]({amazon_url}) \\| {original_vendor}'
                else:
                    new_vendor = f'[Amazon]({amazon_url})'
                clean_cells[vendor_col_idx] = new_vendor
            
            out_lines.append('| ' + ' | '.join(clean_cells) + ' |')
    
    return '\n'.join(out_lines)


def fix_article(filepath: Path) -> tuple[bool, str]:
    """
    Fix a single article file.
    Returns (was_changed, status_message)
    """
    content = filepath.read_text(encoding='utf-8', errors='replace')
    
    # Check if this article has the broken tag or needs fixing
    has_broken = 'errorcodefixe-20' in content
    has_correct = 'errorcodefixes-20' in content
    
    if not has_broken and has_correct:
        return False, "already_correct"
    
    if not has_broken and not has_correct:
        # Check if it has a Parts table at all
        if 'Parts That May Need Replacement' not in content:
            return False, "no_parts_table"
        # Has parts table but no links at all - we'll add them below
    
    # Strategy: find the Parts table section and rebuild it
    # Pattern: finds from "## Parts That May Need Replacement" to the next ## heading or end of file
    parts_section_pattern = re.compile(
        r'(## Parts That May Need Replacement[^\n]*\n)(.*?)(\n## |\Z)',
        re.DOTALL | re.IGNORECASE
    )
    
    match = parts_section_pattern.search(content)
    if not match:
        # Try alternate heading format
        parts_section_pattern2 = re.compile(
            r'(## Parts That May Need Replacement.*?\n)((?:\|.*\n?)+)',
            re.DOTALL | re.IGNORECASE
        )
        match = parts_section_pattern2.search(content)
        if not match:
            return False, "no_table_found"
    
    # Get the table portion
    heading = match.group(1)
    table_content = match.group(2)
    after = match.group(3) if len(match.groups()) >= 3 else ''
    
    # Only process if the table content has | characters
    if '|' not in table_content:
        return False, "no_pipe_table"
    
    # Extract just the table lines from the table_content
    table_lines = []
    non_table_before = []
    non_table_after = []
    in_table = False
    
    for line in table_content.split('\n'):
        if '|' in line and line.strip():
            in_table = True
            table_lines.append(line)
        elif in_table and line.strip() == '':
            # Could be end of table
            table_lines.append(line)
        elif in_table:
            in_table = False
            non_table_after.append(line)
        else:
            non_table_before.append(line)
    
    # Strip trailing empty lines from table
    while table_lines and not table_lines[-1].strip():
        non_table_after.insert(0, table_lines.pop())
    
    if not table_lines:
        return False, "empty_table"
    
    table_text = '\n'.join(table_lines)
    
    # Rebuild the table
    new_table = rebuild_parts_table_from_mangled(table_text, filepath.stem)
    
    if not new_table or new_table == table_text:
        # Fallback: just fix the tag typo at minimum
        new_content = content.replace('errorcodefixe-20', 'errorcodefixes-20')
        if new_content != content:
            filepath.write_text(new_content, encoding='utf-8')
            return True, "tag_fixed_only"
        return False, "no_change"
    
    # Reconstruct the section
    before_parts = []
    after_parts = []
    
    if non_table_before:
        before_parts = non_table_before
    if non_table_after:
        after_parts = non_table_after
    
    new_section_content = '\n'.join(before_parts) + ('\n' if before_parts else '') + new_table + ('\n' + '\n'.join(after_parts) if after_parts else '')
    
    # Replace in full content
    new_content = content[:match.start()] + heading + new_section_content + after
    
    # Final safety: fix any remaining broken tags
    new_content = new_content.replace('errorcodefixe-20', 'errorcodefixes-20')
    
    if new_content == content:
        return False, "no_change"
    
    filepath.write_text(new_content, encoding='utf-8')
    return True, "fixed"


def main():
    BACKUP_DIR.mkdir(exist_ok=True)
    
    files = sorted(BLOG_DIR.glob("*.md"))
    print(f"Total articles: {len(files)}")
    
    stats = {"fixed": 0, "tag_fixed_only": 0, "already_correct": 0, 
             "no_parts_table": 0, "no_table_found": 0, "no_change": 0, 
             "empty_table": 0, "no_pipe_table": 0, "errors": 0}
    
    changed_files = []
    
    for i, filepath in enumerate(files):
        try:
            changed, status = fix_article(filepath)
            stats[status] = stats.get(status, 0) + 1
            if changed:
                changed_files.append(filepath.name)
            
            if (i + 1) % 100 == 0:
                print(f"Progress: {i+1}/{len(files)} | Fixed so far: {stats.get('fixed',0) + stats.get('tag_fixed_only',0)}")
                sys.stdout.flush()
        except Exception as e:
            stats["errors"] += 1
            print(f"ERROR on {filepath.name}: {e}")
    
    print("\n=== RESULTS ===")
    for k, v in sorted(stats.items()):
        print(f"  {k}: {v}")
    print(f"\nTotal changed: {len(changed_files)}")
    print("\nSample changed files:")
    for f in changed_files[:10]:
        print(f"  {f}")
    
    # Write summary
    summary_path = Path(r"C:\Users\Administrator\.openclaw\workspace\industrial-fixes\AFFILIATE_PROGRESS.md")
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write("# Affiliate Link Fix Progress\n\n")
        f.write(f"## Run Stats\n\n")
        for k, v in sorted(stats.items()):
            f.write(f"- {k}: {v}\n")
        f.write(f"\n## Total Changed: {len(changed_files)}\n\n")
        f.write("## Amazon Associates Tag: `errorcodefixes-20`\n\n")
        f.write("## Changed Files (first 50)\n\n")
        for fn in changed_files[:50]:
            f.write(f"- {fn}\n")

if __name__ == "__main__":
    main()
