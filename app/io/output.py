def print_text_in_console(text):
    """Prints the given text to the console.

    Args:
        text (str): The text to be displayed in the console.

    Returns:
        None
    """
    print(text)
    return None

def write_text_in_file(text, file):
    """Writes the given text to a specified file using Python's built-in file handling.

    Args:
        text (str): The text to be written to the file.
        file (str): The file path where the text will be saved.

    Returns:
        None
    """
    with open(file, 'w') as f:
        f.write(text)
    return None