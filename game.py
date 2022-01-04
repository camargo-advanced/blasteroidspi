import pygame
from pygame.locals import *
from galaxy import Galaxy
from score import Score
from ship import Ship
from asteroid import Asteroid
from countdown import CountDown
from utils import *

COLOR_DEPTH = 8
FPS = 50
NUMBER_ASTEROIDS = 5


class Game():
    def __init__(self):
        pygame.init()  # initialize pygame library and set screen mode
        self.screen = pygame.display.set_mode(
            flags=pygame.FULLSCREEN, depth=COLOR_DEPTH)  # initialize the display
        self.screen_size = pygame.display.get_window_size()
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption(
            "Asteroids arcade game")  # set window caption
        self.clock = pygame.time.Clock()  # the time starts
        pygame.event.post(pygame.event.Event(RESTART_GAME))

    def run(self):
        # game main loop!
        done = False
        while not done:
            # Press ALT+F4 (Windows) or CMD+Q (MAC) to quit the game !
            for event in pygame.event.get([QUIT, RESTART_GAME, NEW_PHASE]):

                if event.type == QUIT:
                    done = True

                if event.type == RESTART_GAME:
                    # build a new galaxy with a number of asteroids, a ship and the score,
                    # add a count down to queue game start in a new phase
                    self.galaxy = Galaxy(self.screen_rect)
                    self.score = Score(self.galaxy)
                    self.galaxy.add_entity(self.score)
                    self.galaxy.add_entity(Ship(self.galaxy))
                    for i in range(NUMBER_ASTEROIDS):
                        self.galaxy.add_entity(Asteroid(self.galaxy))
                    self.galaxy.add_entity(CountDown(self.galaxy))
                    pygame.time.set_timer(NEW_PHASE, 6000, 1)

                if event.type == NEW_PHASE:
                    # clears events prior to running the game
                    for event in pygame.event.get([KEYUP, KEYDOWN]):
                        pass
                    self.score.update_game_status(GAME_RUNNING)
                    pygame.time.set_timer(UNSHIELD_EVENT, 5000, 1)

            if len(self.galaxy.get_entities_by_name('asteroid')) == 0:
                # if you run out of asteroids, it changes phases, adding a life
                # but increasing the asteroids speed
                self.score.increase_difficulty_by(1.11)
                self.score.update_lives(+1)
                for i in range(NUMBER_ASTEROIDS):
                    self.galaxy.add_entity(Asteroid(self.galaxy))

            # set the framerate, updates entities in the galaxy
            # render the entities on buffer and flips the buffer to screen
            time_passed = self.clock.tick(FPS)
            self.score.update_fps(self.clock.get_fps())
            self.screen.lock()
            self.galaxy.update(time_passed)
            self.screen.unlock()
            self.galaxy.render(self.screen)
            self.galaxy.cleanup()

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    Game().run()  # start the game !
