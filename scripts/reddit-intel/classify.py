"""Classify raw Reddit hits: extract error code, urgency, equipment category.

All regex heuristics. No LLM call — keeps the runner cheap, deterministic,
and runnable on GitHub Actions free tier.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable


# Common code formats across the brands we cover:
#   E1, E01, E021, F7, F12, H6, P4, L1, U0, AL, dF, HI, LO, CF, OL, OC
#   3-flash / 4-flash / "flashing 7 times"
#   numeric-only: 13, 31, 33, 34, 506, 525
CODE_PATTERNS = [
    # Lettered codes
    re.compile(r"\b([EFHPLUACBD][0-9]{1,3}[A-Z]?)\b"),
    # Two-letter status codes (HI, LO, AL, dF, OC, OL, CF)
    re.compile(r"\b(HI|LO|AL|dF|OC|OL|CF|OF|UV|EE|FF)\b"),
    # "N flashes" / "flashing N times"
    re.compile(r"\b(\d{1,2})\s+(?:flash|blink|red|amber|green)", re.IGNORECASE),
    re.compile(r"flash(?:ing|es)?\s+(\d{1,2})\s+times?", re.IGNORECASE),
    # "error code 34", "fault 506"
    re.compile(r"(?:error|fault|code|alarm)\s*#?\s*([A-Z]?\d{1,4}[A-Z]?)", re.IGNORECASE),
]

URGENCY_KEYWORDS = {
    "high": ["walk-in down", "freezer down", "no heat", "no cool", "emergency",
             "won't start", "shutdown", "shut down", "tripping", "smoking",
             "burning smell", "alarm won't stop", "restaurant", "production down"],
    "medium": ["intermittent", "sometimes", "occasionally", "started yesterday",
               "just installed", "after replacing"],
}

EQUIPMENT_HINTS = {
    "hvac": ["furnace", "ac", "a/c", "air handler", "heat pump", "mini split",
             "mini-split", "thermostat", "condenser", "evaporator"],
    "refrigeration": ["walk-in", "reach-in", "cooler", "freezer", "ice machine",
                      "ice maker", "prep table", "merchandiser"],
    "commercial-kitchen": ["combi oven", "deep fryer", "dishwasher", "range",
                           "salamander", "steamer", "tilt skillet"],
    "boiler": ["boiler", "hydronic", "radiator", "baseboard"],
    "cnc": ["cnc", "lathe", "mill", "milling", "controller", "spindle", "tool change",
            "g-code", "m-code", "fanuc", "haas", "siemens"],
    "vfd": ["vfd", "drive", "powerflex", "yaskawa", "altivar", "abb drive"],
    "forklift": ["forklift", "lift truck", "pallet jack", "reach truck"],
    "generator": ["generator", "genset", "standby", "transfer switch", "ats"],
    "electrical": ["panel", "breaker", "contactor", "relay", "fuse", "ups"],
}


@dataclass
class Classified:
    post_id: str
    subreddit: str
    title: str
    url: str
    brand: str
    extracted_codes: list[str]
    equipment_category: str | None
    urgency: str  # "high" | "medium" | "low"
    age_hours: float
    score: int
    num_comments: int


def _extract_codes(text: str) -> list[str]:
    codes: list[str] = []
    for pat in CODE_PATTERNS:
        for m in pat.findall(text):
            code = m if isinstance(m, str) else m[0]
            code = code.strip().upper()
            if code and code not in codes:
                codes.append(code)
    return codes[:8]  # cap


def _detect_equipment(text: str) -> str | None:
    t = text.lower()
    for cat, hints in EQUIPMENT_HINTS.items():
        if any(h in t for h in hints):
            return cat
    return None


def _detect_urgency(text: str) -> str:
    t = text.lower()
    if any(k in t for k in URGENCY_KEYWORDS["high"]):
        return "high"
    if any(k in t for k in URGENCY_KEYWORDS["medium"]):
        return "medium"
    return "low"


def classify(hits: Iterable[dict], now_utc: float) -> list[Classified]:
    out: list[Classified] = []
    for h in hits:
        text = f"{h.get('title', '')}\n\n{h.get('selftext', '')}"
        codes = _extract_codes(text)
        out.append(Classified(
            post_id=h["post_id"],
            subreddit=h["subreddit"],
            title=h.get("title", ""),
            url=h["url"],
            brand=h.get("matched_brand", ""),
            extracted_codes=codes,
            equipment_category=_detect_equipment(text),
            urgency=_detect_urgency(text),
            age_hours=max(0.0, (now_utc - float(h.get("created_utc", 0))) / 3600.0),
            score=int(h.get("score", 0)),
            num_comments=int(h.get("num_comments", 0)),
        ))
    return out
