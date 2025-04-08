import unittest
from unittest.mock import patch
from level_one import level_one_training


class TestLevelOneTraining(unittest.TestCase):

    @patch("level_one.update_display")
    @patch("level_one.input", return_value="")  # Simulate ENTER
    def test_training_display_and_input(self, mock_input, mock_display):
        level_one_training()

        self.assertTrue(mock_display.called)
        mock_input.assert_called_once()
