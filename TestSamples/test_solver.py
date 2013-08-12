from unittest import TestCase
from Solver import Solver


__author__ = 'mio'
__project__ = 'TestSamples'


class TestSolver(TestCase):
    def test_demo(self):
        self.fail()
    def test_negative_discr(self):
        s = Solver
        self.assertRaises(Exception,s.demo,8,1,2)