import unittest
from unittest.mock import patch
from level_three import handle_trap


class TestHandleTrap(unittest.TestCase):

    @patch("level_three.update_display")
    def test_scorpion_trap(self, _):
        player = {
            "health": 100,
            "gold": 50,
            "position": (5, 5),
            "visible places": {
                "scorpion trap": {"position": (5, 5), "symbol": "🦂"}
            }
        }

        handle_trap(player)

        self.assertEqual(player["health"], 85)
        self.assertEqual(player["gold"], 50)

    @patch("level_three.update_display")
    def test_ambush_trap(self, _):
        player = {
            "health": 80,
            "gold": 20,
            "position": (2, 3),
            "visible places": {
                "ambush": {"position": (2, 3), "symbol": "⚔️"}
            }
        }

        handle_trap(player)

        self.assertEqual(player["health"], 70)
        self.assertEqual(player["gold"], 5)

    @patch("level_three.update_display")
    @patch("level_three.time.sleep")
    @patch("level_three.random.choice", return_value="BOOM")
    @patch("level_three.random.uniform", return_value=0.5)
    @patch("builtins.print")
    def test_drum_circle(self, mock_print, _, __, ___, mock_display):
        player = {
            "health": 100,
            "gold": 40,
            "position": (1, 1),
            "visible places": {
                "drum circle": {"position": (1, 1), "symbol": "🪘"}
            }
        }

        handle_trap(player)

        self.assertEqual(player["health"], 100)
        self.assertEqual(player["gold"], 40)
        self.assertEqual(mock_print.call_count, 6)  # 6 rhythm beats
        mock_display.assert_any_call(["You finally escape as the sun rises. You're tired, but unharmed."],
                                     save_text=True)
