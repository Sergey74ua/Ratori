import pygame as pg


class Button(object):
    pg.font.init()

    _font_ = pg.font.SysFont('Cambria', 36)
    _size_ = 360, 80

    def __init__(self, btn_pos, name):
        """ Кнопка меню """
        self.rect = pg.Rect(btn_pos, self._size_)
        self.name = name
        self.font_color = 'LightSkyBlue'
        self.active = True
        self.focus = False
        self.pressed = False

    def update(self):
        """ Смена цвета кнопки """
        if self.active:
            self.font_color = 'LightSkyBlue'
            if self.focus:
                self.font_color = 'PowderBlue'
                if self.pressed:
                    self.font_color = 'Cyan'
        else:
            self.font_color = 'SteelBlue'

    def draw(self, g):
        """ Отрисовка кнопки """
        pg.draw.rect(g, 'CornFlowerBlue', self.rect, border_radius=24)
        pg.draw.rect(g, 'LightSkyBlue', self.rect, 2, 24)
        self.text_button = self._font_.render(self.name, True, self.font_color)
        self.text_rect = self.text_button.get_rect()
        self.text_rect.center = self.rect.center
        g.blit(self.text_button, self.text_rect)
