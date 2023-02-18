import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvansion:
    """Класс для управления ресурсами и поведения игры."""

    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invansion")

        #Создаём экземпляры, сохраняющего игровую статистику и панель результатов.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #Создание кнопки "Играть".
        self.play_button = Button(self, 'Играть')

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
    
    def _check_events(self):
        """Обрабатывает события клавиатуры и мыши."""
        # отслеживание событий клавиатуры и мыши.
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
        """Нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._check_play_button_by_P()
    
    def _check_keyup_events(self, event):
        """Отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _check_play_button_by_P(self):
        """Запускает новую игру после нажатия кнопки "P" на клавиатуре."""
        if not self.stats.game_active:
            #Сброс игровой статистики.
            self.stats.reset_stats()
            self.settings.initialyze_dynamic_settings()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # Очищение списков.
            self.aliens.empty()
            self.bullets.empty()

            #Создание нового флота и размещение корабля по центру.
            self._create_fleet()
            self.ship.center_ship()

            #Мышка теряется.
            pygame.mouse.set_visible(False)
    
    def _check_play_button(self, mouse_pos):
        """Запускает новую игру после нажатия кнопки "Играть"."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Сброс игровой статистики.
            self.stats.reset_stats()
            self.settings.initialyze_dynamic_settings()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # Очищение списков.
            self.aliens.empty()
            self.bullets.empty()

            #Создание нового флота и размещение корабля по центру.
            self._create_fleet()
            self.ship.center_ship()

            #Мышка теряется.
            pygame.mouse.set_visible(False)
    
    def _fire_bullet(self):
        """Создание нового снаряда и вклчение его в группу bullets."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        self.bullets.update()
        #Удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        #Проверка попаданий по пришельцам.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            #Уничтожаем существующее снаряды и создание нового флота.
            self.bullets.empty()
            sleep(0.1)
            self._create_fleet()
            self.settings.increase_speed()

            #Увеличение уровня.
            self.stats.level += 1
            self.sb.prep_level()
    
    def _create_fleet(self):
        """Создаём флот пришельцов."""
        #Создаём пришельца и расчёт количества инопришеленцев в ряду.
        #Интервал между соседними пришельцами равняется его ширине.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Считаем количество рядов.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #Создание флота пришельцев.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
    def _create_alien(self, alien_number, row_number):
        """Создает инопрешеленца."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)
    
    def _check_fleet_edges(self):
        """Реагирует на достижение края экрана."""
        for allien in self.aliens.sprites():
            if allien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Опускает флот и изменяет направление движения."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев Имперского флота."""
        self._check_fleet_edges()
        self.aliens.update()

        #Проверка коллизий инопрешиленцов с кораблём.
        if pygame.sprite.spritecollideany(self.ship, self.aliens): 
            self._ship_hit()
        
        #Проверка достижения инопришеленцами нижнего края экрана.
        self._check_alliens_bottom()
    
    def _check_alliens_bottom(self):
        """Проверяет достижение инопришеленцами нижнего края экрана."""
        screen_rect = self.screen.get_rect()
        for allien in self.aliens.sprites():
            if allien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _ship_hit(self):
        """Обрабатывает столкновение коробля с пришельцем"""
        #Уменьшаем количество жизней.
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #Очищаем группы снарядов и инопланетного флота.
            self.aliens.empty()
            self.bullets.empty()   

            #Создание нового флота и размещение корабля по центру.
            self._create_fleet()
            self.ship.center_ship()

            #Пауза.
            sleep(0.5)
        else:
            self.sb.prep_ships()
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    def _update_screen(self):
        """Обновляет изображение на экране и отображает кадры."""
        # При каждом проходе цикла перерисовается экран.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #Вывод информации про счёт.
        self.sb.show_score()

        #Кнопка отображается,когда игра неактивна.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # отображение любого прорисованного кадра.
        pygame.display.flip()

if __name__ == '__main__':
    #создание экземпляра и запуск игры.
    ai = AlienInvansion()
    ai.run_game()