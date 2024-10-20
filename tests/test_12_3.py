#!/usr/bin/env python


import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../urban/twelfth_mod')))

from runner_and_tournament import Runner, Tournament


def skip_if_frozen(test_method):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_method(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner1 = Runner('Усэйн', speed=10)
        self.runner2 = Runner('Андрей', speed=9)
        self.runner3 = Runner('Ник', speed=3)

    @skip_if_frozen
    def test_run(self):
        self.runner1.run()
        self.assertEqual(self.runner1.distance, 20)

    @skip_if_frozen
    def test_walk(self):
        self.runner2.walk()
        self.assertEqual(self.runner2.distance, 9)

    @skip_if_frozen
    def test_challenge(self):
        self.assertEqual(self.runner1.name, 'Усэйн')


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.runner1 = Runner('Усэйн', speed=10)
        self.runner2 = Runner('Андрей', speed=9)
        self.runner3 = Runner('Ник', speed=3)

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.assertEqual(results[1].name, 'Усэйн')

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.assertEqual(results[1].name, 'Андрей')

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.assertEqual(results[1].name, 'Усэйн')
