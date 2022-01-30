import pygame
from pygame.locals import *
from asteroid import Asteroid
from galaxy import Galaxy
from utils import *

COLOR_DEPTH = 8
FPS = 50
NUMBER_ASTEROIDS = 7


class Game():
    def __init__(self):
        pygame.init()  # initialize pygame library and set screen mode
        self.screen = pygame.display.set_mode(
            flags=pygame.FULLSCREEN, depth=COLOR_DEPTH)  # initialize the display
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption(
            "Asteroids arcade game")  # set window caption
        self.clock = pygame.time.Clock()  # the time starts

    def run(self):

        # build a new galaxy with a number of asteroids
        self.galaxy = Galaxy(self.screen_rect)
        for i in range(NUMBER_ASTEROIDS):
            self.galaxy.add_entity(Asteroid(self.galaxy))

        # game main loop!
        done = False
        while not done:

            # Press Q (all systems) or ALT+F4 (Windows) or CMD+Q (MAC) to quit the game !
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == KEYDOWN and event.key == K_q or event.type == QUIT:
                    done = True

            # set the framerate, updates entities in the galaxy
            # render the entities on buffer and flips the buffer to screen
            time_passed = self.clock.tick(FPS)
            print(self.clock.get_fps())
            self.screen.lock()
            self.galaxy.update(time_passed, event_list)
            self.screen.unlock()
            self.galaxy.render(self.screen)

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    Game().run()  # start the game !
