from wentity import CLOCKWISE, WEntity
from random import random
from pygame.math import Vector2
from utils import *
from wentity import FORWARD, CLOCKWISE

WIDTH = 3  # line thickness
SCALE_FACTOR = 3

class Asteroid(WEntity):

    def __init__(self, galaxy):
        wireframe = [
            Vector2(-20.0, 20.0),  Vector2(-25.0, 5.0),
            Vector2(-25.0, -10.0), Vector2(-5.0, -10.0),
            Vector2(-10.0, -20.0), Vector2(5.0, -20.0),
            Vector2(20.0, -10.0),  Vector2(20.0, -5.0),
            Vector2(0.0, 0.0),     Vector2(20.0, 10.0),
            Vector2(10.0, 20.0),   Vector2(0.0, 15.0)
        ]
        super().__init__(galaxy, "asteroid", wireframe, WIDTH, WHITE)
        # entity initial position
        width, height = galaxy.size
        self.position = Vector2(random()*width, random()*height)
        # linear velocity in pixels per second at random angle
        self.velocity = Vector2(90.0, 0.0).rotate(random() * 360.0)
        # rotation at center of rock, in degress per second
        self.angular_speed = 17.19
        self.size = SCALE_FACTOR
        self.rotating = CLOCKWISE

#    def render(self, surface):
#        super().render(surface)

#    def update(self, time_passed):
#        super().update(time_passed)
