__author__ = 'Scott'
import pygame
from Constants import *
from Objects import *

class GameCamera(BaseObj):
    def __init__(self, level, position):
        super(GameCamera, self).__init__(level)

        self.offset = Vectors(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.scale = Vectors(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.position = position - self.offset + self.level.player.scale/2
        self.rect = pygame.Rect(self.position, self.scale)
        self.vel = Vectors(0,0)

        self.image = pygame.Surface((10, 10)).convert()
        self.image.fill(BLUE)

    def update(self, milliseconds):
        camera_position = self.position + self.offset
        player_position = self.level.player.position + self.level.player.scale/2
        distance = player_position - camera_position
        cameraX = 0

        camera_position.y = player_position.y

        if distance.x > cameraX:
            camera_position.x = player_position.x - cameraX
        if distance.x < -cameraX:
            camera_position.x = player_position + cameraX

        self.position = camera_position - self.offset
        self.rect.topleft = self.position


