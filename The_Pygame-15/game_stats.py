class GameStats():
    """Статистика игры."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        #Игра запускается
        self.game_active = False

        #Рекорд игры.
        self.high_score = 0
    
    def reset_stats(self):
        """Инициализирует изменчивую статистику."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1