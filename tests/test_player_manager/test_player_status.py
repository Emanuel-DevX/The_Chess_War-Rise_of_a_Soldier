import unittest
from unittest.mock import patch
from display_manager import player_status


class TestPlayerStatus(unittest.TestCase):

    @patch("player_manager.load_player")
    def test_player_status_rook(self, mock_load_player):
        # Simulate player data for rook
        mock_load_player.return_value = {
            "piece": "rook",
            "health": 85,
            "gold": 100,
            "suspicion": 40,
            "next_task": "Find the king",
        }

        expected = [
            "Health: 85",
            "Gold: 100",
            "Total suspicion: 40%",
            "Next task: Find the king",
            "Your goal: Spy in enemy territory to uncover the king's location."
        ]

        self.assertEqual(player_status(), expected)

    @patch("player_manager.load_player")
    def test_player_status_bishop(self, mock_load_player):
        mock_load_player.return_value = {
            "piece": "bishop",
            "health": 90,
            "gold": 30,
            "clues_found": 2,
            "clues": [1, 2, 3],
            "movement_points": 10,
            "moves_taken": 5,
            "max_moves": 15
        }

        expected = [
            "Health: 90",
            "Gold: 30",
            "Clues found: 2/5",
            "Movement points: 10",
            "Moves taken: 5/15",
            "Your goal: Find the spy while avoiding traps!"
        ]

        self.assertEqual(player_status(), expected)

