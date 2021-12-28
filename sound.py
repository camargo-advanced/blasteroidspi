import os
import pygame


class Sound():
    """Load game sounds and make them availaboe to play.
    This class follows the singleton design pattern. """
    _instance = None
    _sounds = {}

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Sound, cls).__new__(cls)
            pygame.mixer.init()
            cls._sounds['bang'] = pygame.mixer.Sound(
                os.path.join('res', 'bang.wav'))
            cls._sounds['beep'] = pygame.mixer.Sound(
                os.path.join('res', 'beep.wav'))
            cls._sounds['fire'] = pygame.mixer.Sound(
                os.path.join('res', 'fire.wav'))
            cls._sounds['siren'] = pygame.mixer.Sound(
                os.path.join('res', 'siren.wav'))
            cls._sounds['thrust'] = pygame.mixer.Sound(
                os.path.join('res', 'thrust.wav'))
        return cls._instance

    def play(self, sound_name):
        pygame.mixer.Sound.play(self._sounds[sound_name])
