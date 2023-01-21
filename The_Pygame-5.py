import pygame
import sys
from pygame.sprite import Sprite

class The_Spider_Rocket_Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1050, 700))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("The Spider Rocket Game")
        self.bg_color = (230, 230, 230)

        self.rocket = The_Spider_Rocket(self)
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_bullets()
            self.screen.fill(self.bg_color)
            self.rocket.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
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
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
    
    def _fire_bullet(self):
        if len(self.bullets) < 3:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)
    
    
class The_Spider_Rocket():
    def __init__(self, ai_game):    
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship_on_the_wall.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1.5
        if self.moving_up and self.rect.top > 0:
            self.y -= 1.5
        
        self.rect.y = self.y
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.color = (60, 60, 60)

        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midright = ai_game.rocket.rect.midright

        self.x = float(self.rect.x)
    
    def update(self):
        self.x += 1
        self.rect.x = self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

trg = The_Spider_Rocket_Game()
trg.run_game()