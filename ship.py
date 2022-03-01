from pygame.locals import *
from blast import Blast 
from wentity import WEntity
from pygame.math import Vector2
from utils import *

WIDTH = 3  # line thickness
SCALE_FACTOR = 5.0
ACCELERATION = 250.0  # pixels per second
DAMPING = 0.57  # some damping
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

        # ship initial position
        self.position = Vector2(self.galaxy.rect.width/2,
                                self.galaxy.rect.height/2)
        self.acceleration = ACCELERATION
        self.damping = DAMPING 
        self.angular_speed = ANGULAR_SPEED
        self.size = SCALE_FACTOR
        self.firing = False 

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)

        self.process_events(event_list)
        if self.firing: 
            # build a new blast, set its position to the ship's,
            # set its velocity vector to ship's orientation
            # and then add it to the galaxy
            blast = Blast(self.galaxy, Vector2(self.position), self.angle)
            self.galaxy.add_entity(blast)
            self.firing = False

        for entity in self.galaxy.get_entities_by_name('asteroid'):
            if self.collide(entity):
                # if a rock hit me, I need to be positioned at the center of screen stationary,
                # and in the same angle I was born. The lives must be reduced by 1
                self.position = Vector2(self.galaxy.rect.width/2,
                                        self.galaxy.rect.height/2)
                self.velocity = Vector2(0.0, 0.0)
                self.angle = 0.0
#>>>>>
                self.galaxy.get_entity_by_name('score').update_lives(-1)

    def render(self, surface):
        super().render(surface)

        if self.accelerating == FORWARD:
            self.wireframe = THRUST_WIREFRAME
            super().render(surface)
            self.wireframe = SHIP_WIREFRAME

    def process_events(self, event_list):
        for event in event_list:

            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    self.start_rotating(CCLOCKWISE)
                if event.key == K_RIGHT or event.key == K_d:
                    self.start_rotating(CLOCKWISE)
                if event.key == K_UP or event.key == K_w:
                    self.start_accelerating(FORWARD)
                if event.key == K_SPACE:
                    self.fire()

            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_a or \
                        event.key == K_RIGHT or event.key == K_d:
                    self.stop_rotating()
                if event.key == K_UP or event.key == K_w:
                    self.stop_accelerating()

    def fire(self): 
        self.firing = True