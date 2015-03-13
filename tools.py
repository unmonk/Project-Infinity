__author__ = 'Scott'
import os
import pygame

class GameControl(object):
    def __init__(self):
        self.fps = 60
        self.title = "Project Infinity"
        self.key = pygame.key.get_pressed()


def load_graphics(directory):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        image = pygame.image.load(os.path.join(directory, pic))
        if image.get_alpha():
            image = image.convert_alpha()
        else:
            image = image.convert()
            image.set_colorkey(255, 0, 255)
        graphics[name] = image
    return graphics


def load_music(directory):
    music = {}
    for songs in os.listdir(directory):
        name, ext = os.path.splitext(songs)
        music[name] = os.path.join(directory, songs)
    return music


def load_soundfx(directory):
    soundfx = {}
    for sounds in os.listdir(directory):
        name, ext = os.path.splitext(sounds)
        soundfx[name] = os.path.join(directory, sounds)
    return soundfx
