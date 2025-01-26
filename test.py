import unittest
from modules.decide import determine_launch
from modules.cmv import lic0
from modules.types import Coordinate, Parameters

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
    #TODO: Add actual tests here
    def test_something(self):
        self.assertEqual('foo'.upper(), 'FOO')

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
        lic_0 = lic0(num_points,points,params)
        self.assertFalse(lic_0)


class FUVTest(unittest.TestCase):
    # TODO: Add actual tests here
    def test_something(self):
        self.assertEqual('foo'.upper(), 'FOO')

class PUMTest(unittest.TestCase):
    # TODO: Add actual tests here
    def test_something(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()