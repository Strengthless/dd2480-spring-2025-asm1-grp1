import numpy as np
import unittest
from src.modules.types import Comp_Type
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


class UtilsTests(unittest.TestCase):
    # float_compare tests
    def test_fc_should_handle_equal(self):
        self.assertEqual(float_compare(0.0, 0.0), Comp_Type.EQ)

    def test_fc_should_handle_lt(self):
        self.assertEqual(float_compare(0.0, 0.1), Comp_Type.LT)

    def test_fc_should_handle_gt(self):
        self.assertEqual(float_compare(0.1, 0.0), Comp_Type.GT)

    def test_fc_should_handle_epsilon(self):
        self.assertEqual(float_compare(0.0000001, 0.0), Comp_Type.EQ)

    # float_lte tests
    def test_flte_should_handle_equal(self):
        self.assertEqual(float_lte(0.0, 0.0), True)

    def test_flte_should_handle_gt(self):
        self.assertEqual(float_lte(0.1, 0.0), False)

    def test_flte_should_handle_lt(self):
        self.assertEqual(float_lte(0.0, 0.1), True)

    def test_flte_should_handle_epsilon(self):
        self.assertEqual(float_lte(0.0000001, 0.0), True)

    # float_gte tests
    def test_fgte_should_handle_equal(self):
        self.assertEqual(float_gte(0.0, 0.0), True)

    def test_fgte_should_handle_gt(self):
        self.assertEqual(float_gte(0.1, 0.0), True)

    def test_fgte_should_handle_lt(self):
        self.assertEqual(float_gte(0.0, 0.1), False)

    def test_fgte_should_handle_epsilon(self):
        self.assertEqual(float_gte(0.0000001, 0.0), True)

    # convert_to_np_point tests
    def test_ctnp_should_convert_correctly(self):
        point = {"x": 0.0, "y": 1.0}
        np_point = convert_to_np_point(point)
        expected_result = np.array([0.0, 1.0])
        self.assertTrue(np.array_equal(np_point, expected_result))

    def test_ctnp_should_convert_ints_correctly(self):
        point = {"x": 0, "y": 1}
        np_point = convert_to_np_point(point)
        expected_result = np.array([0, 1])
        self.assertTrue(np.array_equal(np_point, expected_result))

    # np_points_equal tests
    def test_npe_should_handle_equal(self):
        point1 = np.array([0.0, 1.0])
        point2 = np.array([0.0, 1.0])
        eq = np_points_equal(point1, point2)
        self.assertTrue(eq)

    def test_npe_should_handle_epsilon(self):
        point1 = np.array([0.00000001, 1.0])
        point2 = np.array([0.0, 1.0])
        eq = np_points_equal(point1, point2)
        self.assertTrue(eq)

    # get_distance_between_np_points tests
    def test_gdbnp_should_handle_0_distance(self):
        point1 = np.array([0.0, 0.0])
        point2 = np.array([0.0, 0.0])
        dist = get_distance_between_np_points(point1, point2)
        self.assertEqual(dist, 0.0)

    def test_gdbnp_should_handle_nonzero_distance(self):
        point1 = np.array([0.0, 0.0])
        point2 = np.array([0.0, 1.0])
        dist = get_distance_between_np_points(point1, point2)
        self.assertEqual(dist, 1.0)

    def test_gdbnp_should_handle_nonzero_distance_2(self):
        point1 = np.array([0.0, 0.0])
        point2 = np.array([1.0, 1.0])
        dist = get_distance_between_np_points(point1, point2)
        self.assertEqual(dist, np.sqrt(2))

    # get_triangle_area_from_np_points tests (note that we might have floating point errors)
    def test_gtafnp_should_handle_0_area(self):
        point1 = np.array([0.0, 0.0])
        point2 = np.array([0.0, 0.0])
        point3 = np.array([0.0, 0.0])
        area = get_triangle_area_from_np_points(point1, point2, point3)
        self.assertAlmostEqual(area, 0.0)

    def test_gtafnp_should_handle_nonzero_area(self):
        point1 = np.array([0.0, 0.0])
        point2 = np.array([0.0, 1.0])
        point3 = np.array([1.0, 0.0])
        area = get_triangle_area_from_np_points(point1, point2, point3)
        self.assertAlmostEqual(area, 0.5)

    def test_gtafnp_should_handle_nonzero_area_2(self):
        point1 = np.array([0.0, 0.0])
        point2 = np.array([0.0, 1.0])
        point3 = np.array([1.0, 1.0])
        area = get_triangle_area_from_np_points(point1, point2, point3)
        self.assertAlmostEqual(area, 0.5)

    # get_angle_from_np_points tests (note that we might have floating point errors)
    def test_gafnp_should_handle_0_angle(self):
        point1 = np.array([0.0, 0.0])
        point2 = np.array([0.0, 0.0])
        point3 = np.array([0.0, 0.0])
        angle = get_angle_from_np_points(point1, point2, point3)
        self.assertEqual(angle, 0)

    def test_gafnp_should_handle_nonzero_angle(self):
        point1 = np.array([0.0, 0.0])
        point2 = np.array([0.0, 1.0])
        point3 = np.array([1.0, 0.0])
        angle = get_angle_from_np_points(point1, point2, point3)
        self.assertAlmostEqual(angle, np.pi / 4)

    def test_gafnp_should_handle_nonzero_angle_2(self):
        point1 = np.array([0.0, 0.0])
        point2 = np.array([0.0, 1.0])
        point3 = np.array([1.0, 1.0])
        angle = get_angle_from_np_points(point1, point2, point3)
        self.assertAlmostEqual(angle, np.pi / 2)

    def test_gafnp_should_handle_nonzero_angle_3(self):
        point1 = np.array([0.0, 1.0])
        point2 = np.array([0.0, 0.0])
        point3 = np.array([0.0, -1.0])
        angle = get_angle_from_np_points(point1, point2, point3)
        self.assertAlmostEqual(angle, np.pi)

    # can_three_np_points_fit_in_a_circle tests
    def test_ctnpfic_should_handle_collinear(self):
        point1 = np.array([0.0, 0.0])
        point2 = np.array([0.0, 1.0])
        point3 = np.array([0.0, 2.0])
        can_fit = can_three_np_points_fit_in_a_circle(point1, point2, point3, 1.0)
        self.assertTrue(can_fit)

    def test_ctnpfic_should_handle_acute_triangle(self):
        point1 = np.array([0.0, 0.0])
        point2 = np.array([0.0, 1.0])
        point3 = np.array([1.0, 0.5])
        can_fit = can_three_np_points_fit_in_a_circle(point1, point2, point3, 1.0)
        self.assertTrue(can_fit)

    def test_ctnpfic_should_handle_obtuse_triangle(self):
        point1 = np.array([0.0, 0.0])
        point2 = np.array([1.0, 1.0])
        point3 = np.array([2.0, 0.0])
        can_fit = can_three_np_points_fit_in_a_circle(point1, point2, point3, 1.0)
        self.assertTrue(can_fit)

    def test_ctnpfic_should_handle_right_triangle(self):
        point1 = np.array([0.0, 0.0])
        point2 = np.array([0.0, 1.0])
        point3 = np.array([1.0, 0.0])
        can_fit = can_three_np_points_fit_in_a_circle(point1, point2, point3, 1.0)
        self.assertTrue(can_fit)

    def test_ctnpfic_should_handle_0_radius(self):
        point1 = np.array([0.0, 0.0])
        point2 = np.array([0.0, 1.0])
        point3 = np.array([1.0, 0.0])
        can_fit = can_three_np_points_fit_in_a_circle(point1, point2, point3, 0.5)
        self.assertFalse(can_fit)


if __name__ == "__main__":
    unittest.main()
