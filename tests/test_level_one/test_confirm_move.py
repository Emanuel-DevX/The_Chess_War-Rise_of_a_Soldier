import unittest
from unittest.mock import patch
from level_one import confirm_move


class TestConfirmMove(unittest.TestCase):

    @patch("level_one.player_manager.save_player")
    @patch("level_one.input", return_value="1")
    @patch("level_one.update_display")
    @patch("level_one.random.randint", return_value=2)  # triggers warning
    def test_north_move_with_confirmation(self, _, __, ___, mock_save):
        player = {"boldness": 3}
        result = confirm_move(player, "north")

        self.assertTrue(result)
        self.assertEqual(player["boldness"], 4)
        mock_save.assert_called_once_with(player)
