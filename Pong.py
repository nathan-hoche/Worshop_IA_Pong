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

PosX = 15
PosY = 10

class update():
    self.PosXStart = 15

    def KeyBoard(self, event):
        Key = event.keysym

        if Key == 'Up' and PosXStart >= 30:
            canvas.move(racket, 0, -30)
            PosXStart -= 30
        if Key == 'Down' and PosXStart <= 470:
            canvas.move(racket, 0, 30)
            PosXStart += 30

    canvas = Canvas(gui, width = widthScreen, height = heightScreen, bd = 0, bg = "grey")
    canvas.pack(padx = 10, pady = 10)

    racket = canvas.create_rectangle(PosX, PosY, PosX + 20, PosY + 125, fill='red')


    canvas.focus_set()
    canvas.bind('<Key>',KeyBoard)

    gui.mainloop()

update()