'''PURPOSE: shorten the main py file, eaier to follow'''

import sys 
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien 

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height) - (3* alien_height) - ship_height)
    number_rows = int(available_space_y/(2* alien_height))
    return number_rows

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    if stats.ships_left >0:
    stats.ships_left -=1
    aliens.empty()
    bullets.empty()
    ai_settings.increase_speed()

    create_fleet(ai_settings, screen,ship,aliens)
    ship.center_ship()

    sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)





def check_keydown_events(event, ai_settings,screen,ship,bullets):
    elif event.key ==pygame.K_SPACE:
        fire_bullet(ai_settings, screen,ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets)<ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


        
def check_events(ai_settings, screen, play_button, ship,aliens, bullets):
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y)
            check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)
def check_play_button(ai_settings,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
        if button_clicked and not stats.game_active:
            ai_settings.initialzie_dynamic_settings()
            pygame.mouse.set_visible(False)
        stats.rest_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
def update_screen(ai_settings, screen,stats,ship, alien,bullets,play_button):
    for bullet in bullets.sprites():
        bullets.draw_bullet()
    ship.blitme()
    alien.blitme()
    if not stats.game_active:
        play_buton.draw_button()
    pygame.display.flip()
    
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
def create_fleet(ai_settings, screen, ship,aliens):
    alien = Alien (ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    alien_width = alien.rect.alien_width
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    
def get_number_aliens_x(ai_settings, alien_width):
    available_space_x =ai_settings.screen_width -2 *alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number,row_number):
    for row_number in range(number_rows):   
         
        for alien_number in range (number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
            alien = Alien(ai_settings, screen)
            alien_width = alien.rect.width
            alien.x = alien_width +2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height +2 * alien.rect.height *row_number
            alien.add(alien)

def update_bullets(ai_settings, screen, ship, bullets):
    if len(aliens)==0
    bullets.empty()
    create_fleet(ai_settings, screen, ship, aliens)
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
def check_bullet_alien_collisions(ai_settings, screen, ship,aliens,bullets):
    collisions = pygame.sprite.groupchlllide(bullets,aliens,True,True)
    if len (aliens)==0:
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
        print("Ship hit!!!")
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)
def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break

