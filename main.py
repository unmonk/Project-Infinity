__author__ = 'Scott'
import pygame
import sys
import pytmx
from Game import *

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(GAME_TITLE)
load_images()
clock = pygame.time.Clock()
game = Game()

while True:
    game.keyboardManager()
    game.runLogic()
    game.draw(screen)
    clock.tick(60)

