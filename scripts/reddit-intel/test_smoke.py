"""Module smoke tests — no network. Run with `python -m unittest test_smoke`.

Validates the classification + matching pipeline against synthetic fixtures
so the GH Actions workflow can fail fast on regressions before the live
Reddit call eats a minute of cron time.
"""

from __future__ import annotations

import time
import unittest
from pathlib import Path

import classify
import match_articles


class ClassifyTest(unittest.TestCase):
    def test_extracts_lettered_code(self):
        c = classify.classify(
            [{"post_id": "x", "subreddit": "HVAC", "title": "Carrier E13 fault won't clear",
              "selftext": "", "url": "u", "matched_brand": "Carrier",
              "created_utc": time.time() - 3600, "score": 5, "num_comments": 2}],
            now_utc=time.time(),
        )[0]
        self.assertIn("E13", c.extracted_codes)
        self.assertEqual(c.brand, "Carrier")

    def test_extracts_flash_code(self):
        c = classify.classify(
            [{"post_id": "x", "subreddit": "HVAC", "title": "Goodman furnace flashing 4 times",
              "selftext": "", "url": "u", "matched_brand": "Goodman",
              "created_utc": time.time() - 3600, "score": 0, "num_comments": 0}],
            now_utc=time.time(),
        )[0]
        self.assertIn("4", c.extracted_codes)
        self.assertEqual(c.equipment_category, "hvac")

    def test_urgency_high(self):
        c = classify.classify(
            [{"post_id": "x", "subreddit": "RestaurantOwners",
              "title": "Walk-in down, restaurant is screwed, True T-49 alarm",
              "selftext": "", "url": "u", "matched_brand": "True",
              "created_utc": time.time(), "score": 1, "num_comments": 0}],
            now_utc=time.time(),
        )[0]
        self.assertEqual(c.urgency, "high")
        self.assertEqual(c.equipment_category, "refrigeration")


class MatchTest(unittest.TestCase):
    def setUp(self):
        # Spy a tiny fake corpus
        self.tmp = Path(__file__).resolve().parent / "_test_corpus"
        self.tmp.mkdir(exist_ok=True)
        (self.tmp / "carrier-error-code-13.md").write_text("")
        (self.tmp / "true-refrigeration-error-codes.md").write_text("")

    def tearDown(self):
        for p in self.tmp.glob("*"):
            p.unlink()
        self.tmp.rmdir()

    def test_serp_gap_when_code_known(self):
        hit = classify.Classified(
            post_id="x", subreddit="HVAC", title="Carrier furnace E13",
            url="u", brand="Carrier", extracted_codes=["E13"],
            equipment_category="hvac", urgency="medium",
            age_hours=3, score=1, num_comments=2,
        )
        out = match_articles.annotate([hit], self.tmp)[0]
        self.assertEqual(out["gap_kind"], "serp_gap")
        self.assertEqual(out["matched_slug"], "carrier-error-code-13")

    def test_content_gap_when_code_unknown(self):
        hit = classify.Classified(
            post_id="x", subreddit="HVAC", title="Carrier furnace E999",
            url="u", brand="Carrier", extracted_codes=["E999"],
            equipment_category="hvac", urgency="medium",
            age_hours=3, score=1, num_comments=2,
        )
        out = match_articles.annotate([hit], self.tmp)[0]
        self.assertEqual(out["gap_kind"], "content_gap")


if __name__ == "__main__":
    unittest.main()
