__author__ = 'Scott'
import pygame
import sys
import pytmx
from Game import *

pygame.init()
pygame.display.set_caption(GAME_TITLE)
load_images()
clock = pygame.time.Clock()
game = Game()
pygame.mixer.music.load('data/audio/randu.wav')
pygame.mixer.music.play(-1)

while True:
    game.keyboardManager()
    if(game.runLogic() == -1):
        break #break from loop and end game if lives are less than 0
    game.draw(screen)
    clock.tick(60)

