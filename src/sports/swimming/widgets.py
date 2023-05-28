import tkinter as tk
from typing import Tuple

from src.sports.swimming.close_window import CloseWindowButton
from src.sports.swimming.entry_gaps import EntryGap
from src.sports.swimming.entry_labels import EntryLabel
from src.sports.swimming.menu_labels import MenuLabel


class Widgets:
    def __init__(self, window: tk.Tk, title: str, size: Tuple[int, int]):
        self.window = window
        self.window.title(title)
        self.window.geometry(f"{size[0]}x{size[1]}")
        self.window.minsize(size[0], size[1])
        self.window.maxsize(size[0], size[1])

        self._create_menu_label()
        self._create_label_entry_gap()
        self._create_distance_buttons()
        self._close_window_button()
        self._create_entry_gap()

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

    def _create_distance_buttons(self):
        self.distance_buttons = []
        distances = [
            ("Sprint", 750),
            ("Olympic", 1500),
            ("Half Ironman", 1900),
            ("Ironman", 3800),
        ]
        self.selected_distance = tk.StringVar(value=" ")
        distance_frame = tk.Frame(self.window)
        distance_frame.place(relx=0.15, rely=0.04, relwidth=0.6, relheight=0.06)
        for i, (button_text, distance_value) in enumerate(distances):
            button = tk.Radiobutton(
                distance_frame,
                text=button_text,
                variable=self.selected_distance,
                value=str(distance_value),
                command=self._set_distance,
            )
            button.pack(side="left", padx=5)
            self.distance_buttons.append(button)

    def _set_distance(self):
        distance_value = self.selected_distance.get()
        self.entry_gap["distance"].delete(0, "end")
        self.entry_gap["distance"].insert(0, distance_value)

    def _close_window_button(self):
        CloseWindowButton(
            self.window, button_text="Close", root=self.window.winfo_toplevel()
        )
