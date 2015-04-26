__author__ = 'SIU920142021'
from Tools import *
from Constants import *
from Vector import *


class Projectile(object):

    def __init__(self, spawn, direction):
        self.spawn = Vector(spawn[0], spawn[1])
        self.speed = Vector(direction, 0)
        self.currentWeapon = DATA['playerProjectile'][0]
        self.image = self.currentWeapon
        self.imgX, self.imgY = self.image.get_size()
        self.active = True


    def get_rect(self):
        return pygame.Rect(self.spawn.x, self.spawn.y, self.imgX, self.imgY)

    def update(self):
        self.spawn.add(self.speed)
        #self.checkBorder()

    #def checkBorder(self):
     #   if self.spawn.x > SCREEN_WIDTH or self.spawn.x < 0 or self.spawn.y > SCREEN_HEIGHT or self.spawn.y < 0:
      #      self.active = False

    def display(self):
        if self.active:
            screen.blit(self.image, (self.spawn.x, self.spawn.y))

