__author__ = 'Scott'
import pygame
import pytmx
import os
import sys
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
        self.player.currentLevel = self.currentLevel


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
            self.currentLevel = self.levels[1]
        #powerup = self.player.powerUp() #not currently working I dont know what the powerup tile is called
        self.player.update()
        if self.player.lives <= 0:
            print "DEBUG: GAME OVER"
            #self.gameover()

    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)
        self.currentLevel.draw(screen)
        self.player.draw(screen)
        self.lives()
        pygame.display.flip()
        
    def incrementLevel(self):
        self.levelNumber += 1
    #def gameOver(self):
        #display game over screen
        #return to main menu

