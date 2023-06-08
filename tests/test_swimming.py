import os
import sys
import tkinter as tk
import unittest
from typing import Dict, Union
from unittest.mock import MagicMock, patch

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from src.sports.swimming.swim_calculator import SwimCalculator  # noga
from src.utils.close_window_button import CloseWindowButton  # noga
from src.utils.triathlon_distance_buttons import DistanceButtonsCreator


class TestSwimLabelsEntries(unittest.TestCase):
    def setUp(self) -> None:
        self.window = tk.Tk()

        self.app = SwimCalculator()

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
        result = self.app.result_entry.get()
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


class DistanceButtonsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.window = tk.Tk()
        self.selected_distance = tk.StringVar()
        self.entry_gap = {"distance": tk.Entry(self.window)}
        self.buttons_creator = DistanceButtonsCreator(
            self.window, self.selected_distance, self.entry_gap
        )

    def tearDown(self) -> None:
        self.window.destroy()

    def test_distance_buttons_creations(self):
        distances = [
            ("Sprint", "750"),
            ("Olympic", "1500"),
            ("Half Ironman", "1900"),
            ("Ironman", "3800")
        ]
        self.buttons_creator.create_distance_buttons(distances)

        # Check if the correct number of buttons is created
        self.assertEqual(len(distances), len(self.buttons_creator.distance_frame.winfo_children()))

        # Check if the buttons have the correct text and value
        for i, (button_text, distance_value) in enumerate(distances):
            button = self.buttons_creator.distance_frame.winfo_children()[i]
            self.assertEqual(button.cget("text"), button_text)
            self.assertEqual(button["value"], str(distance_value))

    def test_set_distance(self):
        distance_value = 1500
        self.selected_distance.set(str(distance_value))
        self.buttons_creator._set_distance()

        # Check if the entry_gap["distance"] is updated with the selected distance value
        self.assertEqual(self.entry_gap["distance"].get(), str(distance_value))


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
