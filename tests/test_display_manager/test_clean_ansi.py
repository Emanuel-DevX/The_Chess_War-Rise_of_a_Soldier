import unittest
from display_manager import clean_ansi


class TestCleanAnsi(unittest.TestCase):

    def test_removes_basic_color_code(self):
        raw = "\033[31mRed Text\033[0m"
        expected = "Red Text"
        actual = clean_ansi(raw)
        self.assertEqual(actual, expected)

    def test_removes_bold_and_reset(self):
        raw = "Normal \x1B[1mBold\x1B[0m Text"
        expected = "Normal Bold Text"
        actual = clean_ansi(raw)
        self.assertEqual(actual, expected)

    def test_removes_complex_24bit_color(self):
        raw = "\x1B[38;2;255;0;0mComplex\x1B[0m"
        expected = "Complex"
        actual = clean_ansi(raw)
        self.assertEqual(actual, expected)

    def test_passes_clean_text_untouched(self):
        raw = "No codes here"
        expected = "No codes here"
        actual = clean_ansi(raw)
        self.assertEqual(actual, expected)
