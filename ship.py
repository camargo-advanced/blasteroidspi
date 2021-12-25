from wentity import WEntity
from random import random
from pygame.math import Vector2
from utils import *

WIDTH = 3  # line thickness
SCALE_FACTOR = 5
ROTATING_CW = 1
ROTATING_CCW = -1
NOT_ROTATING = 0
MOVING_FW = 1
MOVING_BW = -1
NOT_MOVING = 0

class Ship(WEntity):

    def __init__(self, galaxy):
        wireframe = [
            Vector2(0.0, -5.0),  Vector2(3.0, 4.0),
            Vector2(1.5, 2.0),   Vector2(-1.5, 2.0),
            Vector2(-3.0, 4.0)
        ]
        super().__init__(galaxy, "ship", wireframe, WIDTH, GREEN)
        # entity initial position
        width, height = galaxy.size
        self.position = Vector2(width/2, height/2)
        self.size = SCALE_FACTOR

    def set_rotation(self, direction):
        self.rotation_velocity = 180 * direction

    def set_movement(self, direction):
        self.linear_velocity = Vector2(90.0, 0.0).rotate(self.rotation_angle-90)