from pygame import Vector2


class Entity():

    def __init__(self, galaxy, name, color):
        self.galaxy = galaxy
        self.name = name
        self.position = Vector2(0.0, 0.0)
        self.color = color
        self.dead = False

    def update(self, time_passed):
        pass

    def render(self, surface):
        pass
