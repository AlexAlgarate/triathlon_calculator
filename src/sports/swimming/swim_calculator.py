import tkinter as tk
from tkinter import messagebox
from typing import Tuple

# from WidgetsSwim import WidgetsSwim
from src.sports.swimming.WidgetsSwim import WidgetsSwim


class SwimCalculator(tk.Tk):
    def __init__(self, title: str, size: Tuple[int, int]):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.maxsize(size[0], size[1])

        self.widget = WidgetsSwim(self)
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
                result = f"0{minutes:01d}:{seconds_left:02d} min/100mts"

                self.result_label = tk.Entry(self)
                self.result_label.config(text=result, background="khaki1")
                self.result_label.place(
                    relx=0.35, rely=0.65, relwidth=0.35, relheight=0.1
                )

                self.result_label.delete(0, "end")
                self.result_label.insert(0, result)

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


# if __name__ == "__main__":
#     swim = SwimCalculator("Swim Calculator", (600, 350))
#     swim.mainloop()
