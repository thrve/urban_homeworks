#!/usr/bin/env python


class House:

    houses_history = []

    def __new__(cls, *args):
        if args:
            cls.houses_history.append(args[0])
        return super(House, cls).__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            raise ValueError("There is no such floor.")
        else:
            print(", ".join(str(i) for i in range(1, new_floor)))

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Name: {self.name}, number of floors: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, int):
            return self.number_of_floors == other
        elif isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors < other
        elif isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, int):
            return self.number_of_floors < other
        elif isinstance(other, House):
            return self.number_of_floors <= self.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors > other
        elif isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, int):
            return self.number_of_floors >= other
        elif isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, int):
            return self.number_of_floors != other
        elif isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return False

    def __add__(self, other):
        if isinstance(other, (int)):
            return House(self.name, self.number_of_floors + other)
        elif isinstance(other, House):
            return House(self.name, self.number_of_floors + other.number_of_floors)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, (int)):
            self.number_of_floors += other
            return self
        elif isinstance(other, House):
            self.number_of_floors += other.number_of_floors
            return self
        else:
            return NotImplemented

    def __del__(self):
        print(f"{self.name} demolished, but it will remain in history")
