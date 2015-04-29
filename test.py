__author__ = 'Scott'
import sys, os
import pygame as pg
import pytmx
from pytmx import *



"""Initialize pygame, create a clock, create the window
with a surface to blit the map onto."""
pg.init()
fps_clock = pg.time.Clock()
main_surface = pg.display.set_mode((420, 420))
main_rect = main_surface.get_rect()


class Renderer(object):
    """
    This object renders tile maps from Tiled
    """
    def __init__(self, filename):
        tm = load_pygame(filename, pixelalpha=True)
        self.size = tm.width * tm.tilewidth, tm.height * tm.tileheight
        self.tmx_data = tm

    def render(self, surface):

        tw = self.tmx_data.tilewidth
        th = self.tmx_data.tileheight
        gt = self.tmx_data.getTileImageByGid

        if self.tmx_data.background_color:
            surface.fill(self.tmx_data.background_color)

        for layer in self.tmx_data.visibleLayers:
            if isinstance(layer, pytmx.TiledLayer):
                for x, y, gid in layer:
                    tile = gt(gid)
                    if tile:
                        surface.blit(tile, (x * tw, y * th))

            elif isinstance(layer, pytmx.TiledObjectGroup):
                pass

            elif isinstance(layer, pytmx.TiledImageLayer):
                image = gt(layer.gid)
                if image:
                    surface.blit(image, (0, 0))

    def make_map(self):
        temp_surface = pg.Surface(self.size)
        self.render(temp_surface)
        return temp_surface




"""Load the tmx file from the current directory,
create the tile_renderer object and load the tmx
file."""
tmx_file = "data/level0.tmx"
tile_renderer = Renderer(tmx_file)


"""Create the map surface using the make_map()
method.  Used to blit onto the main_surface."""
map_surface = tile_renderer.make_map()
map_rect = map_surface.get_rect()


"""Create a list of rects called "blockers" that the
player can collide with. The getObjects() method
returns a list of objects in your tile map. Each
tile has properties like name, type, x, y, width,
height.  Double click objects in Tiled to see these
properties.  These properties are used to make rect
objects in Pygame."""
blockers = []
tilewidth = tile_renderer.tmx_data.tilewidth
for tile_object in tile_renderer.tmx_data.getObjects():
    properties = tile_object.__dict__
    if properties['name'] == 'blocker':
        x = properties['x']
        y = properties['y']
        width = properties['width']
        height = properties['height']
        new_rect = pg.Rect(x, y, width, height)
        blockers.append(new_rect)


"""
The Player class will be a player-controlled sprite
that will collide with the blockers we just created.
We pass in the blockers as a constructor argument so
that we can assign them as an attribute.  During the
update method, we can refer to this attribute to detect
collision.
"""



class Player(pg.sprite.Sprite):
    def __init__(self, blockers):
        super(Player, self).__init__()
        self.image = pg.Surface((22, 22))
        self.image.fill((130, 100, 200))
        self.rect = self.image.get_rect(x=100,
                                        y=300)
        self.x_vel = 0
        self.y_vel = 0
        self.blockers = blockers

    def update(self, keys):
        """
        Set player velocity by keys, move by velocity, check
        for collision.  It's important to check collisions
        for both on the x-axis and y-axis, rather than just once.
        """
        if keys[pg.K_DOWN]:
            self.y_vel = 3
        elif keys[pg.K_UP]:
            self.y_vel = -3
        else:
            self.y_vel = 0
        if keys[pg.K_LEFT]:
            self.x_vel = -3
        elif keys[pg.K_RIGHT]:
            self.x_vel = 3
        else:
            self.x_vel = 0

        self.rect.x += self.x_vel
        for blocker in self.blockers:
            if self.rect.colliderect(blocker):
                self.rect.x -= self.x_vel
                self.x_vel = 0

        self.rect.y += self.y_vel
        for blocker in self.blockers:
            if self.rect.colliderect(blocker):
                self.rect.y -= self.y_vel
                self.y_vel = 0

    def draw(self, surface):
        """
        Blit player image to screen.
        """
        surface.blit(self.image, self.rect)

player = Player(blockers)


"""Simple game loop that updates the player sprite,
blits the map_surface onto the main surface, and blits
the player sprite onto the main surface.
"""
def main():
    while True:
        keys = pg.key.get_pressed()
        player.update(keys)

        main_surface.blit(map_surface, map_rect)
        player.draw(main_surface)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        pg.display.update()
        fps_clock.tick(60)

if __name__ == "__main__":
    main()
