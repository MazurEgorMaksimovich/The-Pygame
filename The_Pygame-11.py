import pygame
import random
import sys
from pygame.sprite import Sprite

class The_Letal_Lovets_Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1050, 700))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("The Letal Lovets Game")
        self.bg_color = (230, 230, 230)
        self.active_game = True
        self.allowed_misses = 3

        self.lovets = The_Lovets(self)
        self.potato_balls = pygame.sprite.Group()
        self._create_potato()
    
    def run_game(self):
        while True:
            self._check_events()
            if self.active_game:
                self.lovets.update()
                self._potato_falling()
            self.screen.fill(self.bg_color)
            self.lovets.blitme()
            self.potato_balls.draw(self.screen)
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
        if event.key == pygame.K_LEFT:
            self.lovets.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.lovets.moving_right = True
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.lovets.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.lovets.moving_right = False
    
    def _create_potato(self):
        potato = Potato_Ball(self)
        self.potato_balls.add(potato)
    
    def _potato_falling(self):
        for potato in self.potato_balls.sprites():
            potato.y += 0.5
            potato.rect.y = potato.y
        if pygame.sprite.spritecollideany(self.lovets, self.potato_balls): 
            self._potato_in_the_box()
        self._check_potatoes_bottom()
    
    def _check_potatoes_bottom(self):
        screen_rect = self.screen.get_rect()
        for potato in self.potato_balls.sprites():
            if potato.rect.bottom >= screen_rect.bottom:
                self._miss_the_potato()
                break
    
    def _potato_in_the_box(self):
        self.potato_balls.empty()
        self._create_potato()
    
    def _miss_the_potato(self):
        if self.allowed_misses > 0:
            self.allowed_misses -= 1
            self.potato_balls.empty()
            self._create_potato()
        else:
            self.active_game = False
    
class The_Lovets():
    def __init__(self, ai_game):    
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/yaytsa_volka.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1.5
        if self.moving_left and self.rect.left > 0:
            self.x -= 1.5
        
        self.rect.x = self.x
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Potato_Ball(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/little_little_potato.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.x = random.randint(0, 1000)

        self.y = float(self.rect.y)

tllg = The_Letal_Lovets_Game()
tllg.run_game()