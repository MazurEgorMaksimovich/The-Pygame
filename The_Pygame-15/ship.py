import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Класс для управления кораблём."""

    def __init__(self, ai_game):
        """Инициализирует корабль, задаёт его начальную позицию."""
        super().__init__()
        self.settings = ai_game.settings      
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и загружает его через прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        #Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)

        # Флаг перемещения.
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Обновляет позицию корабля с учётом флага."""
        #Обновляется атрибут х, а не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #Обновление атрибута rect на основании х
        self.rect.x = self.x
    
    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижнего края экрана."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)