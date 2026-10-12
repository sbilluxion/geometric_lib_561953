import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from square import*
class squareTestCase(unittest.TestCase):
    ## Area tests

    def test_positive_area(self):
        res = area(5)
        return self.assertEqual(res, 25)
    def test_zero_area(self):
        res = area(0)
        return self.assertEqual(res,0)
    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-5)
    def test_float_area(self):
        res = area(2.5)
        return self.assertAlmostEqual(res,6.25)
    def test_large_area(self):
        res = area(100000)
        return self.assertEqual(res,100000**2)
    def test_small_area(self):
        res = area(0.001)
        return self.assertEqual(res, 0.000001)

    ##Perimeter tests

    def test_positive_p(self):
        res = perimeter(5)
        return self.assertEqual(res, 20)
    def test_zero_p(self):
        res = perimeter(0)
        return self.assertEqual(res, 0)
    def test_negative_p(self):
        with self.assertRaises(ValueError):
            perimeter(-5)
    def test_float_p(self):
        res = perimeter(2.3)
        return self.assertAlmostEqual(res, 9.2)
    def test_large_p(self):
        res = perimeter(100000)
        return self.assertEqual(res, 400000)
    def test_small_p(self):
        res =  perimeter(0.001)
        return self.assertAlmostEqual(res, 0.004)
    