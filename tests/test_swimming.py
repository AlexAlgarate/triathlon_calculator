import os
import sys
import tkinter as tk
import unittest
from typing import Dict, Union
from unittest.mock import MagicMock, patch

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from src.sports.swimming.close_window import CloseWindowButton
from src.sports.swimming.swim_calculator import SwimCalculator
from src.sports.swimming.widgets import Widgets


class TestSwimLabelsEntries(unittest.TestCase):
    def setUp(self):
        self.window = tk.Tk()

        self.app = Widgets(self.window, "TEST SWIM", (600, 350))
        self.app = SwimCalculator("TEST SWIM", (600, 350))

    def _entry_gap_get(self):
        distance = self.app.widget.entry_gap["distance"].get()
        hour = self.app.widget.entry_gap["hour"].get()
        minute = self.app.widget.entry_gap["minutes"].get()
        second = self.app.widget.entry_gap["seconds"].get()

        return distance, hour, minute, second

    def _update_gap_values(self, values: Dict[str, Union[int, str]]):
        for key, value in values.items():
            self.app.widget.entry_gap[key].insert(0, value)

    def tearDown(self):
        self.window.destroy()

    def test_create_menu_label(self):
        self.assertEqual(len(self.app.widget.menu_labels), 3)

    def test_create_label_entry_gap(self):
        self.assertEqual(len(self.app.widget.entry_labels), 4)

    def test_create_entry_gap(self):
        self.assertEqual(len(self.app.widget.entry_gap), 4)

    def test_create_distance_buttons(self):
        self.assertEqual(len(self.app.widget.distance_buttons), 4)

    def test_default_values(self):
        distance, hours, minutes, seconds = self._entry_gap_get()
        self.assertEqual(distance, "")
        self.assertEqual(hours, "")
        self.assertEqual(minutes, "")
        self.assertEqual(seconds, "")

    def test_update_values(self):
        values = {"distance": "1500", "hour": "1", "minutes": "30", "seconds": "45"}

        self._update_gap_values(values)
        distance_get, hours_get, minutes_get, seconds_get = self._entry_gap_get()

        self.assertEqual(distance_get, "1500")
        self.assertEqual(hours_get, "1")
        self.assertEqual(minutes_get, "30")
        self.assertEqual(seconds_get, "45")

    def test_swim_pace_calculation(self):
        values = {"distance": "1000", "hour": "0", "minutes": "15", "seconds": "00"}

        self._update_gap_values(values)
        self.app.swim_pace()
        result = self.app.result_label.get()
        self.assertEqual(result, "01:30 min/100mts")

    def test_invalid_values(self):
        values = {"distance": "1000", "hour": "0", "minutes": "15a", "seconds": "00"}
        self._update_gap_values(values)
        showerror_mock = MagicMock()
        with patch(
            "src.sports.swimming.swim_calculator.messagebox.showerror", showerror_mock
        ):
            self.app.swim_pace()
        showerror_mock.assert_called_once()

    def test_zero_distance(self):
        values = {"distance": "0", "hour": "0", "minutes": "15", "seconds": "00"}

        self._update_gap_values(values)
        showerror_mock = MagicMock()
        with patch(
            "src.sports.swimming.swim_calculator.messagebox.showerror", showerror_mock
        ):
            self.app.swim_pace()
        showerror_mock.assert_called_once()

    def test_missing_time_input(self):
        # Test case where time input is missing
        self.app.widget.entry_gap["distance"].insert(0, "1500")

        self.app.swim_pace()
        # Verify that the result label is empty
        self.app.after(100, self.verify_result_label)

    def verify_result_label(self):
        self.assertEqual(self.app.result_label.get(), "")

    def test_no_input(self):
        # Test case where no input is provided
        self.app.after(100, self.verify_result_label)


class TestCloseWindowButton(unittest.TestCase):
    def setUp(self):
        self.window = tk.Tk()
        self.close_button = CloseWindowButton(
            self.window, button_text="Close", root=self.window.winfo_toplevel()
        )

    def tearDown(self):
        self.window.destroy()

    def test_close_window(self):
        window = tk.Toplevel()
        close_button = CloseWindowButton(window, button_text="close", root=window)
        close_button._close_window(window)
        self.assertFalse(window.winfo_exists())


if __name__ == "__main__":
    unittest.main()
