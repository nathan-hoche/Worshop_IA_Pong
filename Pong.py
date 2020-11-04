import os
import tkinter as tk
from tkinter import Canvas

gui = tk.Tk()
gui.geometry("800x500")
gui.resizable(width=False, height=False)
gui.title("Workshop Pong")
gui['background'] = "#000000"

if "nt" == os.name:
    gui.wm_iconbitmap(bitmap = "@image/logo.ico")
else:
    gui.wm_iconbitmap(bitmap = "@image/logo.xbm")

PosX = 60
PosY = 10
PosX2 = 200
PosY2 = 480
dx = 10
dy = 7

def update():

    def KeyBoard(event):
        Key = event.keysym

        if Key == 'Right':
            canvas.move(raquette,30,0)
        if Key == 'Left':
            canvas.move(raquette,-30,0)

    canvas = Canvas(gui,width = 500, height = 500 , bd=0, bg="grey")
    canvas.pack(padx=10,pady=10)

    raquette = canvas.create_rectangle(PosX2,PosY2,PosX2+100,PosY2+10,fill='black')


    canvas.focus_set()
    canvas.bind('<Key>',KeyBoard)

    gui.mainloop()

update()