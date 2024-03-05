import unittest
from unittest.mock import patch
from game_logic import *

class TestCheckNumber(unittest.TestCase):
    def test_check_number_igual(self):
        self.assertEqual(check_number(5, 5), "igual")

    def test_check_number_menor(self):
        self.assertEqual(check_number(10, 5), "menor")

    def test_check_number_mayor(self):
        self.assertEqual(check_number(5, 10), "mayor")

class TestPrintResult(unittest.TestCase):
    def test_igual_user(self):
        expected_output = "¡Felicidades! usuario has adivinado el número correcto."
        with patch('builtins.print') as mocked_print:
            print_result("igual", "user")
            mocked_print.assert_called_once_with(expected_output)

class TestComputerFunction(unittest.TestCase):
    def test_computer_function_no_status(self):
        _, a, b = computer_function(1, 100)
        self.assertTrue(1 <= _ <= 100)
        self.assertEqual(a, 1)
        self.assertEqual(b, 100)

    def test_computer_function_with_status_menor(self):
        _, a, _ = computer_function(1, 100, 50, "menor")
        self.assertTrue(a > 50)

    def test_computer_function_with_status_mayor(self):
        _, _, b = computer_function(1, 100, 50, "mayor")
        self.assertTrue(b < 50)

if __name__ == '__main__':
    unittest.main()
