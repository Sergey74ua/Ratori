from modules.interface.Minimap import Minimap
from modules.interface.Life import Life
from modules.interface.Score import Score
from modules.interface.Bullet import Bullet


class Interface(object):
    """ Пример паттерна 'Фасад" """

    def __init__(self, size):
        """ Интерфейс игры """
        self.size = size
        self.minimap = Minimap(self.size)
        self.life = Life()
        self.score = Score(size)
        self.bullet = Bullet(size)

    def update(self, hero, size):
        """ Обновление интерфейса """
        self.minimap.update(hero, size)
        self.life.update()
        self.score.update(size)
        self.bullet.update(size)

    def draw(self, g):
        """ Отрисовка интерфейса """
        self.minimap.draw(g)
        self.life.draw(g)
        self.score.draw(g)
        self.bullet.draw(g)
