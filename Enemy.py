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
        self.centerx = self.rect.x

    def moveRelPlayer(self, playervx, playervy):
        self.rect.x -= playervx
        self.rect.y -= (playervy - 1)#offset gravitycha
        
    #enemy has to move relative to player try adding change of x and y from player to enemy
    def update(self, playervx, playervy):
        self.rect.x += self.changeX
        self.handleCollision()
        self.rect.y += self.changeY 
        self.jumpingCollision()#need gravity and vertical collisions with tiles
        self.updateAnimationFrames()
        self.lrBehavior()
        #print(self.changeX, self.changeY)

    def updateAnimationFrames(self):
        if pygame.time.get_ticks() - self.frameTime > 80:
            self.frameTime = pygame.time.get_ticks()
            if self.runningFrame == 6 or self.idleFrame == 4:
                self.runningFrame = 0
                self.idleFrame = 0
            else:
                self.runningFrame += 1
                self.idleFrame += 1
    def jumpingCollision(self):
        tileCollision = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        if len(tileCollision) > 0:
            for tile in tileCollision:
                if self.changeY > 0:
                    self.rect.bottom = tile.rect.top
                    self.changeY = 1

                    if self.direction == "right":
                        self.image = self.idleRight[self.idleFrame]
                        #self.doublejump = 0
                    else:
                        self.image = self.idleLeft[self.idleFrame]
                        #self.doublejump = 0
                else:
                    self.rect.top = tile.rect.bottom
                    self.changeY = 0
        else:
            self.changeY += 1
            if self.changeY > 0:
                if self.direction == "right":
                    self.image = self.jumpingRight[0]
                else:
                    self.image = self.jumpingLeft[0]

        if self.running and self.changeY == 1:
            if self.direction == "right":
                self.image = self.walkRight[self.runningFrame]
                #self.doublejump = 0
            else:
                self.image = self.walkLeft[self.runningFrame]
                #self.doublejump = 0
    
    #a simple left right walking behavior moves 100 pixels left and right
    def lrBehavior(self):
        self.changeX = 1
        if self.rect.x-100 >= self.centerx or self.rect.x+100 <= self.centerx:
            print"changed direction"
            self.changeX *= -1 # for some reason not changing direction
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
