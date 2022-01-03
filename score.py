import os
import pygame
from entity import Entity
from pygame.math import Vector2
from ship import Ship
from sound import Sound
from utils import *

NUM_LIVES = 3


class Score(Entity):
    def __init__(self, galaxy):
        super().__init__(galaxy, "score", GREEN)
        self.location = Vector2(30, 5)
        self.score = 0
        self.lives = NUM_LIVES
        self.fps = 0
        self.font = pygame.font.Font(os.path.join(
            'res', 'hyperspace-bold.otf'), 90)
        self.font_fps = pygame.font.Font(os.path.join(
            'res', 'hyperspace-bold.otf'), 20)
        self.ship = Ship(galaxy)  # ship to render the number of lives
        self.difficulty = 1.0
        self.ship_shielded = True
        self.game_status = GAME_DEMO_MODE

    def update(self, time_passed):
        super().update(time_passed)
        if self.lives <= 0 and self.game_status == GAME_RUNNING:
            Sound().play('siren')
            # self.galaxy.add_entity(CountDown(self.galaxy))
            pygame.time.set_timer(RESTART_GAME, 3000, 1)
            self.game_status = GAME_DEMO_MODE

    def render(self, surface):
        super().render(surface)

        # render score
        text = format(self.score, ',')
        if self.ship_shielded:
            text = text + " *"
        text_surface = self.font.render(
            text, False, self.color)
        surface.blit(text_surface, self.location)

        # render number of lives
        for x in range(50, (self.lives*50)+1, 50):
            self.ship.position = Vector2(x, 160)
            self.ship.render(surface)

        # render FPS
        text = 'FPS = ' + format(self.fps, '.2f')
        text_surface = self.font_fps.render(
            text, False, self.color)
        width, height = self.galaxy.size
        surface.blit(text_surface, (width-150, 20))

        # render game over !
        if self.lives <= 0:
            text = 'GAME OVER'
            text_surface = self.font.render(
                text, False, self.color)
            width, height = self.galaxy.size
            surface.blit(text_surface, (width/2-text_surface.get_rect().width /
                                        2, (height/2-text_surface.get_rect().height/2)-200))

    def update_score(self, variation):
        if self.lives > 0:
            self.score += variation

    def update_lives(self, variation):
        self.lives += variation

    def update_fps(self, fps):
        self.fps = fps

    def update_ship_shielded(self, shielded):
        self.ship_shielded = shielded

    def increase_difficulty_by(self, multiplier):
        self.difficulty *= multiplier

    def update_game_status(self, status):
        self.game_status = status
