try:
    import unittest2 as unittest
except ImportError:
    import unittest
from csv_combiner import Csv_Combiner
import contextlib
import csv

class TestCombiner(unittest.TestCase):
    def test_validation(self):
        combiner = Csv_Combiner(
            csv.writer(sys.stdout, lineterminator = "\n", doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)
            )
        
        paths = ["./fixtures_corrupted/household_cleaners.csv", "./fixtures_corrupted/accessories.csv", "./fixtures_corrupted/clothing.csv"]
        self.assertFalse(combiner.check_validity(paths))
                
            
    def test_combination(self):
        combiner = Csv_Combiner(
            csv.writer(sys.stdout, lineterminator = "\n", doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)
            )
        
        paths = ["./fixtures/household_cleaners.csv", "./fixtures/accessories.csv", "./fixtures/clothing.csv"]
        file_path = "./combined.csv"
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            combiner.combine_files(paths)
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)
            for row in reader:
                self.assertTrue(row in f.getvalue)