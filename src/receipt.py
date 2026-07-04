from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Mapping

try:
    from .review_gate import review_gate
except ImportError:
    from review_gate import review_gate


def generate_receipt(task: Mapping[str, Any], generated_at: str | None = None) -> dict[str, Any]:
    gate = review_gate(task)
    timestamp = generated_at or datetime.now(timezone.utc).isoformat()
    return {
        "receipt_type": "human_ai_governance_decision_v1",
        "generated_at": timestamp,
        "task_id": gate["task_id"],
        "task": task.get("task", ""),
        "decision": gate["decision"],
        "risk_level": gate["risk_level"],
        "reason": gate["reason"],
        "receipt_required": gate["receipt_required"],
        "evidence_required": gate["evidence_required"],
        "public_safe_boundary": {
            "toy_example_only": True,
            "contains_private_logs": False,
            "contains_real_system_prompt": False,
            "claims_production_readiness": False,
        },
    }

