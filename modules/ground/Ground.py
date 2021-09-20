import pygame as pg
from modules.ground.Terrain import Terrain


class Ground(object):
    """ Участок карты в окне игры """

    def __init__(self, size):
        """ Карта """
        self.size = size
        self.surface = pg.Surface(self.size)
        self.rect = self.surface.get_rect()
        self.terrain = Terrain()
        self.max_x = len(self.terrain.map[0]) * self.terrain.rate
        self.max_y = len(self.terrain.map) * self.terrain.rate
        self.point_x, self.point_y = self.terrain.start_point
        # Шрифт кодов тайлов (для редактирования)
        #pg.font.init()
        #self.font = pg.font.SysFont('arial', 12, True)

    def update(self, size, turn, speed):
        """ Обновление позиции на карте """

        # Перерасчитываем центр
        if self.size != size:
            self.size = size
            self.surface = pg.Surface(self.size)
            self.rect = self.surface.get_rect()

        # Прокрутка карты
        scroll = round(speed/(100/(6-1)))+1  # ДОРАБОТАТЬ
        scroll = 4  # ВРЕМЕННО
        scroll_d = round(scroll / 1.4)
        if turn == 'right_down':
            self.point_x += scroll_d
            self.point_y += scroll_d
        elif turn == 'left_down':
            self.point_x -= scroll_d
            self.point_y += scroll_d
        elif turn == 'left_up':
            self.point_x -= scroll_d
            self.point_y -= scroll_d
        elif turn == 'right_up':
            self.point_x += scroll_d
            self.point_y -= scroll_d
        elif turn == 'right':
            self.point_x += scroll
        elif turn == 'down':
            self.point_y += scroll
        elif turn == 'left':
            self.point_x -= scroll
        elif turn == 'up':
            self.point_y -= scroll

        # Ограничение краями карты
        if self.point_x < self.size[0] // 2 + scroll:
            self.point_x = self.size[0] // 2 + scroll
        if self.point_x >= self.max_x - self.size[0] // 2 - scroll - 1:
            self.point_x = self.max_x - self.size[0] // 2 - scroll - 1
        if self.point_y < self.size[1] // 2 + scroll:
            self.point_y = self.size[1] // 2 + scroll
        if self.point_y >= self.max_y - self.size[1] // 2 - scroll - 1:
            self.point_y = self.max_y - self.size[1] // 2 - scroll - 1

        self.select()

    def draw(self, g):
        """ Отрисовка карты """
        g.fill('Grey')
        g.blit(self.surface, self.rect)

    def select(self):  # ОШИБКА за краями карты при расширении экрана
        """ Отрисовка фрейма """
        rate = self.terrain.rate

        # Определяем границы окна
        x_left = self.point_x - self.size[0] // 2
        x_right = x_left + self.size[0]
        y_top = self.point_y - self.size[1] // 2
        y_bottom = y_top + self.size[1]

        # Заполняем окно тайлами (желательно обрезать крайние тайлы)
        for y in range(y_top//rate, y_bottom//rate + 1):
            for x in range(x_left//rate, x_right//rate + 1):
                key = self.terrain.map[y][x]
                tile = self.terrain.tile_atlas[key]
                self.surface.blit(tile, (x * rate - x_left, y * rate - y_top, rate, rate))
                # Коды тайлов (для редактирования)
                #text_button = self.font.render(str(y)+'-'+str(x), True, 'DarkBlue')
                #text_rect = text_button.get_rect()
                #self.surface.blit(text_button, (x*self.rate-x_left+4, y*self.rate-y_top+16), text_rect)
