from modules.unit.Gangster import Gangster


class Adapter(Gangster):
    """ Противник через адаптер"""

    def draw(self, g):
        """ Адаптер метода """
        return self.draw_unit(g)
