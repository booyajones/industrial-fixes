#!/usr/bin/env python3
"""
Fix in-body Amazon /dp/ links that point at a GENERIC asin_map.json product.

asin_map.json maps ~22 residential-HVAC/appliance keywords ("thermocouple",
"pressure switch", ...) to one ASIN each. Those ASINs were injected in-body
across hundreds of posts, so a Rational combi-oven cabinet probe and an ABB
drive pressure switch both deep-link the same consumer part. Two defects:

  1. MISLABEL  - anchor says "Search on Amazon" / "Amazon search" but the href
                 is a single product page.
  2. WRONG PART- a generic consumer part is not the part for a commercial /
                 industrial machine class. Returns + it contradicts the site's
                 "we tell you when NOT to buy one" independence claim.

Two transforms, no ASIN guessing (CLAUDE.md hard don't #2):

  RELABEL  (residential class, generic part is plausible)
           keep /dp/<ASIN>, force the anchor to "View on Amazon".
  SEARCH   (commercial/industrial class, or the anchor names a specific OEM
           part number the generic ASIN is definitionally not)
           swap the href for a tagged Amazon SEARCH URL for the part actually
           named, matching the /s?ascsubtag=...&k=...&tag=... pattern already
           used in these same files. Anchor becomes "Search on Amazon".

Out of scope on purpose:
  - drafts and noindexed slugs (not part of the indexable quality core)
  - /dp/ links whose ASIN is NOT in asin_map.json: those 9 are hand-picked,
    product-specific buying-guide links (Fieldpiece SDMN6, Robertshaw 41-404)
    and are already honest.

Dry run by default. Pass --apply to write.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from collections import Counter
from urllib.parse import quote_plus

ROOT = pathlib.Path(__file__).resolve().parent.parent
BLOG = ROOT / "src" / "data" / "blog"
AMAZON_TAG = "errorcodefixes-20"

# --------------------------------------------------------------------------
# Equipment-class vocabulary.
#
# Extends the tag vocabulary in src/utils/partMerchant.ts. That module answers
# "which merchant stocks this?"; this one answers "is a generic residential
# part credible on this page?" - a stricter question, so it needs the
# commercial-foodservice / medical / board-level tags partMerchant folds into
# its broader buckets.
# --------------------------------------------------------------------------

# Board-level industrial electronics - mirrors BOARD_LEVEL in partMerchant.ts.
BOARD_LEVEL = {
    "vfd", "cnc", "plc", "industrial-controls", "drive", "servo", "robot",
}

# Tags that make a page commercial/industrial outright.
STRONG_COMMERCIAL = BOARD_LEVEL | {
    # industrial plant
    "industrial", "industrial-maintenance", "automation", "welding",
    "ups", "generator", "cooling-tower", "boiler-room",
    # commercial HVAC
    "commercial", "commercial-hvac", "chiller", "rooftop-unit", "vrf", "bms",
    "building-automation",
    # commercial foodservice + refrigeration
    "commercial-refrigeration", "commercial-kitchen", "foodservice",
    "food-service", "restaurant", "restaurant-equipment", "ice-machine",
    "ice-maker", "walk-in", "display-case", "grocery", "combi-oven",
    "true-refrigeration", "dishwasher-commercial", "fryer", "steamer",
    # medical / lab
    "medical", "sterilizer", "autoclave", "laboratory",
}

# Tags that mark commercial equipment on this site UNLESS the page also carries
# a residential class tag. "refrigeration" is ~95% commercial foodservice here
# (Hoshizaki, Manitowoc, Scotsman, Hussmann, True, Traulsen...) and "compressor"
# is ~90% industrial air compressors, but both appear on a handful of genuinely
# residential pages (ac-compressor-replacement-cost-guide, daikin-j3).
WEAK_COMMERCIAL = {"refrigeration", "compressor", "oven", "range"}

# Residential/light-commercial classes where the generic asin_map part is a
# credible match: this is the equipment those ASINs were actually sourced for.
RESIDENTIAL = {
    "furnace", "heat-pump", "air-conditioner", "ac", "mini-split", "ductless",
    "water-heater", "tankless", "tankless-water-heater", "geothermal",
    "thermostat", "appliance", "washer", "dryer", "refrigerator", "freezer",
    "cooktop", "microwave", "residential",
}

# Commercial/industrial-only brands. Brand is the strongest single signal on a
# thin-tagged page (e.g. tags: [refrigeration, bohn]).
COMMERCIAL_BRANDS = {
    # ice / commercial refrigeration / foodservice
    "hoshizaki", "manitowoc", "scotsman", "ice-o-matic", "follett", "welbilt",
    "traulsen", "turbo-air", "beverage-air", "hussmann", "heatcraft", "bohn",
    "larkin", "true", "delfield", "continental-refrigeration", "kolpak",
    "master-bilt", "howard-mccray", "alto-shaam", "garland", "vulcan",
    "henny-penny", "hobart", "rational", "fujimak", "winterhalter", "carel",
    "cleveland", "blodgett", "frymaster", "pitco", "lincat", "convotherm",
    "unox", "merrychef", "turbochef", "middleby",
    # industrial compressors / refrigeration compressors
    "atlas-copco", "boge", "chicago-pneumatic", "compair", "elgi",
    "fs-elliott", "gardner-denver", "ingersoll-rand", "kaeser", "quincy",
    "sullair", "sullivan-palatek", "mycom", "bitzer", "copeland", "frick",
    # drives / CNC / PLC / robotics / welding
    "fanuc", "abb", "siemens", "yaskawa", "allen-bradley", "powerflex",
    "sinamics", "danfoss", "mitsubishi-electric", "omron", "schneider",
    "mazak", "haas", "okuma", "sew", "sew-eurodrive", "lenze", "kuka",
    "lincoln-electric", "miller", "esab",
    # medical / lab
    "steris", "midmark", "tuttnauer", "getinge",
    # commercial boilers / building
    "lochinvar", "aerco", "patterson-kelley",
    # data centre / power
    "apc", "eaton", "vertiv", "liebert",
}

# Generic test tools are equipment-agnostic: a clamp meter is the same clamp
# meter on a Fanuc page and a furnace page. Keep the deeplink even on
# industrial pages; only the label needs to be honest.
TOOL_ASINS = {"B08ZJSN5X3"}  # clamp meter / multimeter

# ASINs whose asin_map aliases contradict each other, so the broadest alias
# silently mislabels the product. B09FFFPF5L is keyed BOTH as a "defrost
# termination thermostat" and as a bare "temperature sensor" - but a defrost
# thermostat is a bimetal snap switch and an NTC thermistor is a variable
# resistor. They are not substitutable at all, so every thermistor / ambient-
# sensor row that inherited that alias is the wrong part. Likewise B0D2L5NSMM is
# keyed as a "condenser fan motor" and as a bare "fan motor", which then landed
# on mini-split indoor ECM fans and tankless combustion blowers.
#
# Keep the deeplink ONLY where the part named matches the ASIN's true identity;
# otherwise the part is effectively unknown and CLAUDE.md hard don't #2 applies
# ("Unknown part -> search URL or no link"). The bad alias keys are removed from
# asin_map.json in the same change so nothing re-inherits them.
# Third element is a disqualifier list: device nouns that, if present, mean the
# row names something OTHER THAN (or IN ADDITION TO) this product, so the
# deeplink is not a verified single-part match even though a marker hit. Without
# it, "Condenser Fan Motor Capacitor 5/45 MFD" matches "condenser fan" and keeps
# a fan-motor deeplink on a row selling a capacitor.
AMBIGUOUS_ASINS: dict[str, tuple[str, tuple[str, ...], tuple[str, ...]]] = {
    "B09FFFPF5L": ("defrost termination thermostat",
                   ("defrost termination", "defrost sensor", "defrost thermostat"),
                   ("heater", "motor", "valve", "capacitor", "board", "relay",
                    "fuse", "gasket", "compressor")),
    "B0D2L5NSMM": ("condenser / outdoor fan motor",
                   ("condenser fan", "outdoor fan"),
                   ("capacitor", "relay", "board", "switch", "fuse", "contactor",
                    "belt", "blade", "thermostat", "sensor", "compressor")),
}

# Tags are unreliable on this corpus: allen-bradley-powerflex-525-fault-f003 is
# tagged only [hvac, error-codes] despite being a three-phase VFD page. Slug +
# title are always specific, so they get a second, independent vote. Every
# pattern here must be commercial/industrial-ONLY on this site - anything that
# also names residential kit (carrier, honeywell, mitsubishi, "compressor")
# stays out, because a false positive downgrades a good deeplink to a search
# while a false negative only leaves the status quo.
COMMERCIAL_TEXT = re.compile(
    r"\b("
    # drives / motion / controls
    r"vfd|variable frequency|powerflex|sinamics|micromaster|altivar|movidrive|"
    r"movitrac|acs\d{2,3}|fc\s?30\d|ga800|a1000|v1000|cimr|allen.?bradley|"
    r"\babb\b|siemens|yaskawa|lenze|schneider electric|omron|\bplc\b|\bcnc\b|"
    r"servo|encoder fault|fanuc|mazak|okuma|haas (?:mill|lathe|vf)|"
    r"contrologix|compactlogix|micrologix|panelview|profibus|profinet|"
    r"sew.?eurodrive|\brobot|\bkuka\b|motoman|soft starter|line reactor|"
    # industrial process instrumentation (Watlow/Omega/Eurotherm PID loops)
    r"watlow|eurotherm|\bomega\b|process controller|pid controller|"
    r"temperature controller|"
    # welding
    r"weld(?:er|ing)|lincoln electric|millermatic|\besab\b|"
    # industrial air / refrigeration compressors
    r"air compressor|atlas.?copco|ingersoll|kaeser|quincy|sullair|"
    r"gardner.?denver|\bboge\b|compair|\belgi\b|fs.?elliott|sullivan.?palatek|"
    r"chicago pneumatic|bitzer|copeland|frick|mycom|carlyle|"
    # commercial refrigeration + foodservice
    r"ice machine|ice.?maker|hoshizaki|manitowoc|scotsman|ice.?o.?matic|"
    r"follett|welbilt|traulsen|turbo.?air|beverage.?air|hussmann|heatcraft|"
    r"\bbohn\b|larkin|true[- ](?:refrigeration|t[- ]?\d+|gdm|tssu|freezer)|delfield|"
    r"kolpak|master.?bilt|walk.?in|display case|reach.?in|prep table|"
    r"blast chiller|combi.?oven|icombi|alto.?shaam|garland|vulcan|henny.?penny|"
    r"hobart|rational|fujimak|winterhalter|frymaster|pitco|blodgett|"
    r"merrychef|turbochef|convotherm|\bunox\b|middleby|commercial (?:oven|"
    r"dishwasher|fryer|refrigerat|freezer|kitchen)|deep fryer|proofer|"
    # commercial HVAC / building
    r"rooftop|\brtu\b|chiller|cooling tower|\bvrf\b|\bvrv\b|air handler|"
    r"\bahu\b|makeup air|precedent|weathermaker|voyager|intellipak|centravac|"
    r"\bcarel\b|building automation|metasys|alerton|distech|"
    # medical / lab
    r"sterilizer|autoclave|steris|amsco|midmark|tuttnauer|getinge|"
    # data-centre power
    r"symmetra|smart.?ups|liebert|vertiv|\bups (?:fault|error|alarm|battery)|"
    # commercial boilers
    r"lochinvar|\baerco\b|patterson.?kelley"
    r")\b",
    re.I,
)

# Anchors that carry no product-specific promise, so they are safe to rewrite.
GENERIC_ANCHORS = {
    "amazon", "amazon search", "search on amazon", "view on amazon",
    "check price on amazon", "buy on amazon", "shop on amazon",
    "amazon (generic)", "on amazon",
}

# Tags that are topics, not brands - excluded when sniffing a brand for the
# search query.
BRAND_STOPLIST = (
    STRONG_COMMERCIAL | WEAK_COMMERCIAL | RESIDENTIAL | {
        "hvac", "error-codes", "error-code", "troubleshooting", "diagnostics",
        "heating", "cooling", "plumbing", "electrical", "gas", "ignition",
        "lockout", "buying-guide", "cost-guide", "tools", "lookup", "guide",
        "repair", "replacement", "maintenance", "how-to", "parts", "packaged-unit",
        "probe", "controller", "evaporator", "condenser", "inducer",
        "limit-switch", "pressure-switch", "high-pressure", "temperature-control",
        "instrument", "centrifugal", "boiler",
    }
)

# Explicit OEM part-number markers in the part name. If the copy promises
# "Part # 62-24164-01", a generic universal ASIN is the wrong product no matter
# how residential the machine is.
OEM_MARKER = re.compile(
    r"(?:\bpart\s*(?:#|no\.?|number)\s*\S)"          # "Part # 62-24164-01"
    r"|(?:\bp/n\b)"                                  # "P/N 1234"
    r"|(?:#\s*[A-Za-z0-9][A-Za-z0-9-]{4,})"          # "Carrier #HK06WC085"
    r"|(?:\b\d{2}-\d{3,6}-\d{2}\b)"                  # Rheem/Ruud 42-25101-83
    r"|(?:\b[A-Z]\d-\d{8,}\b)"                       # York S1-02545392000
    r"|(?:\b[A-Z]{2,4}\d{4,}[A-Z]?\d*\b)"            # WV8840B1109, RTG20009B
    r"|(?:\b[A-Z]{2}\d{2}[A-Z]{2}\d{2,}\b)"          # Carrier HH18HA499, HH79NZ074
    r"|(?:\b\d{6,9}\b)",                             # True 800452, Takagi 100004490
    re.I,
)

DP_LINK = re.compile(
    r"\[([^\]]*)\]\((https://www\.amazon\.com/dp/([A-Z0-9]{10})([^)]*))\)"
)
MD_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
CELL_SPLIT = re.compile(r"(?<!\\)\|")     # table column separator, not "\|"


def load_noindex() -> set[str]:
    src = (ROOT / "src" / "data" / "noindex-slugs.ts").read_text()
    return set(re.findall(r'^\s*"([^"]+)",', src, re.M))


def parse_front_matter(text: str) -> tuple[str, dict]:
    if not text.startswith("---"):
        return "", {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return "", {}
    fm = parts[1]
    title_m = re.search(r'^title:\s*"?(.*?)"?\s*$', fm, re.M)
    tags: list[str] = []
    if "tags:" in fm:
        tags = [
            t.strip().lower()
            for t in re.findall(r"^\s+-\s+(.+?)\s*$", fm.split("tags:", 1)[1], re.M)
        ]
    return fm, {
        "title": title_m.group(1) if title_m else "",
        "tags": tags,
        "draft": bool(re.search(r"^draft:\s*true\s*$", fm, re.M)),
    }


def classify_post(tags: list[str], slug: str, title: str) -> tuple[str, str]:
    """Return (class, reason) where class is 'commercial' or 'residential'."""
    tset = set(tags)
    strong = tset & STRONG_COMMERCIAL
    if strong:
        return "commercial", f"tag:{sorted(strong)[0]}"
    brands = tset & COMMERCIAL_BRANDS
    if brands:
        return "commercial", f"brand:{sorted(brands)[0]}"
    m = COMMERCIAL_TEXT.search(f"{slug.replace('-', ' ')} {title}")
    if m:
        return "commercial", f"text:{m.group(1).lower()}"
    weak = tset & WEAK_COMMERCIAL
    if weak and not (tset & RESIDENTIAL):
        return "commercial", f"weak-tag:{sorted(weak)[0]}"
    return "residential", "default"


def strip_markdown(s: str) -> str:
    # Park backslash-escaped characters first. Stripping emphasis before
    # unescaping would eat the char out of "\*" and leave a dangling backslash
    # for the unescape pass to then mangle against whatever followed.
    held: list[str] = []

    def hold(m: re.Match) -> str:
        held.append(m.group(1))
        return f"\x00{len(held) - 1}\x00"

    s = re.sub(r"\\(.)", hold, s)
    s = MD_LINK.sub(r"\1", s)
    s = s.replace("**", "").replace("`", "").replace("*", "")
    # A couple of cells carry leaked query-string debris from an older
    # link-injection script (e.g. "...915146)&tag=)"). Never carry that into a
    # search query. \x00 is excluded from the run so the scrub stops at a parked
    # character instead of eating the placeholder and stranding its index.
    s = re.sub(r"[?&][A-Za-z_]+=[^\s|\x00]*", "", s)
    s = re.sub(r"\s+", " ", s)
    # Trim table/label punctuation BEFORE restoring. The strip set contains
    # "|", "-", "—" and ":" - all of which can legitimately BE the escaped
    # character. Restoring first would let the trim silently eat an escaped
    # char that lands on a boundary, e.g. r"Foo \|" -> "Foo".
    #
    # Known trade-off: a placeholder sitting at the TRUE edge halts the trim, so
    # genuine punctuation just past it survives - r"\| | Foo" -> "| | Foo"
    # rather than "| Foo". That is deliberate: under-trimming leaves a slightly
    # noisy search query, whereas the alternative ordering destroys content with
    # no trace. Zero occurrences in the corpus; pinned by selftest.
    s = s.strip(" -—:|")
    return re.sub(r"\x00(\d+)\x00", lambda m: held[int(m.group(1))], s)


def brand_for(title: str, tags: list[str]) -> str:
    """Brand display string, taken from the title so casing stays natural."""
    for tag in tags:
        if tag in BRAND_STOPLIST:
            continue
        for variant in (tag.replace("-", " "), tag.replace("-", "")):
            m = re.search(rf"\b{re.escape(variant)}\b", title, re.I)
            if m:
                return m.group(0)
    return ""


def identity_matches(asin: str, part_name: str) -> bool:
    """Does the part named on the page match what this ASIN actually is?

    Only meaningful for AMBIGUOUS_ASINS, whose asin_map keys disagree with each
    other. An empty part name cannot be shown to match, so it is a mismatch -
    fail toward a search rather than toward a possibly-wrong product.
    """
    _identity, markers, disqualifiers = AMBIGUOUS_ASINS[asin]
    norm = re.sub(r"[^a-z0-9 ]", " ", part_name.lower())
    norm = re.sub(r"\s+", " ", norm)
    if not any(mk in norm for mk in markers):
        return False
    # A marker hit is necessary but not sufficient: a row naming a second device
    # ("Condenser fan motor + capacitor") cannot be satisfied by one product.
    return not any(dq in norm for dq in disqualifiers)


def part_name_for(line: str, anchor: str, link_md: str) -> str:
    """The part this link is actually about."""
    stripped = line.strip()
    if stripped.startswith("|"):
        body = stripped[1:]
        if body.endswith("|") and not body.endswith("\\|"):
            body = body[:-1]
        # Split on column separators ONLY. A backslash-escaped pipe is a
        # literal "|" inside a cell ("Thermocouple \| K-Type"); splitting on it
        # would truncate the part name and strand a dangling backslash.
        cells = CELL_SPLIT.split(body)
        # If the link lives in a later column, column 1 names the part - but
        # only when column 1 is plain text. If column 1 is itself a link, this
        # is a row of links, not label-then-link, and its anchor describes a
        # DIFFERENT part than the one being rewritten.
        for idx, cell in enumerate(cells):
            if link_md in cell:
                if idx > 0 and not MD_LINK.search(cells[0]):
                    candidate = strip_markdown(cells[0])
                    if candidate:
                        return candidate
                break
    # Bullet / prose / link-is-the-first-cell: the anchor names the part unless
    # it is boilerplate, in which case use the text leading up to the link.
    if anchor.strip().lower() not in GENERIC_ANCHORS:
        return strip_markdown(anchor)
    before = strip_markdown(stripped.split(link_md)[0])
    return before


def build_search_url(slug: str, query: str) -> str:
    return (
        f"https://www.amazon.com/s?ascsubtag=ecf-{slug}"
        f"&k={quote_plus(query)}&tag={AMAZON_TAG}"
    )


def selftest() -> int:
    """Cover the shapes the live corpus does not currently contain.

    The corpus today has no row with two /dp/ links and no literal "\\|" in a
    part-name cell, so those branches get no coverage from a real dry run.
    """
    dp = "https://www.amazon.com/dp/B0FPF84HQP?ascsubtag=ecf-x&tag=errorcodefixes-20"
    dp2 = "https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-x&tag=errorcodefixes-20"
    cases: list[tuple[str, str, str]] = []

    # escaped pipe inside the part-name cell must survive intact
    link = f"[Amazon]({dp})"
    cases.append((
        part_name_for(f"| Thermocouple \\| K-Type Universal | {link} |", "Amazon", link),
        "Thermocouple | K-Type Universal",
        "escaped pipe in column 1",
    ))
    # two links in one row: the second must not inherit the first one's name
    a, b = f"[Part A]({dp})", f"[Part B]({dp2})"
    cases.append((
        part_name_for(f"| {a} | {b} |", "Part B", b),
        "Part B",
        "row of links, second link",
    ))
    # normal label-then-link row still reads column 1
    cases.append((
        part_name_for(f"| Cabinet thermocouple B1 | fault | {link} |", "Amazon", link),
        "Cabinet thermocouple B1",
        "label then link",
    ))
    # escaped asterisk must not leave a dangling backslash
    cases.append((
        strip_markdown(r"Gasket \* 2 required"),
        "Gasket * 2 required",
        "escaped asterisk",
    ))
    # emphasis still stripped
    cases.append((strip_markdown("**Gas valve**"), "Gas valve", "bold stripped"))
    # an escaped char sitting ON a trim boundary must survive: the trim set
    # (" -—:|") overlaps the characters people escape, so trimming after the
    # placeholder restore used to delete these silently.
    for src, want, label in [
        (r"Foo \|", "Foo |", "escaped pipe at end"),
        (r"\| Foo", "| Foo", "escaped pipe at start"),
        (r"\- Foo", "- Foo", "escaped hyphen at start"),
        (r"Foo \:", "Foo :", "escaped colon at end"),
    ]:
        cases.append((strip_markdown(src), want, label))
    # genuine table/label punctuation is still trimmed
    cases.append((strip_markdown("| Gas valve |"), "Gas valve", "real pipes trimmed"))
    cases.append((strip_markdown("- Gas valve"), "Gas valve", "bullet dash trimmed"))
    # ...including when a genuine delimiter sits OUTSIDE an escaped one
    cases.append((strip_markdown(r"| \| Foo |"), "| Foo", "trim outside an escaped char"))
    # Pins the documented trade-off of trimming before restore: a parked char at
    # the true edge halts the trim, so the genuine "|" after it survives. This
    # under-trims by design - the other ordering deletes content silently. If
    # this assertion ever flips to "| Foo", the restore has moved back too early.
    cases.append((strip_markdown(r"\| | Foo"), "| | Foo", "parked char halts trim (known)"))
    # the debris scrub must stop at a parked character, not eat the placeholder
    cases.append((
        strip_markdown(r"heater (e.g., 915146)&tag=\*"),
        "heater (e.g., 915146)*",
        "debris scrub stops at escaped char",
    ))
    # ASIN-identity check: keep the deeplink only when the part named matches
    # what the ASIN actually is, per asin_map's own most specific keys.
    for asin, name, want, label in [
        ("B09FFFPF5L", "Defrost termination thermostat", True, "identity: defrost thermostat keeps"),
        ("B09FFFPF5L", "NTC Temperature Sensor (Inlet)", False, "identity: NTC thermistor converts"),
        ("B09FFFPF5L", "Outdoor ambient temperature sensor", False, "identity: ambient sensor converts"),
        ("B0D2L5NSMM", "Condenser fan motor (1/5 HP)", True, "identity: condenser fan keeps"),
        ("B0D2L5NSMM", "Rinnai Combustion Fan Motor", False, "identity: combustion blower converts"),
        ("B0D2L5NSMM", "Indoor fan motor (BLDC)", False, "identity: indoor ECM fan converts"),
        ("B0D2L5NSMM", "", False, "identity: empty name fails to search"),
        # A marker hit is not sufficient. These rows name a capacitor, or a
        # motor AND a capacitor - one product cannot satisfy either, so the
        # deeplink is not a verified match.
        ("B0D2L5NSMM", "Condenser Fan Motor Capacitor 5/45 MFD", False,
         "identity: capacitor row converts despite marker"),
        ("B0D2L5NSMM", "Condenser fan motor + capacitor", False,
         "identity: two-device row converts"),
        ("B09FFFPF5L", "Defrost thermostat / heater", False,
         "identity: defrost thermostat + heater converts"),
    ]:
        cases.append((identity_matches(asin, name), want, label))
    # leaked query-string debris still scrubbed
    cases.append((
        strip_markdown("True defrost heater (e.g., 915146)&tag=)"),
        "True defrost heater (e.g., 915146)",
        "query-string debris",
    ))
    # an ampersand in a part name must not inject a query parameter
    url = build_search_url("x", "High Pressure Switch & Sensors")
    cases.append((
        url.count("&"), 2, "ampersand encoded, only ascsubtag/k/tag remain",
    ))

    failed = 0
    for got, want, label in cases:
        ok = got == want
        failed += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}")
        if not ok:
            print(f"          got  {got!r}\n          want {want!r}")
    print(f"\n{len(cases) - failed}/{len(cases)} passed")
    return 1 if failed else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes")
    ap.add_argument("--samples", type=int, default=12)
    ap.add_argument("--list", choices=["commercial", "residential", "all"],
                    help="dump per-post classification and exit")
    ap.add_argument("--selftest", action="store_true",
                    help="run parser unit checks and exit")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    asin_map = json.loads((ROOT / "asin_map.json").read_text())
    generic_asins = set(asin_map.values())
    noindex = load_noindex()

    stats = Counter()
    reasons = Counter()
    samples: dict[str, list[str]] = {"search": [], "relabel": [], "skipped-query": []}
    changed_files = 0
    post_class = Counter()
    per_post: list[tuple[str, str, int, int]] = []

    for path in sorted(BLOG.glob("*.md")):
        text = path.read_text()
        fm, meta = parse_front_matter(text)
        if not fm:
            continue
        slug = path.stem
        if meta["draft"]:
            continue
        if slug in noindex:
            continue
        if not DP_LINK.search(text):
            continue

        klass, reason = classify_post(meta["tags"], slug, meta["title"])
        if args.list:
            if args.list in ("all", klass):
                print(f"{klass:11s} {reason:28s} {slug}  ::  {meta['title'][:70]}")
            post_class[klass] += 1
            continue
        brand = brand_for(meta["title"], meta["tags"])
        lines = text.splitlines(keepends=True)
        n_search = n_relabel = 0

        for i, line in enumerate(lines):
            if "amazon.com/dp/" not in line:
                continue

            def replace(m: re.Match) -> str:
                nonlocal n_search, n_relabel
                anchor, url, asin, _rest = m.group(1), m.group(2), m.group(3), m.group(4)
                if asin not in generic_asins:
                    stats["kept-handpicked-asin"] += 1
                    return m.group(0)

                part = part_name_for(line, anchor, m.group(0))
                oem = bool(part and OEM_MARKER.search(part))
                is_tool = asin in TOOL_ASINS

                # A generic test tool stays a deeplink everywhere; only the
                # anchor has to stop pretending to be a search.
                if is_tool:
                    decision = "relabel"
                    why = "tool"
                elif klass == "commercial":
                    decision = "search"
                    why = reason
                elif oem:
                    decision = "search"
                    why = "oem-part-number"
                elif asin in AMBIGUOUS_ASINS and not identity_matches(asin, part):
                    decision = "search"
                    why = "asin-identity-mismatch"
                else:
                    decision = "relabel"
                    why = "residential"

                if decision == "search":
                    query = part
                    if brand and brand.lower() not in query.lower():
                        query = f"{brand} {query}".strip()
                    query = query.strip()
                    if len(query) < 4:
                        # No usable part name on the line - relabelling at least
                        # stops the link from lying about being a search.
                        stats["skipped-no-query"] += 1
                        if len(samples["skipped-query"]) < args.samples:
                            samples["skipped-query"].append(
                                f"{slug}:{i+1}  {line.strip()[:150]}"
                            )
                        decision = "relabel"
                        why = "no-part-name"

                if decision == "search":
                    new_anchor = (
                        "Search on Amazon"
                        if anchor.strip().lower() in GENERIC_ANCHORS
                        else anchor
                    )
                    new_url = build_search_url(slug, query)
                    n_search += 1
                    stats["search"] += 1
                    reasons[why] += 1
                    if len(samples["search"]) < args.samples:
                        samples["search"].append(
                            f"{slug}:{i+1} [{why}]\n"
                            f"      - [{anchor}]({url})\n"
                            f"      + [{new_anchor}]({new_url})"
                        )
                    return f"[{new_anchor}]({new_url})"

                new_anchor = (
                    "View on Amazon"
                    if anchor.strip().lower() in GENERIC_ANCHORS
                    else anchor
                )
                stats["relabel"] += 1
                reasons[why] += 1
                if new_anchor == anchor:
                    stats["relabel-noop"] += 1
                    return m.group(0)
                n_relabel += 1
                if len(samples["relabel"]) < args.samples:
                    samples["relabel"].append(
                        f"{slug}:{i+1} [{why}]\n"
                        f"      - [{anchor}]({url})\n"
                        f"      + [{new_anchor}]({url})"
                    )
                return f"[{new_anchor}]({url})"

            lines[i] = DP_LINK.sub(replace, line)

        post_class[klass] += 1
        if n_search or n_relabel:
            changed_files += 1
            per_post.append((slug, klass, n_search, n_relabel))
            if args.apply:
                path.write_text("".join(lines))

    print("=" * 74)
    print(f"{'APPLIED' if args.apply else 'DRY RUN'} - generic-ASIN in-body link fix")
    print("=" * 74)
    print(f"live posts carrying generic /dp/ links : {sum(post_class.values())}")
    print(f"  commercial/industrial class          : {post_class['commercial']}")
    print(f"  residential class                    : {post_class['residential']}")
    print(f"files modified                         : {changed_files}")
    print()
    print(f"links -> tagged Amazon SEARCH url      : {stats['search']}")
    print(f"links kept as /dp/, anchor relabelled  : {stats['relabel'] - stats['relabel-noop']}")
    print(f"links kept as /dp/, anchor already ok  : {stats['relabel-noop']}")
    print(f"links left alone (hand-picked ASIN)    : {stats['kept-handpicked-asin']}")
    print(f"  (of which: no usable part name -> relabelled instead: {stats['skipped-no-query']})")
    print()
    print("decision reasons:")
    for why, n in reasons.most_common():
        print(f"  {n:5d}  {why}")

    for bucket, rows in samples.items():
        if not rows:
            continue
        print(f"\n--- sample: {bucket} ---")
        for r in rows:
            print(f"  {r}")

    if not args.apply:
        print("\n(dry run - nothing written. re-run with --apply)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
