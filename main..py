import tkinter as tk
from src.sports.swim import SwimCalculator


if __name__ == "__main__":
    window = tk.Tk()
    calcula = SwimCalculator(window)
    window.mainloop()
