__author__ = 'Scott'
import pygame
from Vectors import *


class BaseObj(object):
    __unique_id = 0

    def __init__(self, level, update_order = 0):
        self.level = level

        #The order this is loaded compared to others
        self.update_order = update_order

        #Unique ID:
        self.obj_id = self.__unique_id

        #update number of unique IDs
        BaseObj.__unique_id += 1

        self.isEnabled = True
        self.isStatic = True
        self.position = Vectors(0,0)
        self.commands = None

    def update(self, milliseconds):
        if not self.commands == None:
            exec self.commands


class DrawObj(BaseObj):
    def __init__(self, level, update_order = 0, draw_order = 0):
        super(BaseObj, self).__init__(level, update_order)
        self.draw_order = draw_order

        self.isVisible = True
        self.image = pygame.surface.Surface((0, 0))
        self.offset = Vectors(0, 0)

        self.scale_factor = 1

    def show(self):
        self.isEnabled = True
        self.isVisible = True

    def hide(self):
        self.isEnabled = False
        self.isVisible = False

    def draw(self, milliseconds, surface):
        if self.isStatic:
            surface.blit(self.image, self.position + self.offset)
        else:
            relPos = (self.position + self.offset) - self.level.camera.position
            relPos = Vectors(relPos.x, relPos.y)
            surface.blit(self.image, relPos)




