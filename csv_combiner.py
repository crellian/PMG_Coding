import csv
import sys
import os.path as path
import numpy as np
import copy

class Csv_Combiner():
    def __init__(self, writer):
        self.writer = writer
        self.first_file = True
        self.column_names = []
    
    def check_validity(self, file_paths):
        if len(file_paths) < 1:
            print("Please provide at least one file's name. Example: \"python ./csv-combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv\"")
            return False
        for file_path in file_paths:
            if not (path.isfile(file_path) and file_path.endswith('.csv')):
                print(file_path + " does not exist or is not a csv file.")
                return False
        return True
        
    def __write_file(self, file_path, reader):
        for idx, row in enumerate(reader):
            # Remove empty lines, output columns' names if and only if it is the first file we've read
            if not row:
                continue
            elif idx == 0 and self.first_file: 
                self.column_names = copy.deepcopy(row)   # Memorize the column names of the first file
                row.append("filename")
            elif idx == 0 and not self.first_file: 
                if row != self.column_names:  # Check if column names of csv files are same
                    print(file_path + " could be corrupted.")
                    raise ValueError
                continue
            elif idx != 0:  
                if len(row) != len(self.column_names):  # Check the validity of each row 
                    print(file_path + " could be corrupted.")
                    raise ValueError
                row.append(path.basename(file_path))
            self.writer.writerow(row)
        
    def combine_files(self, file_paths):
        for file_path in file_paths:
            with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
                self.__write_file(
                    file_path,
                    csv.reader(csvfile, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)
                )
            self.first_file = False
            


def main():
    combiner = Csv_Combiner(
        csv.writer(sys.stdout, lineterminator = "\n", doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)
        )
    
    if not combiner.check_validity(sys.argv[1:]):
        return
    
    combiner.combine_files(sys.argv[1:])


if __name__ == '__main__':
   main()