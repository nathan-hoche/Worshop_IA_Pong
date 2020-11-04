obj_ball = None
heightScreen = 500
ia_bar_pos = 0

class user():
    def __init__(self):
        return

    def get_pos(self):
        return obj_ball.get_ball_pos()

    def get_speed(self):
        return obj_ball.get_ball_speed()

    def get_bar_pos(self):
        global ia_bar_pos
        return ia_bar_pos

    def up_ia_bar(self):
        global ia_bar_pos
        if (ia_bar_pos >= heightScreen + 30):
            ia_bar_pos -= 30

    def down_ia_bar(self):
        global ia_bar_pos
        if (ia_bar_pos <= heightScreen - 130):
            ia_bar_pos += 30

class program_init_user():
    def __init__(self):
        return

    def init_obj_ball(self, ball):
        global obj_ball
        obj_ball = ball

    def change_ia_bar_pos(self, y):
        global ia_bar_pos
        ia_bar_pos = y