import tkinter as tk
from typing import Dict


class CloseWindowButton(tk.Button):
    def __init__(self, parent: tk.Tk, button_text: str, root: tk.Tk) -> None:
        place_parameter: Dict[str, float] = {
            "relx": 0.85,
            "rely": 0.85,
            "relheight": 0.1,
            "relwidth": 0.1,
        }
        super().__init__(
            parent, text=button_text, command=lambda: self._close_window(root)
        )
        self.place(
            relx=place_parameter["relx"],
            rely=place_parameter["rely"],
            relheight=place_parameter["relheight"],
            relwidth=place_parameter["relwidth"],
        )

    def _close_window(self, root: tk.Tk) -> None:
        root.destroy()
