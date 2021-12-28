import pygame
from pygame.locals import *
from pygame.math import Vector2
from entity import Entity

CLOCKWISE = 1  # rotating clockwise
CCLOCKWISE = -1  # rotating counter clockwise
FORWARD = 1  # accelerating forward
BACKWARDS = -1  # accelerating backwards


class WEntity(Entity):

    def __init__(self, galaxy, name, color, wireframe, width):
        super().__init__(galaxy, name, color)
        self.wireframe = wireframe
        self.width = width
        self.velocity = Vector2(0.0, 0.0)
        self.acceleration = 0.0
        self.angular_speed = 0.0
        self.angle = 0.0
        self.size = 1
        self.rotating = None
        self.accelerating = None

    def update(self, time_passed):
        super().update(time_passed)
        # update entity angle
        if self.rotating == CLOCKWISE:
            self.angle += self.angular_speed * time_passed
        elif self.rotating == CCLOCKWISE:
            self.angle -= self.angular_speed * time_passed

        # generate a acceleration vector towards current entity angle
        acceleration = Vector2(0.0, 0.0)
        if self.accelerating == FORWARD:
            acceleration = Vector2(0.0, -self.acceleration).rotate(self.angle)
        elif self.accelerating == BACKWARDS:
            acceleration = Vector2(0.0, self.acceleration).rotate(self.angle)

        # update position
        self.position += self.velocity * time_passed + \
            (acceleration * time_passed * time_passed) / 2

        # update velocity vector
        self.velocity += acceleration * time_passed

    def render(self, surface):
        super().render(surface)
        # rotate, scale, translate,
        draw = []
        for point in self.wireframe:
            draw.append(
                Vector2(point).rotate(self.angle) *
                self.size + self.position
            )
        # and draw.
        pygame.draw.lines(surface, self.color, True, draw, self.width)

    def start_rotating(self, direction):
        self.rotating = direction

    def start_accelerating(self, direction):
        self.accelerating = direction

    def stop_rotating(self):
        self.rotating = None

    def stop_accelerating(self):
        self.accelerating = None
