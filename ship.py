from pygame.locals import *
from wentity import WEntity
from pygame.math import Vector2
from utils import *

WIDTH = 3  # line thickness
SCALE_FACTOR = 5.0
ANGULAR_SPEED = 180.0  # degrees per second
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
        self.angular_speed = ANGULAR_SPEED
        self.size = SCALE_FACTOR

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)

        self.process_events(event_list)

    def render(self, surface):
        super().render(surface)

    def process_events(self, event_list):
        for event in event_list:

            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    self.start_rotating(CCLOCKWISE)
                if event.key == K_RIGHT or event.key == K_d:
                    self.start_rotating(CLOCKWISE)

            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_a or \
                        event.key == K_RIGHT or event.key == K_d:
                    self.stop_rotating()
