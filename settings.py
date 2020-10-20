'''store all the settings in one place'''
class Settings (): #store
    def _init_(self):
        self.screen_width = 1200
        self.screen_height =800
        self.bg_color = (230,230,230)
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height =15
        self.bullet_color = 60,60,60
        #bullet travels slower than the ship
        self.bullets_allowed =3
        #SHIP SETTINGS:
        self.ship_spped_factor = 1.5 #50% faster 
        
