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
FPS = 50
NUMBER_ASTEROIDS = 9


def reset_game(screen_size, clock):
    # build a new galaxy with a number of asteroids, a ship and the score
    galaxy = Galaxy(screen_size)
    galaxy.add_entity(Score(galaxy, clock))
    galaxy.add_entity(Ship(galaxy))
    for i in range(NUMBER_ASTEROIDS):
        galaxy.add_entity(Asteroid(galaxy))
    return galaxy


def run():

    pygame.init()  # initialize pygame library and set screen mode
    Sound().play('beep')  # play the first beep to indicate the game has started!
    pygame.display.set_caption("Asteroids arcade game") # set window caption

    # initialize the display and clock
    screen = pygame.display.set_mode(
        flags=pygame.FULLSCREEN, depth=COLOR_DEPTH)
    screen_size = pygame.display.get_window_size()
    clock = pygame.time.Clock()

    galaxy = reset_game(screen_size, clock)  # build a new game

    # main game loop!
    done = False
    while not done:
        # Press ALT+F4 (Windows) or CMD+Q (MAC) to quit the game !
        for event in pygame.event.get([QUIT, RESET_GAME]):
            if event.type == QUIT:
                done = True
            if event.type == RESET_GAME:
                galaxy = reset_game(screen_size, clock)  # build a new game

        if len(galaxy.get_entities_by_name('asteroid')) == 0:
            # if you run out of asteroids, it changes phases, adding a life
            # but increasing the asteroids speed by 21%
            galaxy.get_entity_by_name('score').difficulty *= 1.21
            galaxy.get_entity_by_name('score').update_lives(1)
            for i in range(NUMBER_ASTEROIDS):
                galaxy.add_entity(Asteroid(galaxy))

        # set the framerate, updates entities in the galaxy
        # render the entities on buffer and flips the buffer to screen
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
