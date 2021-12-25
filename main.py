import pygame
from pygame.locals import *
from sys import exit
from asteroid import Asteroid
from galaxy import Galaxy
from ship import Ship

SCREEN_SIZE = (1600, 900)
COLOR_DEPTH = 8
FPS = 50


def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, COLOR_DEPTH)

    galaxy = Galaxy(SCREEN_SIZE)
    for i in range(9):
        galaxy.add_entity(Asteroid(galaxy))

    galaxy.add_entity(Ship(galaxy))

    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get(QUIT):
            done = True

        time_passed = clock.tick(FPS)
        screen.lock()
        galaxy.update(time_passed)
        screen.unlock()
        galaxy.render(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    run()
