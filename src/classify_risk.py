from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


ALLOWED = "allowed"
NEEDS_HUMAN_APPROVAL = "needs_human_approval"
BLOCKED = "blocked"


@dataclass(frozen=True)
class RiskDecision:
    task_id: str
    decision: str
    risk_level: str
    reason: str
    receipt_required: bool
    evidence_required: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "decision": self.decision,
            "risk_level": self.risk_level,
            "reason": self.reason,
            "receipt_required": self.receipt_required,
            "evidence_required": self.evidence_required,
        }


def classify_task(task: Mapping[str, Any]) -> RiskDecision:
    task_id = str(task.get("task_id", "UNKNOWN"))
    uses_private_data = bool(task.get("uses_private_data", False))
    external_action = bool(task.get("external_action", False))
    could_affect_real_people = bool(task.get("could_affect_real_people", False))
    requires_human_approval = bool(task.get("requires_human_approval", False))

    if uses_private_data and external_action:
        return RiskDecision(
            task_id=task_id,
            decision=BLOCKED,
            risk_level="high",
            reason=(
                "Blocked because the task combines private data with an external action. "
                "This toy gate requires a separate, explicit approval path before any such action."
            ),
            receipt_required=True,
            evidence_required=[
                "human approval record",
                "data minimization review",
                "external action rollback plan",
            ],
        )

    if external_action or could_affect_real_people or requires_human_approval or uses_private_data:
        return RiskDecision(
            task_id=task_id,
            decision=NEEDS_HUMAN_APPROVAL,
            risk_level="medium",
            reason=(
                "Needs human approval because the task has an external action, private data, "
                "or potential impact on real people."
            ),
            receipt_required=True,
            evidence_required=[
                "human review checkpoint",
                "approved final output",
                "decision receipt",
            ],
        )

    return RiskDecision(
        task_id=task_id,
        decision=ALLOWED,
        risk_level="low",
        reason=(
            "Synthetic public-safe drafting task with no external action, private data, "
            "or direct impact on real people."
        ),
        receipt_required=True,
        evidence_required=["decision receipt"],
    )

