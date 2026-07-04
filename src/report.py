from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

try:
    from .receipt import generate_receipt
except ImportError:
    from receipt import generate_receipt


def load_tasks(examples_dir: Path) -> list[dict[str, Any]]:
    tasks: list[dict[str, Any]] = []
    for path in sorted(examples_dir.glob("*.json")):
        with path.open("r", encoding="utf-8") as handle:
            tasks.append(json.load(handle))
    return sorted(tasks, key=lambda task: str(task.get("task_id", "")))


def build_report(examples_dir: Path) -> dict[str, Any]:
    receipts = [
        generate_receipt(task, generated_at="2026-07-04T00:00:00+00:00")
        for task in load_tasks(examples_dir)
    ]
    return {
        "report_type": "human_ai_governance_lab_sample_report_v1",
        "scope": "clean-room toy examples only",
        "summary": {
            "total_tasks": len(receipts),
            "allowed": sum(1 for receipt in receipts if receipt["decision"] == "allowed"),
            "needs_human_approval": sum(
                1 for receipt in receipts if receipt["decision"] == "needs_human_approval"
            ),
            "blocked": sum(1 for receipt in receipts if receipt["decision"] == "blocked"),
        },
        "receipts": receipts,
    }


def write_report(examples_dir: Path, output_path: Path) -> dict[str, Any]:
    report = build_report(examples_dir)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
        handle.write("\n")
    return report


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("Usage: python3 src/report.py <examples_dir> <output_report.json>", file=sys.stderr)
        return 2
    write_report(Path(argv[1]), Path(argv[2]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
