# TO-DO:
#       - Trabalhar com múltiplos canais de aidio, para resolver o problema de
#         não sair o som de explosao quando uma rocha bate na nave, caso a
#         nave esteja com o thrust ativado (pois o som dele é que ocupa o canal).
#

import pygame
from pygame.locals import *
from asteroid import Asteroid
from galaxy import Galaxy
from score import RESET_GAME, Score
from ship import Ship
from sound import Sound

COLOR_DEPTH = 8
FPS = 1000
NUMBER_ASTEROIDS_AT_GENESYS = 9


def reset_game(screen_size, clock):
    # build a new galaxy with a number of asteroids, a ship and the score
    galaxy = Galaxy(screen_size)
    for i in range(NUMBER_ASTEROIDS_AT_GENESYS):
        galaxy.add_entity(Asteroid(galaxy))
    galaxy.add_entity(Ship(galaxy))
    galaxy.add_entity(Score(galaxy, clock))
    return galaxy


def run():

    pygame.init()  # initialize pygame library and set screen mode

    Sound().play('beep')  # play the first beep to indicate the game has started!

    # initialize the display and clock
    screen = pygame.display.set_mode(
        flags=pygame.FULLSCREEN, depth=COLOR_DEPTH)
    screen_size = pygame.display.get_window_size()
    clock = pygame.time.Clock()

    galaxy = reset_game(screen_size, clock)  # build a new game

    # main loop: set the framerate, updates entities in the galaxy
    # render the entities on buffer and flips the buffer to screen
    done = False
    while not done:
        # ALT+F4 (Windows) or CMD+Q (MAC)
        for event in pygame.event.get([QUIT, RESET_GAME]):
            if event.type == QUIT:
                done = True
            if event.type == RESET_GAME:
                galaxy = reset_game(screen_size, clock)  # build a new game

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
