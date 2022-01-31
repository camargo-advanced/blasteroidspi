import os
from entity import Entity
from sound import Sound
from utils import *


class CountDown(Entity):
    def __init__(self, galaxy):
        super().__init__(galaxy, "count_down", GREEN)

        self.font = pygame.font.Font(
            os.path.join('res', 'hyperspace-bold.otf'), 90)
        self.count_down = 5
        self.tick = False
        pygame.time.set_timer(COUNT_DOWN_EVENT, 1000, 6)
        Sound().play('beep-countdown')

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)

        self.process_events(event_list)
        if self.tick:
            self.count_down -= 1
            if self.count_down <= -1:
                self.dead = True

    def render(self, surface):
        super().render(surface)

        # render count down number or GO !
        if self.count_down > 0:
            text = str(self.count_down)
        else:
            text = 'GO !'
        text_surface = self.font.render(text, False, self.color)
        text_rect = text_surface.get_rect()
        text_rect.centery = self.galaxy.rect.centery/2
        text_rect.centerx = self.galaxy.rect.centerx
        surface.blit(text_surface, text_rect)

        # render sound
        if self.tick:
            self.tick = False
            if self.count_down > 0:
                Sound().play('beep-countdown')
            elif self.count_down == 0:
                Sound().play('beep')

    def process_events(self, event_list):
        for event in event_list:
            if event.type == COUNT_DOWN_EVENT:
                self.tick = True