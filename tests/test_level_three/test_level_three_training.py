import unittest
from unittest.mock import patch
from level_three import level_three_training



class TestLevelThreeTraining(unittest.TestCase):

    @patch("level_three.random.choice", side_effect=["selam", "dehna neh?"])
    @patch("level_three.input", side_effect=["selam", "dehna"])
    @patch("level_three.update_display")
    def test_training_response_flow(self, mock_display, mock_input, _):
        # Should call input twice and display multiple times
        level_three_training()

        self.assertEqual(mock_input.call_count, 2)
        self.assertGreaterEqual(mock_display.call_count, 3)


