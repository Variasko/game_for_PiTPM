from sys import *
from pygame import *
from settings import *
from ship import *
from function import *
from bullet import *
from pygame.sprite import Group

def run_game():
    init()
    setting = Setting(1000, 800, (114, 138, 131), 'Вторжение')

    screen = display.set_mode((setting.w, setting.h))
    display.set_caption(setting.title)

    ship = Ship(screen)

    bullets = Group()

    while True:
        check_events(ship, setting, screen, bullets)
        ship.update()
        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        update_screen(screen, ship, setting, bullets)
        display.flip()

run_game()