import os
import pygame


class Sound():
    """Load game sounds and make them availaboe to play.
    This class follows the singleton design pattern. """
    _instance = None
    _sounds = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Sound, cls).__new__(cls)

            print(pygame.mixer.set_reserved(2))
            reserved_channel_0 = pygame.mixer.Channel(0)
            reserved_channel_1 = pygame.mixer.Channel(1)

            cls._sounds = {
                'bang': {
                    'sound_key': pygame.mixer.Sound(os.path.join('res', 'bang.wav')),
                    'channel': reserved_channel_0
                },
                'beep': {
                    'sound_key': pygame.mixer.Sound(os.path.join('res', 'beep.wav')),
                    'channel': None
                },
                'fire': {
                    'sound_key': pygame.mixer.Sound(os.path.join('res', 'fire.wav')),
                    'channel': None
                },
                'siren': {
                    'sound_key': pygame.mixer.Sound(os.path.join('res', 'siren.wav')),
                    'channel': None
                },
                'thrust': {
                    'sound_key': pygame.mixer.Sound(os.path.join('res', 'thrust.wav')),
                    'channel': reserved_channel_1
                },
                'beep-countdown': {
                    'sound_key': pygame.mixer.Sound(os.path.join('res', 'beep-countdown.wav')),
                    'channel': None
                }
            }
        return cls._instance

    def play(self, sound_key):
        sound = self._sounds[sound_key]['sound_key']
        channel = self._sounds[sound_key]['channel']
        if channel != None and not channel.get_busy():
            channel.play(sound)
        elif channel == None:
            sound.play()
