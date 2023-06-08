import tkinter as tk
from typing import List, Tuple, Union

from src.utils.close_window_button import CloseWindowButton
from src.utils.triathlon_distance_buttons import DistanceButtonsCreator
from src.utils.entry_gaps import EntryGap
from src.utils.entry_labels import EntryLabel
from src.utils.menu_labels import MenuLabel


class Widgets:
    selected_distance: tk.StringVar

    def __init__(self, window: tk.Tk, title: str, size: Tuple[int, int]):
        self.window = window
        self.window.title(title)
        self.window.geometry(f"{size[0]}x{size[1]}")
        self.window.minsize(size[0], size[1])
        self.window.maxsize(size[0], size[1])

        self.selected_distance = tk.StringVar(value=" ")

        self._create_menu_label()
        self._create_label_entry_gap()
        self._create_entry_gap()
        self._close_window_button()

    def _create_menu_label(self):
        self.menu_labels = []
        self.menu_labels.append(
            MenuLabel(
                self.window,
                text="Distance",
                rely_value=0.18,
                background="PaleTurquoise2",
            )
        )
        self.menu_labels.append(
            MenuLabel(
                self.window, text="Time", rely_value=0.33, background="PaleTurquoise2"
            )
        )
        self.menu_labels.append(
            MenuLabel(
                self.window, text="Speed", rely_value=0.65, background="PaleTurquoise2"
            )
        )

    def _create_label_entry_gap(self):
        self.entry_labels = []
        self.entry_labels.append(
            EntryLabel(
                self.window,
                text="meters",
                relx_value=0.6,
                rely_value=0.18,
                relwidth_value=0.13,
            )
        )
        self.entry_labels.append(
            EntryLabel(
                self.window,
                text="h",
                relx_value=0.41,
                rely_value=0.33,
                relwidth_value=0.06,
            )
        )
        self.entry_labels.append(
            EntryLabel(
                self.window,
                text="min",
                relx_value=0.545,
                rely_value=0.33,
                relwidth_value=0.06,
            )
        )
        self.entry_labels.append(
            EntryLabel(
                self.window,
                text="secs",
                relx_value=0.71,
                rely_value=0.33,
                relwidth_value=0.06,
            )
        )

    def _create_entry_gap(self):
        self.entry_gap = {}
        entries = [
            EntryGap(
                self.window,
                name="distance",
                background="khaki1",
                relx_value=0.35,
                rely_value=0.18,
                relwidth_value=0.22,
            ),
            EntryGap(
                self.window,
                name="hour",
                background="khaki1",
                relx_value=0.35,
                rely_value=0.33,
                relwidth_value=0.06,
            ),
            EntryGap(
                self.window,
                name="minutes",
                background="khaki1",
                relx_value=0.47,
                rely_value=0.33,
                relwidth_value=0.06,
            ),
            EntryGap(
                self.window,
                name="seconds",
                background="khaki1",
                relx_value=0.63,
                rely_value=0.33,
                relwidth_value=0.06,
            ),
        ]
        for item in entries:
            entry = item
            self.entry_gap[entry.name] = entry

    def create_distance_buttons(self, distances: List[Tuple[str, Union[int, float]]]):
        distance_buttons_creator = DistanceButtonsCreator(
            self.window, self.selected_distance, self.entry_gap
        )
        distance_buttons_creator.create_distance_buttons(distances)

    def create_result_gap(self, result_gap: str):
        result_entry = tk.Entry(self.window)
        result_entry.config(text=result_gap, background="khaki1")
        result_entry.place(relx=0.35, rely=0.65, relwidth=0.35, relheight=0.1)
        return result_entry

    def _close_window_button(self):
        CloseWindowButton(
            self.window, button_text="Close", root=self.window.winfo_toplevel()
        )
