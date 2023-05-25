import tkinter as tk
from src.sports import cycling


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MAIN WINDOW")
        self.geometry("400x200")

        swim_button = tk.Button(self, text="swimming", command=self.open_swim_window)
        swim_button.pack(pady=20)

        ride_button = tk.Button(self, text="ride", command=self.open_cycling)
        ride_button.pack(pady=20)

        destroy_button = tk.Button(self, text="close", command=self.close_window)
        destroy_button.pack(pady=50)

    def open_swim_window(self):
        swim_app = Swim("Swim Calculator", (600, 250))
        swim_app.run()

    def open_cycling(self):
        ride = tk.Toplevel(self)
        cycling.CyclingCalculator(ride)

    def close_window(self):
        self.destroy()


window = MainWindow()
window.mainloop()
