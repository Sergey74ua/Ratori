import pygame as pg


class Hero(object):
    pg.init()
    _atlas_ = pg.image.load('images/sprite.gif')
    _atlas_ = pg.transform.scale(_atlas_, (9 * 70, 8 * 70))  # ВРЕМЕННО
    _sound_ = pg.mixer.Sound('sounds/step.mp3')

    def __init__(self):
        """ Игровой персонаж (графический атлас) """
        self.rate = 35 * 2   # ТОЖЕ ВРЕМЕННО
        self.sound = self._sound_
        self.tile_atlas = []
        self.tile_atlas = self.filling()
        self.row = 0
        self.col = 0
        self.step = 0
        self.image = self.tile_atlas[self.row][self.col]
        self.rect = self.image.get_rect()

    def update(self, turn, speed):
        """ Обновление персонажа """
        if turn == 'stop':
            self.image = self.tile_atlas[0][0]
        else:
            if turn == 'right_down':
                self.row = 1
            elif turn == 'left_down':
                self.row = 7
            elif turn == 'left_up':
                self.row = 5
            elif turn == 'right_up':
                self.row = 3
            elif turn == 'right':
                self.row = 2
            elif turn == 'down':
                self.row = 0
            elif turn == 'left':
                self.row = 6
            elif turn == 'up':
                self.row = 4
            self.image = self.select(speed)

    def draw(self, g):
        """ Отрисовка персонажа """
        g.blit(self.image, self.rect)
        pg.draw.line(g, 'red', (600, 320), (680, 400), 1)  ########
        pg.draw.line(g, 'red', (600, 400), (680, 320), 1)  ########

    def select(self, speed):
        """ Позиция персонажа """
        step = 48*speed/100  # ДОРАБОТАТЬ
        if self.step > 32:  # ПОДОГНАТЬ ДЛИНУ ШАГА (16 px *2)
            if self.col > 7:
                pg.mixer.Sound.play(self.sound)
                self.col = 1
            else:
                self.col += 1
                self.step = 0
        else:
            self.step += step
        return self.tile_atlas[self.row][self.col]

    def filling(self):
        """ Заполняем набор тайлов """
        size = self.rate, self.rate
        for row in range(8):
            self.tile_atlas.append([])
            for col in range(9):
                rect = (self.rate * col, self.rate * row)
                image = self._atlas_.subsurface(rect, size)
                self.tile_atlas[row].append(image)
        return self.tile_atlas
