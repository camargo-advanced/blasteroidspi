import pygame
from pygame.locals import *
from asteroid import Asteroid
from galaxy import Galaxy
from ship import Ship

SCREEN_SIZE = (1600, 900)
COLOR_DEPTH = 8
FPS = 50
NUMBER_OF_ASTEROIDS_AT_GENESYS = 9


def run():
    # initializes pygame library and set screen mode
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, COLOR_DEPTH)

    # build a new galaxy with a number of asteroids and a ship
    galaxy = Galaxy(SCREEN_SIZE)
    for i in range(NUMBER_OF_ASTEROIDS_AT_GENESYS):
        galaxy.add_entity(Asteroid(galaxy))
    galaxy.add_entity(Ship(galaxy))

    # main loop: set the framerate, updates entities in the galaxy
    # render entities in the buffer and flips the buffer to screen
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

    # leaves the game
    pygame.quit()


if __name__ == "__main__":
    run()
