import pygame
import sys
from pygame.sprite import Sprite
import pygame.font

class The_Uchenia_Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1050, 700))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("The Uchenia Game")
        self.bg_color = (230, 230, 230)

        self.game_active = False
        self.misses = 0
        self.target_speed = 0.75

        self.rocket = The_Spider_Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)

        self.play_button = Button(self, "Играть")
    
    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                self.rocket.update()
                self._update_bullets()
                self.target_speed += 0.0001
                self.target.update(self.target_speed)
                self._check_hitting_the_target()
            self.screen.fill(self.bg_color)
            self.rocket.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.target.draw_tagret()
            if not self.game_active:
                self.play_button.draw_button()
            pygame.display.flip()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
    
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
                self.mimo()

    def _check_hitting_the_target(self):
        pygame.sprite.spritecollide(self.target, self.bullets, True)
    
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.game_active = True
            self.target_speed = 0.75
            self.misses = 0
            self.bullets.empty()
            self.rocket.center()
            self.target.center()
    
    def mimo(self):
        self.misses += 1
        if self.misses >= 3:
            self.game_active = False
    
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
    
    def center(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

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
    
class Target():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.color = (60, 60, 60)

        self.rect = pygame.Rect(0, 0, 25, 60)
        self.rect.midright = self.screen_rect.midright

        self.y = float(self.rect.y)
        self.direction = 1
    
    def check_edges(self):
        if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:
            self.direction *= -1
    
    def update(self, speed):
        self.check_edges()
        self.y += speed*self.direction
        self.rect.y = self.y
    
    def draw_tagret(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def center(self):
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)

class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 100, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

trg = The_Uchenia_Game()
trg.run_game()