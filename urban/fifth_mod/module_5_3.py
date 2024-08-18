#!/usr/bin/env python


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("There is no such floor.")
            exit(0)
        else:
            print(", ".join(str(i) for i in range(1, new_floor)))

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Name: {self.name}, number of floors: {self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return

    # __gt__(>), __ge__(>=), __ne__(!=)
