import sys
import io
import contextlib
import csv
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
        paths = ["./fixtures/household_cleaners.csv", "./fixtures/accessories.csv", "./fixtures/clothing.csv"]
        file_path = "./combined.csv"
        with contextlib.redirect_stdout(io.StringIO()) as f:
            self.combiner.combine_files(paths)
            with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)
                for row in reader:
                    self.assertTrue(row in f.getvalue)

if __name__ == '__main__':
    unittest.main()
