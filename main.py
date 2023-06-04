from sys import *
from pygame import *
from settings import Setting
from ship import Ship
from function import *
from bullet import Bullet
from pygame.sprite import Group
from alien import Alien
from stats import GameStats
from buttons import Button

def run_game():
    init()
    setting = Setting(1000, 800, (114, 138, 131), 'Вторжение')

    screen = display.set_mode((setting.w, setting.h))
    display.set_caption(setting.title)

    ship = Ship(screen)

    aliens = Group()

    bullets = Group()

    create_fleet(setting, screen, ship, aliens)

    stats = GameStats(setting)

    play_button = Button(setting, screen, "Play")
    pbr = play_button.rect

    while True:
        check_events(setting, screen, stats, play_button, ship, aliens, bullets, pbr)
        if stats.game_active:
            ship.update()
            bullets.update()
            update_bullets(aliens, bullets, setting, screen, ship)
            update_aliens(aliens, setting, ship, stats, screen, bullets)

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        update_screen(setting, screen, stats, ship, aliens, bullets, play_button)
        display.flip()

run_game()