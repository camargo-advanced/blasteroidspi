from wentity import WEntity
from pygame.math import Vector2
from utils import *

WIDTH = 3  # line thickness
SPEED = 500.0  # pixels per second
BLAST_WIREFRAME = [
    Vector2(0.5, 0.0),  Vector2(-0.5, -1.0),
    Vector2(0.5, -2.0), Vector2(-0.5, -3.0)
]


class Blast(WEntity):

    def __init__(self, galaxy):
        super().__init__(galaxy, "blast", BLAST_WIREFRAME, WIDTH, WHITE)

        # linear velocity in pixels per second
        self.velocity = Vector2(0.0, -SPEED)
