import pygame as pg
from random import randint
from modules.unit.Adapter import Adapter
from modules.unit.Cat import Cat
from modules.unit.Dog import Dog
from modules.unit.Shot import Shot


class Units(object):
    """ Юниты """

    def __init__(self, size, count):
        """ Список юнитов """
        tile_atlas = Adapter.filling()
        tile_atlas_cat = Cat.filling()
        tile_atlas_dog = Dog.filling()
        self.size = size
        self.list_unit = []
        self.list_pet = []
        self.list_shot = []
        self.count = count
        for i in range(self.count):
            unit = Adapter(size, tile_atlas)
            self.list_unit.append(unit)
        for i in range(self.count):
            unit = Cat(size, tile_atlas_cat)
            self.list_pet.append(unit)
            unit = Dog(size, tile_atlas_dog)
            self.list_pet.append(unit)
        self.unit_speed = 3
        self.unit_speed_d = 2
        self.shot_time = 60

    def update(self, turn, speed):
        """ Обновление юнитов """
        for unit in self.list_unit:
            if not unit.arrest:
                if unit.rect.collidepoint(self.size[0] // 2, self.size[1] // 2):
                    unit.arrest = True
                elif unit.time_move < 1:
                    unit.time_move = randint(30, 150)
                    unit.unit_turn = randint(0, 8)
                unit.time_move -= 1
                self.move_unit(unit)
            unit.rect.x, unit.rect.y = unit.pos_unit(turn)
            unit.update(speed)

        for pet in self.list_pet:
            pet.point_x, pet.point_y = pet.pos_unit(turn)
            self.move_unit(pet)
            pet.update(speed)

        for i in range(len(self.list_shot)):
            if self.list_shot[i].del_time <= 0:
                del self.list_shot[i]
                break
            else:
                self.list_shot[i].update(turn)

        if self.shot_time > 0:
            self.shot_time -= 1

    def draw(self, g):
        """ Отрисовка юнитов """
        for unit in self.list_unit:
            unit.draw(g)

        for unit in self.list_pet:
            unit.draw(g)

        for shot in self.list_shot:
            shot.draw(g)

    def add_shot(self, turn):
        if self.shot_time <= 0:
            shot = Shot(self.size, turn)
            self.list_shot.append(shot)
            self.shot_time = 30

    def move_unit(self, unit):
        """ Движение юнита """
        if unit.unit_turn == 1:
            unit.point_x += self.unit_speed_d
            unit.point_y += self.unit_speed_d
        elif unit.unit_turn == 7:
            unit.point_x -= self.unit_speed_d
            unit.point_y += self.unit_speed_d
        elif unit.unit_turn == 5:
            unit.point_x -= self.unit_speed_d
            unit.point_y -= self.unit_speed_d
        elif unit.unit_turn == 3:
            unit.point_x += self.unit_speed_d
            unit.point_y -= self.unit_speed_d
        elif unit.unit_turn == 2:
            unit.point_x += self.unit_speed
        elif unit.unit_turn == 0:
            unit.point_y += self.unit_speed
        elif unit.unit_turn == 6:
            unit.point_x -= self.unit_speed
        elif unit.unit_turn == 4:
            unit.point_y -= self.unit_speed

        return unit.point_x, unit.point_y
