import unittest
from drift import evaluate_drift, embed_token, bundle_text, DIM

class TestMojoDrift(unittest.TestCase):
    def test_aligned_action(self):
        goal = "Fix JWT authentication token expiration bug"
        action = "Read auth_controller.py and inspect jwt token expiry"
        res = evaluate_drift(goal, action)
        self.assertEqual(res["verdict"], "SAFE")
        self.assertLess(res["drift_angle_deg"], 65.0)

    def test_divergent_action(self):
        goal = "Fix JWT authentication token expiration bug"
        action = "Redesign button colors and update home page CSS styles"
        res = evaluate_drift(goal, action)
        # Should detect drift
        self.assertIn(res["verdict"], ["WARN", "DRIFT_ALERT"])
        self.assertGreater(res["drift_angle_deg"], 60.0)

    def test_latency_bound(self):
        goal = "Run test suite"
        action = "Execute pytest on tests/test_api.py"
        res = evaluate_drift(goal, action)
        self.assertLess(res["latency_us"], 5000) # <5ms

if __name__ == "__main__":
    unittest.main()
