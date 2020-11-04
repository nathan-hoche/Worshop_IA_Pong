heightScreen = 500
ia_bar_pos = 15
ball_pos = [0, 0]
ball_speed = [0, 0]

class user():
    def __init__(self):
        return

    def get_pos(self):
        global ball_pos
        return ball_pos

    def get_speed(self):
        global ball_speed
        return ball_speed

    def get_bar_pos(self):
        global ia_bar_pos
        return ia_bar_pos

    def up_ia_bar(self):
        global ia_bar_pos
        if (ia_bar_pos >= 30):
            ia_bar_pos -= 30

    def down_ia_bar(self):
        global ia_bar_pos
        if (ia_bar_pos <= heightScreen - 130):
            ia_bar_pos += 30

class program_init_user():
    def __init__(self):
        return

    def get_ia_bar_pos(self):
        global ia_bar_pos
        return ia_bar_pos

    def set_ball_pos(self, pos):
        global ball_pos
        ball_pos = pos

    def set_ball_speed(self, pos):
        global ball_speed
        ball_speed = pos