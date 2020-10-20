'''PURPOSE: shorten the main py file, eaier to follow'''

import sys 
import pygame
from bullet import bullet


def check_keydown_events(event, ai_settings,screen,ship,bullets):
    elif event.key ==pygame.K_SPACE:
        if len(bullets)<ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
        
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
def update_screen(ai_settings, screen,ship, bullets):
    for bullet in bullets.sprites():
        bullets.draw_bullet()
        def check_keydown_events(event,ship):
            if event.key ==pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key ==pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        def check_keyup_events(event,ship):
            if event.key ==pygame.KRIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
                ship.rect.centerx +=1


def update_screen(ai_settings, screen, ship):#then update the while loop from main file


