import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from rectangle import*

class rectangleTestCase(unittest.TestCase):
    ## Area tests

    def test_positive_area(self):
        res = area(2,5)
        return self.assertEqual(res, 10)

    def test_zero_area(self):
        res = area(0,0)
        return self.assertEqual(res, 0)

    def test_negative1_area(self):
        with self.assertRaises(ValueError):
            area(-5,2)

    def test_negative2_area(self):
        with self.assertRaises(ValueError):
            area(5,-2)

    def test_float_area(self):
        res = area(2.5, 1.3)
        return self.assertAlmostEqual(res, 3.25)

    def test_large_area(self):
        res = area(10000,20000)
        return self.assertEqual(res, 200000000)

    def test_small_area(self):
        res = area(0.001,0.003)
        return self.assertAlmostEqual(res, 0.000003)

    ## Perimeter tests

    def test_positive_p(self):
        res = perimeter(2,5)
        return self.assertEqual(res, 14)
        
    def test_zero_p(self):
        res = perimeter(0,0)
        return self.assertEqual(res, 0)

    def test_negative1_p(self):
        with self.assertRaises(ValueError):
            perimeter(-5,2)

    def test_negative2_p(self):
        with self.assertRaises(ValueError):
            perimeter(5,-2)

    def test_float_p(self):
        res = perimeter(2.5, 1.3)
        return self.assertAlmostEqual(res, 7.6)

    def test_large_p(self):
        res = perimeter(10000,20000)
        return self.assertEqual(res, 60000)

    def test_small_p(self):
        res = perimeter(0.001,0.003)
        return self.assertAlmostEqual(res, 0.008)