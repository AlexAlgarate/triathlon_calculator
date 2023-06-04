import tkinter as tk
from tkinter import messagebox

from src.utils.widgets import Widgets


class SwimCalculator(tk.Tk):
    DISTANCES = [
        ("Sprint", 750),
        ("Olympic", 1500),
        ("Half Ironman", 1900),
        ("Ironman", 3800),
    ]
    result_entry: tk.Entry

    def __init__(self):
        super().__init__()

        self.widget = Widgets(self, title="Swim Calculator", size=(600, 350))
        self.widget.create_distance_buttons(self.DISTANCES)

        self.update_result()

    def swim_pace(self, event=None):
        distance_gap = self.widget.entry_gap["distance"].get()
        hour_gap = self.widget.entry_gap["hour"].get() or 0
        minute_gap = self.widget.entry_gap["minutes"].get() or 0
        seconds_gap = self.widget.entry_gap["seconds"].get() or 0
        if distance_gap and (hour_gap or minute_gap or seconds_gap):
            try:
                distance_gap = int(distance_gap)
                hour_gap = int(hour_gap)
                minute_gap = int(minute_gap)
                seconds_gap = int(seconds_gap)

                total_seconds = (hour_gap * 3600) + (minute_gap * 60) + seconds_gap
                pace_seconds = (total_seconds * 100) / distance_gap
                minutes = int(pace_seconds // 60)
                seconds_left = int(pace_seconds % 60)
                self.result = f"0{minutes:01d}:{seconds_left:02d} min/100mts"

                self.result_entry = self.widget.create_result_gap(result_gap=self.result)
                self.result_entry.delete(0, "end")
                self.result_entry.insert(0, self.result)

                if not distance_gap:
                    messagebox.showerror(
                        title="Error",
                        message="Distance value is required."
                    )

            except ValueError:
                messagebox.showerror(
                    "Error", "Invalid input. Please enter numbers only."
                )
                return
            except ZeroDivisionError:
                messagebox.showerror(
                    "Error", "Invalid distance. Please enter a distance number"
                )
                return

        self.after(5000, self.swim_pace)

    def update_result(self):
        self.widget.entry_gap["distance"].bind("<Return>", self.swim_pace)
        self.widget.entry_gap["hour"].bind("<Return>", self.swim_pace)
        self.widget.entry_gap["minutes"].bind("<Return>", self.swim_pace)
        self.widget.entry_gap["seconds"].bind("<Return>", self.swim_pace)
        self.after(1000, self.swim_pace)
