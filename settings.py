class Setting:
    def __init__(self, w, h, bg, title):

        self.bg = bg
        self.h = h
        self.w = w
        self.title = title

        self.ship_limit = 3

        self.bullet_w = 2
        self.bullet_h = 15
        self.bullet_color = (235, 223, 223)
        self.bullet_speed_factor = 2.5
        self.bullets_allowed = 15


        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
