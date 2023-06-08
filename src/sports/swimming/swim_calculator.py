import tkinter as tk
from tkinter import messagebox
from typing import Any, Dict, Literal

from src.utils.widgets import CreateWindow


class SwimCalculator(tk.Tk):
    result_entry: tk.Entry

    def __init__(self) -> None:
        super().__init__()

        self.widget = CreateWindow(self, title="Swim Calculator", size=(600, 350))

        self._bind_events()
        self._schedule_swim_pace()

    def swim_pace(self, event=None) -> None:  # type: ignore
        distance_gap: Any = self.widget.entry_gap["distance"].get()
        hour_gap: Any | Literal[0] = self.widget.entry_gap["hour"].get() or 0
        minute_gap: Any | Literal[0] = self.widget.entry_gap["minutes"].get() or 0
        seconds_gap: Any | Literal[0] = self.widget.entry_gap["seconds"].get() or 0

        if distance_gap and (hour_gap or minute_gap or seconds_gap):
            try:
                distance_gap = int(distance_gap)
                hour_gap = int(hour_gap)
                minute_gap = int(minute_gap)
                seconds_gap = int(seconds_gap)

                total_seconds: int = (hour_gap * 3600) + (minute_gap * 60) + seconds_gap
                pace_seconds: Any = (total_seconds * 100) / distance_gap
                minutes = int(pace_seconds // 60)
                seconds_left = int(pace_seconds % 60)
                self.result: str = f"0{minutes:01d}:{seconds_left:02d} min/100mts"

                self.result_entry: tk.Entry = self.widget.create_result_gap(
                    result_gap=self.result
                )
                self.result_entry.delete(0, "end")
                self.result_entry.insert(0, self.result)

            except ValueError:
                messagebox.showerror(  # type: ignore
                    "Error", "Invalid input. Please enter numbers only."
                )
                return
            except ZeroDivisionError:
                messagebox.showerror(  # type: ignore
                    "Error", "Invalid distance. Please enter a distance number"
                )
                return

        self.after(5000, self.swim_pace)  # type: ignore

    def _bind_events(self) -> None:
        entry_gap: Dict[Any, Any] = self.widget.entry_gap
        for entry in entry_gap.values():
            entry.bind("<Return>", self.swim_pace)  # type: ignore

    def _schedule_swim_pace(self) -> None:
        self.after(1000, self.swim_pace)  # type: ignore
