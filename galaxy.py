from utils import *
import pygame
from pygame.locals import *
from wentity import FORWARD, BACKWARDS, CLOCKWISE, CCLOCKWISE


class Galaxy():

    def __init__(self, size):
        self.size = size
        self.entities = {}
        self.entity_id = 0

    def add_entity(self, entity):
        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1

    def remove_entity(self, entity):
        del self.entities[entity.id]

    def get_entity(self, entity_id):
        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None

    def get_entity_by_name(self, entity_name):
        for entity in self.entities.values():
            if entity.name == entity_name:
                return entity
        return None

    def update(self, time_passed):
        self.process_events()
        time_passed_seconds = time_passed / 1000.0
        for entity in list(self.entities.values()):
            entity.update(time_passed_seconds)
            # entities require authorization to leave the galaxy,
            # thus we need to keep entities inside it !
            wrap_coordinates(entity.position, self.size)

    def render(self, surface):
        surface.fill(BLACK)
        for entity in self.entities.values():
            entity.render(surface)

    def process_events(self):
        for event in pygame.event.get([KEYUP, KEYDOWN]):
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.get_entity_by_name('ship').start_rotating(CCLOCKWISE)
                if event.key == K_RIGHT:
                    self.get_entity_by_name('ship').start_rotating(CLOCKWISE)
                if event.key == K_UP:
                    self.get_entity_by_name('ship').start_accelerating(FORWARD)
                if event.key == K_DOWN:
                    self.get_entity_by_name('ship').start_accelerating(BACKWARDS)
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    self.get_entity_by_name('ship').stop_rotating()
                if event.key == K_UP or event.key == K_DOWN:
                    self.get_entity_by_name('ship').stop_accelerating()
