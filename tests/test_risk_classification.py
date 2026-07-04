import unittest

from src.classify_risk import ALLOWED, BLOCKED, NEEDS_HUMAN_APPROVAL, classify_task


class RiskClassificationTests(unittest.TestCase):
    def test_low_risk_public_safe_task_is_allowed(self):
        decision = classify_task(
            {
                "task_id": "TASK-001",
                "task": "Draft a public README section from synthetic notes",
                "uses_private_data": False,
                "external_action": False,
                "could_affect_real_people": False,
                "requires_human_approval": False,
            }
        )

        self.assertEqual(decision.decision, ALLOWED)
        self.assertEqual(decision.risk_level, "low")
        self.assertTrue(decision.receipt_required)

    def test_external_or_people_affecting_task_needs_human_approval(self):
        decision = classify_task(
            {
                "task_id": "TASK-002",
                "uses_private_data": False,
                "external_action": True,
                "could_affect_real_people": True,
                "requires_human_approval": True,
            }
        )

        self.assertEqual(decision.decision, NEEDS_HUMAN_APPROVAL)
        self.assertEqual(decision.risk_level, "medium")
        self.assertIn("human review checkpoint", decision.evidence_required)

    def test_private_data_external_action_is_blocked(self):
        decision = classify_task(
            {
                "task_id": "TASK-003",
                "uses_private_data": True,
                "external_action": True,
                "could_affect_real_people": True,
                "requires_human_approval": False,
            }
        )

        self.assertEqual(decision.decision, BLOCKED)
        self.assertEqual(decision.risk_level, "high")
        self.assertIn("data minimization review", decision.evidence_required)


if __name__ == "__main__":
    unittest.main()

