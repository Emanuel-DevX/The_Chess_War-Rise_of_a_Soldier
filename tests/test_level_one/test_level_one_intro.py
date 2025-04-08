import unittest
from unittest.mock import patch
from level_one import level_one_intro


class TestLevelOneIntro(unittest.TestCase):

    @patch("level_one.update_display")
    @patch("level_one.input", return_value="")  # simulate ENTER press
    def test_intro_display_and_input(self, mock_input, mock_display):
        level_one_intro()
        self.assertTrue(mock_display.called)
        mock_input.assert_called_once()
