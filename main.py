import sys

from app.io.input import read_text, read_from_file, read_pandas
from app.io.output import write_text, write_into_file


def main():
    sys.stdout = open("test_files/outputs/output.txt", "w")

    text_data = read_text()
    print("Text data: ", text_data)

    file_data = read_from_file("test_files/test_file.txt")
    print("Data from file:\n", file_data)

    pandas_data = read_pandas("test_files/test_file_2.csv")
    print("Pandas data: ", pandas_data)

    sys.stdout.close()
    # Restore default stdout
    sys.stdout = sys.__stdout__

    write_text("Hello world!")
    write_into_file("This text is to be written into a file", "write_to_file.txt")



if __name__ == "__main__":
    main()
