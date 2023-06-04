class GameStats():


    def __init__(self, settings):

        self.game_active = False

        self.ai_settings = settings
        self.reset_stats()

    def reset_stats(self):

        self.ships_left = self.ai_settings.ship_limit
