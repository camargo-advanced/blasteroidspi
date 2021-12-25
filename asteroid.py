from entity import Entity
from random import random
from pygame.math import Vector2

WHITE = (255, 255, 255)  # line color
WIDTH = 3  # line thickness


class Asteroid(Entity):

    def __init__(self, galaxy):
        wireframe = [
            Vector2(-20.0, 20.0),  Vector2(-25.0, 5.0),   Vector2(-25.0, -10.0),
            Vector2(-5.0, -10.0),  Vector2(-10.0, -20.0), Vector2(5.0, -20.0),
            Vector2(20.0, -10.0),  Vector2(20.0, -5.0),   Vector2(0.0, 0.0),
            Vector2(20.0, 10.0),   Vector2(10.0, 20.0),   Vector2(0.0, 15.0)
        ]
        super().__init__(galaxy, "asteroid", wireframe, WIDTH, WHITE)
        width, height = galaxy.size
        self.position = Vector2(random()*width, random()*height) # # rock start position
        self.linear_velocity = Vector2(90.0,0.0).rotate(random()*359.99) # in pixels per second at random angle
        self.rotation_velocity = 17.19 # rotation at center of rock, in degress per second
        self.size = 3 # scale factor

#    def render(self, surface):
#        super().render(surface)

#    def update(self, time_passed):
#        super().update(time_passed)
