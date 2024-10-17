#!/usr/bin/env python


import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../urban/twelfth')))

from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('John')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('Jane')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner('Runner1')
        runner2 = Runner('Runner2')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
