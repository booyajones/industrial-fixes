#!/usr/bin/env python
"""
Inject Amazon affiliate links into articles that are missing them.
Tag: errorcodefixes-20
Strategy: find the first markdown table in the article that looks like a parts table,
and add Amazon search links to any part names that don't already have links.
"""

import os
import re
import urllib.parse

BLOG_DIR = r"C:\Users\Administrator\.openclaw\workspace\industrial-fixes\src\data\blog"
TAG = "errorcodefixes-20"
TAG_PATTERN = f"tag={TAG}"

def make_amazon_link(part_name):
    """Generate an Amazon search link for a part."""
    # Clean up the part name for search
    clean = re.sub(r'\*+', '', part_name).strip()
    clean = re.sub(r'\s+', ' ', clean)
    if len(clean) < 3:
        return None
    query = urllib.parse.quote_plus(clean)
    return f"https://www.amazon.com/s?k={query}&tag={TAG}"

def inject_affiliate_into_table_row(line, tag):
    """
    Given a markdown table row that has a part name in the first column,
    add an Amazon affiliate link if there isn't one already.
    Pattern: | Part Name | reason | cost |
    """
    if tag in line:
        return line  # Already has affiliate link
    
    # Match table rows: | col1 | col2 | ...
    if not line.strip().startswith('|'):
        return line
    
    # Skip header/separator rows
    if re.match(r'\|\s*[-:]+\s*\|', line):
        return line
    if re.match(r'\|\s*(Part|Component|Item|Name|Product)\s*\|', line, re.IGNORECASE):
        return line
    
    # Extract first column (part name)
    parts = line.split('|')
    if len(parts) < 3:
        return line
    
    first_col = parts[1].strip()
    
    # Skip if first col is empty, is a header, or already has a link
    if not first_col or first_col.startswith('[') or first_col.startswith('-'):
        return line
    if re.search(r'https?://', first_col):
        return line
    
    # Skip rows where first col looks like a header
    if first_col.lower() in ['part', 'component', 'item', 'name', 'product', 'description', 'symptom', 'cause', 'fix', 'tool']:
        return line
    
    # Clean part name (remove bold markers etc)
    clean_name = re.sub(r'\*+', '', first_col).strip()
    if len(clean_name) < 4:
        return line
    
    # Generate link
    link = make_amazon_link(clean_name)
    if not link:
        return line
    
    # Replace first column with linked version
    parts[1] = f" [{first_col}]({link}) "
    return '|'.join(parts)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if TAG_PATTERN in content:
        return False  # Already has links
    
    lines = content.split('\n')
    modified = False
    new_lines = []
    in_table = False
    
    for line in lines:
        stripped = line.strip()
        
        # Track if we're in a table
        if stripped.startswith('|'):
            in_table = True
        elif in_table and not stripped.startswith('|'):
            in_table = False
        
        if in_table and stripped.startswith('|') and TAG_PATTERN not in line:
            new_line = inject_affiliate_into_table_row(line, TAG_PATTERN)
            if new_line != line:
                modified = True
                new_lines.append(new_line)
                continue
        
        new_lines.append(line)
    
    # If no table links were added, try to add a simple "Find parts on Amazon" section
    if not modified:
        # Add an Amazon parts search section before the FAQ or at the end
        insert_text = f"""
## Find Parts on Amazon

Search for replacement parts directly on Amazon:

- [Search HVAC parts on Amazon](https://www.amazon.com/s?k=hvac+repair+parts&tag={TAG})
- [Search refrigeration parts on Amazon](https://www.amazon.com/s?k=commercial+refrigeration+parts&tag={TAG})
- [Search VFD drives and parts on Amazon](https://www.amazon.com/s?k=variable+frequency+drive+parts&tag={TAG})

"""
        # Find a good insertion point (before FAQ section or at end)
        result = '\n'.join(new_lines)
        if '## Frequently Asked Questions' in result:
            result = result.replace('## Frequently Asked Questions', insert_text + '## Frequently Asked Questions', 1)
            modified = True
        elif '## FAQ' in result:
            result = result.replace('## FAQ', insert_text + '## FAQ', 1)
            modified = True
        else:
            result = result + insert_text
            modified = True
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(result)
            return True
        return False
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
    
    return modified

def main():
    files = [f for f in os.listdir(BLOG_DIR) if f.endswith('.md')]
    
    to_process = []
    for fname in files:
        fpath = os.path.join(BLOG_DIR, fname)
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        if TAG_PATTERN not in content:
            to_process.append(fpath)
    
    print(f"Found {len(to_process)} articles without affiliate links")
    
    updated = 0
    for fpath in to_process:
        fname = os.path.basename(fpath)
        try:
            if process_file(fpath):
                print(f"  OK {fname}")
                updated += 1
            else:
                print(f"  -- {fname} (skipped - no suitable location)")
        except Exception as e:
            print(f"  ERR {fname}: {e}")
    
    print(f"\nDone. Updated {updated}/{len(to_process)} files.")

if __name__ == '__main__':
    main()
