import unittest

from src.review_gate import review_gate


class ReviewGateTests(unittest.TestCase):
    def test_allowed_task_can_continue_without_human_checkpoint(self):
        gate = review_gate(
            {
                "task_id": "TASK-001",
                "uses_private_data": False,
                "external_action": False,
                "could_affect_real_people": False,
                "requires_human_approval": False,
            }
        )

        self.assertTrue(gate["allowed_to_continue"])
        self.assertFalse(gate["human_checkpoint_required"])
        self.assertFalse(gate["blocked"])

    def test_medium_risk_task_stops_at_human_checkpoint(self):
        gate = review_gate(
            {
                "task_id": "TASK-002",
                "uses_private_data": False,
                "external_action": True,
                "could_affect_real_people": False,
                "requires_human_approval": False,
            }
        )

        self.assertFalse(gate["allowed_to_continue"])
        self.assertTrue(gate["human_checkpoint_required"])
        self.assertFalse(gate["blocked"])

    def test_blocked_task_cannot_continue(self):
        gate = review_gate(
            {
                "task_id": "TASK-003",
                "uses_private_data": True,
                "external_action": True,
                "could_affect_real_people": True,
                "requires_human_approval": False,
            }
        )

        self.assertFalse(gate["allowed_to_continue"])
        self.assertFalse(gate["human_checkpoint_required"])
        self.assertTrue(gate["blocked"])


if __name__ == "__main__":
    unittest.main()

