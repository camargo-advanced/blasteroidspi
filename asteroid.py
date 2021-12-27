from ship import ANGULAR_SPEED
from wentity import WEntity, CLOCKWISE, CLOCKWISE
from random import random
from pygame.math import Vector2
from utils import *

WIDTH = 3  # line thickness
SCALE_FACTOR = 3
SPEED = 90.0  # pixels per second
ANGULAR_SPEED = 17.19  # degrees per second
ASTERIOD_WIREFRAME = [
    Vector2(-20.0, 20.0),  Vector2(-25.0, 5.0), Vector2(-25.0, -10.0),
    Vector2(-5.0, -10.0), Vector2(-10.0, -20.0), Vector2(5.0, -20.0),
    Vector2(20.0, -10.0),  Vector2(20.0, -5.0), Vector2(0.0, 0.0),
    Vector2(20.0, 10.0), Vector2(10.0, 20.0),   Vector2(0.0, 15.0)
]


class Asteroid(WEntity):

    def __init__(self, galaxy):
        super().__init__(galaxy, "asteroid", ASTERIOD_WIREFRAME, WIDTH, WHITE)

        # entity initial position
        width, height = self.galaxy.size
        self.position = Vector2(random()*width, random()*height)

        # linear velocity in pixels per second at random angle
        self.velocity = Vector2(0.0, SPEED).rotate(random() * 360.0)

        # rotation at center of rock, in degress per second
        self.angular_speed = ANGULAR_SPEED
        self.rotating = CLOCKWISE

        # for scaling the wireframe
        self.size = SCALE_FACTOR
