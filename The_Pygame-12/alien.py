import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс для одного пишельца."""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задаёт его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Загружаем изображение.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Каждый новый пришелец появляется слева сверху.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Сохраняем х пришельца.
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Возвращает True если инопришеленец у края."""
        sreen_rect = self.screen.get_rect()
        if self.rect.right >= sreen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Перемещает инопришеленца."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x