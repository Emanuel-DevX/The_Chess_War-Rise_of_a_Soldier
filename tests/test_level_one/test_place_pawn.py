import unittest
from unittest.mock import patch
from level_one import place_pawn


class TestPlacePawn(unittest.TestCase):

    @patch("level_one.update_display")
    @patch("level_one.input", return_value="1")  # Accept the first placement
    @patch("level_one.assign_position_attributes", return_value=("Safe Zone", 5, 10))
    @patch("level_one.column_to_file", return_value="e")
    @patch("level_one.random.randint", return_value=4)
    @patch("level_one.player_manager.save_player")
    def test_place_pawn_accept_position(self, mock_save, _, __, ___, ____, _____):
        player = {
            "position": None,
            "health": 90,
            "knowledge": []
        }
        place_pawn(player)

        self.assertEqual(player["position"], (25, 4))
        self.assertEqual(player["health"], 100)
        self.assertIn("Started in a Safe Zone area", player["knowledge"])

        mock_save.assert_called_once_with(player)
