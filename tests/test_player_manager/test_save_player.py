import unittest
from unittest.mock import mock_open, patch
import json
import player_manager  # assuming your function is in player_manager.py

class TestSavePlayer(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_save_player(self, mock_json_dump, mock_file):
        test_data = {
            "name": "Emanuel",
            "position": [2, 3],
            "health": 90
        }

        player_manager.save_player(test_data)

        # Check that open was called with the correct file and mode
        mock_file.assert_called_once_with("player.json", "w")

        # Check that json.dump was called with the correct data and indentation
        mock_json_dump.assert_called_once_with(test_data, mock_file(), indent=4)

