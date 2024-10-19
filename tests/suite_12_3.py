#!/usr/bin/env python


import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../urban/twelfth')))


from test_12_3 import RunnerTest, TournamentTest

suite = unittest.TestSuite()

suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(suite)
