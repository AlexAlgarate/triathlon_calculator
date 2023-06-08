import tkinter as tk


class EntryGap(tk.Entry):
    def __init__(
        self,
        parent: tk.Tk,
        name: str,
        background: str,
        relx_value: float,
        rely_value: float,
        relwidth_value: float,
    ) -> None:
        super().__init__(parent, background=background)
        self.place(
            relx=relx_value, rely=rely_value, relwidth=relwidth_value, relheight=0.1
        )
        self.name: str = name
