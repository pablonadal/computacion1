import unittest
from tp7ej5 import *

class test_consecutive(unittest.TestCase):
    def test_1(self):
        self.assertEqual(consecutive([1, 3, 5, 7], 3, 7),False)
    def test_2(self):
        self.assertEqual(consecutive([1, 3, 5, 7], 3, 1),True)
    def test_3(self):
        self.assertEqual(consecutive([1,6,9,-3,4,-78,0],-3,4),True)

test = test_consecutive()
test.test_1()
test.test_2()
test.test_3()