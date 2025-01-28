import unittest
from main import parse_input
from modules.decide import determine_launch
from modules.fuv import get_fuv
from modules.pum import get_pum
from modules.types import Connectors, Coordinate
from snapshottest import TestCase
import modules.cmv as cmv


class MainTests(TestCase):
    def test_should_parse_correctly(self):
        output = parse_input("test_valid.txt")
        self.assertMatchSnapshot(output, "Correct inputs should be parsed correctly.")

    def test_should_raise_error_if_numpoints_lt_2(self):
        self.assertRaises(ValueError, parse_input, "test_invalid_numpoints_1.txt")

    def test_should_raise_error_if_numpoints_gt_100(self):
        self.assertRaises(ValueError, parse_input, "test_invalid_numpoints_2.txt")

    def test_should_raise_error_if_numpoints_not_int(self):
        self.assertRaises(ValueError, parse_input, "test_invalid_numpoints_3.txt")

    def test_should_raise_error_if_numpoints_not_provided(self):
        self.assertRaises(ValueError, parse_input, "test_invalid_numpoints_4.txt")

    def test_should_raise_error_if_point_has_invalid_type(self):
        self.assertRaises(ValueError, parse_input, "test_invalid_points_1.txt")

    def test_should_raise_error_if_point_has_invalid_length(self):
        self.assertRaises(ValueError, parse_input, "test_invalid_points_2.txt")

    def test_should_raise_error_if_points_mismatch_numpoints(self):
        self.assertRaises(ValueError, parse_input, "test_invalid_points_3.txt")

    def test_should_raise_error_if_params_neq_19(self):
        self.assertRaises(ValueError, parse_input, "test_invalid_params_1.txt")

    def test_should_raise_error_if_params_have_invalid_types(self):
        self.assertRaises(ValueError, parse_input, "test_invalid_params_2.txt")

    def test_should_raise_error_if_lcm_has_invalid_types(self):
        self.assertRaises(TypeError, parse_input, "test_invalid_lcm_1.txt")

    def test_should_raise_error_if_lcm_has_invalid_size(self):
        self.assertRaises(ValueError, parse_input, "test_invalid_lcm_2.txt")

    def test_should_raise_error_if_puv_has_invalid_length(self):
        self.assertRaises(ValueError, parse_input, "test_invalid_puv_1.txt")

    def test_should_raise_error_if_puv_has_invalid_types(self):
        self.assertRaises(TypeError, parse_input, "test_invalid_puv_2.txt")


class DecideTests(unittest.TestCase):
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


