import pygame.font


class Button:
    def __init__(self, ai_game, msg, type):
        """Инициализирует атрибуты кнопки."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.type = type

         #Размеры и свойства кнопки.
        self.width, self.height = 200, 50
        self.button_color = (0, 100, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        #Строим объект в центре экрана.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        if self.type == 'start':
            self.width, self.height = 200, 50
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.center = self.screen_rect.center
            
        elif self.type == 'easy':
            self.width, self.height = 170, 40
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.font = pygame.font.SysFont(None, 25)
            self.rect.centerx = self.screen_rect.centerx - 200
            self.rect.centery = self.screen_rect.centery + 75
        
        elif self.type == 'middle':
            self.width, self.height = 170, 40
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.font = pygame.font.SysFont(None, 25)
            self.rect.centerx = self.screen_rect.centerx
            self.rect.centery = self.screen_rect.centery + 75
        
        elif self.type == 'heavy':
            self.width, self.height = 170, 40
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.font = pygame.font.SysFont(None, 25)
            self.rect.centerx = self.screen_rect.centerx + 200
            self.rect.centery = self.screen_rect.centery + 75

        #Сообщение в кнопке
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Превращает сообщение в прямоугольник и равняет текст по его центру."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center
        if self.type == 'easy':
            self.msg_image_rect.centerx = self.screen_rect.centerx - 200
            self.msg_image_rect.centery = self.screen_rect.centery + 75
        elif self.type == 'middle':
            self.msg_image_rect.centerx = self.screen_rect.centerx
            self.msg_image_rect.centery = self.screen_rect.centery + 75
        elif self.type == 'heavy':
            self.msg_image_rect.centerx = self.screen_rect.centerx + 200
            self.msg_image_rect.centery = self.screen_rect.centery + 75
    
    def draw_button(self):
        """Отображение пустой кнопки и вывод сообщения."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)