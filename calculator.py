import tkinter as tk
from tkinter import messagebox


class VelocityCalculator:
    def __init__(self, window: tk.Tk, geometry: str = "400x300") -> None:
        self.window = window
        self.window.title("Triathlon Calculator")
        self.window.geometry(geometry)

        self._create_category_labels()
        self._create_label_entry_fields()
        self._create_entry_fields()
        self._create_result_field()

    def _create_category_labels(self):
        labels = [
            ("Distance", 0.04),
            ("Time", 0.17),
            ("Velocity", 0.35)
        ]

        for label_text, rely_value in labels:
            label = tk.Label(
                self.window, text=label_text, bg="PaleTurquoise2"
            )
            label.place(
                relx=0.05, rely=rely_value, relwidth=0.23, relheight=0.1
            )

    def _create_label_entry_fields(self):
        labels = [
            ("meters", 0.6, 0.04, 0.13),
            ("h", 0.41, 0.17, 0.06),
            ("min", 0.545, 0.17, 0.06),
            ("secs", 0.71, 0.17, 0.06)
        ]

        for label_text, relx_value, rely_value, relwidht_value in labels:
            label = tk.Label(self.window, text=label_text)
            label.place(
                relx=relx_value, rely=rely_value,
                relwidth=relwidht_value, relheight=0.1
            )

    def _create_entry_fields(self):
        self.entry_fields = {}
        entries = [
            ("distance", 0.35, 0.04, 0.22),
            ("hour", 0.35, 0.17, 0.06),
            ("minute", 0.47, 0.17, 0.06),
            ("seconds", 0.63, 0.17, 0.06)
        ]

        for name, relx_value, rely_value, relwidt_value in entries:
            entry = tk.Entry(self.window, bg="khaki1")
            entry.place(
                relx=relx_value, rely=rely_value,
                relwidth=relwidt_value, relheight=0.1
            )
            self.entry_fields[name] = entry

    def _create_result_field(self):
        self.calculator = tk.Button(
            self.window, text="Calculate", command=self._swim_pace
        )
        self.calculator.place(
            relx=0.7, rely=0.6, relwidth=0.20, relheight=0.1
        )

        self.velocity_result = tk.Entry(self.window, bg="khaki1")
        self.velocity_result.place(
            relx=0.35, rely=0.35, relwidth=0.44, relheight=0.1
        )

    def _swim_pace(self):
        try:
            distance_field = int(self.entry_fields["distance"].get())
            hour_field = int(self.entry_fields["hour"].get() or 0)
            minute_field = int(self.entry_fields["minute"].get() or 0)
            seconds_field = int(self.entry_fields["seconds"].get() or 0)

        except ValueError:
            messagebox.showerror(
                "Error", "Invalid input. Please enter numbers only."
            )
            return

        total_seconds = (hour_field * 3600) + (minute_field * 60) + seconds_field
        pace_seconds = (total_seconds * 100) / distance_field
        minutes = int(pace_seconds // 60)
        seconds_left = int(pace_seconds % 60)
        result = f"0{minutes:01d}:{seconds_left:02d} min/100mts"
        # Clear the current content of the velocity entry field
        self.velocity_result.delete(0, "end")
        # Insert the calculated result at the beginning of the velocity entry field
        str(self.velocity_result.insert(0, result))


if __name__ == "__main__":
    window = tk.Tk()
    calcula = VelocityCalculator(window)
    window.mainloop()
