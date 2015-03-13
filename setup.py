__author__ = 'Scott'

import os
import pygame
from tools import *
from Constants import *

pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT])
pygame.display.setcaption(GAME_CAPTION)
screen = pygame.display.set_mode(SCREEN_SIZE)
screen_rect = screen.get_rect()

MUSIC = load_music(os.path.join("data", "music"))
GRAPHICS = load_graphics(os.path.join("data", "graphics"))
SOUNDFX = load_soundfx(os.path.join("data", "soundfx"))