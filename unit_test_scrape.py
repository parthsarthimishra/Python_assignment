

import unittest
from scrap_soup import *
import io
import scrap_soup as sc
from io import  StringIO
import sys


class testit(unittest.TestCase):
    
    def test_db(self):
        sys.stdout = io.StringIO()
        scrap("radhikagarg1601")
        sys.stdout = sys.__stdout__
        self.assertEqual(io.StringIO().getvalue(), "My name is Radhika Garg and my current city is Roorkee")
    def testnew(self):
        with self.assertRaises(ValueError):
            scrap("radhika")

if __name__ == "__main__":
    unittest.main()




