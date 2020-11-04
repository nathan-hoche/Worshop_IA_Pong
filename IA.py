from src.user import user

class launch_ia():
    def __init__(self):
        self.info = user()
        self.nb = 10
        return

    def program_IA(self):
        if (self.nb != 0):
            self.info.down_ia_bar()
            self.nb -= 1
            print(self.info.get_speed())
            print(self.info.get_pos())
        return