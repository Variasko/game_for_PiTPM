from pygame import *
from pygame.sprite import Sprite as s

class Bullet(s):
    def __init__(self, setting, screen, ship):
         """Создает объект пули в текущей позиции корабля."""
         super(Bullet, self).__init__()
         self.screen = screen
         self.rect = Rect(0, 0, setting.bullet_w, setting.bullet_h)
         self.rect.centerx = ship.rect.centerx
         self.rect.top = ship.rect.top
         self.y = float(self.rect.y)
         self.color = setting.bullet_color
         self.speed_factor = setting.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        draw.rect(self.screen, self.color, self.rect)