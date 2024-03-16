def write_text(text):
    """
    Display text into console.

    Args:
        text (str): The text data to be displayed.
    """
    print(text)


def write_into_file(data, file_path):
    """
       Writes data into a file.

       Args:
           data: The data to be written into the file.
           file_path (str): The path to the file.
    """
    with open(file_path, "w") as file:
        file.write(str(data))
