import pygame
from pygame.math import Vector2
from math import cos, sin
from random import random
from utils import wrap_coordinates

class Entity(object):

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
        self.id = 0

    def render(self, surface):
        if self.wireframe and len(self.wireframe) > 0:
            
            # Rotate, scale and translate
            draw = []
            for point in self.wireframe:
                draw.append(
                    Vector2(point).rotate(self.rotation_angle) *
                    self.size + self.position
                )

            # Draw
            pygame.draw.lines(surface, self.color, True, draw, self.width)

    def update(self, time_passed):
        self.position += self.linear_velocity * time_passed
        wrap_coordinates(self.position, self.galaxy.size)
        self.rotation_angle += self.rotation_velocity * time_passed


