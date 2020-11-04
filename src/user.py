heightScreen = 500
ia_bar_pos = 15

class user():
    def __init__(self):
        return

    def get_pos(self):
        return

    def get_speed(self):
        return

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