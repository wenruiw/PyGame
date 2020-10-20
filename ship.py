'''manage the behavior of the ship'''
import pygame 
class Ship():
    def _int_(self,ai_settings,screen):
        self.screen = screen'''set screen'''
        self.ai_settings = ai_settings
        self.image=pygame.image.load('images/ship.bmp')#load ship get its rect
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
            #start each new ship at the bottom
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.center = float (self.rect.centerx)

        self.moving_right = False 
        self.moving_left= False
    
    def update(self):
        '''UPDATE THE POSITION BASED ON MOVENMENT FLAGS'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
            self.rect.centerx += 1#moving right is True
            #true when right is pressed, false when released
        if self.moving_left and self.rect.left > 0:
            self.center-=self.ai_settings.ship_speed_factor
            self.rect.centerx -= 1
        
        self.rect.centerx = self.center

    def blitme(self):#draw the image to the screen that is specified by se;f.rect
        self.screen.blit(self.image,self.rect) '''draw at current location'''
