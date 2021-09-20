from abc import ABC, abstractmethod


class Abstract(ABC):
    """ Абстрактный класс для наследования юнитов """
    scroll_line = 4
    scroll = round(scroll_line / 1.4)

    @abstractmethod
    def update(self, turn):
        """ Обновление """
        pass

    @abstractmethod
    def draw(self, r):
        """ Отрисовка """
        pass

    def pos_unit(self, turn):
        """ Позиция юнита """
        if turn == "right_down":
            self.point_x -= self.scroll
            self.point_y -= self.scroll
        elif turn == 'left_down':
            self.point_x += self.scroll
            self.point_y -= self.scroll
        elif turn == 'left_up':
            self.point_x += self.scroll
            self.point_y += self.scroll
        elif turn == 'right_up':
            self.point_x -= self.scroll
            self.point_y += self.scroll
        elif turn == 'down':
            self.point_y -= self.scroll_line
        elif turn == 'left':
            self.point_x += self.scroll_line
        elif turn == 'right':
            self.point_x -= self.scroll_line
        elif turn == 'up':
            self.point_y += self.scroll_line

        return self.point_x, self.point_y