class CMVTests(unittest.TestCase):
    # Test fixtures, with sections A (0-4), B (5-9) and C (10-14).
    def setUp(self):
        # Longest distance between points is 5.24
        self.mock_points_a1: list[Coordinate] = [
            {"x": 1.0, "y": 2.0},
            {"x": 1.5, "y": 4.5},
            {"x": -1.2, "y": 0.0},
        ]

        self.mock_points_c1: list[Coordinate] = [
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 3, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 3, "y": 3},
        ]

        self.mock_points_c2: list[Coordinate] = [
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
        ]

    # LIC 0 test cases
    def test_lic_0_should_fail_if_no_distance_greater_than_length1(self):
        params = {"length1": 5.3}
        points = self.mock_points_a1
        num_points = len(points)

        self.assertFalse(cmv.check_lic_0(num_points, points, params))

    def test_lic_0_should_pass_if_point_distance_less_than_length1(self):
        params = {"length1": 5.1}
        points = self.mock_points_a1
        num_points = len(points)

        self.assertTrue(cmv.check_lic_0(num_points, points, params))

    def test_lic_0_should_fail_if_length1_is_0(self):
        params = {"length1": 0}
        points = self.mock_points_a1
        num_points = len(points)

        self.assertFalse(cmv.check_lic_0(num_points, points, params))

    def test_lic_0_should_fail_if_num_points_less_than_2(self):
        params = {"length1": 0}
        points: list[Coordinate] = [
            {"x": 1.0, "y": 2.0},
        ]
        num_points = len(points)

        self.assertFalse(cmv.check_lic_0(num_points, points, params))

    def test_lic_7_invalid_input(self):
        parameters = {"k_pts": 0, "length1": -5}
        points = [
            {"x": 1, "y": 2},
            {"x": 1, "y": 2},
            {"x": 2, "y": 2},
        ]
        num_points = len(points)

        self.assertFalse(
            cmv.check_lic_7(num_points, points, parameters),
            "LIC 7: invalid input (k_pts < 1 & negative length)",
        )

    def test_lic_7_should_fail_if_distance_is_not_enough(self):
        parameters = {"k_pts": 1, "length1": 5}
        points = [
            {"x": 1, "y": 2},
            {"x": 2, "y": 2},
            {"x": 1, "y": 2},
            {"x": 1, "y": 2},
        ]
        num_points = len(points)

        self.assertFalse(
            cmv.check_lic_7(num_points, points, parameters),
            "LIC 7: distance between two points <= length1",
        )

    def test_lic_7_should_pass_if_distance_is_enough(self):
        parameters = {"k_pts": 1, "length1": 3}
        points = [
            {"x": 2, "y": 2},
            {"x": 2, "y": 2},
            {"x": 1, "y": 2},
            {"x": 5, "y": 5},
        ]
        num_points = len(points)

        self.assertTrue(
            cmv.check_lic_7(num_points, points, parameters),
            "LIC 7: distance between two points > length1",
        )

    # LIC 10 test cases
    def test_lic_10_should_pass_if_area_gt_area1(self):
        parameters = {"area1": 1, "e_pts": 3, "f_pts": 4}
        mock_points = self.mock_points_c1
        num_points = len(mock_points)
        self.assertTrue(cmv.check_lic_10(num_points, mock_points, parameters))

    def test_lic_10_should_fail_if_area_lte_area1(self):
        parameters = {"area1": 5, "e_pts": 3, "f_pts": 4}
        mock_points = self.mock_points_c1
        num_points = len(mock_points)
        self.assertFalse(cmv.check_lic_10(num_points, mock_points, parameters))

    def test_lic_10_should_fail_if_epts_is_invalid(self):
        parameters = {"area1": 2, "e_pts": 0, "f_pts": 4}
        mock_points = self.mock_points_c2
        num_points = len(mock_points)
        self.assertFalse(
            cmv.check_lic_10(num_points, mock_points, parameters),
            "LIC returns false because e_pts (0) < 1.",
        )

    def test_lic_10_should_fail_if_fpts_is_invalid(self):
        parameters = {"area1": 2, "e_pts": 3, "f_pts": 0}
        mock_points = self.mock_points_c2
        num_points = len(mock_points)
        self.assertFalse(
            cmv.check_lic_10(num_points, mock_points, parameters),
            "LIC returns false because f_pts (0) < 1.",
        )

    def test_lic_10_should_fail_if_epts_fpts_and_points_mismatch(self):
        parameters = {"area1": 2, "e_pts": 8, "f_pts": 4}
        mock_points = self.mock_points_c2
        num_points = len(mock_points)
        self.assertFalse(
            cmv.check_lic_10(num_points, mock_points, parameters),
            "LIC returns false because e_pts + f_pts (12) > num_points - 3 (3).",
        )

    # LIC 11 test cases
    def test_lic_11_should_pass_if_sub_lt_0(self):
        parameters = {"g_pts": 2}
        points = [
            {"x": 5, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 3, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
        ]
        num_points = len(points)
        self.assertTrue(
            cmv.check_lic_11(num_points, points, parameters),
            "There exists some two points that are 2 units apart, such that point 2 < point 1.",
        )

    def test_lic_11_should_fail_if_sub_gt_0(self):
        parameters = {"g_pts": 2}
        points = [
            {"x": 0, "y": 0},
            {"x": 1, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 5, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 10, "y": 0},
        ]
        num_points = len(points)
        self.assertFalse(
            cmv.check_lic_11(num_points, points, parameters),
            "For all pairs of points that are 2 units apart, point 2 >= point 1.",
        )

    def test_lic_11_should_raise_error_if_gpts_and_points_mismatch(self):
        parameters = {"g_pts": 5}
        points = [
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
        ]
        num_points = len(points)
        self.assertFalse(
            cmv.check_lic_11(num_points, points, parameters),
            "LIC returns false because g_pts (5) > num_points - 2 (4).",
        )


class FUVTest(unittest.TestCase):
    def test_fuv_should_be_true_if_all_puv_false(self):
        puv = [False] * 15
        pum = [[False] * 15 for _ in range(15)]
        fuv = get_fuv(pum=pum, puv=puv)
        expectedResult = [True] * 15
        self.assertEqual(fuv, expectedResult)

    def test_fuv_should_be_the_same_as_in_the_example_in_assignment(self):
        # generate test data
        puv = [True] * 15
        puv[1] = False
        pum_false_pos = [(1, 0), (0, 1), (0, 3), (3, 0)]
        fuv_false_pos = [0, 3]
        pum = [[(i, j) not in pum_false_pos for j in range(15)] for i in range(15)]
        expectedResult = [i not in fuv_false_pos for i in range(15)]

        # get fuv
        fuv = get_fuv(pum=pum, puv=puv)
        self.assertEqual(fuv, expectedResult)


class PUMTest(unittest.TestCase):
    def setUp(self):
        self.cmv_all_false = [False] * 15
        self.cmv_all_true = [True] * 15

        self.create_cmv_pattern = lambda base, *indices: [
            base[i] if i not in indices else not base[i] for i in range(15)
        ]

        self.lcm_all_orr = [[Connectors.ORR] * 15] * 15
        self.lcm_all_andd = [[Connectors.ANDD] * 15] * 15
        self.lcm_all_notused = [[Connectors.NOTUSED] * 15] * 15

    def test_pum_should_be_true_if_all_lcm_are_notused(self):
        lcm = self.lcm_all_notused
        cmv = self.cmv_all_false
        pum = get_pum(cmv, lcm)
        self.assertEqual(pum, [[True] * 15] * 15)

    def test_pum_pattern_for_lcm_all_or_and_single_cmv_true(self):
        lcm = self.lcm_all_orr
        cmv = self.create_cmv_pattern(self.cmv_all_false, 2)
        pum = get_pum(cmv, lcm)
        expectedResult = [
            [(i == 2 or j == 2 or i == j) for j in range(15)] for i in range(15)
        ]
        self.assertEqual(pum, expectedResult)

    def test_pum_pattern_for_lcm_all_and_and_single_cmv_true(self):
        lcm = self.lcm_all_andd
        cmv = self.create_cmv_pattern(self.cmv_all_false, 2)
        pum = get_pum(cmv, lcm)
        expectedResult = [[(i == j) for j in range(15)] for i in range(15)]
        self.assertEqual(pum, expectedResult)


if __name__ == "__main__":
    unittest.main()
