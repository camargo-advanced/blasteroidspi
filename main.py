import pygame
from pygame.locals import *
from sys import exit
from asteroid import Asteroid
from galaxy import Galaxy

SCREEN_SIZE = (1600, 900)
FPS = 50


def run():

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 8)

    galaxy = Galaxy(SCREEN_SIZE)
    galaxy.add_entity(Asteroid(galaxy))
    galaxy.add_entity(Asteroid(galaxy))
    galaxy.add_entity(Asteroid(galaxy))

    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
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
