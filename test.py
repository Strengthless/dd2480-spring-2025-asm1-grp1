import unittest
from main import parse_input
from modules.decide import determine_launch
from modules.pum import get_pum
from modules.types import Connectors
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
    # TODO: Add actual tests here
    def test_something(self):
        self.assertEqual('foo'.upper(), 'FOO')

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