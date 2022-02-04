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
        self.angular_speed = 0.0
        self.angle = 0.0
        self.size = 1
        self.rotating = None

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)

        # update entity rotation angle
        angle_increment = self.angular_speed * time_passed
        if self.rotating == CLOCKWISE:
            self.angle += angle_increment
        elif self.rotating == CCLOCKWISE:
            self.angle -= angle_increment

        # update position
        self.position += self.velocity * time_passed 

    def render(self, surface):
        super().render(surface)

        draw = []
        for point in self.wireframe:
            draw.append(
                Vector2(point).rotate(self.angle) * self.size + self.position
            )

        pygame.draw.lines(surface, self.color, True, draw, self.width)
