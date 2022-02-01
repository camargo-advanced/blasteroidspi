from utils import *


class Galaxy():

    def __init__(self, rect):
        self.rect = rect
        self.entities = {}
        self.entity_id = 0

    def add_entity(self, entity):
        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1

    def update(self, time_passed, event_list):
        time_passed_seconds = time_passed / 1000.0
        for entity in self.entities.values():
            entity.update(time_passed, event_list)

    def render(self, surface):
        surface.fill(BLACK)
        for entity in self.entities.values():
            entity.render(surface)