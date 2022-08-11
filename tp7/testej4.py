import unittest
from tp7ej4 import *

class test_missing_no(unittest.TestCase):
    def test_1(self):
        self.assertEqual(verificar([1,2,3,4,5,7,9,14,15,16]), True)
    def test_2(self):
        self.assertEqual(verificar([20, 12, 23, 14, 6, 22, 12, 17, 2, 26]), False)
    def test_3(self):
        self.assertEqual(verificar([1, 2, 3, 7, 5, 14, 7, 15, 9, 10]), True)
    def test_4(self):
        self.assertEqual(verificar([5, 2, 13, 7, 5, 14, 17, 15, 9, 10]), True)

test = test_missing_no()
test.test_1()
test.test_2()
test.test_3()
test.test_4()