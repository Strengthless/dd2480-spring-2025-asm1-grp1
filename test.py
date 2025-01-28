import unittest

import unittest.test
from main import parse_input
from modules.decide import determine_launch
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

    # LIC 10 test cases
    def test_lic_10_should_pass_if_area_gt_area1(self):
        parameters = {"area1": 1, "e_pts": 3, "f_pts": 4}
        mock_points = self.mock_points_c1
        num_points = len(mock_points)
        self.assertTrue(cmv.check_lic_10(num_points, mock_points, parameters))

    def test_lic_10_should_fail_if_area_lte_area1(self):
        parameters = {"area1": 2, "e_pts": 3, "f_pts": 4}
        mock_points = self.mock_points_c1
        num_points = len(mock_points)
        self.assertTrue(cmv.check_lic_10(num_points, mock_points, parameters))

    def test_lic_10_should_raise_error_if_epts_is_invalid(self):
        with self.assertRaises(ValueError):
            parameters = {"area1": 2, "e_pts": 0, "f_pts": 4}
            mock_points = self.mock_points_c2
            num_points = len(mock_points)
            cmv.check_lic_10(num_points, mock_points, parameters)

    def test_lic_10_should_raise_error_if_fpts_is_invalid(self):
        with self.assertRaises(ValueError):
            parameters = {"area1": 2, "e_pts": 3, "f_pts": 0}
            mock_points = self.mock_points_c2
            num_points = len(mock_points)
            cmv.check_lic_10(num_points, mock_points, parameters)

    def test_lic_10_should_raise_error_if_epts_fpts_and_points_mismatch(self):
        with self.assertRaises(ValueError):
            parameters = {"area1": 2, "e_pts": 8, "f_pts": 4}
            mock_points = self.mock_points_c2
            num_points = len(mock_points)
            cmv.check_lic_10(num_points, mock_points, parameters)

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
        with self.assertRaises(ValueError):
            parameters = {"g_pts": 5}
            points = [
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
            ]
            num_points = len(points)
            cmv.check_lic_11(num_points, points, parameters)

    # LIC 12 test cases
    def test_lic_12_should_pass_if_length_gt_length1_lt_length2(self):
        parameters = {"k_pts": 3, "length1": 5, "length2": 3}
        points = [
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 6},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
        ]  # True
        num_points = len(points)
        self.assertTrue(cmv.check_lic_12(num_points, points, parameters))

    def test_lic_12_should_fail_if_length_lt_length1_gt_length2(self):
        parameters = {"k_pts": 3, "length1": 5, "length2": 3}
        points = [
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 4},
            {"x": 0, "y": 0},
            {"x": 3, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
        ]  # False
        num_points = len(points)
        self.assertFalse(cmv.check_lic_12(num_points, points, parameters))

    def test_lic_12_should_fail_if_length2_lt_0(self):
        points = [
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
        ]
        parameters = {"k_pts": 3, "length1": 5, "length2": -1}
        num_points = len(points)
        self.assertFalse(cmv.check_lic_12(num_points, points, parameters))

    def test_lic_12_should_fail_if_num_points_lt_3(self):
        parameters = {"k_pts": 3, "length1": 5, "length2": 3}
        points = [{"x": 0, "y": 0}, {"x": 0, "y": 0}]  # False
        num_points = len(points)
        self.assertFalse(cmv.check_lic_12(num_points, points, parameters))


class FUVTest(unittest.TestCase):
    # TODO: Add actual tests here
    def test_something(self):
        self.assertEqual("foo".upper(), "FOO")


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
