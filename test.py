import unittest
import tkinter as tk
from src.sports.swim import SwimCalculator


class SwimCalculatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.window = tk.Tk()
        self.calculator = SwimCalculator(self.window)

    def tearDown(self) -> None:
        self.window.destroy()

    def test_swim_pace_valid_input(self):
        self.calculator.entry_fields["distance"].insert(0, "1000")
        self.calculator.entry_fields["hour"].insert(0, "0")
        self.calculator.entry_fields["minute"].insert(0, "15")
        self.calculator.entry_fields["seconds"].insert(0, "0")

        self.calculator._swim_pace()

        expected_result = "01:30 min/100mts"
        actual_result = self.calculator.velocity_result.get()

        self.assertEqual(actual_result, expected_result)

    def test_swim_pace_invalid_input(self):
        self.calculator.entry_fields["distance"].insert(0, "1000")
        self.calculator.entry_fields["hour"].insert(0, "0")
        self.calculator.entry_fields["minute"].insert(0, "15.2")
        self.calculator.entry_fields["seconds"].insert(0, "0")

        self.calculator._swim_pace()

        expected_result = ""
        actual_result = self.calculator.velocity_result.get()

        self.assertEqual(actual_result, expected_result)
        self.assertTrue(self.calculator.velocity_result.winfo_ismapped())


if __name__ == "__main__":
    unittest.main()
