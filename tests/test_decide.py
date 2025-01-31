import unittest
from src.modules.decide import decide, determine_launch


class DecideTests(unittest.TestCase):
    # TODO: Refactor decide.py so that we can inject cmv data for integration testing.
    # At the moment, it's extremely difficult to mock the points and parameters for all LICs to pass.
    # However, every child component is thoroughly tested so we should be fine for now.

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
