import pygame
import sys

class The_Rocket_Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1050, 700))
        pygame.display.set_caption("Blue Death Screen")
        self.bg_color = (230, 230, 230)

        self.rocket = The_Rocket(self)
    
    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self.screen.fill(self.bg_color)
            self.rocket.blitme()
            pygame.display.flip()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
    
    
class The_Rocket():
    def __init__(self, ai_game):    
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1.5
        if self.moving_left and self.rect.left > 0:
            self.x -= 1.5
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1.5
        if self.moving_up and self.rect.top > 0:
            self.y -= 1.5
        
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

trg = The_Rocket_Game()
trg.run_game()