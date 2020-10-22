'''store all the settings in one place'''
class Settings (): #store
    def _init_(self):
        self.screen_width = 1200
        self.screen_height =800
        self.bg_color = (230,230,230)
        self.bullet_speed_factor = 1
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height =15
        self.bullet_color = 60,60,60
        #bullet travels slower than the ship
        self.bullets_allowed =3
        #SHIP SETTINGS:
        self.ship_spped_factor = 1.5 #50% faster 
        self.ship_limit = 3
        self.fleet_drop_speed = 10
        self.alien_speed_factor = 1
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
    def update(self):
        self.x +=self.ai_settings.alien_speed_factor
        self.rect.x = self.x

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor =1
        self.fleet_direction =1

    def increase_speed(self):
        self.ship_speed_factor *=self.speedup_scale
        self.bullet_speed_factor *=self.speedup_scale
        self.alien_speed_factor *=self.speedup_scale
        
        
