import os
from entity import Entity
from pygame.math import Vector2
from sound import Sound
from utils import *


class CountDown(Entity):
    def __init__(self, galaxy):
        super().__init__(galaxy, "count_down", GREEN)
        self.location = Vector2(300, 500)
        self.font = pygame.font.Font(os.path.join(
            'res', 'hyperspace-bold.otf'), 90)
        self.count_down = 5
        self.tick = False
        pygame.time.set_timer(COUNT_DOWN_EVENT, 1000, 6)
        Sound().play('beep-countdown')

    def update(self, time_passed):
        super().update(time_passed)
        self.process_events()
        if self.tick:
            self.count_down -= 1
            if self.count_down == -1:
                self.dead = True

    def render(self, surface):
        super().render(surface)

        # render count down
        if self.count_down > 0:
            text = str(self.count_down)
        else:
            text = 'GO !'
        text_surface = self.font.render(
            text, False, self.color)
        width, height = self.galaxy.size
        surface.blit(text_surface, (width/2-text_surface.get_rect().width /
                                    2, (height/2-text_surface.get_rect().height/2)-height*0.3))

        # render sound
        if self.tick:
            self.tick = False
            if self.count_down > 0:
                Sound().play('beep-countdown')
            elif self.count_down == 0:
                Sound().play('beep')

    def process_events(self):
        for event in pygame.event.get([COUNT_DOWN_EVENT]):
            self.tick = True