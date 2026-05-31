#!/usr/bin/env python3
"""
Task 4: Reassign the anonymous byline to a named, credentialed author by tags.

Articles whose frontmatter has author "Industrial Error Code Fixes" are
reassigned based on their tags:

  Industrial (Dana Kowalski):
    vfd, cnc, plc, servo, industrial-controls, compressor, drive, inverter
  Plumbing (James Rutherford):
    boiler, water-heater, tankless, plumbing, kitchen
  HVAC (Marcus Webb):
    hvac, furnace, heat-pump, mini-split, refrigeration,
    commercial-refrigeration, ac, thermostat

Priority when multiple categories match: Dana > James > Marcus.
  - If an industrial tag is present -> Dana.
  - Else if a plumbing tag is present -> James.
  - Else if an HVAC tag is present -> Marcus.
  - Else: no matching tag -> leave anonymous (reported).

ONLY the `author:` line in frontmatter is modified. modDatetime and every other
field are left untouched.
"""
import re
import glob
import os

BLOG_DIR = os.path.join(os.path.dirname(__file__), "..", "src", "data", "blog")
ANON = "Industrial Error Code Fixes"

INDUSTRIAL = {"vfd", "cnc", "plc", "servo", "industrial-controls",
              "compressor", "drive", "inverter"}
PLUMBING = {"boiler", "water-heater", "tankless", "plumbing", "kitchen"}
HVAC = {"hvac", "furnace", "heat-pump", "mini-split", "refrigeration",
        "commercial-refrigeration", "ac", "thermostat"}

DANA = "Dana Kowalski"
JAMES = "James Rutherford"
MARCUS = "Marcus Webb"

FM_RE = re.compile(r"^(---\r?\n)(.*?)(\r?\n---)", re.S)
AUTHOR_LINE_RE = re.compile(r'^(author:\s*)"' + re.escape(ANON) + r'"\s*$', re.M)


def parse_tags(frontmatter: str):
    """Extract tag values from a block-style `tags:` list in frontmatter."""
    m = re.search(r"^tags:\s*\n((?:[ \t]*-[ \t]*.+\r?\n?)+)", frontmatter, re.M)
    tags = []
    if m:
        for line in m.group(1).splitlines():
            tm = re.match(r"[ \t]*-[ \t]*(.+)", line)
            if tm:
                tags.append(tm.group(1).strip().strip('"').strip("'").lower())
    # Also handle inline `tags: [a, b, c]` just in case.
    if not tags:
        mi = re.search(r"^tags:\s*\[(.*?)\]", frontmatter, re.M)
        if mi:
            tags = [t.strip().strip('"').strip("'").lower()
                    for t in mi.group(1).split(",") if t.strip()]
    return set(tags)


def pick_author(tags: set):
    if tags & INDUSTRIAL:
        return DANA
    if tags & PLUMBING:
        return JAMES
    if tags & HVAC:
        return MARCUS
    return None


def main():
    files = sorted(glob.glob(os.path.join(BLOG_DIR, "*.md")))
    dist = {DANA: 0, JAMES: 0, MARCUS: 0}
    reassigned = 0
    left_anon = []
    samples = []

    for fp in files:
        with open(fp, encoding="utf-8") as fh:
            txt = fh.read()

        fm_match = FM_RE.match(txt)
        if not fm_match:
            continue
        frontmatter = fm_match.group(2)
        if not AUTHOR_LINE_RE.search(frontmatter):
            continue  # not an anonymous-author article

        tags = parse_tags(frontmatter)
        author = pick_author(tags)
        if author is None:
            left_anon.append((os.path.basename(fp), sorted(tags)))
            continue

        new_fm = AUTHOR_LINE_RE.sub(r'\g<1>"' + author + '"', frontmatter, count=1)
        new_txt = txt[:fm_match.start(2)] + new_fm + txt[fm_match.end(2):]
        with open(fp, "w", encoding="utf-8", newline="") as fh:
            fh.write(new_txt)

        dist[author] += 1
        reassigned += 1
        if len(samples) < 3:
            samples.append((os.path.basename(fp), author, sorted(tags)))

    print("TASK 4 - Author reassignment by tags")
    print(f"Total reassigned: {reassigned}")
    print("Per-author distribution:")
    for a in (DANA, JAMES, MARCUS):
        print(f"  {a}: {dist[a]}")
    print(f"Left anonymous (no matching tag): {len(left_anon)}")
    for fname, tags in left_anon:
        print(f"  {fname}  tags={tags}")
    print("Samples (file -> author [matched tags]):")
    for fname, author, tags in samples:
        print(f"  {fname} -> {author}   tags={tags}")


if __name__ == "__main__":
    main()
