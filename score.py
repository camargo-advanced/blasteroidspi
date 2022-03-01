import os
import pygame
from entity import Entity
from utils import *


class Score(Entity):
    def __init__(self, galaxy):
        super().__init__(galaxy, "score", GREEN)
        self.score = 0
        self.font = pygame.font.Font(
            os.path.join('res', 'hyperspace-bold.otf'), 90)

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)
        # build text with current score
        self.text = "{0:,}".format(self.score)

    def render(self, surface):
        super().render(surface)
        # render score
        score_surface = self.font.render(self.text, False, self.color)
        surface.blit(score_surface, (30, 5))

    def update_score(self, variation):
        self.score += variation
