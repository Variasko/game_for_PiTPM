from sys import *
import pygame
from bullet import Bullet

def check_events(ship, setting, screen, bullets):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_d:
                ship.moving_right = True
            elif e.key == pygame.K_a:
                ship.moving_left = True
            elif e.key == pygame.K_SPACE:
                if len(bullets) < setting.bullets_allowed:
                    new_bullet = Bullet(setting, screen, ship)
                    bullets.add(new_bullet)

        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_d:
                ship.moving_right = False
            if e.key == pygame.K_a:
                ship.moving_left = False



def update_screen(screen, ship, setting, bullets):
    screen.fill(setting.bg)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()
