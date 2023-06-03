class Setting:
    def __init__(self, w, h, bg, title):

        self.bg = bg
        self.h = h
        self.w = w
        self.title = title
        self.bullet_w = 2
        self.bullet_h = 15
        self.bullet_color = (235, 223, 223)
        self.bullet_speed_factor = 1.5
        self.bullets_allowed = 10
