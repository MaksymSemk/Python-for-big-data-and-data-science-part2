import pandas as pd

def read_text_from_console():
    """Reads text from the console and returns the input.

    Returns:
        str: The text entered by the user.
    """
    return input()

def read_text_from_file_with_builtin_func(file):
    """Reads text from a file using Python's built-in file handling functions.

    Args:
        file (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.
    """
    with open(file, 'r') as f:
        text=""
        for line in f:
            text += line
        return text

def read_text_from_file_with_pandas(file):
    """Reads text from a file using the pandas library.

    Args:
        file (str): The path to the file to be read.

    Returns:
        str: The contents of the file as a string.
    """
    df = pd.read_csv(file, header=None)
    res=""
    for index, row in df.iterrows():
        for col in df.columns:
            res+=str(row[col])+"\n"
    return res



