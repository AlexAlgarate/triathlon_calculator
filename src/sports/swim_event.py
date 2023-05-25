import tkinter as tk
from tkinter import messagebox
from typing import Dict, Tuple


class Swim(tk.Tk):
    def __init__(self, title: str, size: Tuple[int, int]):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.maxsize(size[0], size[1])

        self.create_menu_label()
        self.create_label_entry_gap()
        self.create_entry_gap()
        self.create_distance_buttons()
        self.create_result_frame()
        self.close_window_button()

        self.entry_gap["distance"].bind("<Return>", self.swim_pace)
        self.entry_gap["hour"].bind("<Return>", self.swim_pace)
        self.entry_gap["minute"].bind("<Return>", self.swim_pace)
        self.entry_gap["seconds"].bind("<Return>", self.swim_pace)
        self.after(5000, self.swim_pace)
        self.mainloop()

    def create_menu_label(self):
        MenuLabel(self, text="Distance", rely_value=0.18, background="PaleTurquoise2")
        MenuLabel(self, text="Time", rely_value=0.33, background="PaleTurquoise2")
        MenuLabel(self, text="Speed", rely_value=0.65, background="PaleTurquoise2")

    def create_label_entry_gap(self):
        EntryLabel(self, text="meters", relx_value=0.6, rely_value=0.18, relwidth_value=0.13)
        EntryLabel(self, text="h", relx_value=0.41, rely_value=0.33, relwidth_value=0.06)
        EntryLabel(self, text="min", relx_value=0.545, rely_value=0.33, relwidth_value=0.06)
        EntryLabel(self, text="secs", relx_value=0.71, rely_value=0.33, relwidth_value=0.06)

    def create_entry_gap(self):
        self.entry_gap = {}
        entries = [
            EntryGap(
                self,
                name="distance",
                background="khaki1",
                relx_value=0.35,
                rely_value=0.18,
                relwidth_value=0.22,
            ),
            EntryGap(
                self,
                name="hour",
                background="khaki1",
                relx_value=0.35,
                rely_value=0.33,
                relwidth_value=0.06,
            ),
            EntryGap(
                self,
                name="minute",
                background="khaki1",
                relx_value=0.47,
                rely_value=0.33,
                relwidth_value=0.06,
            ),
            EntryGap(
                self,
                name="seconds",
                background="khaki1",
                relx_value=0.63,
                rely_value=0.33,
                relwidth_value=0.06,
            )
        ]
        for item in entries:
            entry = item
            self.entry_gap[entry.name] = entry

    def create_distance_buttons(self):
        distances = [
            ("Sprint", 750),
            ("Olympic", 1500),
            ("Half Ironman", 1900),
            ("Ironman", 3800),
        ]
        self.selected_distance = tk.StringVar(value=" ")

        distance_frame = tk.Frame(self)
        distance_frame.place(relx=0.15, rely=0.04, relwidth=0.6, relheight=0.06)

        for i, (button_text, distance_value) in enumerate(distances):
            button = tk.Radiobutton(
                distance_frame,
                text=button_text,
                variable=self.selected_distance,
                value=str(distance_value),
                command=self.set_distance,
            )
            button.pack(side="left", padx=5)

    def set_distance(self):
        distance_value = self.selected_distance.get()
        self.entry_gap["distance"].delete(0, "end")
        self.entry_gap["distance"].insert(0, distance_value)

    def create_result_frame(self):
        self.calculator = tk.Button(self, text="Calculate", command=self.swim_pace)
        self.calculator.place(relx=0.75, rely=0.65, relwidth=0.20, relheight=0.1)
        self.speed_result = ResultGap(self, background="khaki1")
        self.result_label = tk.Label(self)

    def swim_pace(self):
        try:
            self.after(1000, self.swim_pace)
            distance_gap = int(self.entry_gap["distance"].get())
            hour_gap = int(self.entry_gap["hour"].get() or 0)
            minute_gap = int(self.entry_gap["minute"].get() or 0)
            seconds_gap = int(self.entry_gap["seconds"].get() or 0)

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numbers only.")
            return

        total_seconds = (hour_gap * 3600) + (minute_gap * 60) + seconds_gap
        pace_seconds = (total_seconds * 100) / distance_gap
        minutes = int(pace_seconds // 60)
        seconds_left = int(pace_seconds % 60)
        result = f"0{minutes:01d}:{seconds_left:02d} min/100mts"

        self.result_label.config(text=result, background="khaki1")
        self.result_label.place(relx=0.45, rely=0.49, relwidth=0.3, relheight=0.1)

        self.speed_result.delete(0, "end")
        self.speed_result.insert(0, result)

    def close_window_button(self):
        CloseWindowButton(self, button_text="Close", root=self.winfo_toplevel())


class ResultGap(tk.Entry):
    def __init__(
        self,
        parent,
        background: str
    ):
        place_parameter: Dict[str, float] = {
            "relx": 0.35,
            "rely": 0.65,
            "relwidth": 0.35,
            "relheight": 0.1
        }
        super().__init__(parent, background=background)
        self.place(
            relx=place_parameter["relx"],
            rely=place_parameter["rely"],
            relwidth=place_parameter["relwidth"],
            relheight=place_parameter["relheight"]
        )


class MenuLabel(tk.Label):
    def __init__(
        self,
        parent,
        text: str,
        background: str,
        rely_value: float
    ):
        place_parameter: Dict[str, float] = {
            "relx": 0.05,
            "relwidth": 0.23,
            "relheight": 0.1
        }
        super().__init__(parent, text=text, background=background)
        self.place(
            relx=place_parameter["relx"],
            rely=rely_value,
            relwidth=place_parameter["relwidth"],
            relheight=place_parameter["relheight"])


class EntryLabel(tk.Label):
    def __init__(
        self,
        parent,
        text: str,
        relx_value: float,
        rely_value: float,
        relwidth_value: float,
    ):
        super().__init__(parent, text=text)
        self.place(
            relx=relx_value, rely=rely_value, relwidth=relwidth_value, relheight=0.1
        )


class EntryGap(tk.Entry):
    def __init__(
        self,
        parent,
        name: str,
        background: str,
        relx_value: float,
        rely_value: float,
        relwidth_value: float,
    ):
        super().__init__(parent, background=background)
        self.place(relx=relx_value, rely=rely_value, relwidth=relwidth_value, relheight=0.1)
        self.name = name


class CloseWindowButton(tk.Button):
    def __init__(self, parent, button_text: str, root):
        place_parameter: Dict[str, float] = {
            "relx": 0.85,
            "rely": 0.85,
            "relheight": 0.1,
            "relwidth": 0.10
        }
        super().__init__(parent, text=button_text, command=lambda: self._close_window(root))
        self.place(
            relx=place_parameter["relx"],
            rely=place_parameter["rely"],
            relheight=place_parameter["relheight"],
            relwidth=place_parameter["relwidth"]
        )

    def _close_window(self, root):
        root.destroy()


if __name__ == "__main__":
    Swim(title="Swim Calculator", size=(600, 350))
