import sys # used to exist when player quits the game
import pygame #fucntion that makes the game

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from alien import Alien

import game_functions as gf #from game_function.py

def run_game():#create a screen (how game start)
    alien = Alien(ai_settings,screen)
    ship = Ship(ai_settings, screen)# make a ship
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    pygame.int()
    stats = GameStats(ai_settings)
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                     ai_settings.screen_height))
    

    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen,"Play")

    '''SET BG COLOR''' #RGB colors, red,green, blue range from (0-255)
    bg_color = (230,230,230)#ve specified only ONCE, define BEFORE entering the loop
'''230,230,230 mix equaly of the 3 colors RED GREEN BLUE'''

    ship = Ship(screen) 
    while True: 
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)#game_functions.py
    #how is game being controlled
    if stats.game_active:
        ship.update()
        gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
        gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings, screen,stats, ship, alien, bullets,play_button)

        for bullet in bullets.copy():
            if bullet.rect.bottom<=0:
                bullet.remove(bullet)
        print(len(bullets))
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        '''make the while loop simpler & easier'''
        '''use game_functions instead of run_game()'''

            '''REDRAW the screen'''
        screen.fill(bg_color)#just 1 arg 

    def check_events(ship):

        for event in pygame.event.get(): #keyboard &mouse event
            if event.type==pygame.QUIT:
                sys.exit()#exit the game 

            elif event.type ==pygame.KEYDOWN:
                if event.key ==pygame.K_RIGHT:#move to right
                    
                    ship.rect.centerx +=1 #move by increasing values

        screen.fill(ai_settings.bg_color)
    def update_screen(ai_settings,screen,ship,aliens,bullets):
        ship.blitme()
        aliens.draw(screen)

        pygame.display.flip()#make the last drawn visible, draw new screen every time and removes the old screen
        #update the display to show the new elements and hide the old ones.
run_game()#initial the game and start the main loop

'''load image is bilt()'''





