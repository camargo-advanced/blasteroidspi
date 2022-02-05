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
            entity.update(time_passed_seconds, event_list)
            if not self.in_screen_space(entity.position):
                # entities require authorization to leave the galaxy,
                # thus we must keep entities inside it !
                self.wrap_coordinates(entity.position)

    def render(self, surface):
        surface.fill(BLACK)
        for entity in self.entities.values():
            entity.render(surface)

    def wrap_coordinates(self, position):
        width, height = self.rect.width, self.rect.height
        if position.x < 0.0:
            position.x += width
        if position.x >= width:
            position.x -= width
        if position.y < 0.0:
            position.y += height
        if position.y >= height:
            position.y -= height

    def in_screen_space(self, position):
        width, height = self.rect.width, self.rect.height
        if (position.x < 0.0):
            return False
        if (position.x >= width):
            return False
        if (position.y < 0.0):
            return False
        if (position.y >= height):
            return False
        return True
