__author__ = 'Scott'
import pygame
import sys, os
from Objects import *

#pulled from ragnarok engine
#Copyright

class KeyState(object):
    def __init__(self):
        #Contains a reference to all pressed status of all the keys
        self.key_states = []

    def copy(self):
        new_keys = []
        for key in self.key_states:
            new_keys.append(key)
        state_cpy = KeyState()
        state_cpy.key_states = new_keys
        return state_cpy

    def query_state(self, key):
        """
       Query the state of a key. True if the key is down, false if it is up.
       key is a pygame key.
       """
        return self.key_states[key]

class Keyboard(BaseObj):
    def __init__(self):
        super(Keyboard, self).__init__(None)
        self.current_state = KeyState()
        self.previous_state = KeyState()
        self.current_state.key_states = pygame.key.get_pressed()

    def is_down(self, key):
        return self.current_state.query_state(key)

    def is_up(self, key):
        return not self.current_state.query_state(key)

    def is_clicked(self, key):
        return self.current_state.query_state(key) and (not self.previous_state.query_state(key))

    def is_released(self, key):
        return self.previous_state.query_state(key) and (not self.current_state.query_state(key))

    def is_any_down(self):
        """Is any button depressed?"""
        for key in range(len(self.current_state.key_states)):
            if self.is_down(key):
                return True
        return False

    def is_any_clicked(self):
        """Is any button clicked?"""
        for key in range(len(self.current_state.key_states)):
            if self.is_clicked(key):
                return True
        return False

    def update(self, milliseconds):
        keys = pygame.key.get_pressed()
        self.previous_state = self.current_state.copy()
        self.current_state.key_states = keys
        super(Keyboard, self).update(milliseconds)