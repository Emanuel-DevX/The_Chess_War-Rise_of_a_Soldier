import unittest
from unittest.mock import patch
from display_manager import update_display_text


class TestUpdateDisplayText(unittest.TestCase):

    @patch("display_manager.load_display_text", return_value=["Previous message"])
    def test_appends_single_message(self, _):
        new_msg = ["New message"]
        expected = ["Previous message", "", "New message"]
        actual = update_display_text(new_msg, max_len=10)
        self.assertEqual(actual, expected)

    @patch("display_manager.load_display_text", return_value=["Line A", "=" * 80, "Line B"])
    def test_inserts_separator_when_saving(self, _):
        new_msg = ["Fresh"]
        expected = ["Line A", "Line B", "", "=" * 80, "Fresh"]
        actual = update_display_text(new_msg, max_len=10, save_text=True)
        self.assertEqual(actual, expected)

    @patch("display_manager.load_display_text", return_value=[])
    def test_handles_empty_history(self, _):
        new_msg = ["First"]
        expected = ["", "First"]
        actual = update_display_text(new_msg, max_len=5)
        self.assertEqual(actual, expected)

    @patch("display_manager.load_display_text", return_value=["Stuff"])
    def test_ignores_separator_if_no_save(self, _):
        new_msg = ["Thing"]
        expected = ["Stuff", "", "Thing"]
        actual = update_display_text(new_msg, max_len=10, save_text=False)
        self.assertEqual(actual, expected)
