from pygame import time
from blast import Blast
from sound import Sound
from wentity import WEntity
from pygame.math import Vector2
from utils import *
from wentity import FORWARD

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
        super().__init__(galaxy, "ship", GREEN, SHIP_WIREFRAME, WIDTH)

        # entity initial position
        width, height = self.galaxy.size
        self.position = Vector2(width/2, height/2)

        # linear acceleration and angular speed
        self.acceleration = ACCELERATION
        self.angular_speed = ANGULAR_SPEED

        # for scaling the wireframe
        self.size = SCALE_FACTOR

        self.firing = False

    def update(self, time_passed):
        super().update(time_passed)
        if self.firing:
            # build a new blast, set its position to the ship's,
            # set its velocity vector to ship's orientation
            # and then add it to the galaxy
            blast = Blast(self.galaxy, Vector2(self.position), self.angle)
            self.galaxy.add_entity(blast)

    def render(self, surface):
        # render visuals and sounds
        super().render(surface)
        if self.accelerating == FORWARD:
            if not Sound().busy():
                Sound().play('thrust')
            self.wireframe = THRUST_WIREFRAME
            super().render(surface)
            self.wireframe = SHIP_WIREFRAME
        if self.firing:
            Sound().play('fire')
            self.firing = False

    def fire(self):
        self.firing = True
