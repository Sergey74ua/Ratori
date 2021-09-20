import pygame as pg
from modules.ground.Terrain import Terrain


class Minimap(object):
    """ Миникарта в игровом окне """

    def __init__(self, size):
        """ Миникарта """
        self.size = size
        self.terrain = Terrain()
        self.count_x = len(self.terrain.map[0])
        self.count_y = len(self.terrain.map)
        self.rate = self.terrain.rate
        self.scale = self.rate
        self.rect = self.calculation()
        self.surface = pg.Surface((self.rect.width, self.rect.height))
        self.hero = self.position(self.terrain.start_point)
        self.visio = pg.Rect(self.visibility())
        self.filling()

    def update(self, hero, size):
        """ Обновление миникарты """
        # Перерасчет размера миникарты
        if self.size != size:
            self.size = size
            self.rect = self.calculation()
            self.surface = pg.Surface((self.rect.width, self.rect.height))
            self.filling()
        # Обновления позиции персонажа на миникарте
        self.hero = self.position(hero)
        self.visio = self.visibility()

    def draw(self, g):
        """ Отрисовка """
        g.blit(self.surface, self.rect)
        pg.draw.circle(g, 'Blue', self.hero, 5)
        pg.draw.rect(g, 'Green', self.visio, 1)
        pg.draw.rect(g, 'Black', self.rect, 3)

    def calculation(self):
        """ Перерасчет размеров миникарты """
        if self.count_x > self.count_y:  # ДОДЕЛАТЬ масштабируемость
            self.rate = self.size[0] // (self.count_x * 3)
        else:
            self.rate = self.size[1] // (self.count_y * 3)
        width = self.count_x * self.rate
        height = self.count_y * self.rate
        rect = pg.Rect(1, self.size[1] - height - 1, width, height)
        self.scale = self.terrain.rate // self.rate
        return rect

    def position(self, hero):
        """ Перерасчет позиции героя """
        hero_x = hero[0] // self.scale
        hero_y = self.rect[1] + hero[1] // self.scale
        return hero_x, hero_y

    def visibility(self):
        """ Перерасчет зоны видимости на миникарте """
        width = self.size[0] // self.scale
        height = self.size[1] // self.scale
        pos_x = self.hero[0] - width // 2
        pos_y = self.hero[1] - height // 2
        return pos_x, pos_y, width, height

    def filling(self):
        """ Заполнение миникарты """
        self.surface.set_alpha(207)
        self.surface.fill('Grey')  # Фон за краями карты
        # Заполняем миникарту минитайлами
        for y in range(self.count_y):
            for x in range(self.count_x):
                key = self.terrain.map[y][x]
                tile = self.terrain.tile_atlas[key]
                tile = pg.transform.scale(tile, (self.rate, self.rate))
                self.surface.blit(tile, (x * self.rate, y * self.rate, self.rate, self.rate))
