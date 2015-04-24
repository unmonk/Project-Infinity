__author__ = 'Scott'

import os
import pygame
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
GAME_TITLE = "Project Infinity"
MAP_COLLISION_LAYER = 2
MAP_DEATH_LAYER = 3
MAP_BACKGROUND_LAYER = 0
MAP_FORGROUND_LAYER = 1
MAP_ENDOFLEVEL_LAYER = 5
MAP_ITEM_LAYER = 4
BACKGROUND_COLOR = (20, 20, 20)

#Main Character Licensed to Scott Weaver



PLAYERPATH = 'data/ninja/'

IMAGE_PATH =\
    {
        'playerIdle': [],
        'playerDie': [],
        'playerFlip': [],
        'playerJump': [],
        'playerRun': [],
        'playerSlide': [],
        'playerStun': [],
        'playerWallGrab': []

    }

for i in range(1, 6):
    IMAGE_PATH['playerIdle'].append(os.path.join(PLAYERPATH, "idle_0%d.png" %i))
for i in range(1, 5):
    IMAGE_PATH['playerDie'].append(os.path.join(PLAYERPATH, "die_0%d.png" %i))
for i in range(1, 7):
    IMAGE_PATH['playerFlip'].append(os.path.join(PLAYERPATH, "flip_0%d.png" %i))
for i in range(1, 8):
    IMAGE_PATH['playerRun'].append(os.path.join(PLAYERPATH, "run_0%d.png" %i))
for i in range(1, 4):
    IMAGE_PATH['playerStun'].append(os.path.join(PLAYERPATH, "stunned_0%d.png" %i))
IMAGE_PATH['playerJump'].append(os.path.join(PLAYERPATH, "jumpDown.png"))
IMAGE_PATH['playerJump'].append(os.path.join(PLAYERPATH, "jumpUp.png"))
IMAGE_PATH['playerWallGrab'].append(os.path.join(PLAYERPATH, "wallGrab.png"))
IMAGE_PATH['playerSlide'].append(os.path.join(PLAYERPATH, "slideDuck.png"))

DATA = \
    {
        'playerIdle': [],
        'playerDie': [],
        'playerFlip': [],
        'playerJump': [],
        'playerRun': [],
        'playerSlide':[],
        'playerStun':[],
        'playerWallGrab':[]
    }

def load_images():
    for i in range(0, 5):
        DATA['playerIdle'].append(pygame.image.load(IMAGE_PATH['playerIdle'][i]).convert_alpha())
    for i in range(0, 4):
        DATA['playerDie'].append(pygame.image.load(IMAGE_PATH['playerDie'][i]).convert_alpha())
    for i in range(0, 6):
        DATA['playerFlip'].append(pygame.image.load(IMAGE_PATH['playerFlip'][i]).convert_alpha())
    for i in range(0, 7):
        DATA['playerRun'].append(pygame.image.load(IMAGE_PATH['playerRun'][i]).convert_alpha())
    for i in range(0, 3):
        DATA['playerStun'].append(pygame.image.load(IMAGE_PATH['playerStun'][i]).convert_alpha())
    DATA['playerJump'].append(pygame.image.load(IMAGE_PATH['playerJump'][0]).convert_alpha())
    DATA['playerJump'].append(pygame.image.load(IMAGE_PATH['playerJump'][1]).convert_alpha())
    DATA['playerWallGrab'].append(pygame.image.load(IMAGE_PATH['playerWallGrab'][0]).convert_alpha())
    DATA['playerSlide'].append(pygame.image.load(IMAGE_PATH['playerSlide'][0]).convert_alpha())

    print(DATA['playerJump'])



def get_image(name, frame):
    return DATA[name][frame]