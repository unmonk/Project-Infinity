__author__ = 'Scott'
import pygame
class SpriteBase(pygame.sprite.Sprite):
    allSpritesGroup = pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_string):
        pygame.sprite.Sprite.__init__(self)
        SpriteBase.allSpritesGroup.add(self)

        self.image = pygame.image.load(image_string)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.width = width
        self.height = height

    def sprite_sheet(size, file, pos):
        len_sprt_x,len_sprt_y = size
        sprt_rect_x,sprt_rect_y = pos
        sheet = pygame.image.load(file).convert_alpha()
        sheet_rect = sheet.get_rect()
        sprites = []
        print sheet_rect.height, sheet_rect.width
        for i in range(0,sheet_rect.height-len_sprt_y,size[1]):
            print "row"
            for i in range(0,sheet_rect.width-len_sprt_x,size[0]):
                print "column"
                sheet.set_clip(pygame.Rect(sprt_rect_x, sprt_rect_y, len_sprt_x, len_sprt_y))
                sprite = sheet.subsurface(sheet.get_clip())
                allSpritesGroup.add(sprite)
                sprt_rect_x += len_sprt_x

            sprt_rect_y += len_sprt_y
            sprt_rect_x = 0
            print sprites
            return sprites