import pygame
from blast import Blast
from sound import Sound
from wentity import CCLOCKWISE, CLOCKWISE, FORWARD, WEntity
from pygame.math import Vector2
from utils import *
from pygame.locals import *

WIDTH = 3  # line thickness
SCALE_FACTOR = 5.0
ACCELERATION = 150.0  # pixels per second
ANGULAR_SPEED = 180.0  # degrees per second
SHIP_WIREFRAME = [
    Vector2(0.0, -5.0),  Vector2(3.0, 4.0), Vector2(1.5, 2.0),
    Vector2(-1.5, 2.0), Vector2(-3.0, 4.0)
]
THRUST_WIREFRAME = [
    Vector2(1.0, 2.0), Vector2(0.0, 5.0), Vector2(-1.0, 2.0)
]


class Ship(WEntity):

    def __init__(self, galaxy):
        super().__init__(galaxy, "ship", GREEN, SHIP_WIREFRAME, WIDTH)

        # entity initial position
        width, height = self.galaxy.size
        self.position = Vector2(width/2, height/2)

        # linear acceleration and angular speed
        self.acceleration = ACCELERATION
        self.angular_speed = ANGULAR_SPEED

        self.size = SCALE_FACTOR
        self.shielded = True
        self.firing = False
        self.dying = False

    def update(self, time_passed):
        super().update(time_passed)

        if self.galaxy.get_entity_by_name('score').game_status != GAME_RUNNING:
            return

        self.process_events()

        if self.firing:
            # build a new blast, set its position to the ship's,
            # set its velocity vector to ship's orientation
            # and then add it to the galaxy
            blast = Blast(self.galaxy, Vector2(self.position), self.angle)
            self.galaxy.add_entity(blast)

        for entity in self.galaxy.get_entities_by_name('asteroid'):
            if not self.shielded and self.collide(entity):
                # if a rock hit me, I lose a life but I'm shielded for 5 sec!
                # I also need to be positioned at the center of screen stationary,
                # and in the same angle I was born. The lives must be reduced by 1
                self.dying = True
                self.shield()
                pygame.time.set_timer(UNSHIELD_EVENT, 2500, 1)
                width, height = self.galaxy.size
                self.position = Vector2(width/2, height/2)
                self.velocity = Vector2(0.0, 0.0)
                self.angle = 0.0
                self.galaxy.get_entity_by_name('score').update_lives(-1)

    def render(self, surface):
        # render visuals and sounds
        super().render(surface)

        if self.accelerating == FORWARD:
            if self.galaxy.get_entity_by_name('score').game_status == GAME_RUNNING:
                Sound().play('thrust')
            self.wireframe = THRUST_WIREFRAME
            super().render(surface)
            self.wireframe = SHIP_WIREFRAME

        if self.firing:
            if self.galaxy.get_entity_by_name('score').game_status == GAME_RUNNING:
                Sound().play('fire')
            self.firing = False

        if self.dying:
            if self.galaxy.get_entity_by_name('score').game_status == GAME_RUNNING:
                Sound().play('bang')
            self.dying = False

    def process_events(self):
        for event in pygame.event.get([KEYUP, KEYDOWN, UNSHIELD_EVENT]):

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.start_rotating(CCLOCKWISE)
                if event.key == K_RIGHT:
                    self.start_rotating(CLOCKWISE)
                if event.key == K_UP:
                    self.start_accelerating(FORWARD)
                if event.key == K_SPACE:
                    self.fire()

            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    self.stop_rotating()
                if event.key == K_UP:
                    self.stop_accelerating()

            if event.type == UNSHIELD_EVENT:
                self.unshield()

    def fire(self):
        self.firing = True

    def unshield(self):
        self.shielded = False
        self.galaxy.get_entity_by_name('score').update_ship_shielded(False)

    def shield(self):
        self.shielded = True
        print("*", self.galaxy.get_entity_by_name('score'))
        self.galaxy.get_entity_by_name('score').update_ship_shielded(True)
