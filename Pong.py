import os
import tkinter as tk
from tkinter import Canvas
from src.ball import ball
from IA import launch_ia
from src.user import program_init_user

widthScreen = 800
heightScreen = 500

obj_ball = ball()
IA_params = program_init_user()
IA_params.init_obj_ball(obj_ball)

# Bar player
class user_bar():
    def __init__(self):
        self.PosXStart = 15
        self.canvas = None
        self.racket_user = None
        self.PosX = 15
        self.PosY = 10

    def KeyBoard(self, event):
        Key = event.keysym

        if Key == 'Up' and self.PosXStart >= 30:
            self.canvas.move(self.racket_user, 0, -30)
            self.PosXStart -= 30
        elif Key == 'Down' and self.PosXStart <= heightScreen - 130:
            self.canvas.move(self.racket_user, 0, 30)
            self.PosXStart += 30

    def init_canvas(self, canvas):
        self.canvas = canvas
        self.racket_user = canvas.create_rectangle(self.PosX, self.PosY, self.PosX + 20, self.PosY + 100, fill='white')

class ia_bar():
    def __init__(self):
        self.PosXStart = 15
        self.canvas = None
        self.racket_user = None
        self.PosX = 745
        self.PosY = 10

    def change_bar_pos(self, new_pos):
        if self.PosXStart >= 30 and self.PosXStart > new_pos:
            self.canvas.move(self.racket_user, 0, -30)
            self.PosXStart -= 30
        elif self.PosXStart <= heightScreen - 130 and self.PosXStart < new_pos:
            self.canvas.move(self.racket_user, 0, 30)
            self.PosXStart += 30

    def init_canvas(self, canvas):
        self.canvas = canvas
        self.racket_user = canvas.create_rectangle(self.PosX, self.PosY, self.PosX + 20, self.PosY + 100, fill='white')

# tkinter init
gui = tk.Tk()
gui.geometry(str(widthScreen) + "x" + str(heightScreen))
gui.resizable(width = False, height = False)
gui.title("Workshop Pong")
gui['background'] = "#000000"

if "nt" == os.name:
    gui.wm_iconbitmap(bitmap = "@image/logo.ico")
else:
    gui.wm_iconbitmap(bitmap = "@image/logo.xbm")

# user_bar
canvas = Canvas(gui, width = widthScreen, height = heightScreen, bd = 0, bg = "grey")
canvas.pack(padx = 10, pady = 10)
canvas.focus_set()
info = user_bar()
canvas.bind('<Key>', info.KeyBoard)
info.init_canvas(canvas)

# IA
ia_bar = ia_bar()
ia_bar.init_canvas(canvas)
IA_prog = launch_ia()

def game_loop():
    IA_prog.program_IA()
    new_ia_bar_pos = IA_params.get_ia_bar_pos()
    ia_bar.change_bar_pos(new_ia_bar_pos)
    gui.after(10, game_loop)

gui.after_idle(game_loop)
gui.mainloop()