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
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
LAST_LEVEL = 1

#Main Character Licensed to Scott Weaver

#Platform tiles CC0
#background music CC0

#Jump Sounds Credit: dklon
pygame.mixer.init()
jump1 = pygame.mixer.Sound('data/audio/jump_01.wav')
jump2 = pygame.mixer.Sound('data/audio/jump_03.wav')
heart = pygame.mixer.Sound('data/audio/upshort.wav')





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
        'playerWallGrab': [],
        'playerProjectile': [],
        'playerLives': []

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
IMAGE_PATH['playerProjectile'].append(os.path.join(PLAYERPATH, "knife.png"))
IMAGE_PATH['playerLives'].append(os.path.join(PLAYERPATH, "heart.png"))

DATA = \
    {
        'playerIdle': [],
        'playerDie': [],
        'playerFlip': [],
        'playerJump': [],
        'playerRun': [],
        'playerSlide':[],
        'playerStun':[],
        'playerWallGrab':[],
        'playerProjectile':[],
        'playerLives': []
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
    DATA['playerProjectile'].append(pygame.image.load(IMAGE_PATH['playerProjectile'][0]).convert_alpha())
    DATA['playerProjectile'].append(pygame.transform.flip(DATA['playerProjectile'][0], True, False))
    DATA['playerLives'].append(pygame.image.load(IMAGE_PATH['playerLives'][0]).convert_alpha())


    print "DEBUG IMAGES:", DATA



def get_image(name, frame):
    return DATA[name][frame]