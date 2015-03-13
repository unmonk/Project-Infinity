__author__ = 'Scott'
import pygame, sys


class CreateSprites(pygame.sprite.Sprites):
    def __init__(self, size, file, startpos):
        (self.spriteSizeX, self.spriteSizeY) = size
        (self.spriteStartX, self.spriteStartY) = startpos
        self.filename = file

        sheet = pygame.image.load(self.filename).convert_alpha()
        sheet_rect = sheet.get_rect()
        self.sprites = []
        print sheet_rect.height, sheet_rect.width
        for i in range(0, sheet_rect.height - self.spriteSizeY, size[1]): #rows
            print "row"
            for i in range(0, sheet_rect.width - self.spriteSizeX, size[0]):
                print "column"
                sheet.set_clip(pygame.Rect(self.spriteStartX, self.spriteStartY, self.spriteSizeX, self.spriteSizeY))
                sprite = sheet.subsurace(sheet.get_clip())
                self.sprites.append(sprite)
                self.spriteStartX += self.spriteSizeX
            self.spriteStartY += self.spriteSizeY
            self.spriteStartX = 0
        print self.sprites










