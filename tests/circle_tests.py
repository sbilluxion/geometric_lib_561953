import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from circle import*
from math import pi


class CircleTestCase(unittest.TestCase):

    ## Area tests

    def test_positive_area(self):
        res = area(5)
        self.assertAlmostEqual(res, 25 * pi)

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_float_area(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25 * pi)

    def test_large_area(self):
        res = area(100000)
        self.assertAlmostEqual(res, 100000**2 * pi)

    def test_small_area(self):
        res = area(0.001)
        self.assertAlmostEqual(res, 0.000001 * pi)

    ## Perimeter tests

    def test_positive_perimeter(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 10 * pi)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_float_perimeter(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 5 * pi)

    def test_large_perimeter(self):
        res = perimeter(100000)
        self.assertAlmostEqual(res, 200000 * pi)

    def test_small_perimeter(self):
        res = perimeter(0.001)
        self.assertAlmostEqual(res, 0.002 * pi)
    def test_error_perimeter(self):
            res = perimeter(0.005)
            self.assertAlmostEqual(res, 0.002 * pi)