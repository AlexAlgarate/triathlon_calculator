import tkinter as tk


class EntryLabel(tk.Label):
    def __init__(
        self,
        parent: tk.Tk,
        text: str,
        relx_value: float,
        rely_value: float,
        relwidth_value: float,
    ) -> None:
        super().__init__(parent, text=text)
        self.place(
            relx=relx_value, rely=rely_value, relwidth=relwidth_value, relheight=0.1
        )
