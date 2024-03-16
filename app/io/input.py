import pandas as pd


def read_text():
    """
       Reads user input.

       Returns:
           str: The text data.
    """
    input("Enter some text: ")


def read_from_file(file_path):
    """
    Reads data from a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The data read from the file.
    """
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        print("Error reading file:", e)
        return None


def read_pandas(file_path):
    """
    Reads data from file using Pandas.

    Args:
        file_path (str): The path to the file.

    Returns:
        pandas.DataFrame: The data as a Pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print("Error reading file:", e)
        return None
