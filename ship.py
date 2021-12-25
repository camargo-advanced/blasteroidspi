from wentity import WEntity
from random import random
from pygame.math import Vector2
from utils import *

WIDTH = 3  # line thickness


class Ship(WEntity):

    def __init__(self, galaxy):
        wireframe = [
            Vector2(0.0, -5.0),  Vector2(3.0, 4.0),
            Vector2(1.5, 2.0),   Vector2(-1.5, 2.0),
            Vector2(-3.0, 4.0)
        ]
        super().__init__(galaxy, "ship", wireframe, WIDTH, WHITE)
        # entity initial position
        width, height = galaxy.size
        self.position = Vector2(width/2, height/2)
        self.size = 5  # scale factor
