__author__ = 'Scott'
import pygame
import pytmx
from Constants import *
from Tools import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = SpriteSheet("data/mainchar.png")
        # sprites are 18x24
        # 9 spacing y, 14 spacing x
        #((Location Start x, Location Start y, size X, size Y), colorkey)
        #Stand Right
        self.idleRight = self.sprites.image_at((0, 0, 18, 24), None)
        #Stand Left
        self.idleLeft = self.sprites.image_at((0, 24, 18, 24), None)

        #Walking Right Animation
        self.walkRight =[(self.sprites.image_at((18, 0, 18, 24), None)),
        (self.sprites.image_at((36, 0, 18, 24), None)),
        (self.sprites.image_at((54, 0, 18, 24), None))]

        #Walking Left Animation
        self.walkLeft = [(self.sprites.image_at((18, 24, 18, 24), None)),
        (self.sprites.image_at((36, 24, 18, 24), None)),
        (self.sprites.image_at((54, 24, 18, 24), None))]

        #Jump Right Animation
        self.jumpingRight = [(self.sprites.image_at((90, 0, 18, 24), None)),
        (self.sprites.image_at((108, 0, 18, 24), None)),
        (self.sprites.image_at((126, 0, 18, 24), None)),
        (self.sprites.image_at((144, 0, 18, 24), None))]

        #Jump Left Animation
        self.jumpingLeft = [(self.sprites.image_at((90, 24, 18, 24), None)),
        (self.sprites.image_at((108, 24, 18, 24), None)),
        (self.sprites.image_at((126, 24, 18, 24), None)),
        (self.sprites.image_at((144, 24, 18, 24), None))]



        self.image = self.idleRight
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
            self.currentLevel.shiftLevel(-difference)

        if self.rect.left <= 200:
            difference = 200 - self.rect.left
            self.rect.left = 200
            self.currentLevel.shiftLevel(difference)

        self.rect.y += self.changeY
        tileCollision = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        if len(tileCollision) > 0:
            for tile in tileCollision:
                if self.changeY > 0:
                    self.rect.bottom = tile.rect.top
                    self.changeY = 1

                    if self.direction == "right":
                        self.image = self.idleRight
                    else:
                        self.image = self.idleLeft
                else:
                    self.rect.top = tile.rect.bottom
                    self.changeY = 0
        else:
            self.changeY += 0.2
            if self.changeY > 0:
                if self.direction == "right":
                    self.image = self.jumpingRight[1]
                else:
                    self.image = self.jumpingLeft[1]

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
        self.rect.y += 20
        tileCollision = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        self.rect.y -= 20

        if len(tileCollision) > 0:
            if self.direction == "right":
                self.image = self.jumpingRight[0]
            else:
                self.image = self.jumpingLeft[0]

            self.changeY = -6

    def goRight(self):
        self.direction = "right"
        self.running = True
        self.changeX = 3

    def goLeft(self):
        self.direction = "left"
        self.running = True
        self.changeX = -3

    def stop(self):
        self.running = False
        self.changeX = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)










