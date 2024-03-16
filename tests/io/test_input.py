import os
import unittest

import pandas as pd

from app.io.input import read_from_file


class TestFileOperations(unittest.TestCase):

    def SetUp(self):
        # Create a test file with some data
        with open("test_file.txt", "w") as file:
            file.write("This is a test file.")

        # Create a test CSV file with some data
        data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
        df = pd.DataFrame(data)
        df.to_csv("test_fileІуе.csv", index=False)

    def tearDown(self):
        # Clean up created test files
        os.remove("test_file.txt")
        os.remove("test_file.csv")