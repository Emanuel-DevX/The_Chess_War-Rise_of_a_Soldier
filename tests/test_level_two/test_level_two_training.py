from level_two import level_two_training
from unittest import TestCase
from unittest.mock import patch


class TestLevelTwoTraining(TestCase):
    @patch("builtins.input", return_value="")
    @patch("level_two.update_display")
    def test_level_two_training(self, mock_update_display, mock_input):
        level_two_training()

        args, kwargs = mock_update_display.call_args
        actual_text = args[0]

        self.assertIn("LEVEL 2 TRAINING", "".join(actual_text))
        self.assertIn("As a **bishop**, your movement is now limited", "".join(actual_text))
        self.assertIn("MOVE OPTIONS:", "".join(actual_text))
        self.assertIn("⚔️ **Movement Rules:**", "".join(actual_text))
        self.assertFalse(kwargs.get("status", True))  # Verify status=False

        mock_input.assert_called_once()