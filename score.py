import os
import pygame
from entity import Entity
from pygame.math import Vector2
from ship import Ship
from sound import Sound
from utils import *

NUM_LIVES = 3
RESET_GAME = pygame.USEREVENT + 1


class Score(Entity):
    def __init__(self, galaxy, clock):
        super().__init__(galaxy, "score", GREEN)
        self.clock = clock
        self.location = Vector2(30, 5)
        self.score = 0
        self.lives = NUM_LIVES
        self.font = pygame.font.Font(os.path.join(
            'res', 'hyperspace-bold.otf'), 90)
        self.font_fps = pygame.font.Font(os.path.join(
            'res', 'hyperspace-bold.otf'), 20)
        self.ship = Ship(galaxy)  # ship to render the number of lives
        self.game_over = False

    def update(self, time_passed):
        super().update(time_passed)
        if self.lives <= 0 and self.game_over == False:
            Sound().play('siren')
            pygame.time.set_timer(RESET_GAME, 5000, 1)
            self.game_over = True

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

        # render FPS
        text = 'FPS = ' + format(self.clock.get_fps(), '.2f')
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
