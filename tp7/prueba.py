def funcion(x):
    return x

import unittest

class My_Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(funcion(9),9)

    def test_2(self):
        self.assertEqual(funcion(2), 2)

test = My_Test()
test.test_1()
test.test_2()
