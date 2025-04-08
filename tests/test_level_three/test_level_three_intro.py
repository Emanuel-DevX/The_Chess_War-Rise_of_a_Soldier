import unittest
from unittest.mock import patch
from level_three import level_three_intro


class TestLevelThreeIntro(unittest.TestCase):

    @patch("level_three.input", return_value="")  # mock ENTER press
    @patch("level_three.update_display")
    def test_intro_display_and_input(self, mock_display, mock_input):
        level_three_intro()

        self.assertTrue(mock_display.called)

        mock_input.assert_called_once()

