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

    def remove_entity(self, entity):
        del self.entities[entity.id]

    def get_entity_by_name(self, entity_name):
        for entity in self.entities.values():
            if entity.name == entity_name:
                return entity
        return None

    def get_entities_by_name(self, entity_name):
        entities = []
        for entity in self.entities.values():
            if entity.name == entity_name:
                entities.append(entity)
        return entities

    def update(self, time_passed, event_list):
        time_passed_seconds = time_passed / 1000.0
        for entity in list(self.entities.values()):
            entity.update(time_passed_seconds, event_list)
            if not self.in_screen_space(entity.position):
                # entities require authorization to leave the galaxy,
                # thus we must keep entities inside it !
                if entity.name == 'asteroid' or entity.name == 'ship':
                    self.wrap_coordinates(entity.position)
                elif entity.name == 'blast':
                    entity.dead = True

    def render(self, surface):
        surface.fill(BLACK)
        for entity in self.entities.values():
            entity.render(surface)

    def cleanup(self):
        # remove all dead entities
        for entity in list(self.entities.values()):
            if entity.dead == True:
                self.remove_entity(entity)

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
