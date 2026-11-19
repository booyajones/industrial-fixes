"""Offline regression tests; all credentials, HTTP, and Slack calls are mocked."""
import contextlib
import io
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import ecf_daily_report as report


def response(status=200, payload=None):
    return Mock(status_code=status, json=Mock(return_value=payload or {}))


def metrics(*values):
    return {"metricValues": [{"value": str(v)} for v in values]}


class DailyReportTests(unittest.TestCase):
    def setUp(self):
        creds = patch.object(report.service_account.Credentials,
                             "from_service_account_file")
        self.creds = creds.start()
        self.addCleanup(creds.stop)

    def test_summary_http_errors_return_none_without_followup_requests(self):
        for status in (400, 401, 403, 429, 500, 503):
            with self.subTest(status=status), patch.object(
                report.requests, "post", return_value=response(status)
            ) as post, contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertIsNone(report.get_ga4_data())
                post.assert_called_once()
                self.assertEqual(output.getvalue().strip(),
                                 f"GA4 summary request failed (HTTP {status})")

    def test_success_returns_mapping_with_metrics_pages_and_sources(self):
        replies = [
            response(payload={"rows": [metrics(10, 8, 20, .5, 65),
                                      metrics(70, 50, 140, .4, 80)]}),
            response(payload={"rows": [{
                "dimensionValues": [{"value": "/example"}],
                "metricValues": [{"value": "12"}]}]}),
            response(payload={"rows": [{
                "dimensionValues": [{"value": "Organic Search"}],
                "metricValues": [{"value": "7"}]}]}),
        ]
        with patch.object(report.requests, "post", side_effect=replies) as post:
            result = report.get_ga4_data()
        self.assertIsInstance(result, dict)
        self.assertEqual(result["yesterday"]["sessions"], 10)
        self.assertEqual(result["week"]["sessions"], 70)
        self.assertEqual(result["top_pages"], [{"path": "/example", "views": 12}])
        self.assertEqual(result["sources"],
                         [{"channel": "Organic Search", "sessions": 7}])
        self.assertEqual(post.call_count, 3)

    def test_empty_success_is_not_request_failure(self):
        with patch.object(report.requests, "post", return_value=response()):
            result = report.get_ga4_data()
        self.assertEqual(result, {"yesterday": None, "week": None,
                                 "top_pages": [], "sources": []})
        message = self.render(result)
        self.assertIn("No data yet for yesterday", message)
        self.assertNotIn("request failed", message)

    def test_optional_request_failures_preserve_summary(self):
        with patch.object(report.requests, "post", side_effect=[
            response(payload={"rows": [metrics(10, 8, 20, .5, 65)]}),
            response(503), response(403)
        ]):
            result = report.get_ga4_data()
        self.assertEqual(result["yesterday"]["sessions"], 10)
        self.assertEqual(result["top_pages"], [])
        self.assertEqual(result["sources"], [])

    def render(self, ga4, cf=None):
        with patch.object(report, "get_ga4_data", return_value=ga4), \
             patch.object(report, "get_cf_data", return_value=cf), \
             patch.object(report.requests, "post",
                          return_value=response(payload={"ok": True})) as post, \
             contextlib.redirect_stdout(io.StringIO()):
            report.send_report()
        post.assert_called_once()
        self.assertEqual(post.call_args.args[0],
                         "https://slack.com/api/chat.postMessage")
        return post.call_args.kwargs["json"]["text"]

    def test_failed_summary_does_not_crash_or_mislabel_as_zero_traffic(self):
        cf = {"requests": 100, "uniques": 10, "page_views": 20,
              "bandwidth_mb": 1.5, "threats": 0, "date": "2026-11-12"}
        message = self.render(None, cf)
        self.assertIn("Unavailable: summary request failed", message)
        self.assertNotIn("No data yet", message)
        self.assertIn("Cloudflare", message)
        self.assertIn("*100*", message)

    def test_successful_summary_is_formatted(self):
        message = self.render({
            "yesterday": {"sessions": 10, "users": 8, "pageviews": 20,
                          "bounce_rate": .5, "avg_duration": 65},
            "week": None, "top_pages": [], "sources": []
        })
        self.assertIn("Sessions: *10*", message)
        self.assertIn("1m 5s", message)
        self.assertNotIn("Unavailable", message)


if __name__ == "__main__":
    unittest.main()
