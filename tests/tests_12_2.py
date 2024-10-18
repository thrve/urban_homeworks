#!/usr/bin/env python


import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../urban/twelfth')))

from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.runner1 = Runner('Усэйн', speed=10)
        self.runner2 = Runner('Андрей', speed=9)
        self.runner3 = Runner('Ник', speed=3)

    def test_race_usain_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        formatted_result = {place: str(runner) for place, runner in results.items()}
        print(formatted_result)

    def test_race_andrey_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        formatted_result = {place: str(runner) for place, runner in results.items()}
        print(formatted_result)

    def test_race_usain_andrey_nik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        formatted_result = {place: str(runner) for place, runner in results.items()}
        print(formatted_result)


if __name__ == '__main__':
    unittest.main()
