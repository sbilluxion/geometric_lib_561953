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
    