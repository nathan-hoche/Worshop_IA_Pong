import os
import random
import tkinter as tk
from tkinter import Canvas
from IA import launch_ia
from src.user import program_init_user

widthScreen = 800
heightScreen = 500

IA_params = program_init_user()

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

    def get_pos_bar(self):
        return self.PosXStart

    def init_canvas(self, canvas):
        self.canvas = canvas
        self.racket_user = canvas.create_rectangle(self.PosX, self.PosY, self.PosX + 20, self.PosY + 100, fill='white')

# Bar IA
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

    def get_pos_bar(self):
        return self.PosXStart

    def init_canvas(self, canvas):
        self.canvas = canvas
        self.racket_user = canvas.create_rectangle(self.PosX, self.PosY, self.PosX + 20, self.PosY + 100, fill='white')

# IA ball
class ia_ball():
    def __init__(self):
        self.PosXStart = 15
        self.canvas = None
        self.ball = None
        self.PosX = widthScreen / 2 - 10
        self.PosY = heightScreen / 2 - 10
        self.speed = [8, -8]

    def move_ball(self):
        self.canvas.move(self.ball, self.speed[0], self.speed[1])
        self.PosX += self.speed[0]
        self.PosY += self.speed[1]

    def check_wall_rebound(self):
        if (self.PosY <= 0 or self.PosY >= heightScreen - 40):
            self.speed[1] *= -1
        
    def check_ball_user_contact(self, PosX, PosY):
        if (PosX <= self.PosY and self.PosY <= PosX + 100 
        and PosY <= self.PosX and self.PosX <= PosY + 24):
            if (random.randrange(0, 1) == 0):
                self.speed[0] = 8 + random.randint(0, 4)
                self.speed[1] = -8 - random.randint(0, 4)
            else:
                self.speed[0] = 8 + random.randint(0, 4)
                self.speed[1] = 8 + random.randint(0, 4)

    def get_pos_ball(self):
        return [self.PosX, self.PosY]

    def get_speed_ball(self):
        return self.speed

    def check_ball_ia_contact(self, PosX, PosY):
        if (PosX <= self.PosY and self.PosY <= PosX + 100 
        and PosY -24 <= self.PosX  and self.PosX <= PosY + 24):
            self.speed[0] *= -1
            self.speed[1] *= -1

    def init_canvas(self, canvas):
        self.canvas = canvas
        self.ball = canvas.create_oval(self.PosX, self.PosY, self.PosX + 20, self.PosY + 20, fill='white')


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
user_bar = user_bar()
canvas.bind('<Key>', user_bar.KeyBoard)
user_bar.init_canvas(canvas)

# Ball
ia_ball = ia_ball()
ia_ball.init_canvas(canvas)

# IA
ia_bar = ia_bar()
ia_bar.init_canvas(canvas)
IA_prog = launch_ia()

def game_loop():
    IA_prog.program_IA()
    new_ia_bar_pos = IA_params.get_ia_bar_pos()
    ia_bar.change_bar_pos(new_ia_bar_pos)

    ia_ball.check_wall_rebound()
    ia_ball.check_ball_user_contact(user_bar.get_pos_bar(), 15)
    ia_ball.check_ball_ia_contact(ia_bar.get_pos_bar(), 745)

    IA_params.set_ball_pos(ia_ball.get_pos_ball())
    IA_params.set_ball_speed(ia_ball.get_speed_ball())
    ia_ball.move_ball()

    gui.after(75, game_loop)

gui.after_idle(game_loop)
gui.mainloop()