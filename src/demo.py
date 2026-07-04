from __future__ import annotations

import json
from pathlib import Path

try:
    from .report import write_report
except ImportError:
    from report import write_report


def main() -> int:
    report = write_report(Path("examples"), Path("reports/sample_report.json"))
    print(json.dumps(report["summary"], indent=2))
    print("Wrote reports/sample_report.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

