import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления снарядами, выпущеными кораблём."""

    def __init__(self, ai_game):
        """Создаёт объект наряда в текуще позиции корабля."""
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.color = self.settings.bullet_color

        #Создание снаряда и назначение позиции.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Позиция снаряда в вещественном формате.
        self.y = float(self.rect.y)
    
    def update(self):
        """Перемещает снаряд вверх по экрану."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Вывод снаряда на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)