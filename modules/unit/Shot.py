import pygame as pg
from modules.unit.Abstract import Abstract


class Shot(Abstract):

    def __init__(self, size, turn):
        """ Пуля """
        self.size = size
        self.unit_turn = turn
        self.speed = 6
        self.speedD = 4
        self.point_x = self.size[0] // 2
        self.point_y = self.size[1] // 2
        self.del_time = 300

    def update(self, turn):
        """ Обновление координат """
        self.del_time -= 1
        self.point_x, self.point_y = self.pos_unit(turn)
        self.pos_shot()

    def draw(self, g):
        """ Отрисовка пули """
        pg.draw.circle(g, 'Red', (self.point_x, self.point_y), 3)

    def pos_shot(self):
        """ Направление выстрела """
        if self.unit_turn == "right_down":
            self.point_x += self.scroll
            self.point_y += self.scroll
        elif self.unit_turn == 'left_down':
            self.point_x -= self.scroll
            self.point_y += self.scroll
        elif self.unit_turn == 'left_up':
            self.point_x -= self.scroll
            self.point_y -= self.scroll
        elif self.unit_turn == 'right_up':
            self.point_x += self.scroll
            self.point_y -= self.scroll
        elif self.unit_turn == 'down':
            self.point_y += self.scroll_line
        elif self.unit_turn == 'left':
            self.point_x -= self.scroll_line
        elif self.unit_turn == 'right' or self.unit_turn == 'stop':
            self.point_x += self.scroll_line
        elif self.unit_turn == 'up':
            self.point_y += self.scroll_line

        return self.point_x, self.point_y
