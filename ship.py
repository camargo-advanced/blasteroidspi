import pygame
from wentity import WEntity
from random import random
from pygame.math import Vector2
from utils import *
from wentity import FORWARD

WIDTH = 3  # line thickness
SCALE_FACTOR = 5.0
ACCELERATION = 150.0  # pixels per second
ANGULAR_SPEED = 180.0  # degrees per second


class Ship(WEntity):

    def __init__(self, galaxy):
        wireframe = [
            Vector2(0.0, -5.0),  Vector2(3.0, 4.0),
            Vector2(1.5, 2.0),   Vector2(-1.5, 2.0),
            Vector2(-3.0, 4.0)
        ]
        self.wireframe_thrust = [
            Vector2(1.0, 2.0), Vector2(0.0, 5.0),
            Vector2(-1.0, 2.0)
        ]

        super().__init__(galaxy, "ship", wireframe, WIDTH, GREEN)

        # entity initial position
        width, height = galaxy.size
        self.position = Vector2(width/2, height/2)

        # linear acceleration and angular speed
        self.acceleration = ACCELERATION
        self.angular_speed = ANGULAR_SPEED

        # for scaling the wireframe
        self.size = SCALE_FACTOR

    def render(self, surface):
        super().render(surface)
        if self.accelerating == FORWARD:
            # rotate, scale, translate,
            draw = []
            for point in self.wireframe_thrust:
                draw.append(
                    Vector2(point).rotate(self.angle) *
                    self.size + self.position
                )
            # and draw.
            pygame.draw.lines(surface, self.color, True, draw, self.width)
