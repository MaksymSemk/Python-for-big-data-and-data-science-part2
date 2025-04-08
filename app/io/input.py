import pandas as pd
import os

def read_text_from_console():
    """Reads text from the console and returns the input.

    Returns:
        str: The text entered by the user.
    """
    return input()

def read_text_from_file_with_builtin_func(file):
    """Reads text from a file using Python's built-in file handling functions.

    This function opens the file encoded in UTF-8 in read mode and reads its content line by line.
    It concatenates each line into a single string and returns it. The function
    ensures that the file is properly closed after reading using a context manager.

    Args:
        file (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.
    """
    with open(file, 'r', encoding='utf-8') as f:
        text = ""
        for line in f:
            text += line
        return text


def read_text_from_file_with_pandas(file):
    """Reads text from a file using the pandas library.

    This function reads the file using pandas' `read_csv` method and handles
    the case where the file is empty. If the file is not empty, it iterates
    through each row and column in the DataFrame and concatenates them into a
    single string.

    Args:
        file (str): The path to the file to be read.

    Returns:
        str: The contents of the file as a string. Returns an empty string if the file is empty.
    """
    if os.path.getsize(file) == 0:
        return ""

    df = pd.read_csv(file, header=None)
    res = ""
    for index, row in df.iterrows():
        for col in df.columns:
            if index != 0:
                res += '\n'
            res += str(row[col])
    return res
