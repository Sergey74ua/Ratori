import pygame as pg
from modules.ground.map_game import map, start_point


class Terrain(object):
    """ Карта игры """
    _atlas_ = pg.image.load('images/sprite.bmp')
    _atlas_.set_colorkey((255, 255, 255))
    _rate_ = 48

    def __init__(self):
        """ Графический атлас (graphic atlas / tile) """
        self.map = map
        self.rate = self._rate_
        self.tile_atlas = {}
        self.tile_atlas = self.filling()
        self.start_point = start_point

    def filling(self):
        """ Заполняем набор тайлов """
        atlas = self._atlas_
        rate = self.rate
        for row in range(atlas.get_height() // rate):
            for col in range(atlas.get_width() // rate):
                rect = (rate * col, rate * row)
                image = atlas.subsurface(rect, (rate, rate))
                key = str(f'{row:0{2}}') + str(f'{col:0{2}}')
                self.tile_atlas[key] = image
        return self.tile_atlas
