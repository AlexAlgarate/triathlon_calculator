import tkinter as tk
from typing import Any, Dict, List, Tuple

from src.utils.close_window_button import CloseWindowButton
from src.utils.entry_gaps import EntryGap
from src.utils.entry_labels import EntryLabel
from src.utils.menu_labels import MenuLabel
from src.utils.triathlon_distance_buttons import DistanceButtonsCreator


class Widgets:
    selected_distance: tk.StringVar
    LABEL_COLOUR: str = "PaleTurquoise2"
    ENTRY_COLOUR: str = "khaki1"
    DISTANCES: List[Tuple[str, int]] = [
        ("Sprint", 750),
        ("Olympic", 1500),
        ("Half Ironman", 1900),
        ("Ironman", 3800),
    ]

    def __init__(self, window: tk.Tk, title: str, size: Tuple[int, int]) -> None:
        self.window: tk.Tk = window
        self.window.title(title)
        self.window.geometry(f"{size[0]}x{size[1]}")
        self.window.minsize(size[0], size[1])
        self.window.maxsize(size[0], size[1])

        self.selected_distance = tk.StringVar(value=" ")

        self._create_menu_label()
        self._create_label_entry_gap()
        self._create_entry_gap()
        self._close_window_button()
        self._create_distance_buttons(self.DISTANCES)

    def _create_menu_label(self) -> None:
        self.menu_labels: List[Any] = []
        self.menu_labels.append(
            MenuLabel(
                self.window,
                text="Distance",
                rely_value=0.18,
                background=self.LABEL_COLOUR,
            )
        )
        self.menu_labels.append(
            MenuLabel(
                self.window, text="Time", rely_value=0.33, background=self.LABEL_COLOUR
            )
        )
        self.menu_labels.append(
            MenuLabel(
                self.window, text="Speed", rely_value=0.65, background=self.LABEL_COLOUR
            )
        )

    def _create_label_entry_gap(self) -> None:
        self.entry_labels: List[Any] = []
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

    def _create_entry_gap(self) -> None:
        self.entry_gap: Dict[Any, Any] = {}
        entries: List[EntryGap] = [
            EntryGap(
                self.window,
                name="distance",
                background=self.ENTRY_COLOUR,
                relx_value=0.35,
                rely_value=0.18,
                relwidth_value=0.22,
            ),
            EntryGap(
                self.window,
                name="hour",
                background=self.ENTRY_COLOUR,
                relx_value=0.35,
                rely_value=0.33,
                relwidth_value=0.06,
            ),
            EntryGap(
                self.window,
                name="minutes",
                background=self.ENTRY_COLOUR,
                relx_value=0.47,
                rely_value=0.33,
                relwidth_value=0.06,
            ),
            EntryGap(
                self.window,
                name="seconds",
                background=self.ENTRY_COLOUR,
                relx_value=0.63,
                rely_value=0.33,
                relwidth_value=0.06,
            ),
        ]
        for item in entries:
            entry: EntryGap = item
            self.entry_gap[entry.name] = entry

    def _create_distance_buttons(self, distances: List[Tuple[str, int]]) -> None:
        triathlon_buttons = DistanceButtonsCreator(
            self.window, self.selected_distance, self.entry_gap
        )
        return triathlon_buttons.create_distance_buttons(distances=distances)

    def create_result_gap(self, result_gap: str) -> tk.Entry:
        result_entry = tk.Entry(self.window)
        result_entry.config(text=result_gap, background=self.ENTRY_COLOUR)  # type: ignore
        result_entry.place(relx=0.35, rely=0.65, relwidth=0.35, relheight=0.1)
        return result_entry

    def _close_window_button(self) -> None:
        CloseWindowButton(
            self.window, button_text="Close", root=self.window.winfo_toplevel()
        )
