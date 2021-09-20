import pygame as pg
from modules.ground.Ground import Ground
from modules.unit.Hero import Hero
from modules.unit.Units import Units
from modules.interface.Interface import Interface


class Game(object):

    def __init__(self, size, speed):
        """ Игра """
        self.game_state = True
        self.size = size
        self.speed = speed
        self.ground = Ground(self.size)
        self.units = Units(self.size, 10)
        self.hero = Hero()
        self.interface = Interface(size)
        self.hero.rect.center = self.position(size)
        self.turn = 'stop'

    def update(self, e):
        """ Обновление игры """

        # Переразмещаем элементы в окне
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            self.hero.rect.center = self.position(size)

        # Список кликов кнопок клавиатуры
        keys = pg.key.get_pressed()
        if (keys[pg.K_RIGHT] and keys[pg.K_DOWN]) or (keys[pg.K_d] and keys[pg.K_s]):
            self.turn = 'right_down'
        elif (keys[pg.K_LEFT] and keys[pg.K_DOWN]) or (keys[pg.K_a] and keys[pg.K_s]):
            self.turn = 'left_down'
        elif (keys[pg.K_LEFT] and keys[pg.K_UP]) or (keys[pg.K_a] and keys[pg.K_w]):
            self.turn = 'left_up'
        elif (keys[pg.K_RIGHT] and keys[pg.K_UP]) or (keys[pg.K_d] and keys[pg.K_w]):
            self.turn = 'right_up'
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.turn = 'right'
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.turn = 'down'
        elif keys[pg.K_LEFT] or keys[pg.K_a]:
            self.turn = 'left'
        elif keys[pg.K_UP] or keys[pg.K_w]:
            self.turn = 'up'
        else:
            self.turn = 'stop'

        # Клики кнопок мышки (события)
        click = pg.mouse.get_pressed(3)
        if click[0]:
            #target = pg.mouse.get_pos()
            self.units.add_shot(self.turn)
        elif click[2]:
            print("Нажата кнопка № ", e.button, " в позиции ", click)

        self.ground.update(self.size, self.turn, self.speed)
        self.units.update(self.turn, self.speed)
        self.hero.update(self.turn, self.speed)
        self.interface.update((self.ground.point_x, self.ground.point_y), self.size)

    def draw(self, g):
        """ Отрисовка игры """
        g.fill('Grey')
        self.ground.draw(g)
        self.units.draw(g)
        self.hero.draw(g)
        self.interface.draw(g)

    def position(self, size):  # РАСШИРИТЬ ДЛЯ ПРОЧИХ ПЕРСОНАЖЕЙ
        """ Перерассчет позиций """
        pos_x = size[0] // 2
        pos_y = size[1] // 2
        return pos_x, pos_y
