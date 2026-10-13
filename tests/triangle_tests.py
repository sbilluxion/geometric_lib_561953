import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from triangle import*

class TriangleTestCase(unittest.TestCase):

    ## Area tests

    def test_positive_area(self):
        res = area(5, 4)
        self.assertEqual(res, 10)

    def test_zero_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_zero_height_area(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_negative_side_area(self):
        with self.assertRaises(ValueError):
            area(-5, 4)

    def test_negative_height_area(self):
        with self.assertRaises(ValueError):
            area(5, -4)

    def test_float_area(self):
        res = area(2.5, 1.3)
        self.assertAlmostEqual(res, 1.625)

    def test_large_area(self):
        res = area(100000, 200000)
        self.assertEqual(res, 10000000000)

    def test_small_area(self):
        res = area(0.001, 0.003)
        self.assertAlmostEqual(res, 0.0000015)

    ## Perimeter tests

    def test_positive_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_zero_side_perimeter(self):
        res = perimeter(0, 4, 5)
        self.assertEqual(res, 9)

    def test_negative_first_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)

    def test_negative_second_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)

    def test_negative_third_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(3, 4, -5)

    def test_float_perimeter(self):
        res = perimeter(2.5, 3.5, 4.5)
        self.assertAlmostEqual(res, 10.5)

    def test_large_perimeter(self):
        res = perimeter(100000, 200000, 300000)
        self.assertEqual(res, 600000)

    def test_small_perimeter(self):
        res = perimeter(0.001, 0.002, 0.003)
        self.assertAlmostEqual(res, 0.006)