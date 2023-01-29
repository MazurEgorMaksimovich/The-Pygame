import pygame
import sys
from pygame.sprite import Sprite
from math import ceil

class Dribble_Army_Raining:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1050, 700))
        pygame.display.set_caption("Dribble Army Raining")
        self.bg_color = (200, 200, 200)

        self.dribbles = pygame.sprite.Group()
        self._create_army()
    
    def _create_army(self):
        dribble = Dribble(self)
        dribble_width, dribble_height = dribble.rect.size
        available_space_x = 1050
        number_dribble_x = available_space_x // (2 * dribble_width)
        self.dribbles_in_row = number_dribble_x

        available_space_y = 700
        number_rows = available_space_y // (2 * dribble_height)
        self.rows = number_rows

        for row_number in range(number_rows):
            for dribble_number in range(number_dribble_x):
                self._create_dribble(dribble_number, row_number)
    
    def _create_dribble(self, dribble_number, row_number):
        dribble = Dribble(self)
        dribble_width, dribble_height = dribble.rect.size
        dribble.x = dribble_width + 2 * dribble_width * dribble_number
        dribble.rect.x = dribble.x
        dribble.rect.y = dribble_height + 2 * dribble_height * row_number
        self.dribbles.add(dribble)
    
    def _create_one_row(self, dribble_number, row_number):
        dribble = Dribble(self)
        dribble_width, dribble_height = dribble.rect.size
        dribble.x = dribble_width + 2 * dribble_width * dribble_number
        dribble.rect.x = dribble.x
        dribble.rect.y = 0
        self.dribbles.add(dribble)
    
    def _dribbles_droping(self):
        for dribble in self.dribbles.sprites():
            dribble.rect.y += 1
        for dribble in self.dribbles.copy():
            if dribble.rect.top >= dribble.screen_rect.bottom:
                self.dribbles.remove(dribble)
                self._new_dribble_row()
    
    def _new_dribble_row(self):
        if ceil(len(self.dribbles)/self.dribbles_in_row) < self.rows:
            for dribble_number in range(self.dribbles_in_row):
                self._create_one_row(dribble_number, 1)
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._dribbles_droping()
            self.screen.fill(self.bg_color)
            self.dribbles.draw(self.screen)
            pygame.display.flip()

class Dribble(Sprite):

    def __init__(self, ai_game):
        super().__init__()    
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/dribble.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

dar = Dribble_Army_Raining()
dar.run_game()