class ball():
    def __init__(self):
        self.x = 400
        self.y = 250
        self.speed = [0, 0]

    def change_ball_pos(self, x, y):
        self.x = x
        self.y = y

    def check_wall_rebound(self, x_speed, y_speed):
        if (self.y <= 0):
            y_speed *= -1
        elif (self.y >= 800):
            y_speed *= -1
        self.speed = [x_speed, y_speed]
        return x_speed, y_speed

    def get_ball_speed(self):
        return self.speed

    def get_ball_pos(self):
        return self.speed