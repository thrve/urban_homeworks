#!/usr/bin/env python


class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled=False):
        self.__set_sides(sides)
        self.__color = color
        self.filled = filled

    def __set_sides(self, sides):
        if isinstance(sides, list) and all(isinstance(side, int) for side in sides):
            self.__sides = sides
        else:
            raise ValueError('the sides parameter expects a list of integers')


class Circle:
    pass


class Triangle:
    pass


class Cube:
    pass
