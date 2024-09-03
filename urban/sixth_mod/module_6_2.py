#!/usr/bin/env python


class Vehicle:
    __COLOR_VARIANTS: list[str] = ["Reg", "Blue", "Green", "Black", "White"]

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self) -> str:
        return f"model: {self.__model}"

    def get_horsepower(self) -> str:
        return f"engine power: {self.__engine_power}"

    def get_color(self) -> str:
        return f"color: {self.__color}"

    def print_info(self) -> None:
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"owner: {self.owner}")

    def set_color(self, new_color: str) -> None:
        if new_color.lower() in [color.lower() for color in Vehicle.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Unable to change color to {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)
