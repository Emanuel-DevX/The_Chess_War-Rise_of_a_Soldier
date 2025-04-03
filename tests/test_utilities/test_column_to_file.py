from unittest import TestCase
from utilities import column_to_file


class TestColumnToFile(TestCase):
    def test_min_column(self):
        actual = column_to_file(0)
        expected = 'A'
        self.assertEqual(actual, expected)

    def test_max_column(self):
        actual = column_to_file(7)
        expected = 'H'
        self.assertEqual(actual, expected)

    def test_middle_column1(self):
        actual = column_to_file(3)
        expected = 'D'
        self.assertEqual(actual, expected)

    def test_middle_column2(self):
        actual = column_to_file(4)
        expected = 'E'
        self.assertEqual(actual, expected)

    def test_docstring_example1(self):
        actual = column_to_file(3)
        expected = 'D'
        self.assertEqual(actual, expected)

    def test_docstring_example2(self):
        actual = column_to_file(1)
        expected = 'B'
        self.assertEqual(actual, expected)

