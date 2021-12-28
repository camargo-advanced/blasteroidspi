from ship import ANGULAR_SPEED
from sound import Sound
from wentity import WEntity, CLOCKWISE, CLOCKWISE
from random import random
from pygame.math import Vector2
from math import sqrt
from utils import *

WIDTH = 3  # line thickness
SCALE_FACTOR = 3
SPEED = 90.0  # pixels per second
ANGULAR_SPEED = 17.19  # degrees per second
ASTEROID_WIREFRAME = [
    Vector2(-20.0, 20.0),  Vector2(-25.0, 5.0), Vector2(-25.0, -10.0),
    Vector2(-5.0, -10.0), Vector2(-10.0, -20.0), Vector2(5.0, -20.0),
    Vector2(20.0, -10.0),  Vector2(20.0, -5.0), Vector2(0.0, 0.0),
    Vector2(20.0, 10.0), Vector2(10.0, 20.0),   Vector2(0.0, 15.0)
]


class Asteroid(WEntity):

    def __init__(self, galaxy):
        super().__init__(galaxy, "asteroid", ASTEROID_WIREFRAME, WIDTH, WHITE)

        # entity initial position is random
        width, height = self.galaxy.size
        self.position = Vector2(random()*width, random()*height)

        # linear velocity in pixels per second at random angle
        self.velocity = Vector2(0.0, SPEED).rotate(random() * 360.0)

        self.angular_speed = ANGULAR_SPEED
        self.rotating = CLOCKWISE
        self.size = SCALE_FACTOR
        self.times_hit = 0
        self.exploding = False

    def update(self, time_passed):
        super().update(time_passed)

        # if a blast hit me, I need to break myself
        # into 2 smaller rocks !
        for entity in list(self.galaxy.entities.values()):
            if entity.name == 'blast':
                if self.point_in_circle(entity.position):
                    self.exploding = True
                    self.times_hit += 1
                    if self.times_hit < 3:
                        self.size /= 2
                        self.velocity *= 1.5
                        self.velocity.rotate_ip(random()*360)
                        self.galaxy.add_entity(self.fragment())
                        entity.dead = True
                    else:
                        self.exploding = True
                        self.dead = True

    def render(self, surface):
        # render visuals,
        super().render(surface)
        # and sounds
        if self.exploding:
            Sound().play('bang')
            self.exploding = False

    def fragment(self):
        fragment = Asteroid(self.galaxy)
        fragment.position = Vector2(self.position)
        fragment.velocity = Vector2(self.velocity)
        fragment.velocity.rotate_ip(random()*360)
        fragment.size = self.size
        fragment.times_hit = self.times_hit
        return fragment

    def diameter(self):
        x_max, y_max = 0.0, 0.0
        x_min, y_min = self.galaxy.size

        for point in self.wireframe:
            # find the max of x and y
            if point.x > x_max:
                x_max = point.x
            if point.y > y_max:
                y_max = point.y

            # find the min of x and y
            if point.x < x_min:
                x_min = point.x
            if point.y < y_min:
                y_min = point.y

        if abs(x_max-x_min) > abs(y_max-y_min):
            return abs(x_max-x_min) * self.size
        else:
            return abs(y_max-y_min) * self.size

    def point_in_circle(self, other_position):
        # calculate the distance between 2 points in 2D space
        distance = sqrt((other_position.x-self.position.x) ** 2
                        + (other_position.y-self.position.y) ** 2)

        # if distance is less than the radius, we assume the objects have colided
        if (distance <= self.diameter()/2):
            return True
        else:
            return False
