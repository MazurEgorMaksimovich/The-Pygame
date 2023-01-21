import pygame
import sys

class Potato_in_the_Middle:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1050, 700))
        pygame.display.set_caption("Potato in the Middle")
        self.bg_color = (200, 200, 200)

        self.potato = Potato(self)
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.potato.blitme()
            pygame.display.flip()

class Potato():

    def __init__(self, ai_game):    
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/potato.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

pitm = Potato_in_the_Middle()
pitm.run_game()