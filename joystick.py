import pygame
from pygame.locals import *


class Joystick():
    def __init__(self, input_list):
        self.input_list = input_list

    def to_keyboard_events(self):
        output_list = []
        for event in self.input_list:
            
            if event.type == JOYBUTTONDOWN:
                if event.button in range(0,4):
                    output_list.append(pygame.event.Event(KEYDOWN, {'key': K_SPACE}))
                if event.button in range(4,6):
                    output_list.append(pygame.event.Event(KEYDOWN, {'key': K_UP}))
            
            if event.type == JOYBUTTONUP:
                if event.button in range(4,6):
                    output_list.append(pygame.event.Event(KEYUP, {'key': K_UP}))

            if event.type == JOYAXISMOTION:
                if abs(event.value) < 0.1:
                    event.value = 0.0
                if event.axis == 0 and event.value < 0:
                    output_list.append(pygame.event.Event(KEYDOWN, {'key': K_LEFT}))
                if event.axis == 0 and event.value > 0:
                    output_list.append(pygame.event.Event(KEYDOWN, {'key': K_RIGHT}))
                if event.axis == 0 and event.value == 0:
                    output_list.append(pygame.event.Event(KEYUP, {'key': K_LEFT}))

        return output_list

    