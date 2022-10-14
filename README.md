# Coding Assessment

### file structure
    .
    ├── ...
    ├── fixtures            # test case 1
    ├── fixtures_corrupted  # test case 2
    ├── combined.csv        # ground truth
    ├── generatefixtures.py # randomly test case generation
    ├── csv_combiner.py     # main program
    ├── tests.py            # testbench
    └── ...

Run the program: `python csv_combiner.py ./fixtures/household_cleaners.csv ./fixtures/accessories.csv ./fixtures/clothing.csv`\
Run the unit tests: `python tests.py`
