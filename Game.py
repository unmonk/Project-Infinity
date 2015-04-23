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

        self.player = Player(300, 900)
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
                elif event.key == pygame.K_UP:
                    self.player.jump()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.player.changeX < 0:
                    self.player.stop()
                elif event.key == pygame.K_RIGHT and self.player.changeX > 0:
                    self.player.stop()

        return False

    def runLogic(self):
        self.player.update()

    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)
        self.currentLevel.draw(screen)
        self.player.draw(screen)
        pygame.display.flip()
