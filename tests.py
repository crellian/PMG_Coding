import sys
import csv
from io import StringIO
try:
    import unittest2 as unittest  ## for Python 2
except ImportError:
    import unittest               ## for Python 3
try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO       ## for Python 3
    
from csv_combiner import Csv_Combiner


class TestCombiner(unittest.TestCase):
    def setUp(self):
        self.capturedOutput = StringIO()
        sys.stdout = self.capturedOutput
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
        #paths = ["./fixtures/household_cleaners.csv"]
        self.combiner.combine_files(paths)

        with open("./combined.csv", 'r') as file:
            data = file.read()
            self.assertEqual(data, self.capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()
