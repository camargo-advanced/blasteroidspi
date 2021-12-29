import pygame
from pygame.locals import *
from asteroid import Asteroid
from galaxy import Galaxy
from score import Score
from ship import Ship
from sound import Sound

#SCREEN_SIZE = (1600, 900)
COLOR_DEPTH = 8
FPS = 50
NUMBER_ASTEROIDS_AT_GENESYS = 9


def run():
    # initialize pygame library and set screen mode
    pygame.init()

    # initialize the sound system and plays the first beep
    Sound().play('beep')

    # initialize the display
    #screen = pygame.display.set_mode(SCREEN_SIZE, 0, COLOR_DEPTH)
    screen = pygame.display.set_mode(flags=pygame.FULLSCREEN, depth=COLOR_DEPTH)
    screen_size = pygame.display.get_window_size()

    # build a new galaxy with a number of asteroids, a ship and the score
    galaxy = Galaxy(screen_size)
    for i in range(NUMBER_ASTEROIDS_AT_GENESYS):
        galaxy.add_entity(Asteroid(galaxy))
    galaxy.add_entity(Ship(galaxy))
    galaxy.add_entity(Score(galaxy))

    # main loop: set the framerate, updates entities in the galaxy
    # render the entities on buffer and flips the buffer to screen
    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get(QUIT): # CTR+Q (Windows) or CMD+Q (MAC)
            done = True

        time_passed = clock.tick(FPS)
        screen.lock()
        galaxy.update(time_passed)
        screen.unlock()
        galaxy.render(screen)
        galaxy.cleanup()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    run()
