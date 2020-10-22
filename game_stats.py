class GameStats():
    def __int__(self,ai_settings):
    self.ai_settings = ai_settings
    self.rest_stats()

    self.game_active = False
    self.game_active = True
    def rest_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
