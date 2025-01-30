import unittest
from src.modules.pum import get_pum
from src.modules.types import Connectors


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
        expected_result = [
            [(i == 2 or j == 2 or i == j) for j in range(15)] for i in range(15)
        ]
        self.assertEqual(pum, expected_result)

    def test_pum_pattern_for_lcm_all_and_and_single_cmv_true(self):
        lcm = self.lcm_all_andd
        cmv = self.create_cmv_pattern(self.cmv_all_false, 2)
        pum = get_pum(cmv, lcm)
        expected_result = [[(i == j) for j in range(15)] for i in range(15)]
        self.assertEqual(pum, expected_result)


if __name__ == "__main__":
    unittest.main()
