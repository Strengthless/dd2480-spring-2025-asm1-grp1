import numpy as np
import unittest
from snapshottest import TestCase
from src.main import parse_input
from src.modules import cmv
from src.modules.decide import determine_launch
from src.modules.fuv import get_fuv
from src.modules.pum import get_pum
from src.modules.types import Comp_Type, Connectors, Coordinate
from src.modules.utils import (
    can_three_np_points_fit_in_a_circle,
    convert_to_np_point,
    float_compare,
    float_gte,
    float_lte,
    get_angle_from_np_points,
    get_distance_between_np_points,
    get_triangle_area_from_np_points,
    np_points_equal,
)


class CMVTests(unittest.TestCase):
    def setUp(self):
        # Factory method to create mock points
        self.mutate_points = lambda base_points, mutations: [
            mutations.get(i, base_points[i]) for i in range(len(base_points))
        ]

        self.duplicate_points = lambda base_point, n: [base_point for _ in range(n)]

        self.create_zero_points = lambda n: self.duplicate_points({"x": 0, "y": 0}, n)

        # Test fixtures, with sections A (0-4), B (5-9) and C (10-14).
        # Section A
        self.mock_points_a1: list[Coordinate] = [
            {"x": 1.0, "y": 2.0},
            {"x": 1.5, "y": 4.5},
            {"x": -1.2, "y": 0.0},
        ]

        self.mock_points_a2: list[Coordinate] = [
            {"x": 0.0, "y": 2.0},
            {"x": -1.0, "y": 1.0},
            {"x": -1.0, "y": -1.0},
            {"x": 2.0, "y": -1.0},
            {"x": -3.0, "y": -6.0},
            {"x": -2.0, "y": 2.0},
        ]

        self.mock_points_a3: list[Coordinate] = [
            {"x": 0.0, "y": 1.0},
            {"x": 1.0, "y": 0.0},
            {"x": 0.0, "y": 0.0},
            {"x": 3, "y": 1},
        ]

        self.mock_points_a4: list[Coordinate] = [
            {"x": 0.0, "y": 2.0},
            {"x": 2.0, "y": 0.0},
            {"x": 0.0, "y": 0.0},
            {"x": 0.0, "y": 0.0},
        ]

        self.mock_points_a5: list[Coordinate] = [
            {"x": 0.0, "y": 2.0},
            {"x": 0.0, "y": 0.0},
            {"x": -1.0, "y": 0.0},
            {"x": 1.0, "y": -1.0},
            {"x": 1.0, "y": 1.0},
        ]

        self.mock_points_a6: list[Coordinate] = [
            {"x": 0.0, "y": 2.0},
            {"x": -1.0, "y": -1.0},
            {"x": -1.0, "y": 0.0},
            {"x": 2.0, "y": 1.0},
            {"x": -3.0, "y": -6.0},
            {"x": -2.0, "y": 2.0},
        ]

        # Section B
        self.mock_points_b1: list[Coordinate] = [
            {"x": 0, "y": 1},
            {"x": 1, "y": 1},
            {"x": 2, "y": 1},
            {"x": 3, "y": 1},
        ]

        self.mock_points_b2: list[Coordinate] = [
            {"x": 6, "y": 5},
            {"x": 2, "y": 4},
            {"x": 5, "y": 1},
            {"x": 10, "y": 13},
            {"x": 2, "y": 5},
            {"x": 3, "y": 5},
        ]

        self.mock_points_b3: list[Coordinate] = [
            {"x": 0, "y": 0},
            {"x": 2, "y": 4},
            {"x": 6, "y": 0},
            {"x": 10, "y": 13},
            {"x": 2, "y": 5},
            {"x": 0, "y": 8},
        ]

        self.mock_points_b4: list[Coordinate] = [
            {"x": 6, "y": 5},
            {"x": 2, "y": 4},
            {"x": 5, "y": 1},
            {"x": 10, "y": 13},
            {"x": 2, "y": 5},
            {"x": 3, "y": 5},
        ]

        self.mock_points_b5: list[Coordinate] = [
            {"x": 1, "y": 1},
            {"x": 2, "y": 2},
            {"x": 3, "y": 3},
            {"x": 5, "y": 5},
            {"x": 10, "y": 10},
        ]

        self.mock_points_b6: list[Coordinate] = [
            {"x": 5, "y": 2},
            {"x": 8, "y": 6},
            {"x": 3, "y": -2},
            {"x": 2, "y": 2},
            {"x": 1, "y": 3},
            {"x": 1, "y": 2},
            {"x": 2, "y": 2},
            {"x": 2, "y": 1},
            {"x": 1, "y": 2},
            {"x": 5, "y": 2},
        ]

        self.mock_points_b7: list[Coordinate] = [
            {"x": 0, "y": 1},
            {"x": 5, "y": 2},
            {"x": 1, "y": 1},
            {"x": 2, "y": 5},
            {"x": 2, "y": 1},
        ]

        self.mock_points_b8: list[Coordinate] = [
            {"x": 1, "y": 0},
            {"x": 5, "y": 2},
            {"x": 1, "y": 0},
            {"x": 2, "y": 5},
            {"x": 1, "y": 0},
        ]

        self.mock_points_b9: list[Coordinate] = [
            {"x": 0, "y": 0},
            {"x": 1, "y": 1},
            {"x": 4, "y": 0},
            {"x": 5, "y": 1},
        ]

        self.mock_points_b10: list[Coordinate] = [
            {"x": 1, "y": 2},
            {"x": 2, "y": 2},
            {"x": 1, "y": 2},
            {"x": 1, "y": 2},
        ]

        self.mock_points_b11: list[Coordinate] = [
            {"x": 2, "y": 2},
            {"x": 2, "y": 2},
            {"x": 1, "y": 2},
            {"x": 5, "y": 5},
        ]

        # Section C
        self.mock_points_c1: list[Coordinate] = self.mutate_points(
            self.create_zero_points(12),
            {6: {"x": 3, "y": 0}, 11: {"x": 3, "y": 3}},
        )

        self.mock_points_c2: list[Coordinate] = self.create_zero_points(12)

        self.mock_points_c3: list[Coordinate] = self.mutate_points(
            self.create_zero_points(6), {0: {"x": 5, "y": 0}, 3: {"x": 3, "y": 0}}
        )

        self.mock_points_c4 = self.mutate_points(
            self.create_zero_points(8),
            {1: {"x": 1, "y": 0}, 4: {"x": 5, "y": 0}, 7: {"x": 10, "y": 0}},
        )

        self.mock_points_c5 = self.mutate_points(
            self.create_zero_points(12), {3: {"x": 0, "y": 6}}
        )

        self.mock_points_c6 = self.mutate_points(
            self.create_zero_points(12), {3: {"x": 0, "y": 4}, 5: {"x": 3, "y": 0}}
        )

        self.mock_points_c7 = self.mutate_points(
            self.create_zero_points(12), {3: {"x": 0, "y": 6}}
        )

        self.mock_points_c8 = self.mutate_points(
            self.create_zero_points(12), {3: {"x": 0, "y": 3}, 7: {"x": 4, "y": 0}}
        )

        self.mock_points_c9 = self.mutate_points(
            self.create_zero_points(9),
            {
                1: {"x": 0, "y": 10},
                3: {"x": 0, "y": 3},
                7: {"x": 4, "y": 0},
                8: {"x": 4, "y": 0},
            },
        )

        self.mock_points_c10 = self.mutate_points(
            self.create_zero_points(12), {3: {"x": 0, "y": 10}, 6: {"x": 10, "y": 0}}
        )

        self.mock_points_c11 = self.mutate_points(
            self.create_zero_points(12), {8: {"x": 2.5, "y": 0}, 11: {"x": 0, "y": 2}}
        )

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
        points: list[Coordinate] = [{"x": 1.0, "y": 2.0}]
        num_points = len(points)
        self.assertFalse(cmv.check_lic_0(num_points, points, params))

    # LIC 3 test cases
    def test_lic_3_should_fail_if_area_pts_less_than_param(self):
        params = {"area1": 0.6}
        points = self.mock_points_a3
        num_points = len(points)
        self.assertFalse(
            cmv.check_lic_3(num_points, points, params),
            "LIC 3: Area1 is greater than area from points",
        )

    def test_lic_3_should_pass_if_area_pts_greater_than_param(self):
        params = {"area1": 1.9}
        points = self.mock_points_a4
        num_points = len(points)
        self.assertTrue(
            cmv.check_lic_3(num_points, points, params),
            "LIC 3: Area1 is less than area from points",
        )

    def test_lic_3_should_fail_if_not_enough_points(self):
        params = {"area1": 1.9}
        points = [{"x": 0.0, "y": 2.0}, {"x": 2.0, "y": 0.0}]
        num_points = len(points)
        self.assertFalse(
            cmv.check_lic_3(num_points, points, params),
            "LIC 3: Not enough coordinates",
        )

    # LIC 4 test cases
    def test_lic_4_should_pass_if_nr_quads_gt_param_quads(self):
        params = {"quads": 2, "q_pts": 3}
        points: list[Coordinate] = self.mock_points_a5
        num_points = len(points)
        self.assertTrue(cmv.check_lic_4(num_points, points, params))

    def test_lic_4_should_fail_if_nr_quads_lt_param_quads(self):
        params = {"quads": 3, "q_pts": 5}
        points: list[Coordinate] = self.mock_points_a6
        num_points = len(points)
        self.assertFalse(
            cmv.check_lic_4(num_points, points, params),
            "LIC 4: Returns False as pts in 3 quads, not 4",
        )

    def test_lic_4_should_fail_if_quads_invalid(self):
        params = {"quads": 4, "q_pts": 5}
        points: list[Coordinate] = self.mock_points_a2
        num_points = len(points)
        self.assertFalse(
            cmv.check_lic_4(num_points, points, params),
            "LIC 4: Returns False as QUADS greater than 3",
        )

    def test_lic_4_should_fail_if_q_pts_invalid(self):
        params = {"quads": 4, "q_pts": 1}
        points: list[Coordinate] = self.mock_points_a2
        num_points = len(points)
        self.assertFalse(
            cmv.check_lic_4(num_points, points, params),
            "LIC 4: Returns False as q_pts are less than 2",
        )

    # LIC 5 test cases
    def test_lic_5_should_fail_if_points_are_increasingly_far(self):
        points = self.mock_points_b1
        self.assertFalse(
            cmv.check_lic_5(points), "LIC 5: Points are increasingly far away (x1 > x2)"
        )

    def test_lic_5_should_pass_if_points_are_increasingly_close(self):
        points = sorted(self.mock_points_b1, key=lambda p: p["x"], reverse=True)
        self.assertTrue(
            cmv.check_lic_5(points), "LIC 5: Points are increasingly close (x1 < x2)"
        )

    def test_lic_5_should_fail_if_points_have_the_same_coordinates(self):
        points = self.duplicate_points({"x": 1, "y": 1}, 4)
        self.assertFalse(
            cmv.check_lic_5(points), "LIC 5: Points are the same (x1 = x2)"
        )

    # LIC 6 test cases
    def test_lic_6_should_fail_if_points_are_close_to_line(self):
        parameters = {"dist": 1, "n_pts": 3}
        points = self.mock_points_b9
        num_points = len(points)
        self.assertFalse(
            cmv.check_lic_6(num_points, points, parameters),
            "LIC 6: Points that are compared with dist will be close to the two created lines",
        )

    def test_lic_6_should_pass_if_points_are_far_away_from_line(self):
        parameters = {"dist": 2, "n_pts": 3}
        points = [{"x": 0, "y": 0}, {"x": 2, "y": 4}, {"x": 4, "y": 0}]
        num_points = len(points)
        self.assertTrue(
            cmv.check_lic_6(num_points, points, parameters),
            "LIC 6: The point compared with dist will be far away from the line",
        )

    def test_lic_6_should_pass_if_point_is_far_away_from_line_point(self):
        parameters = {"dist": 2, "n_pts": 3}
        points = [{"x": 0, "y": 0}, {"x": 2, "y": 2}, {"x": 0, "y": 0}]
        num_points = len(points)
        self.assertTrue(
            cmv.check_lic_6(num_points, points, parameters),
            "LIC 6: The point compared with dist will be far away from the line-point, the two points for the line are the same",
        )

    def test_lic_6_should_fail_if_input_is_illegal(self):
        parameters = {"dist": -4, "n_pts": 2}
        points = [{"x": 0, "y": 0}, {"x": 2, "y": 2}]
        num_points = len(points)
        self.assertFalse(
            cmv.check_lic_6(num_points, points, parameters), "LIC 6: Illegal input"
        )

    # LIC 7 test cases
    def test_lic_7_invalid_input(self):
        parameters = {"k_pts": 0, "length1": -5}
        points = self.duplicate_points({"x": 1, "y": 2}, 4)
        num_points = len(points)

        self.assertFalse(
            cmv.check_lic_7(num_points, points, parameters),
            "LIC 7: invalid input (k_pts < 1 & negative length)",
        )

    def test_lic_7_should_fail_if_distance_is_not_enough(self):
        parameters = {"k_pts": 1, "length1": 5}
        points = self.mock_points_b10
        num_points = len(points)

        self.assertFalse(
            cmv.check_lic_7(num_points, points, parameters),
            "LIC 7: distance between two points <= length1",
        )

    def test_lic_7_should_pass_if_distance_is_enough(self):
        parameters = {"k_pts": 1, "length1": 3}
        points = self.mock_points_b11
        num_points = len(points)

        self.assertTrue(
            cmv.check_lic_7(num_points, points, parameters),
            "LIC 7: distance between two points > length1",
        )

    # LIC 8 test cases
    def test_lic_8_should_pass_if_obtuse_triangles_are_considered(self):
        parameters = {"a_pts": 1, "b_pts": 1, "radius1": 10}
        points = self.mock_points_b2
        num_points = len(points)

        self.assertFalse(
            cmv.check_lic_8(num_points, points, parameters),
            "LIC 8: Obtuse triangle",
        )

    def test_lic_8_should_fail_if_radius1_is_greater_than_triangle_circumcircle(self):
        parameters = {"a_pts": 1, "b_pts": 1, "radius1": 15}
        points = self.mutate_points(self.mock_points_b2, {5: {"x": 3, "y": 10}})
        num_points = len(points)

        self.assertFalse(
            cmv.check_lic_8(num_points, points, parameters),
            "LIC 8: Radius1 > circumcircle radius",
        )

    def test_lic_8_should_fail_if_radius1_equals_triangle_circumcircle(self):
        parameters = {"a_pts": 1, "b_pts": 2, "radius1": 5}
        points = self.mock_points_b3
        num_points = len(points)

        self.assertFalse(
            cmv.check_lic_8(num_points, points, parameters),
            "LIC 8: Radius1 == circumcircle radius",
        )

    def test_lic_8_should_pass_if_radius1_is_less_than_triangle_circumcircle(self):
        parameters = {"a_pts": 2, "b_pts": 1, "radius1": 4}
        points = self.mock_points_b4
        num_points = len(points)

        self.assertTrue(
            cmv.check_lic_8(num_points, points, parameters),
            "LIC 8: Radius1 < circumcircle radius",
        )

    def test_lic_8_should_fail_if_input_is_illegal(self):
        parameters = {"a_pts": 0.5, "b_pts": 10, "radius1": -5}
        points = [{"x": 1, "y": 1}]
        num_points = len(points)

        self.assertFalse(
            cmv.check_lic_8(num_points, points, parameters),
            "LIC 8: Illegal input",
        )

    def test_lic_8_should_fail_if_points_are_identical(self):
        parameters = {"a_pts": 2, "b_pts": 2, "radius1": 1}
        points = self.duplicate_points({"x": 1, "y": 1}, 8)
        num_points = len(points)

        self.assertFalse(
            cmv.check_lic_8(num_points, points, parameters),
            "LIC 8: Identical points",
        )

    def test_lic_8_should_pass_if_colinear_are_regarded(self):
        parameters = {"a_pts": 1, "b_pts": 1, "radius1": 4}
        points = self.mock_points_b5
        num_points = len(points)

        self.assertTrue(
            cmv.check_lic_8(num_points, points, parameters),
            "LIC 8: Colinear points are regarded as a triangle",
        )

    # LIC 9 test cases
    def test_lic9_should_pass_if_valid_angle_exists(self):
        parameters = {"c_pts": 2, "d_pts": 2, "epsilon": 0.1}
        points = self.mock_points_b6
        num_points = len(points)

        self.assertTrue(
            cmv.check_lic_9(num_points, points, parameters), "LIC9: valid angle exists."
        )

    def test_lic9_should_fail_if_no_valid_angle_exists(self):
        parameters = {"c_pts": 1, "d_pts": 1, "epsilon": 0.1}
        points = self.mock_points_b7
        num_points = len(points)

        self.assertFalse(
            cmv.check_lic_9(num_points, points, parameters),
            "LIC9: no valid angle exists.",
        )

    def test_lic9_should_fail_if_all_points_coincide(self):
        parameters = {"c_pts": 1, "d_pts": 1, "epsilon": 0.1}
        points = self.mock_points_b8
        num_points = len(points)

        self.assertFalse(
            cmv.check_lic_9(num_points, points, parameters),
            "LIC9: all points coincide with the vertex.",
        )

    def test_lic9_should_fail_if_input_is_illegal(self):
        parameters = {"c_pts": 0, "d_pts": -3, "epsilon": 0.1}
        points = self.mock_points_b8
        num_points = len(points)

        self.assertFalse(
            cmv.check_lic_9(num_points, points, parameters), "LIC9: illegal input"
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
        points = self.mock_points_c3
        num_points = len(points)
        self.assertTrue(
            cmv.check_lic_11(num_points, points, parameters),
            "There exists some two points that are 2 units apart, such that point 2 < point 1.",
        )

    def test_lic_11_should_fail_if_sub_gt_0(self):
        parameters = {"g_pts": 2}
        points = self.mock_points_c4
        num_points = len(points)
        self.assertFalse(
            cmv.check_lic_11(num_points, points, parameters),
            "For all pairs of points that are 2 units apart, point 2 >= point 1.",
        )

    def test_lic_11_should_raise_error_if_gpts_and_points_mismatch(self):
        parameters = {"g_pts": 5}
        points = self.create_zero_points(7)
        num_points = len(points)
        self.assertFalse(
            cmv.check_lic_11(num_points, points, parameters),
            "LIC returns false because g_pts (5) > num_points - 2 (4).",
        )

    # LIC 12 test cases
    def test_lic_12_should_pass_if_length_gt_length1_lt_length2(self):
        parameters = {"k_pts": 3, "length1": 5, "length2": 3}
        points = self.mock_points_c5
        num_points = len(points)
        self.assertTrue(cmv.check_lic_12(num_points, points, parameters))

    def test_lic_12_should_fail_if_length_lt_length1_gt_length2(self):
        parameters = {"k_pts": 3, "length1": 5, "length2": 3}
        points = self.mock_points_c6
        num_points = len(points)
        self.assertFalse(cmv.check_lic_12(num_points, points, parameters))

    def test_lic_12_should_fail_if_length2_lt_0(self):
        points = self.mock_points_c7
        parameters = {"k_pts": 3, "length1": 5, "length2": -1}
        num_points = len(points)
        self.assertFalse(cmv.check_lic_12(num_points, points, parameters))

    def test_lic_12_should_fail_if_num_points_lt_3(self):
        parameters = {"k_pts": 3, "length1": 5, "length2": 3}
        points = self.create_zero_points(2)
        num_points = len(points)
        self.assertFalse(cmv.check_lic_12(num_points, points, parameters))

    # LIC 13 test cases
    def test_lic_13_should_pass_if_radius_gt_radius1_lt_radius2(self):
        parameters = {"a_pts": 2, "b_pts": 3, "radius1": 2, "radius2": 2.4}
        points = self.mock_points_c8
        num_points = len(points)
        self.assertTrue(cmv.check_lic_13(num_points, points, parameters))

    def test_lic_13_should_fail_if_radius_lt_radius1_gt_radius2(self):
        parameters = {"a_pts": 2, "b_pts": 3, "radius1": 2, "radius2": 2.4}
        points = self.mock_points_c9
        num_points = len(points)
        self.assertFalse(cmv.check_lic_13(num_points, points, parameters))

    def test_lic_13_should_fail_if_radius2_lt_0(self):
        parameters = {"a_pts": 2, "b_pts": 3, "radius1": 2, "radius2": -1}
        points = self.mock_points_c8
        num_points = len(points)
        self.assertFalse(cmv.check_lic_13(num_points, points, parameters))

    def test_lic_13_should_fail_if_num_points_lt_5(self):
        parameters = {"a_pts": 2, "b_pts": 3, "radius1": 2, "radius2": 2.4}
        points = self.create_zero_points(3)
        num_points = len(points)
        self.assertFalse(cmv.check_lic_13(num_points, points, parameters))

    # LIC 14 test cases
    def test_lic_14_should_pass_if_area_gt_area1_lt_area2(self):
        parameters = {"area1": 3, "area2": 2, "e_pts": 2, "f_pts": 2}
        points = self.mock_points_c10
        num_points = len(points)
        self.assertTrue(cmv.check_lic_14(num_points, points, parameters))

    def test_lic_14_should_fail_if_area_lt_area1_gt_area2(self):
        parameters = {"area1": 3, "area2": 2, "e_pts": 2, "f_pts": 2}
        points = self.mock_points_c11
        num_points = len(points)
        self.assertFalse(cmv.check_lic_14(num_points, points, parameters))

    def test_lic_14_should_fail_if_area2_lt_0(self):
        parameters = {"area1": 3, "area2": -1, "e_pts": 2, "f_pts": 2}
        points = self.mock_points_c10
        num_points = len(points)
        self.assertFalse(cmv.check_lic_14(num_points, points, parameters))

    def test_lic_14_should_fail_if_num_points_lt_5(self):
        parameters = {"area1": 3, "area2": 2, "e_pts": 2, "f_pts": 2}
        points = self.create_zero_points(2)
        num_points = len(points)
        self.assertFalse(cmv.check_lic_14(num_points, points, parameters))


if __name__ == "__main__":
    unittest.main()
