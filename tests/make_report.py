"""Build the Markdown report card from the per-OS JSON files written by report.py."""
import json
import sys
from datetime import datetime, timezone


def mark(ok):
    return "✅" if ok else "❌"


def main():
    sha, *paths = sys.argv[1:]
    reports = sorted((json.load(open(path, encoding="utf-8")) for path in paths), key=lambda r: r["os"])

    def is_ok(report):
        return report["built"] and report["run"] > 0 and report["passed"] == report["run"]

    all_ok = bool(reports) and all(is_ok(r) for r in reports)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# 📊 Report Card",
        "",
        "## Overview",
        "- All tests passed successfully ✅🎉" if all_ok else "- Some checks failed ❌",
        "",
        "## Test matrix",
        "",
        "| | " + " | ".join(f"`{r['os']}`" for r in reports) + " |",
        "|---" + "|:---:" * len(reports) + "|",
        "| *Built?* | " + " | ".join(mark(r["built"]) for r in reports) + " |",
        "| **UnitTests** | " + " | ".join(f"`{r['passed']}/{r['run']}` {mark(is_ok(r))}" for r in reports) + " |",
        "",
        f"*This report was generated for the commit `{sha[:7]}` on {now}.*",
    ]
    print("\n".join(lines))


if __name__ == "__main__":
    main()
