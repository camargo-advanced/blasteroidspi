import pygame
from pygame.locals import *
from asteroid import Asteroid
from galaxy import Galaxy
from ship import Ship
#>>>>>
from fps import Fps
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

        self.galaxy = Galaxy(self.screen_rect)
        self.galaxy.add_entity(Ship(self.galaxy))
        #>>>>>
        self.fps = Fps(self.galaxy)
        self.galaxy.add_entity(self.fps)
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
#>>>>>
            self.fps.update_fps(self.clock.get_fps())
            self.galaxy.update(time_passed, event_list)
            self.galaxy.render(self.screen)
            self.galaxy.cleanup()

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    Game().run()  # start the game !