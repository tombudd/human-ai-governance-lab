import unittest

from src.receipt import generate_receipt


class ReceiptOutputTests(unittest.TestCase):
    def test_receipt_contains_public_safe_boundary(self):
        receipt = generate_receipt(
            {
                "task_id": "TASK-001",
                "task": "Draft a public README section from synthetic notes",
                "uses_private_data": False,
                "external_action": False,
                "could_affect_real_people": False,
                "requires_human_approval": False,
            },
            generated_at="2026-07-04T00:00:00+00:00",
        )

        self.assertEqual(receipt["receipt_type"], "human_ai_governance_decision_v1")
        self.assertEqual(receipt["decision"], "allowed")
        self.assertTrue(receipt["public_safe_boundary"]["toy_example_only"])
        self.assertFalse(receipt["public_safe_boundary"]["contains_private_logs"])
        self.assertFalse(receipt["public_safe_boundary"]["claims_production_readiness"])


if __name__ == "__main__":
    unittest.main()

