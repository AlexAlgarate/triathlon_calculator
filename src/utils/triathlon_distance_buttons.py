import tkinter as tk
from typing import Dict, List, Tuple


class DistanceButtonsCreator:
    def __init__(
        self, window: tk.Tk, selected_distance: tk.StringVar, entry_gap: Dict[str, str]
    ) -> None:
        self.window: tk.Tk = window
        self.selected_distance: tk.StringVar = selected_distance
        self.entry_gap: Dict[str, str] = entry_gap
        self.distance_frame = tk.Frame(self.window)

    def create_distance_buttons(self, distances: List[Tuple[str, int]]) -> None:
        self.distance_frame.place(relx=0.15, rely=0.04, relwidth=0.6, relheight=0.06)
        for i, (button_text, distance_value) in enumerate(distances):  # type: ignore
            button = tk.Radiobutton(
                self.distance_frame,
                text=button_text,
                variable=self.selected_distance,
                value=str(distance_value),
                command=self._set_distance,
            )
            button.pack(side="left", padx=5)

    def _set_distance(self) -> None:
        distance_value: str = self.selected_distance.get()
        self.entry_gap["distance"].delete(0, "end")  # type: ignore
        self.entry_gap["distance"].insert(0, distance_value)  # type: ignore
