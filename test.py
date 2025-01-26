import unittest
from modules.decide import determine_launch
from modules.pum import get_pum
from modules.types import Connectors
from modules.cmv import *

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

    def test_lic_10(self):

        # Define the parameters for LIC 10 test

        parameters = {
            "area1": 2,
            "e_pts": 3,
            "f_pts": 4
        }

        points_1 = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        points_2 = [(0,0),(0,0),(0,0),(0,0),(10,0),(0,0),(0,0),(0,0),(0,0),(0,10),(0,0),(0,0)]
        points_3 = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,1),(0,0),(0,0),(0,0),(0,0),(1,0),(0,0)]
        points_4 = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(3,0),(0,0),(0,0),(0,0),(0,0),(3,3)]

        # Test the LIC 10 logic

        self.assertFalse(check_lic_10(points_1, parameters))
        self.assertTrue(check_lic_10(points_2, parameters))
        self.assertFalse(check_lic_10(points_3, parameters))
        self.assertTrue(check_lic_10(points_4, parameters))

        parameters["area1"] = 51
        
        self.assertFalse(check_lic_10(points_2, parameters))
        self.assertFalse(check_lic_10(points_4, parameters))

        # Testing if the built in assertions work

        with self.assertRaises(AssertionError):
            parameters["e_pts"] = 0
            parameters["f_pts"] = 1
            check_lic_10(points_1, parameters)
        
        with self.assertRaises(AssertionError):
            parameters["e_pts"] = 1
            parameters["f_pts"] = 0
            check_lic_10(points_1, parameters)

        with self.assertRaises(AssertionError):
            parameters["e_pts"] = 1
            parameters["f_pts"] = 3
            points_5 = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
            check_lic_10(points_5, parameters)

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