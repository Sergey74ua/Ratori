import pygame as pg
from random import randint
from modules.unit.Abstract import Abstract


class Gangster(Abstract):
    """ Противник """

    @staticmethod
    def filling():
        """ Заполняем набор тайлов """
        pg.init()
        atlas = pg.image.load('images/gangster.png')
        atlas = pg.transform.scale(atlas, (8 * 80, 9 * 65))
        tile_atlas = []
        rate_x = 80
        rate_y = 65
        for row in range(9):
            tile_atlas.append([])
            for col in range(8):
                rect = (rate_x * col, rate_y * row)
                image = atlas.subsurface(rect, (rate_x, rate_y))
                tile_atlas[row].append(image)
        return tile_atlas

    def __init__(self, size, tile_atlas):
        """ Персонаж противника """
        self.rate_x = 80
        self.rate_y = 65
        self.tile_atlas = tile_atlas
        self.row = 6
        self.col = 0
        self.step = 0
        self.unit_turn = 8
        self.time_move = randint(15, 60)
        self.point_x = randint(size[0]//2-size[0]//3, size[0]//2+size[0]//3)
        self.point_y = randint(size[1]//2-size[1]//3, size[1]//2+size[1]//3)
        self.image = self.tile_atlas[self.row][self.col]
        self.rect = pg.Rect(self.point_x, self.point_y, self.rate_x, self.rate_y)
        self.arrest = False

    def update(self, speed):
        """ Обновление персонажа """
        if self.arrest:
            self.image = self.tile_atlas[8][self.col]
        elif self.unit_turn == 8:
            self.image = self.tile_atlas[6][0]
        else:
            self.col = self.unit_turn
            self.image = self.select(speed)

    def draw_unit(self, g):
        """ Отрисовка персонажа """
        g.blit(self.image, self.rect)
        pg.draw.rect(g, 'black', self.rect, 1)  ########

    def select(self, speed):
        """ Позиция персонажа """
        step = 48*speed/100
        if self.step > 120:
            if self.row > 4:
                self.row = 0
            else:
                self.row += 1
                self.step = 0
        else:
            self.step += step
        return self.tile_atlas[self.row][self.col]
