from unittest import TestCase
from unittest.mock import patch
from level_two import spy_mission

class TestSpyMission(TestCase):
    @patch("builtins.input", return_value="")
    @patch("level_two.update_display")
    def test_spy_mission(self, mock_update_display, mock_input):
        spy_mission()

        mock_update_display.assert_called_once()

        args, kwargs = mock_update_display.call_args
        displayed_text = args[0]
        full_text = " ".join(displayed_text)

        # Key content assertions (partial matching for robustness)
        self.assertIn("The spy could be anyone", full_text)
        self.assertIn("Move with caution", full_text)
        self.assertIn("Spy Indicators", full_text)
        self.assertIn("Avoid Ambushes", full_text)
        self.assertIn("Find the Spy", full_text)
        self.assertIn("Press ENTER to begin", full_text)

        self.assertFalse(kwargs.get('status', True))

        mock_input.assert_called_once()