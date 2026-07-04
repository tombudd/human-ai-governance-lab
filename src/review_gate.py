from __future__ import annotations

from typing import Any, Mapping

try:
    from .classify_risk import classify_task
except ImportError:
    from classify_risk import classify_task


def review_gate(task: Mapping[str, Any]) -> dict[str, Any]:
    decision = classify_task(task)
    return {
        "task_id": decision.task_id,
        "decision": decision.decision,
        "risk_level": decision.risk_level,
        "allowed_to_continue": decision.decision == "allowed",
        "human_checkpoint_required": decision.decision == "needs_human_approval",
        "blocked": decision.decision == "blocked",
        "reason": decision.reason,
        "evidence_required": decision.evidence_required,
        "receipt_required": decision.receipt_required,
    }

