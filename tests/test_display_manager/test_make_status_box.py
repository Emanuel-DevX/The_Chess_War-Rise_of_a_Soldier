import unittest
from display_manager import make_status_box
from colorama import Fore, Style
import re

def strip_ansi(text):
    """Helper to remove ANSI escape sequences from a string for test comparison."""
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

class TestMakeStatusBox(unittest.TestCase):

    def test_basic_box_structure(self):
        status = ["Health: 100", "Gold: 50"]
        box = make_status_box(status)

        clean_box = [strip_ansi(line) for line in box]

        self.assertEqual(len(clean_box), 4)

        self.assertTrue(clean_box[0].startswith("┌") and clean_box[0].endswith("┐"))
        self.assertTrue(clean_box[-1].startswith("└") and clean_box[-1].endswith("┘"))

        for line in clean_box[1:-1]:
            self.assertTrue(line.startswith("│"))
            self.assertTrue(line.endswith("│"))

    def test_box_width_consistency(self):
        status = ["HP: 90", "Longer stat: 75"]
        box = make_status_box(status)
        clean_box = [strip_ansi(line) for line in box]

        # All lines should be the same length
        line_lengths = {len(line) for line in clean_box}
        self.assertEqual(len(line_lengths), 1, f"Inconsistent line lengths: {line_lengths}")
