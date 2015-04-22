__author__ = 'Scott'
import pygame
import pytmx
from Constants import *
from Tools import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

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
        self.jumpingRight = DATA['playerJump'][0]

        #Jump Left Animation
        self.jumpingLeft = pygame.transform.flip(self.jumpingRight, True, False)



        self.image = self.idleRight[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.direction = "right"

        self.running = False
        self.runningFrame = 0
        self.runningTime = pygame.time.get_ticks()

        self.changeX = 0
        self.changeY = 0

        self.currentLevel = None

    def update(self):
        self.rect.x += self.changeX
        tileCollision = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        for tile in tileCollision:
            if self.changeX > 0:
                self.rect.right = tile.rect.left
            else:
                self.rect.left = tile.rect.right
        if self.rect.right >= SCREEN_WIDTH - 200:
            difference = self.rect.right - (SCREEN_WIDTH-200)
            self.rect.right = SCREEN_WIDTH - 200
            self.currentLevel.shiftLevelX(-difference)

        if self.rect.left <= 200:
            difference = 200 - self.rect.left
            self.rect.left = 200
            self.currentLevel.shiftLevelX(difference)

        if self.rect.bottom >= SCREEN_HEIGHT - 70:
            difference = self.rect.bottom - (SCREEN_HEIGHT-70)
            self.rect.bottom = SCREEN_HEIGHT - 70
            self.currentLevel.shiftLevelY(-difference)

        if self.rect.top <= 200:
            difference = 200 - self.rect.top
            self.rect.top = 200
            self.currentLevel.shiftLevelY(difference)

        self.rect.y += self.changeY
        tileCollision = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        if len(tileCollision) > 0:
            for tile in tileCollision:
                if self.changeY > 0:
                    self.rect.bottom = tile.rect.top
                    self.changeY = 1

                    if self.direction == "right":
                        self.image = self.idleRight[0]
                    else:
                        self.image = self.idleLeft[0]
                else:
                    self.rect.top = tile.rect.bottom
                    self.changeY = 0
        else:
            self.changeY += 0.2
            if self.changeY > 0:
                if self.direction == "right":
                    self.image = self.jumpingRight
                else:
                    self.image = self.jumpingLeft

        if self.running and self.changeY == 1:
            if self.direction == "right":
                self.image = self.walkRight[self.runningFrame]
            else:
                self.image = self.walkLeft[self.runningFrame]

        if pygame.time.get_ticks() - self.runningTime > 50:
            self.runningTime = pygame.time.get_ticks()
            if self.runningFrame == 2:
                self.runningFrame = 0
            else:
                self.runningFrame += 1

    def jump(self):
        self.rect.y += 40
        tileCollision = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        self.rect.y -= 40

        if len(tileCollision) > 0:
            if self.direction == "right":
                self.image = self.jumpingRight
            else:
                self.image = self.jumpingLeft

            self.changeY = -10

    def goRight(self):
        self.direction = "right"
        self.running = True
        self.changeX = 20

    def goLeft(self):
        self.direction = "left"
        self.running = True
        self.changeX = -20

    def stop(self):
        self.running = False
        self.changeX = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)










