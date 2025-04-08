import unittest
from app.io.input import *

class TestFunctions(unittest.TestCase):

    #testing read_text_from_file_with_builtin_func
    def test_read_text_from_file_with_builtin_func_from_empty_file(self):
        read_text= read_text_from_file_with_builtin_func("TestFiles/emptyFile.txt")
        self.assertEqual(read_text, "")

    def test_read_text_from_file_with_builtin_func_from_simple_file(self):
        read_text= read_text_from_file_with_builtin_func("TestFiles/simpleFile.txt")
        self.assertEqual(read_text, "simple file\nwith some text\nnothing special")
        
    def test_read_text_from_file_with_builtin_func_from_file_with_cyrylic_letters(self):
        read_text= read_text_from_file_with_builtin_func("TestFiles/cyrylicFile.txt")
        self.assertEqual(read_text, "Це text with\nкириличними літерами\nfor тестування")

    # testing read_text_from_file_with_pandas
    def test_read_text_from_file_with_pandas_from_empty_file(self):
        read_text = read_text_from_file_with_pandas("TestFiles/emptyFile.txt")
        self.assertEqual(read_text, "")

    def test_read_text_from_file_with_pandas_from_simple_file(self):
        read_text = read_text_from_file_with_pandas("TestFiles/simpleFile.txt")
        self.assertEqual(read_text, "simple file\nwith some text\nnothing special")

    def test_read_text_from_file_with_pandas_from_file_with_cyrylic_letters(self):
        read_text = read_text_from_file_with_pandas("TestFiles/cyrylicFile.txt")
        self.assertEqual(read_text, "Це text with\nкириличними літерами\nfor тестування")


if __name__ == '__main__':
    unittest.main()
