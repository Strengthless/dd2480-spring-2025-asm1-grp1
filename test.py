import unittest
from modules.decide import determine_launch
from modules.fuv import get_fuv
from modules.types import Connectors

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
        pum_false_pos = [(1,0), (0,1), (0,3), (3,0)]
        fuv_false_pos = [0, 3]
        pum = [[(i,j) not in pum_false_pos for j in range(15)] for i in range(15)]
        expectedResult = [i not in fuv_false_pos for i in range(15)] 

        # get fuv
        fuv = get_fuv(pum=pum, puv=puv)
        self.assertEqual(fuv, expectedResult)

class PUMTest(unittest.TestCase):
    # TODO: Add actual tests here
    def test_something(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()