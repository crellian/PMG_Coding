import sys
import io
import contextlib
import csv
import filecmp
try:
    import unittest2 as unittest
except ImportError:
    import unittest
from csv_combiner import Csv_Combiner



class TestCombiner(unittest.TestCase):
    def setUp(self):
        self.combiner = Csv_Combiner(
            csv.writer(sys.stdout, lineterminator = "\n", doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)
            )
            
    def test_validation(self):  # illegal path 
        paths = ["./11.mp4"]  
        self.assertFalse(self.combiner.check_validity(paths))
                
    def test_corruption(self):  # corrupted csv files
        paths = ["./fixtures_corrupted/household_cleaners.csv", "./fixtures_corrupted/accessories.csv", "./fixtures_corrupted/clothing.csv"]  
        with self.assertRaises(ValueError):
            self.combiner.combine_files(paths)
            
    def test_combination(self):  # successful combination
        with open('output.csv', 'w', newline='') as csvfile:
            self.combiner = Csv_Combiner(
                csv.writer(csvfile, lineterminator = "\n", doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)
                )
            paths = ["./fixtures/household_cleaners.csv", "./fixtures/accessories.csv", "./fixtures/clothing.csv"]
        
            self.combiner.combine_files(paths)
        self.assertTrue(filecmp.cmp("combined.csv", "output.csv", shallow=False))


if __name__ == '__main__':
    unittest.main()
