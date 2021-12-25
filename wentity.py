import pygame
from pygame.locals import *
from pygame.math import Vector2


class WEntity():

    def __init__(self, galaxy, name, wireframe, width, color):
        self.galaxy = galaxy
        self.name = name
        self.wireframe = wireframe
        self.width = width
        self.color = color
        self.position = Vector2(.0, 0.0)
        self.linear_velocity = Vector2(.0, 0.0)
        self.rotation_velocity = 0.0
        self.size = 0.0
        self.rotation_angle = 0.0

    def render(self, surface):
        # if there is a wireframe to render,
        if self.wireframe and len(self.wireframe) > 0:
            # rotate, scale, translate,
            draw = []
            for point in self.wireframe:
                draw.append(
                    Vector2(point).rotate(self.rotation_angle) *
                    self.size + self.position
                )
            # and draw.
            pygame.draw.lines(surface, self.color, True, draw, self.width)

    def update(self, time_passed):
        self.position += self.linear_velocity * time_passed
        self.rotation_angle += self.rotation_velocity * time_passed
