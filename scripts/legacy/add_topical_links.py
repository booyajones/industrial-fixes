#!/usr/bin/env python
"""
Add cross-brand topical internal links to articles that don't already have
a Related Articles section (or have one but could benefit from topical links).

Strategy: group by topic/equipment type, then add links across brands.
"""

import os
import re

BLOG_DIR = r"C:\Users\Administrator\.openclaw\workspace\industrial-fixes\src\data\blog"

# Topic groups - keywords in filename that indicate topic
TOPIC_GROUPS = {
    "water-heater": ["water-heater", "tankless", "bradford-white", "ao-smith-water", "rheem-water", "navien", "rinnai", "noritz", "state-water", "american-water", "lochinvar-boiler", "weil-mclain", "burnham-boiler", "triangle-tube"],
    "mini-split": ["mini-split", "ductless", "heat-pump-e"],
    "heat-pump": ["heat-pump", "geothermal"],
    "furnace": ["furnace", "flashes", "flash"],
    "vfd": ["vfd", "inverter", "powerflex", "altivar", "acs", "fr-", "a1000", "v1000", "ga700", "u1000", "lenze", "danfoss-vlt", "fuji-vfd", "toshiba-vfd", "hitachi-vfd", "baldor-vfd", "eaton-vfd", "nidec-vfd", "parker-ac30", "yaskawa-vfd", "yaskawa-a1000", "yaskawa-v1000", "yaskawa-ga700"],
    "cnc": ["cnc", "fanuc", "haas", "mazak", "okuma", "siemens-828", "siemens-840", "siemens-sinumerik", "num-cnc", "mitsubishi-mr"],
    "ice-machine": ["ice-machine", "scotsman", "manitowoc", "hoshizaki", "ice-o-matic"],
    "commercial-refrigeration": ["refrigerator-error", "refrigeration-error", "walk-in", "reach-in", "true-t", "true-tssu", "traulsen", "beverage-air", "turbo-air", "master-bilt", "victory-refrigerator", "norlake"],
    "boiler": ["boiler", "weil-mclain", "burnham", "lochinvar", "triangle-tube", "slant-fin", "peerless", "crown-boiler"],
    "compressor": ["compressor", "atlas-copco", "kaeser", "sullair", "ingersoll", "boge", "sullivan"],
    "elevator": ["elevator", "otis-elevator", "kone-elevator", "schindler", "thyssenkrupp"],
}

def get_frontmatter_title(content):
    m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"\'')
    return None

def get_slug(filename):
    return filename.replace('.md', '')

def get_topics(filename):
    name = filename.lower().replace('.md', '')
    topics = []
    for topic, keywords in TOPIC_GROUPS.items():
        for kw in keywords:
            if kw in name:
                topics.append(topic)
                break
    return topics

def main():
    files = [f for f in os.listdir(BLOG_DIR) if f.endswith('.md')]
    
    # Build index: filename -> title, topics
    index = {}
    for fname in files:
        fpath = os.path.join(BLOG_DIR, fname)
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        title = get_frontmatter_title(content)
        topics = get_topics(fname)
        has_related = '## Related Articles' in content
        index[fname] = {
            'title': title,
            'topics': topics,
            'has_related': has_related,
            'content': content,
        }
    
    # Build topic -> files map
    topic_map = {t: [] for t in TOPIC_GROUPS}
    for fname, info in index.items():
        for topic in info['topics']:
            topic_map[topic].append(fname)
    
    print("Topic coverage:")
    for topic, fnames in topic_map.items():
        print(f"  {topic}: {len(fnames)} articles")
    
    updated = 0
    skipped_already = 0
    skipped_small = 0
    
    for fname, info in index.items():
        if info['has_related']:
            skipped_already += 1
            continue
        
        if not info['topics']:
            continue
        
        # Collect candidates from all topics this article belongs to
        candidates = []
        for topic in info['topics']:
            for other_fname in topic_map[topic]:
                if other_fname != fname and other_fname not in candidates:
                    candidates.append(other_fname)
        
        # Filter to those with titles, dedupe
        valid = []
        seen_slugs = set()
        for c in candidates:
            if index[c]['title'] and get_slug(c) not in seen_slugs:
                valid.append(c)
                seen_slugs.add(get_slug(c))
        
        if len(valid) < 3:
            skipped_small += 1
            continue
        
        # Pick up to 5 (prefer different brand prefix)
        picked = valid[:5]
        
        # Build section
        links = []
        for p in picked:
            t = index[p]['title']
            slug = get_slug(p)
            links.append(f"- [{t}](/posts/{slug}/)")
        
        section = "\n## Related Articles\n\n" + "\n".join(links) + "\n"
        
        # Append to file
        fpath = os.path.join(BLOG_DIR, fname)
        new_content = info['content'].rstrip() + "\n" + section
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        updated += 1
    
    print(f"\nResults:")
    print(f"  Updated: {updated}")
    print(f"  Already had Related Articles: {skipped_already}")
    print(f"  Skipped (too few in topic group): {skipped_small}")
    print(f"  No topic match: {len(files) - updated - skipped_already - skipped_small}")

if __name__ == '__main__':
    main()
