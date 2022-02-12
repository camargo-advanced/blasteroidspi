import pygame
from pygame.locals import *
from pygame.math import Vector2
from entity import Entity
from utils import *


class WEntity(Entity):

    def __init__(self, galaxy, name, color, wireframe, width):
        super().__init__(galaxy, name, color)
        self.wireframe = wireframe
        self.width = width
        self.velocity = Vector2(0.0, 0.0)
        self.acceleration = 0.0
        self.damping = 1 #@@@@@ no damping
        self.angular_speed = 0.0
        self.angle = 0.0
        self.size = 1
        self.rotating = None
        self.accelerating = None

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)

        # update entity rotation angle
        angle_increment = self.angular_speed * time_passed
        if self.rotating == CLOCKWISE:
            self.angle += angle_increment
        elif self.rotating == CCLOCKWISE:
            self.angle -= angle_increment

        # generate a acceleration vector towards current entity angle
        acceleration = Vector2(0.0, 0.0)
        if self.accelerating == FORWARD:
            acceleration = Vector2(0.0, -self.acceleration).rotate(self.angle)

        # update position
        self.position += self.velocity * time_passed 

        # update velocity vector
        self.velocity += acceleration * time_passed
        self.velocity *= self.damping ** time_passed #@@@@@

    def render(self, surface):
        super().render(surface)

        draw = []
        for point in self.wireframe:
            draw.append(
                Vector2(point).rotate(self.angle) * self.size + self.position
            )

        pygame.draw.lines(surface, self.color, True, draw, self.width)

    def start_rotating(self, direction):
        self.rotating = direction

    def stop_rotating(self):
        self.rotating = None

    def start_accelerating(self, direction):
        self.accelerating = direction

    def stop_accelerating(self):
        self.accelerating = None
