import os
import pygame
from entity import Entity
from pygame.math import Vector2
from ship import Ship
from utils import *

NUM_LIVES = 3


class Score(Entity):
    def __init__(self, galaxy):
        super().__init__(galaxy, "score", GREEN)
        self.location = Vector2(30, 5)
        self.reset_score()
        self.reset_lives()
        self.font = pygame.font.Font(os.path.join(
            'res', 'hyperspace-bold.otf'), 90)
        self.ship = Ship(galaxy)  # ship template to render number of lives

    def update(self, time_passed):
        super().update(time_passed)

    def render(self, surface):
        super().render(surface)
        # render score
        text = str(self.score)
        if self.galaxy.get_entity_by_name('ship').shielded:
            text = text + " *"
        text_surface = self.font.render(
            text, False, self.color)
        surface.blit(text_surface, self.location)
        # render number of lives
        for x in range(50, (self.lives*50)+1, 50):
            self.ship.position = Vector2(x, 160)
            self.ship.render(surface)

    def reset_score(self):
        self.score = 0

    def reset_lives(self):
        self.lives = NUM_LIVES

    def update_score(self, variation):
        self.score += variation

    def update_lives(self, variation):
        self.lives += variation
