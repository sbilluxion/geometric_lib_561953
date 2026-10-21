"""Run the unit tests and save the results as JSON for the report card."""
import argparse
import importlib
import json
import sys
import unittest
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_DIR))

FIGURE_MODULES = ["circle", "rectangle", "square", "triangle"]


def check_built():
    try:
        for name in FIGURE_MODULES:
            importlib.import_module(name)
    except ImportError as error:
        print(error, file=sys.stderr)
        return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--os", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    report = {"os": args.os, "built": check_built(), "run": 0, "passed": 0}

    if report["built"]:
        # tests.py collects every *_tests module, so it stays the single list of tests
        import tests

        suite = unittest.defaultTestLoader.loadTestsFromModule(tests)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        report["run"] = result.testsRun
        report["passed"] = result.testsRun - len(result.failures) - len(result.errors)

    Path(args.out).write_text(json.dumps(report), encoding="utf-8")
    return 0 if report["built"] and report["run"] == report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
