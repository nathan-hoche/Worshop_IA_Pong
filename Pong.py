import os
import tkinter as tk
from tkinter import ttk

gui = tk.Tk()
gui.geometry("800x500")
gui.resizable(width=False, height=False)
gui.title("Workshop Pong")
gui['background'] = "#000000"

if "nt" == os.name:
    gui.wm_iconbitmap(bitmap = "@image/logo.ico")
else:
    gui.wm_iconbitmap(bitmap = "@image/logo.xbm")

gui.mainloop()