import unittest
from main import parse_input
from modules.decide import determine_launch
from modules.pum import get_pum
from modules.types import Connectors, Coordinate, Parameters
from modules.cmv import *
from snapshottest import TestCase

class MainTests(TestCase):
    def test_should_parse_correctly(self):
        output = parse_input('test_valid.txt')
        self.assertMatchSnapshot(output, 'Correct inputs should be parsed correctly.')

    def test_should_raise_error_if_numpoints_lt_2(self):
        self.assertRaises(ValueError, parse_input, 'test_invalid_numpoints_1.txt')

    def test_should_raise_error_if_numpoints_gt_100(self):
        self.assertRaises(ValueError, parse_input, 'test_invalid_numpoints_2.txt')

    def test_should_raise_error_if_numpoints_not_int(self):
        self.assertRaises(TypeError, parse_input, 'test_invalid_numpoints_3.txt')

    def test_should_raise_error_if_numpoints_not_provided(self):
        self.assertRaises(TypeError, parse_input, 'test_invalid_numpoints_4.txt')

    def test_should_raise_error_if_point_has_invalid_type(self):
        self.assertRaises(TypeError, parse_input, 'test_invalid_points_1.txt')

    def test_should_raise_error_if_point_has_invalid_length(self):
        self.assertRaises(ValueError, parse_input, 'test_invalid_points_2.txt')

    def test_should_raise_error_if_points_mismatch_numpoints(self):
        self.assertRaises(ValueError, parse_input, 'test_invalid_points_3.txt')

    def test_should_raise_error_if_params_neq_19(self):
        self.assertRaises(ValueError, parse_input, 'test_invalid_params_1.txt')

    def test_should_raise_error_if_params_have_invalid_types(self):
        self.assertRaises(TypeError, parse_input, 'test_invalid_params_2.txt')

    def test_should_raise_error_if_lcm_has_invalid_types(self):
        self.assertRaises(TypeError, parse_input, 'test_invalid_lcm_1.txt')

    def test_should_raise_error_if_lcm_has_invalid_size(self):
        self.assertRaises(ValueError, parse_input, 'test_invalid_lcm_2.txt')

    def test_should_raise_error_if_puv_has_invalid_length(self):
        self.assertRaises(ValueError, parse_input, 'test_invalid_puv_1.txt')

    def test_should_raise_error_if_puv_has_invalid_types(self):
        self.assertRaises(TypeError, parse_input, 'test_invalid_puv_2.txt')

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
  def test_lic_0_no_distance_greater_than_length(self):
        params = Parameters(
            length1=5.3,   # Length in LICs 0, 7, 12
            radius1=3.0,   # Radius in LICs 1, 8, 13
            epsilon=0.1,   # Deviation from PI in LICs 2, 9
            area1=10.0,    # Area in LICs 3, 10, 14
            q_pts=5,       # No. of consecutive points in LIC 4
            quads=2,       # No. of quadrants in LIC 4
            dist=1.0,      # Distance in LIC 6
            n_pts=2,       # No. of consecutive points in LIC 6
            k_pts=3,       # No. of int. points in LICs 7, 12
            a_pts=4,       # No. of int. points in LICs 8, 13
            b_pts=4,       # No. of int. points in LICs 8, 13 (duplicate key reference in your comment)
            c_pts=2,       # No. of int. points in LICs 9
            d_pts=2,       # No. of int. points in LICs 9 (duplicate key reference in your comment)
            e_pts=6,       # No. of int. points in LICs 10, 14
            f_pts=6,       # No. of int. points in LICs 10, 14 (duplicate key reference in your comment)
            g_pts=1,       # No. of int. points in LIC 11
            length2=15.0,  # Maximum length in LIC 12
            radius2=10.0,  # Maximum radius in LIC 13
            area2=25.0     # Maximum area in LIC 14
            )
        
        points: list[Coordinate] = [
            {"x": 1.0, "y": 2.0},
            {"x": 1.5, "y": 4.5},
            {"x": -1.2, "y": 0.0},
            ]
        
        num_points = 3
        self.assertFalse(check_lic_0(num_points,points,params))

    def test_lic_10_should_pass_if_area_gt_area1(self):
        parameters = {
            "area1": 1,
            "e_pts": 3,
            "f_pts": 4
        }
        points_1 = [{'x':0, 'y':0},{'x':0, 'y':0},{'x':0, 'y':0},{'x':0, 'y':0},
                    {'x':0, 'y':0},{'x':0, 'y':0},{'x':3, 'y':0},{'x':0, 'y':0},
                    {'x':0, 'y':0},{'x':0, 'y':0},{'x':0, 'y':0},{'x':3, 'y':3}]
        self.assertTrue(check_lic_10(points_1, parameters))

    def test_lic_10_should_fail_if_area_lte_area1(self):
        parameters = {
            "area1": 2,
            "e_pts": 3,
            "f_pts": 4
        }
        points_1 = [{'x':0, 'y':0},{'x':0, 'y':0},{'x':0, 'y':0},{'x':0, 'y':0},
                    {'x':0, 'y':0},{'x':0, 'y':0},{'x':3, 'y':0},{'x':0, 'y':0},
                    {'x':0, 'y':0},{'x':0, 'y':0},{'x':0, 'y':0},{'x':3, 'y':3}]
        self.assertTrue(check_lic_10(points_1, parameters))

    def test_lic_10_should_raise_error_if_epts_is_invalid(self):
        with self.assertRaises(ValueError):
            points_1 = [{'x':0, 'y':0},{'x':0, 'y':0},{'x':0, 'y':0},
                        {'x':0, 'y':0},{'x':0, 'y':0},{'x':0, 'y':0}]
            parameters = {
            "area1": 2,
            "e_pts": 0,
            "f_pts": 4
            }   
            check_lic_10(points_1, parameters)
    
    def test_lic_10_should_raise_error_if_fpts_is_invalid(self):
        with self.assertRaises(ValueError):
            points_1 = [{'x':0, 'y':0},{'x':0, 'y':0},{'x':0, 'y':0},
                        {'x':0, 'y':0},{'x':0, 'y':0},{'x':0, 'y':0}]
            parameters = {
            "area1": 2,
            "e_pts": 3,
            "f_pts": 0
            }   
            check_lic_10(points_1, parameters)

    def test_lic_10_should_raise_error_if_epts_fpts_and_points_mismatch(self):
        with self.assertRaises(ValueError):
            points_1 = [{'x':0, 'y':0},{'x':0, 'y':0},{'x':0, 'y':0},
                        {'x':0, 'y':0},{'x':0, 'y':0},{'x':0, 'y':0}]
            parameters = {
            "area1": 2,
            "e_pts": 8,
            "f_pts": 4
            }   
            check_lic_10(points_1, parameters)


class FUVTest(unittest.TestCase):
    # TODO: Add actual tests here
    def test_something(self):
        self.assertEqual('foo'.upper(), 'FOO')

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
        expectedResult = [[(i == 2 or j == 2 or i == j) for j in range(15)] for i in range(15)]
        self.assertEqual(pum, expectedResult)

    def test_pum_pattern_for_lcm_all_and_and_single_cmv_true(self):
        lcm = [[Connectors.ANDD] * 15] * 15
        cmv = [False] * 15
        cmv[2] = True
        pum = get_pum(cmv=cmv, lcm=lcm)
        expectedResult = [[(i == j) for j in range(15)] for i in range(15)]
        self.assertEqual(pum, expectedResult)


if __name__ == '__main__':
    unittest.main()