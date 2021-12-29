from pygame import time
import pygame
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
UNSHIELD_EVENT = pygame.USEREVENT + 1
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

        self.size = SCALE_FACTOR
        self.shielded = True
        pygame.time.set_timer(UNSHIELD_EVENT, 5000, 1)
        self.firing = False
        self.dying = False

    def update(self, time_passed):
        super().update(time_passed)
        if self.firing:
            # build a new blast, set its position to the ship's,
            # set its velocity vector to ship's orientation
            # and then add it to the galaxy
            blast = Blast(self.galaxy, Vector2(self.position), self.angle)
            self.galaxy.add_entity(blast)

        for entity in self.galaxy.get_entities_by_name('asteroid'):
            if not self.shielded and self.point_in_circle(entity):
                # if a rock hit me, I lose a life
                self.dying = True
                self.shielded = True
                pygame.time.set_timer(UNSHIELD_EVENT, 5000, 1)
                width, height = self.galaxy.size
                self.position = Vector2(width/2, height/2)
                self.velocity = Vector2(0.0, 0.0)
                self.angle = 0.0
                self.galaxy.get_entity_by_name(
                    'score').update_lives(-1)

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
        if self.dying:
            if not Sound().busy():
                Sound().play('bang')
            self.dying = False

    def fire(self):
        self.firing = True

    def unshield(self):
        self.shielded = False
