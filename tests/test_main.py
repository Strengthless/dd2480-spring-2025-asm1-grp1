import unittest
from snapshottest import TestCase
from src.main import parse_input


class MainTests(TestCase):
    def test_should_parse_correctly(self):
        output = parse_input("./inputs/test_valid.txt")
        self.assertMatchSnapshot(output, "Correct inputs should be parsed correctly.")

    def test_should_raise_error_if_numpoints_lt_2(self):
        self.assertRaises(
            ValueError, parse_input, "./inputs/test_invalid_numpoints_1.txt"
        )

    def test_should_raise_error_if_numpoints_gt_100(self):
        self.assertRaises(
            ValueError, parse_input, "./inputs/test_invalid_numpoints_2.txt"
        )

    def test_should_raise_error_if_numpoints_not_int(self):
        self.assertRaises(
            ValueError, parse_input, "./inputs/test_invalid_numpoints_3.txt"
        )

    def test_should_raise_error_if_numpoints_not_provided(self):
        self.assertRaises(
            ValueError, parse_input, "./inputs/test_invalid_numpoints_4.txt"
        )

    def test_should_raise_error_if_point_has_invalid_type(self):
        self.assertRaises(ValueError, parse_input, "./inputs/test_invalid_points_1.txt")

    def test_should_raise_error_if_point_has_invalid_length(self):
        self.assertRaises(ValueError, parse_input, "./inputs/test_invalid_points_2.txt")

    def test_should_raise_error_if_points_mismatch_numpoints(self):
        self.assertRaises(ValueError, parse_input, "./inputs/test_invalid_points_3.txt")

    def test_should_raise_error_if_params_neq_19(self):
        self.assertRaises(ValueError, parse_input, "./inputs/test_invalid_params_1.txt")

    def test_should_raise_error_if_params_have_invalid_types(self):
        self.assertRaises(ValueError, parse_input, "./inputs/test_invalid_params_2.txt")

    def test_should_raise_error_if_lcm_has_invalid_types(self):
        self.assertRaises(TypeError, parse_input, "./inputs/test_invalid_lcm_1.txt")

    def test_should_raise_error_if_lcm_has_invalid_size(self):
        self.assertRaises(ValueError, parse_input, "./inputs/test_invalid_lcm_2.txt")

    def test_should_raise_error_if_puv_has_invalid_length(self):
        self.assertRaises(ValueError, parse_input, "./inputs/test_invalid_puv_1.txt")

    def test_should_raise_error_if_puv_has_invalid_types(self):
        self.assertRaises(TypeError, parse_input, "./inputs/test_invalid_puv_2.txt")


if __name__ == "__main__":
    unittest.main()
