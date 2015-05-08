__author__ = 'Ryan'

import pygame
import pytmx
from Constants import *
from Tools import *
from Projectile import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, lives):
        pygame.sprite.Sprite.__init__(self)
        ###############################################ANIMATION START############################################################
        #Stand Right
        self.idleRight = []
        for i in range(0, 5):
            self.idleRight.append(DATA['playerIdle'][i])
        #Stand Left
        self.idleLeft = []
        for i in range(0, 5):
            self.idleLeft.append(pygame.transform.flip(self.idleRight[i], True, False))
        #Walking Right Animation
        self.walkRight = []
        for i in range(0, 7):
            self.walkRight.append(DATA['playerRun'][i])
        #Walking Left Animation
        self.walkLeft = []
        for i in range(0, 7):
            self.walkLeft.append(pygame.transform.flip(self.walkRight[i], True, False))
        #Jump Right Animation
        self.jumpingRight = []
        self.jumpingRight.append(DATA['playerJump'][0])
        self.jumpingRight.append(DATA['playerJump'][1])
        #Jump Left Animation
        self.jumpingLeft = []
        self.jumpingLeft.append(pygame.transform.flip(self.jumpingRight[0], True, False))
        self.jumpingLeft.append(pygame.transform.flip(self.jumpingRight[1], True, False))
        #Player Slide/Wall Jump
        self.wallAnim = DATA['playerSlide'][0]
        #animation frames
        self.running = False
        self.runningFrame = 0
        self.frameTime = pygame.time.get_ticks()
        self.idleFrame = 0
        ####################################################END ANIMATION#############################################

        self.image = self.idleRight[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = "right"
        self.changeX = 0
        self.changeY = 0
        #What level char is on > move to game
        self.currentLevel = None
        #lives
        self.lives = lives
        #player State
        self.state = "none"
        #firing
        self.projectiles = []
        self.doublejump = 0

    def moveRelPlayer(self, playervx, playervy):
        self.rect.x -= playervx
        self.rect.y -= (playervy - 1)#offset gravitycha
        
    #enemy has to move relative to player try adding change of x and y from player to enemy
    def update(self, playervx, playervy):
        self.rect.x += self.changeX
        self.handleCollision()
        self.rect.y += self.changeY 
        self.updateAnimationFrames()
        print(self.changeX, self.changeY)

    def updateAnimationFrames(self):
        if pygame.time.get_ticks() - self.frameTime > 80:
            self.frameTime = pygame.time.get_ticks()
            if self.runningFrame == 6 or self.idleFrame == 4:
                self.runningFrame = 0
                self.idleFrame = 0
            else:
                self.runningFrame += 1
                self.idleFrame += 1

    def handleCollision(self):
        tileCollision = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        for tile in tileCollision:
            if self.changeX > 0:
                self.rect.right = tile.rect.left
            else:
                self.rect.left = tile.rect.right


    def draw(self, screen):
        #pygame.draw.rect(screen,(0,0,0), (self.rect.x, self.rect.y, 40, 40))
        screen.blit(self.image, self.rect)
        for k in self.projectiles:
            k.display()
