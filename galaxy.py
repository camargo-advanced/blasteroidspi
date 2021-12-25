from utils import *


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

    def get(self, entity_id):
        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None

    def update(self, time_passed):
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
