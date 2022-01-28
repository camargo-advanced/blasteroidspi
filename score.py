import os
import pygame
from entity import Entity
from pygame.math import Vector2
from ship import Ship
from sound import Sound
from utils import *

INITIAL_LIVES = 3
MAX_LIVES = 4


class Score(Entity):
    def __init__(self, galaxy):
        super().__init__(galaxy, "score", GREEN)
        self.location_score = Vector2(30, 5)
        self.text_game_over = 'GAME OVER'
        self.score = 0
        self.lives = INITIAL_LIVES
        self.fps = 0.0
        self.font = pygame.font.Font(
            os.path.join('res', 'hyperspace-bold.otf'), 90)
        self.font_fps = pygame.font.Font(os.path.join(
            'res', 'hyperspace-bold.otf'), 20)
        self.ship = Ship(galaxy)  # ship to render the number of lives
        self.difficulty = 1.0
        self.ship_shielded = True
        self.game_status = GAME_DEMO_MODE

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)

        if self.lives <= 0 and self.game_status == GAME_RUNNING:
            Sound().play('siren')
            pygame.time.set_timer(RESTART_GAME, 3000, 1)
            self.game_status = GAME_DEMO_MODE

    def render(self, surface):
        super().render(surface)

        # render score
        if self.ship_shielded:
            text = "{0:,} *".format(self.score)
        else:
            text = "{0:,}".format(self.score)
        text_surface = self.font.render(text, False, self.color)
        surface.blit(text_surface, self.location_score)

        # render number of lives
        for x in range(50, (self.lives*50)+1, 50):
            self.ship.position = Vector2(x, 160)
            self.ship.render(surface)

        # render FPS
        text = "FPS = {0:.1f}".format(self.fps)
        text_surface = self.font_fps.render(text, False, self.color)
        text_rect = text_surface.get_rect()
        text_rect.centerx = self.galaxy.rect.width - 100
        text_rect.y = 20
        surface.blit(text_surface, text_rect)

        # render game over !
        if self.lives <= 0:
            text_surface = self.font.render(
                self.text_game_over, False, self.color)
            text_rect = text_surface.get_rect()
            text_rect.centerx = self.galaxy.rect.centerx
            text_rect.centery = self.galaxy.rect.centery - 200
            surface.blit(text_surface, text_rect)

    def update_score(self, variation):
        if self.lives > 0:
            self.score += variation

    def update_lives(self, variation):
        self.lives += variation
        if self.lives < 0:
            self.lives = 0
        elif self.lives > MAX_LIVES:
            self.lives = MAX_LIVES

    def update_fps(self, fps):
        self.fps = fps

    def update_ship_shielded(self, shielded):
        self.ship_shielded = shielded

    def increase_difficulty_by(self, multiplier):
        self.difficulty *= multiplier

    def update_game_status(self, status):
        self.game_status = status
