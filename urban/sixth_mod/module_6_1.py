#!/usr/bin/env python


class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} ate the {food.name}")
                self.fed = True
            else:
                print(f"{self.name} didn't eat {food.name}")
                self.alive = False
        else:
            print("this is not a plant")

    def __str__(self):
        return self.name


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

    def __str__(self):
        return self.name


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True
