__author__ = 'Scott'
import pygame, sys
from SpriteBase import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
background = pygame.image.load("background.png").convert()


while True:
    screen.blit(background [0,0])
    screen.blit(sprites[1])
    pygame.display.flip()