import tkinter as tk
from typing import Dict


class MenuLabel(tk.Label):
    def __init__(
        self, parent: tk.Tk, text: str, background: str, rely_value: float
    ) -> None:
        place_parameter: Dict[str, float] = {
            "relx": 0.05,
            "relwidth": 0.23,
            "relheight": 0.1,
        }
        super().__init__(parent, text=text, background=background)
        self.place(
            relx=place_parameter["relx"],
            rely=rely_value,
            relwidth=place_parameter["relwidth"],
            relheight=place_parameter["relheight"],
        )
