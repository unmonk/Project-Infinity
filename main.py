__author__ = 'Scott'
import pygame
import sys
import pytmx
from Game import *
from menu import *

def runMenu():
    menu_items = ('Start', 'Quit')
    funcs = {'Start': runGame,
                 'Quit': sys.exit}
    game_menu = GameMenu(screen, funcs.keys(), funcs)
    game_menu.run()
    

def runGame():
    load_images()
    clock = pygame.time.Clock()
    game = Game()
    pygame.mixer.music.load('data/audio/randu.wav')
    pygame.mixer.music.play(-1)
    
    while True:
        game.keyboardManager()
        if(game.runLogic() == -1):
            break #break from loop and end game if lives are less than 0
        game.draw(screen)
        clock.tick(60)
    pygame.mixer.music.stop()#stop music playback    
    runMenu()#return to menu
    
pygame.init()
pygame.display.set_caption(GAME_TITLE)

runMenu()



