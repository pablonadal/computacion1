import unittest
from tp7ej1 import *

class test_sum_of_differences(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_of_differences(1,2,10),9)
    def test_2(self):
        self.assertEqual(sum_of_differences(-3,-2,-1),2)
    def test_3(self):
        self.assertEqual(sum_of_differences(-17,17),34)

tests = test_sum_of_differences()
tests.test_1()
tests.test_2()
tests.test_3()