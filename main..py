import tkinter as tk
from typing import Tuple

from src.sports import cycling, run, swim


class MainMenu(tk.Tk):
    def __init__(self, title: str, size: Tuple[int, int] = (400, 300)) -> None:
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.maxsize(size[0], size[0])

        self._create_buttons()

        self.mainloop()

    def _create_buttons(self):
        swim_button = tk.Button(
            self, text="Swimming", command=self._open_swim_calculator
        )
        swim_button.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.1)

        cycling_button = tk.Button(
            self, text="Cycling", command=self._open_cycling_calculator
        )
        cycling_button.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)

        run_button = tk.Button(
            self, text="Running", command=self._open_run_calculator
        )
        run_button.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.1)

    def _open_swim_calculator(self):
        self.withdraw()  # Ocultar la ventana principal
        swim_window = tk.Toplevel(self)
        swim.SwimCalculator(swim_window)

    def _open_cycling_calculator(self):
        # self.withdraw()  # Ocultar la ventana principal
        cycling_window = tk.Toplevel(self)
        cycling.CyclingCalculator(cycling_window)

    def _open_run_calculator(self):
        self.withdraw()  # Ocultar la ventana principal
        run_window = tk.Toplevel(self)
        run.RunCalculator(run_window)


if __name__ == "__main__":
    MainMenu(title="Main Menu")
