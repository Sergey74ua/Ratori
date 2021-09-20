import ctypes
import pygame as pg
from modules.Menu import Menu
from modules.Game import Game


class Main(object):
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID()
    _image_ = pg.image.load("images/icon.bmp")

    def __init__(self):
        """ Окно приложения """
        self.game_version = 1
        self.flag = int(pg.RESIZABLE)
        self.size = self.width, self.height = 1280, 720
        self.fps = 60
        pg.display.set_mode(self.size, self.flag)
        pg.display.set_icon(self._image_)
        pg.display.set_caption("RATORI")

    def game_start(self):
        """ Новая игра """
        self.speed = 50  # до 100
        self.menu = Menu(self.size)
        self.game = Game(self.size, self.speed)
        self.mode = self.menu
        self.game_cycle()

    def game_cycle(self):
        """ Цикл обновления кадров """
        g = pg.display.get_surface()

        while self.game.game_state:
            # Опрелеляем активный режим
            if self.menu.menu_state:
                self.mode = self.menu
            else:
                self.mode = self.game

            # Проверка событий и управление
            for e in pg.event.get():
                self.control(e)

            self.mode.update(e)  # НЕ КОРРЕКТНО (но работает)
            self.mode.draw(g)

            pg.display.flip()
            pg.time.Clock().tick(self.fps)

        # Выход из игры
        self.menu.menu_state = True

    def control(self, e):
        """ Управление """

        # Переключение паузы / игры
        if e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
            self.menu.menu_state = not self.menu.menu_state

        # Полноэкранный режим (ИСПРАВИТЬ ПЕРЕХОД ИЗ ПОЛНОЭКРАННОГО РЕЖИМА)
        if e.type == pg.KEYDOWN and e.key == pg.K_F11:
            if pg.display.get_surface().get_flags() & pg.FULLSCREEN:
                self.flag = pg.RESIZABLE
            else:
                self.flag = pg.FULLSCREEN
            pg.display.set_mode((self.width, self.height), self.flag)
            pg.display.update()

        # Выход из программы
        if e.type == pg.QUIT:
            pg.quit()
            quit()
