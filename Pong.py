import os
import tkinter as tk
from tkinter import Canvas

widthScreen = 800
heightScreen = 500

gui = tk.Tk()
gui.geometry(str(widthScreen) + "x" + str(heightScreen))
gui.resizable(width=False, height=False)
gui.title("Workshop Pong")
gui['background'] = "#000000"

if "nt" == os.name:
    gui.wm_iconbitmap(bitmap = "@image/logo.ico")
else:
    gui.wm_iconbitmap(bitmap = "@image/logo.xbm")

PosX = 60
PosY = 10

def update():

    def KeyBoard(event):
        Key = event.keysym

        if Key == 'Right':
            canvas.move(raquette,30,0)
        if Key == 'Left':
            canvas.move(raquette,-30,0)

    canvas = Canvas(gui, width = widthScreen, height = heightScreen, bd = 0, bg = "grey")
    canvas.pack(padx = 10, pady = 10)

    raquette = canvas.create_rectangle(PosX ,PosY ,PosX + 100,PosY + 20,fill='red')


    canvas.focus_set()
    canvas.bind('<Key>',KeyBoard)

    gui.mainloop()

update()