import unittest

class SimpleTest(unittest.TestCase):

    def test_case_01(self):
        self.assertEqual(0.1 + 0.2, 0.3)

    def test_case_02(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3)   

    def test_case_03(self):
        self.assertAlmostEqual(0.1234567, 0.1234567)

    def test_case_04(self):
        self.assertAlmostEqual(0.12345678, 0.12345679)

    def test_case_05(self):
        self.assertAlmostEqual(0.12345674, 0.12345679, 6)