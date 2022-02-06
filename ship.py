from wentity import WEntity
from pygame.math import Vector2
from utils import *


WIDTH = 3  # line thickness
SCALE_FACTOR = 5.0
SHIP_WIREFRAME = [
    Vector2(0.0, -5.0),  Vector2(3.0, 4.0), Vector2(1.5, 2.0),
    Vector2(-1.5, 2.0), Vector2(-3.0, 4.0)
]


class Ship(WEntity):

    def __init__(self, galaxy):
        super().__init__(galaxy, "ship", GREEN, SHIP_WIREFRAME, WIDTH)

        # ship initial position
        self.position = Vector2(self.galaxy.rect.width/2,
                                self.galaxy.rect.height/2)

        self.size = SCALE_FACTOR

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)

    def render(self, surface):
        super().render(surface)
