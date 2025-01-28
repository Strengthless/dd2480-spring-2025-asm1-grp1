import unittest
from main import parse_input
from modules.decide import determine_launch
from modules.pum import get_pum
from modules.types import Connectors
from modules.cmv import *
from snapshottest import TestCase


class MainTests(TestCase):
    def test_should_parse_correctly(self):
        output = parse_input("test_valid.txt")
        self.assertMatchSnapshot(output, "Correct inputs should be parsed correctly.")

    def test_should_raise_error_if_numpoints_lt_2(self):
        self.assertRaises(ValueError, parse_input, "test_invalid_numpoints_1.txt")

    def test_should_raise_error_if_numpoints_gt_100(self):
        self.assertRaises(ValueError, parse_input, "test_invalid_numpoints_2.txt")

    def test_should_raise_error_if_numpoints_not_int(self):
        self.assertRaises(TypeError, parse_input, "test_invalid_numpoints_3.txt")

    def test_should_raise_error_if_numpoints_not_provided(self):
        self.assertRaises(TypeError, parse_input, "test_invalid_numpoints_4.txt")

    def test_should_raise_error_if_point_has_invalid_type(self):
        self.assertRaises(TypeError, parse_input, "test_invalid_points_1.txt")

    def test_should_raise_error_if_point_has_invalid_length(self):
        self.assertRaises(ValueError, parse_input, "test_invalid_points_2.txt")

    def test_should_raise_error_if_points_mismatch_numpoints(self):
        self.assertRaises(ValueError, parse_input, "test_invalid_points_3.txt")

    def test_should_raise_error_if_params_neq_19(self):
        self.assertRaises(ValueError, parse_input, "test_invalid_params_1.txt")

    def test_should_raise_error_if_params_have_invalid_types(self):
        self.assertRaises(TypeError, parse_input, "test_invalid_params_2.txt")

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

    def test_lic_6_should_fail_if_points_are_close_to_line(self):
        parameters = {"dist": 1, "n_pts": 3}
        points = [
            {"x": 0, "y": 0},
            {"x": 1, "y": 1},
            {"x": 4, "y": 0},
            {"x": 5, "y": 1},
        ]
        num_points = len(points)
        self.assertFalse(
            check_lic_6(num_points, points, parameters),
            "LIC 6: Points that are compared with dist will be close to the two created lines",
        )

    def test_lic_6_should_pass_if_points_are_far_away_from_line(self):
        parameters = {"dist": 2, "n_pts": 3}
        points = [{"x": 0, "y": 0}, {"x": 2, "y": 4}, {"x": 4, "y": 0}]
        num_points = len(points)
        self.assertTrue(
            check_lic_6(num_points, points, parameters),
            "LIC 6: The point compared with dist will be far away from the line",
        )

    def test_lic_6_should_pass_if_point_is_far_away_from_line_point(self):
        parameters = {"dist": 2, "n_pts": 3}
        points = [{"x": 0, "y": 0}, {"x": 2, "y": 2}, {"x": 0, "y": 0}]
        num_points = len(points)
        self.assertTrue(
            check_lic_6(num_points, points, parameters),
            "LIC 6: The point compared with dist will be far away from the line-point, the two points for the line are the same",
        )

    def test_lic_6_should_fail_if_input_is_illegal(self):
        parameters = {"dist": -4, "n_pts": 2}
        points = [{"x": 0, "y": 0}, {"x": 2, "y": 2}]
        num_points = len(points)
        self.assertFalse(
            check_lic_6(num_points, points, parameters), "LIC 6: Illegal input"
        )

    def test_lic_10_should_pass_if_area_gt_area1(self):
        parameters = {"area1": 1, "e_pts": 3, "f_pts": 4}
        points_1 = [
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
        self.assertTrue(check_lic_10(points_1, parameters))

    def test_lic_10_should_fail_if_area_lte_area1(self):
        parameters = {"area1": 2, "e_pts": 3, "f_pts": 4}
        points_1 = [
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
        self.assertTrue(check_lic_10(points_1, parameters))

    def test_lic_10_should_raise_error_if_epts_is_invalid(self):
        with self.assertRaises(ValueError):
            points_1 = [
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
            ]
            parameters = {"area1": 2, "e_pts": 0, "f_pts": 4}
            check_lic_10(points_1, parameters)

    def test_lic_10_should_raise_error_if_fpts_is_invalid(self):
        with self.assertRaises(ValueError):
            points_1 = [
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
            ]
            parameters = {"area1": 2, "e_pts": 3, "f_pts": 0}
            check_lic_10(points_1, parameters)

    def test_lic_10_should_raise_error_if_epts_fpts_and_points_mismatch(self):
        with self.assertRaises(ValueError):
            points_1 = [
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
                {"x": 0, "y": 0},
            ]
            parameters = {"area1": 2, "e_pts": 8, "f_pts": 4}
            check_lic_10(points_1, parameters)


class FUVTest(unittest.TestCase):
    # TODO: Add actual tests here
    def test_something(self):
        self.assertEqual("foo".upper(), "FOO")


class PUMTest(unittest.TestCase):
    def test_pum_should_be_true_if_all_lcm_are_notused(self):
        lcm = [[Connectors.NOTUSED] * 15] * 15
        cmv = [False] * 15
        pum = get_pum(cmv=cmv, lcm=lcm)
        self.assertEqual(pum, [[True] * 15] * 15)

    def test_pum_pattern_for_lcm_all_or_and_single_cmv_true(self):
        lcm = [[Connectors.ORR] * 15] * 15
        cmv = [False] * 15
        cmv[2] = True
        pum = get_pum(cmv=cmv, lcm=lcm)
        expectedResult = [
            [(i == 2 or j == 2 or i == j) for j in range(15)] for i in range(15)
        ]
        self.assertEqual(pum, expectedResult)

    def test_pum_pattern_for_lcm_all_and_and_single_cmv_true(self):
        lcm = [[Connectors.ANDD] * 15] * 15
        cmv = [False] * 15
        cmv[2] = True
        pum = get_pum(cmv=cmv, lcm=lcm)
        expectedResult = [[(i == j) for j in range(15)] for i in range(15)]
        self.assertEqual(pum, expectedResult)


if __name__ == "__main__":
    unittest.main()
