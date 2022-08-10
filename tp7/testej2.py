import unittest
from tp7ej2 import *

class test_pin_atm(unittest.TestCase):
    def test_1(self):
        self.assertEqual(pin_atm("12345"),False)
    def test_2(self):
        self.assertEqual(pin_atm("1234"),True)
    def test_3(self):
        self.assertEqual(pin_atm("a123"),False)

test = test_pin_atm()
test.test_1()
test.test_2()
test.test_3()