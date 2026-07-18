#!/usr/bin/env python3
"""Apply the verified enrichment (scripts workflow output) to the thin blog pages.

Reads /tmp/ecf_enrich_clean.json (parsed VERIFY_SCHEMA outputs, one per slug) and,
for each page: updates title/description frontmatter, then APPENDS a verified
fault-code table (deduped against codes already on the page), a troubleshooting
section, an FAQ section, and cluster-sibling internal links. Only verified content
is written; nothing is invented here (this script renders, it does not author).
"""
import json, re, os, sys

BLOG = r"C:\Users\chris\industrial-fixes\src\data\blog"
INPUT = next((a for a in sys.argv[1:] if a.endswith(".json")), "/tmp/ecf_enrich_clean.json")
ENR = json.load(open(INPUT, encoding="utf-8"))

CLUSTERS = {
 "abb":["abb-vfd-fault-codes","abb-880-fault-codes","abb-acs580-fault-codes","abb-acs880-complete-guide","abb-ach580-fault-codes","abb-acs550-complete-guide","abb-acs150-fault-codes","abb-acs-drives-plc-fault"],
 "compressors":["sullivan-palatek-compressor-faults","kaeser-compressor-error-codes","elgi-compressor-fault-codes","copeland-scroll-compressor-fault-codes","sullair-compressor-fault-codes","compair-compressor-fault-codes","boge-compressor-error-codes","bitzer-compressor-fault-codes","air-compressor-fault-codes","ingersoll-rand-r-series-faults"],
 "vfd_drives":["sew-eurodrive-vfd-fault-codes","sew-eurodrive-fault-f07","delta-vfd-fault-codes","siemens-sinumerik-alarm-25000-drive-fault","abb-acs880-complete-guide"],
 "cnc":["hurco-cnc-fault-codes","makino-cnc-fault-codes","doosan-cnc-fault-codes-complete","fanuc-alarm-300","fanuc-0i-md-alarm-codes"],
 "chillers_hvac":["carrier-vrf-error-codes","carrier-aquasnap-fault-codes","florida-heat-pump-error-codes","daikin-f9-error-code","daikin-vrv-vrf-u4-error-code","daikin-e1-error-code","york-chiller-fault-codes"],
 "generators":["cummins-onan-fault-codes","generac-generator-error-codes"],
 "commercial_kitchen":["hobart-dishwasher-error-codes","frymaster-fryer-error-codes","manitowoc-indigo-nxt-complete-guide","rational-combi-oven-error-codes","icombi-classic-e01-error","meiko-dishwasher-fault-codes"],
 "ups_power":["apc-ups-error-codes"],
 "boilers_wh":["laars-boiler-fault-codes","burnham-alpine-error-codes","weil-mclain-e04-error-code"],
 "misc":["miller-welder-fault-code-h1","emerson-e2-controller-error-codes","dixell-xr60c-p1-error-code"],
}
slug2cluster = {s: c for c, ss in CLUSTERS.items() for s in ss}

def cell(t):  # markdown table cell: strip pipes/newlines, collapse ws
    return re.sub(r"\s+", " ", str(t or "").replace("|", "/").replace("\n", " ")).strip()

def yq(s):    # yaml double-quoted scalar
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'

def title_from_slug(s):
    return re.sub(r"\b(vfd|ups|cnc|hvac|vrf|vrv|mdc)\b", lambda m: m.group(0).upper(),
                  s.replace("-", " ").title())

APPLY = "--apply" in sys.argv
report = []
for slug, v in ENR.items():
    f = os.path.join(BLOG, slug + ".md")
    if not os.path.exists(f):
        report.append((slug, "MISSING FILE")); continue
    txt = open(f, encoding="utf-8").read()
    m = re.match(r"^(---\n.*?\n---\n)(.*)$", txt, re.S)
    if not m:
        report.append((slug, "NO FRONTMATTER")); continue
    fm, body = m.group(1), m.group(2)
    w0 = len(re.findall(r"\w+", body))

    # 1) title/description (only if verifier marked safe)
    if v.get("titleMetaSafe") and v.get("approvedTitle"):
        fm = re.sub(r'(?m)^title:.*$', "title: " + yq(v["approvedTitle"]), fm, count=1)
    if v.get("titleMetaSafe") and v.get("approvedMeta"):
        if re.search(r'(?m)^description:', fm):
            fm = re.sub(r'(?m)^description:.*$', "description: " + yq(v["approvedMeta"]), fm, count=1)

    # 2) dedupe verified codes against codes already on the page
    codes = v.get("verifiedFaultCodes") or []
    fresh = [c for c in codes if not re.search(r'(?<![\w-])' + re.escape(c["code"].split()[0]) + r'(?![\w-])', body)]

    blocks = []
    eq = title_from_slug(slug).replace(" Error Codes", "").replace(" Fault Codes", "").replace(" Faults", "").strip()
    if fresh:
        rows = "\n".join(f"| {cell(c['code'])} | {cell(c['meaning'])} | {cell(c['cause'])} | {cell(c['fix'])} |" for c in fresh)
        blocks.append(f"## More {eq} fault codes\n\nCompiled from manufacturer service manuals and authorized documentation.\n\n| Code | What it means | Likely cause | How to fix |\n| --- | --- | --- | --- |\n{rows}\n")
    ts = (v.get("troubleshootingCorrected") or "").strip()
    if v.get("troubleshootingApproved") and ts and not re.search(r'(?im)^##\s+how to troubleshoot', body):
        blocks.append(f"## How to troubleshoot {eq}\n\n{ts}\n")
    faqs = v.get("verifiedFaqs") or []
    if faqs and not re.search(r'(?im)^##\s+(frequently asked|faq)', body):
        qa = "\n\n".join(f"### {cell(q['q'])}\n\n{q['a'].strip()}" for q in faqs)
        blocks.append(f"## Frequently asked questions\n\n{qa}\n")
    # cluster sibling links
    sibs = [s for s in CLUSTERS.get(slug2cluster.get(slug, ""), []) if s != slug and os.path.exists(os.path.join(BLOG, s + ".md"))][:4]
    if sibs and not re.search(r'(?im)^##\s+related', body):
        links = "\n".join(f"- [{title_from_slug(s)}](/posts/{s}/)" for s in sibs)
        blocks.append(f"## Related guides\n\n{links}\n")

    if not blocks and fm == m.group(1):
        report.append((slug, "no change")); continue
    new_body = body.rstrip() + "\n\n" + "\n\n".join(blocks) + "\n" if blocks else body
    out = fm + new_body
    w1 = len(re.findall(r"\w+", new_body))
    report.append((slug, f"+{len(fresh)} codes ({len(codes)-len(fresh)} dup), +{len(faqs)} faq, +{len(sibs)} links | {w0}->{w1}w"))
    if APPLY:
        open(f, "w", encoding="utf-8", newline="\n").write(out)

print(("APPLIED" if APPLY else "DRY RUN") + f" — {len(report)} pages")
for s, r in sorted(report): print(f"  {s:<38} {r}")
