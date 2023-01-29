import pygame
import sys
import random
from pygame.sprite import Sprite

class Stars_Potatoes_Random_Army:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1050, 700))
        pygame.display.set_caption("Stars Potatoes Random Army")
        self.bg_color = (200, 200, 200)

        self.potatoes = pygame.sprite.Group()
        self._create_army()
    
    def _create_army(self):
        potato = Potato(self)
        potato_width, potato_height = potato.rect.size
        available_space_x = 1050
        number_potato_x = available_space_x // (2 * potato_width)

        available_space_y = 700
        number_rows = available_space_y // (2 * potato_height)

        for row_number in range(number_rows):
            for potato_number in range(number_potato_x):
                self._create_potato(potato_number, row_number)
    
    def _create_potato(self, potato_number, row_number):
        potato = Potato(self)
        potato_width, potato_height = potato.rect.size
        potato.x = potato_width + 2 * potato_width * potato_number + random.randint(-15, 15)
        potato.rect.x = potato.x
        potato.rect.y = potato_height + 2 * potato_height * row_number + random.randint(-15, 15)
        self.potatoes.add(potato)
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.potatoes.draw(self.screen)
            pygame.display.flip()

class Potato(Sprite):

    def __init__(self, ai_game):
        super().__init__()    
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/little_potato.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

psra = Stars_Potatoes_Random_Army()
psra.run_game()