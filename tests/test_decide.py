import unittest
from src.modules.decide import decide, determine_launch
from src.modules.types import Connectors, Coordinate, Parameters


class DecideTests(unittest.TestCase):
    def setUp(self):
        self.mock_points: list[Coordinate] = [
            {"x": 0.0, "y": 0.0},
        ] * 15

        self.mock_params: Parameters = {
            "a_pts": 1,
            "area1": 1.0,
            "area2": 1.0,
            "b_pts": 1,
            "c_pts": 1,
            "d_pts": 1,
            "dist": 1.0,
            "e_pts": 1,
            "epsilon": 0.1,
            "f_pts": 1,
            "g_pts": 1,
            "k_pts": 1,
            "length1": 2.0,
            "length2": 1.0,
            "n_pts": 1,
            "q_pts": 1,
            "quads": 1,
            "radius1": 1.0,
            "radius2": 1.0,
        }

        self.mock_lcm_notused: list[list[Connectors]] = [
            [Connectors.NOTUSED] * 15,
        ] * 15

        self.mock_lcm_andd: list[list[Connectors]] = [
            [Connectors.ANDD] * 15,
        ] * 15

        self.mock_puv_false: list[bool] = [False] * 15

        self.mock_puv_true: list[bool] = [True] * 15

    # Decide tests (integration)
    # TODO: Refactor decide.py so that we can inject cmv data for integration testing.
    # At the moment, it's extremely difficult to mock the points and parameters to fully verify the CMV LICs.
    # However, every child component is thoroughly tested so we should be fine for now.
    def test_decision_should_return_true_if_lcm_is_all_notused(self):
        decision = decide(
            len(self.mock_points),
            self.mock_points,
            self.mock_params,
            self.mock_lcm_notused,  # LCM disabled, bypassing the final decision
            self.mock_puv_true,  # PUV enabled
        )
        self.assertTrue(decision.launch)

    def test_decision_should_return_return_true_if_puv_is_all_false(self):
        decision = decide(
            len(self.mock_points),
            self.mock_points,
            self.mock_params,
            self.mock_lcm_andd,  # LCM enabled
            self.mock_puv_false,  # PUV disabled, bypassing the final decision
        )
        self.assertTrue(decision.launch)

    def test_decision_should_return_false_if_puv_and_lcm_are_in_use(self):
        decision = decide(
            len(self.mock_points),
            self.mock_points,
            self.mock_params,
            self.mock_lcm_andd,  # LCM enabled, checking for ANDD
            self.mock_puv_true,  # PUV enabled, validating the decision
        )
        self.assertFalse(decision.launch)

    # determine_launch tests (unit)
    def test_should_launch_if_fuv_is_all_true(self):
        some_fuv = [True] * 15
        launch = determine_launch(some_fuv)
        self.assertEqual(launch, True)

    def test_should_not_launch_if_fuv_has_some_false(self):
        some_fuv = [True] * 15
        some_fuv[6] = False
        launch = determine_launch(some_fuv)
        self.assertEqual(launch, False)

    def test_should_not_launch_if_fuv_is_all_false(self):
        some_fuv = [False] * 15
        launch = determine_launch(some_fuv)
        self.assertEqual(launch, False)


if __name__ == "__main__":
    unittest.main()
