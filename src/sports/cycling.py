import tkinter as tk
from tkinter import messagebox


class CyclingCalculator:
    def __init__(self, window: tk.Tk, geometry: str = "600x300") -> None:
        """
        Initializes the speedCalculator class.

        Args:
            window (tk.Tk): The main window of the application.
            geometry (str): The initial size of the window (default is "400x300").
        """
        self.window = window
        self.window.title("Triathlon Calculator")
        self.window.geometry(geometry)

        self._create_category_labels()
        self._create_label_entry_fields()
        self._create_entry_fields()
        self._create_distance_buttons()
        self._create_result_field()

    def _create_category_labels(self):
        """
        Creates the category labels (Distance, Time, Speed) in the GUI window.
        """
        labels = [
            ("Distance", 0.11),
            ("Time", 0.24),
            ("Speed", 0.42)
        ]

        for label_text, rely_value in labels:
            label = tk.Label(
                self.window, text=label_text, bg="PaleTurquoise2"
            )
            label.place(
                relx=0.05, rely=rely_value, relwidth=0.23, relheight=0.1
            )

    def _create_label_entry_fields(self):
        """
        Creates the label entry fields (meters, h, min, secs) in the GUI window.
        """
        labels = [
            ("km", 0.6, 0.11, 0.13),
            ("h", 0.41, 0.24, 0.06),
            ("min", 0.545, 0.24, 0.06),
            ("secs", 0.71, 0.24, 0.06)
        ]

        for label_text, relx_value, rely_value, relwidht_value in labels:
            label = tk.Label(self.window, text=label_text)
            label.place(
                relx=relx_value, rely=rely_value,
                relwidth=relwidht_value, relheight=0.1
            )

    def _create_entry_fields(self):
        """
        Creates the entry fields for user input in the GUI window.
        """
        self.entry_fields = {}
        entries = [
            ("distance", 0.35, 0.11, 0.22),
            ("hour", 0.35, 0.24, 0.06),
            ("minute", 0.47, 0.24, 0.06),
            ("seconds", 0.63, 0.24, 0.06)
        ]

        for name, relx_value, rely_value, relwidt_value in entries:
            entry = tk.Entry(self.window, bg="khaki1")
            entry.place(
                relx=relx_value, rely=rely_value,
                relwidth=relwidt_value, relheight=0.1
            )
            self.entry_fields[name] = entry

    def _create_result_field(self):
        """
        Creates the result field and calculate button in the GUI window.
        """
        self.calculator = tk.Button(
            self.window, text="Calculate", command=self._cycling_speed
        )
        self.calculator.place(
            relx=0.7, rely=0.6, relwidth=0.20, relheight=0.1
        )

        self.speed_result = tk.Entry(self.window, bg="khaki1")
        self.speed_result.place(
            relx=0.35, rely=0.42, relwidth=0.35, relheight=0.1
        )

    def _create_distance_buttons(self):
        distances = [
            ("Sprint", 20),
            ("Olympic", 40),
            ("Half Ironman", 90),
            ("Ironman", 180)
        ]
        # Assign an initial empty value
        self.selected_distance = tk.StringVar(value=" ")

        distance_frame = tk.Frame(self.window)
        distance_frame.place(
            relx=0.15, rely=0.04, relwidth=0.6, relheight=0.06
        )
        for i, (button_text, distance_value) in enumerate(distances):
            button = tk.Radiobutton(
                distance_frame, text=button_text,
                variable=self.selected_distance,
                value=str(distance_value),
                command=self._set_distance
            )
            button.pack(side="left", padx=5)

    def _set_distance(self):
        distance_value = self.selected_distance.get()
        self.entry_fields["distance"].delete(0, "end")
        self.entry_fields["distance"].insert(0, distance_value)

    def _cycling_speed(self):
        """
        Calculates the cycling speed based on the user input and displays the result.

        This method is called when the "Calculate" button is clicked.
        """
        try:
            distance_field = float(self.entry_fields["distance"].get())
            hour_field = float(self.entry_fields["hour"].get() or 0)
            minute_field = float(self.entry_fields["minute"].get() or 0)
            seconds_field = float(self.entry_fields["seconds"].get() or 0)

        except ValueError:
            messagebox.showerror(
                "Error", "Invalid input. Please enter numbers only."
            )
            return

        total_hour = hour_field + (minute_field / 60) + (seconds_field / 3600)
        speed = distance_field / total_hour
        result = f"{speed:.2f} km/h"

        # Clear the current content of the speed entry field
        self.speed_result.delete(0, "end")
        # Insert the calculated result at the beginning of the speed entry field
        self.speed_result.insert(0, result)


if __name__ == "__main__":
    window = tk.Tk()
    CyclingCalculator(window)
    window.mainloop()
