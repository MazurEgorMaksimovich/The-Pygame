import pygame
import sys

class BlueDeathScreen:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1050, 700))
        pygame.display.set_caption("Blue Death Screen")
        self.bg_color = (0, 0, 250)
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()

bds = BlueDeathScreen()
bds.run_game()