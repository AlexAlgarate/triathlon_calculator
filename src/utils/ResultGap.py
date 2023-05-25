import tkinter as tk
from typing import Dict


class ResultGap(tk.Entry):
    def __init__(self, parent, background: str):
        place_parameter: Dict[str, float] = {
            "relx": 0.35,
            "rely": 0.42,
            "relwidth": 0.35,
            "relheight": 0.1,
        }
        super().__init__(parent, background=background)
        self.place(
            relx=place_parameter["relx"],
            rely=place_parameter["rely"],
            relwidth=place_parameter["relwidth"],
            relheight=place_parameter["relheight"],
        )
