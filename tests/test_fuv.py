import unittest
from src.modules.fuv import get_fuv


class FUVTest(unittest.TestCase):
    def setUp(self):
        # Factory methods
        self.all_true_1d = [True] * 15
        self.all_false_1d = [False] * 15

        self.all_true_2d = [[True] * 15 for _ in range(15)]
        self.all_false_2d = [[False] * 15 for _ in range(15)]

        self.mutate_1d = lambda base, *indices: [
            base[i] if i not in indices else not base[i] for i in range(15)
        ]

        self.generate_pum = lambda false_pos: [
            [(i, j) not in false_pos for j in range(15)] for i in range(15)
        ]

        self.generate_mock_fuv = lambda false_pos: [
            i not in false_pos for i in range(15)
        ]

        # Test fixtures
        self.pum_false_pos_1 = [
            (1, 0),
            (0, 1),
            (0, 3),
            (3, 0),
            (4, 5),
            (5, 4),
            (6, 4),
            (4, 6),
            (14, 2),
            (2, 14),
        ]

        self.pum_false_pos_2 = [
            (1, 0),
            (0, 1),
            (0, 3),
            (3, 0),
            (4, 5),
            (5, 4),
            (6, 4),
            (4, 6),
            (15, 2),
            (2, 15),
        ]

    def test_fuv_should_be_true_if_all_puv_false(self):
        puv = self.all_false_1d
        pum = self.all_false_2d

        fuv = get_fuv(pum=pum, puv=puv)

        expected_result = self.all_true_1d
        self.assertEqual(fuv, expected_result)

    def test_fuv_should_be_the_same_as_in_the_example_in_assignment(self):
        puv = self.mutate_1d(self.all_true_1d, 1)
        pum_false_pos = [(1, 0), (0, 1), (0, 3), (3, 0)]
        pum = self.generate_pum(pum_false_pos)

        fuv = get_fuv(pum=pum, puv=puv)

        expected_result = self.generate_mock_fuv([0, 3])
        self.assertEqual(fuv, expected_result)

    def test_fuv_should_be_a_certain_value_given_specific_pattern_with_puv_mostly_true(
        self,
    ):
        puv = self.mutate_1d(self.all_true_1d, 3, 5, 8)
        pum_false_pos = self.pum_false_pos_1
        pum = self.generate_pum(pum_false_pos)

        fuv = get_fuv(pum=pum, puv=puv)

        expected_result = self.generate_mock_fuv([0, 1, 2, 4, 6, 14])
        self.assertEqual(fuv, expected_result)

    def test_fuv_should_be_a_certain_value_given_specific_pattern_with_puv_mostly_false(
        self,
    ):
        puv = self.mutate_1d(self.all_false_1d, 3, 6, 8)
        pum_false_pos = self.pum_false_pos_2
        pum = self.generate_pum(pum_false_pos)

        fuv = get_fuv(pum=pum, puv=puv)

        expected_result = self.generate_mock_fuv([3, 6])
        self.assertEqual(fuv, expected_result)

    def test_fuv_throw_exception_when_puv_dimension_mismatch(self):
        puv = [False] * 14  # wrong dimension
        pum = [[True] * 15] * 15
        self.assertRaises(ValueError, get_fuv, pum, puv)

    def test_fuv_throw_exception_when_pum_dimension_mismatch(self):
        puv = [False] * 15
        pum = [[True] * 15] * 14  # wrong dimension
        self.assertRaises(ValueError, get_fuv, pum, puv)


if __name__ == "__main__":
    unittest.main()
