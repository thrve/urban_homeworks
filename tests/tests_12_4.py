#!/usr/bin/env python


import logging
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../urban/twelfth_mod')))

from rt_with_exceptions import Runner

logging.basicConfig(
    level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='utf-8', format='%(levelname)s: %(message)s'
)


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner('Test Runner', -5)
        except ValueError:
            logging.warning('Неверная скорость для Runner')
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(123, 5)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')
        else:
            logging.info('"test_run" выполнен успешно')


if __name__ == '__main__':
    unittest.main()
