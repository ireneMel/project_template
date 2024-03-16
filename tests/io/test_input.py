import os
import unittest

import pandas as pd

from app.io.input import read_from_file, read_pandas


class TestFileOperations(unittest.TestCase):

    def setUp(self):
        # Create a test file with some data
        with open("../test_files/test_file.txt", "w") as file:
            file.write("This is a test file.")

        # Create a test CSV file with some data
        data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
        df = pd.DataFrame(data)
        df.to_csv("../test_files/test_file.csv", index=False)

    def test_read_from_file_success(self):
        file_path = "../test_files/test_file.txt"
        expected_output = "This is a test file."
        self.assertEqual(read_from_file(file_path), expected_output)

    def test_read_from_file_invalid_path(self):
        file_path = "non_existing_file.txt"
        self.assertIsNone(read_from_file(file_path))

    def test_read_pandas_success(self):
        file_path = "../test_files/test_file.csv"
        expected_output = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        pd.testing.assert_frame_equal(read_pandas(file_path), expected_output)

    # def tearDown(self):
    #     # Clean up created test files
    #     os.remove("../test_files/test_file.txt")
    #     os.remove("../test_files/test_file.csv")
