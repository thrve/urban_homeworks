#!/usr/bin/env python


from threading import Thread
from time import sleep


class Knight(Thread):
    enemies = 100

    def __init__(self, name, power) -> None:
        super().__init__()
        self.name = name
        self.power = power

    def run(self) -> None:
        print(f'{self.name}, на нас напали!')
        days = 0
        while Knight.enemies > 0:
            Knight.enemies -= self.power
            sleep(1)
            days += 1
            print(f'{self.name} сражается {days} дней, осталось {Knight.enemies} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
