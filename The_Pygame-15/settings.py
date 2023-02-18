class Settings():
    """Класс для хранения всех настроек игры."""

    def __init__(self):
        """Инициализирует настройки игры"""
        #Параметры экрана.
        self.screen_width = 1050
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        
        # Настройки корабля.
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Параметры снаряда.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        #Параметры пришельцев.
        self.fleet_drop_speed = 10

        #Темп ускорения игры.
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        #Подсчёт очков.
        self.alien_points = 50

        self.mode = None

        self.initialyze_dynamic_settings()
    
    def initialyze_dynamic_settings(self):
        """Инициализирует настройки игры, которые меняются в её процессе"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0
        
        if self.mode == 'easy':
            self.bullet_speed = 1.75
            self.alien_speed = 0.75
        
        if self.mode == 'heavy':
            self.bullet_speed = 1.25
            self.alien_speed = 1.25

        self.fleet_direction = 1
    
    def increase_speed(self):
        """Увеличивает все скорости."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
    
    def choose_game_mode(self, mode):
        self.mode = mode
        if self.mode == 'easy':
            self.bullet_speed = 1.75
            self.alien_speed = 0.75
            self.speedup_scale = 1.05
            self.bullet_allowed = 5
        if self.mode == 'middle':
            pass
        if self.mode == 'heavy':
            self.bullet_speed = 1.25
            self.alien_speed = 1.25
            self.speedup_scale = 1.15
            self.bullet_allowed = 1