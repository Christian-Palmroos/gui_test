#!/home/chospa/anaconda3/bin/python

import os
import tkinter as tk
from tkinter import ttk
import numpy as np


def main():
    """
    The main function, executed when running as a script.
    """

    main_window = tk.Tk()

    frame = ttk.Frame(main_window, padding=100)
    frame.grid()

    ttk.Label(frame, text="Huutista :D").grid(column=0, row=0)
    ttk.Button(frame, text="Lopeta D:", command=main_window.destroy).grid(column=1, row=0)

    main_window.mainloop()


if __name__ == "__main__":

    main()
