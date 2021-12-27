import random
from blast import Blast
from wentity import WEntity
from pygame.math import Vector2
from utils import *
from wentity import FORWARD
from random import random

WIDTH = 3  # line thickness
SCALE_FACTOR = 5.0
ACCELERATION = 150.0  # pixels per second
ANGULAR_SPEED = 180.0  # degrees per second
SHIP_WIREFRAME = [
    Vector2(0.0, -5.0),  Vector2(3.0, 4.0), Vector2(1.5, 2.0),
    Vector2(-1.5, 2.0), Vector2(-3.0, 4.0)
]
THRUST_WIREFRAME = [
    Vector2(1.0, 2.0), Vector2(0.0, 5.0), Vector2(-1.0, 2.0)
]


class Ship(WEntity):

    def __init__(self, galaxy):
        super().__init__(galaxy, "ship", SHIP_WIREFRAME, WIDTH, GREEN)

        # entity initial position
        width, height = self.galaxy.size
        self.position = Vector2(width/2, height/2)

        # linear acceleration and angular speed
        self.acceleration = ACCELERATION
        self.angular_speed = ANGULAR_SPEED

        # for scaling the wireframe
        self.size = SCALE_FACTOR

    def render(self, surface):
        super().render(surface)
        if self.accelerating == FORWARD:
            self.wireframe = THRUST_WIREFRAME
            super().render(surface)
            self.wireframe = SHIP_WIREFRAME

    def fire(self):
        # build a new blast, set its position to the ship's,
        # set its velocity vector to ship's orientation
        # and then add it to the galaxy
        blast = Blast(self.galaxy)
        blast.position = Vector2(self.position)
        blast.velocity = blast.velocity.rotate(self.angle)
        self.galaxy.add_entity(blast)
