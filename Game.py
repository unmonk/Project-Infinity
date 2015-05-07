__author__ = 'Scott'
import pygame
import pytmx
import os
import sys
from Enemy import *
from Tools import *
from Player import *
from Constants import *


class Game(object):
    def __init__(self):
        self.levelNumber = 0
        self.levels = []
        self.levels.append(Level("data/level0.tmx"))
        self.levels.append(Level("data/level1.tmx"))
        self.currentLevel = self.levels[self.levelNumber]
        self.player = Player(300, 900, 5)
        self.enemy1 = Enemy(400, 900, 1)
        self.player.currentLevel = self.currentLevel
        self.enemy1.currentLevel = self.currentLevel


    def keyboardManager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.goLeft()
                elif event.key == pygame.K_RIGHT:
                    self.player.goRight()
                elif event.key == pygame.K_z:
                    self.player.jump()
                elif event.key == pygame.K_x:
                    self.player.shoot()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.player.changeX < 0:
                    self.player.stop()
                elif event.key == pygame.K_RIGHT and self.player.changeX > 0:
                    self.player.stop()

        return False

    def lives(self):
        self.livesImage = DATA['playerLives'][0]
        for i in range(0, self.player.lives):
            screen.blit(self.livesImage, (40+(i*20), 40))

    def runLogic(self):
        value = self.player.exitCollision()
        if value == 1:
            self.levelNumber += 1

            newValue = self.player.lives
            self.currentLevel = self.levels[1]
            self.player = Player(300, 300, newValue)
            self.enemy1 = Enemy(400, 300, 1)
            self.player.currentLevel = self.currentLevel
            self.enemy1.currentLevel = self.currentLevel
            value = 0


        #powerup = self.player.powerUp() #not currently working I dont know what the powerup tile is called
        self.player.update()
        self.enemy1.update()
        print self.enemy1.rect
        if self.player.lives <= 0 or self.levelNumber>LAST_LEVEL:#quit if dead or player hits last level
            print "DEBUG: GAME OVER"
            
            return -1 #break from loop in main
        return 0
    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)
        self.currentLevel.draw(screen)
        self.player.draw(screen)
        self.enemy1.draw(screen)
        self.lives()
        pygame.display.flip()
        
    def incrementLevel(self):
        self.levelNumber += 1
    #def gameOver(self):
        #display game over screen
        #return to main menu

