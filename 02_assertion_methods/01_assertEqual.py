import unittest

class SimpleTest(unittest.TestCase):

    def test_case_01(self):
        self.assertEqual("aws".upper(), "AWS")

    def test_case_02(self):
        self.assertEqual("aws".upper(), "AWS")

    def test_case_03(self):
        self.assertEqual("3.9.0".split("."), ["3","9","0"])

    def test_case_04(self):
        self.assertEqual(tuple("3.9.0".split(".")), ("3","9","0"))

    def test_case_05(self):
        self.assertEqual({3, 9, 0}, {3,9,0})   
