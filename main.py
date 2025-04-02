from app.io.input import *
from app.io.output import *

def main():
    text_from_console=read_text_from_console()
    text_from_file_builtin_func=read_text_from_file_with_builtin_func("data/test_file.txt")
    text_from_file_with_pands=read_text_from_file_with_pandas("data/test_file.txt")

    print_text_in_console(text_from_console)
    print_text_in_console(text_from_file_builtin_func)
    print_text_in_console(text_from_file_with_pands)

    write_text_in_file(text_from_console, "data/Output_file1.txt")
    write_text_in_file(text_from_file_builtin_func, "data/Output_file2.txt")
    write_text_in_file(text_from_file_with_pands, "data/Output_file3.txt")


if __name__ == '__main__':
    main()