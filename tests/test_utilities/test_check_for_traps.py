from unittest import TestCase
from unittest.mock import patch
from utilities import check_for_trap


class TestCheckForTrap(TestCase):

    @patch('random.randint')
    def test_trap_triggered(self, mock_randint):
        """Test when position is in traps"""
        mock_randint.return_value = 10  # Fixed damage value
        player = {"health": 100, "knowledge": []}
        traps = [(1, 1), (2, 2)]

        result, message = check_for_trap((1, 1), traps, player)

        self.assertTrue(result)
        self.assertEqual(player["health"], 90)
        self.assertIn("Discovered trap location", player["knowledge"])
        self.assertEqual(message, [
            "⚠️ YOU TRIGGERED A TRAP! ⚠️",
            "You take 10 damage.",
            f"Remaining health: 90"
        ])

    def test_no_trap_triggered(self):
        player = {"health": 100, "knowledge": []}
        traps = [(1, 1), (2, 2)]

        result = check_for_trap((3, 3), traps, player)[0]

        self.assertFalse(result)
        self.assertEqual(player["health"], 100)
        self.assertEqual(len(player["knowledge"]), 0)

    @patch('random.randint')
    def test_random_damage_range_min(self, mock_randint):
        player = {"health": 100, "knowledge": []}
        traps = [(1, 1)]

        mock_randint.return_value = 5
        check_for_trap((1, 1), traps, player)
        self.assertEqual(player["health"], 95)

    @patch('random.randint')
    def test_random_damage_range_max(self, mock_randint):
        player = {"health": 100, "knowledge": []}
        traps = [(1, 1)]

        player["health"] = 100
        mock_randint.return_value = 15
        check_for_trap((1, 1), traps, player)
        self.assertEqual(player["health"], 85)
