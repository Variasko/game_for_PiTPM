from sys import *
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep




def check_events(ship, setting, screen, bullets, stats, play_button, aliens, pbr):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

        elif e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(setting, screen, stats, play_button, ship, aliens, bullets, pbr, mouse_x, mouse_y)

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

def check_play_button(setting, screen, stats, play_button, ship, aliens, bullets, pbr, mouse_x, mouse_y):

    if pbr.collidepoint(mouse_x, mouse_y):

        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_fleet(setting, screen, ship, aliens)
        ship.center_ship()

def get_number_aliens_x(ai_settings, alien_width):
    """Вычисляет количество пришельцев в ряду."""
    available_space_x = ai_settings.w - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Создает пришельца и размещает его в ряду."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Создает флот пришельцев."""
    # Создание пришельца и вычисление количества пришельцев в ряду.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    # Создание первого ряда пришельцев.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                         row_number)


def get_number_rows(ai_settings, ship_height, alien_height):

    available_space_y = (ai_settings.h - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (3 * alien_height))
    return number_rows

def update_aliens(aliens, settings, ship, stats, screen, bullets):

    check_fleet_edges(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(settings, stats, screen, ship, aliens,
                        bullets)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):

    if stats.ships_left > 0:
        stats.ships_left -= 1


        aliens.empty()
        bullets.empty()


        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(2)
    else:
        stats.game_active = False

def check_fleet_edges(ai_settings, aliens):

    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:

            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def change_fleet_direction(ai_settings, aliens):

    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_screen(setting, screen, stats, ship, alien, bullets, play_button):
    screen.fill(setting.bg)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def update_bullets(aliens, bullets, settings, screen, ship):

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:

        bullets.empty()
        create_fleet(settings, screen, ship, aliens)
