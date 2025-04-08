import unittest
from unittest.mock import patch
from level_three import get_player_movement_choice


class TestGetPlayerMovementChoice(unittest.TestCase):

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="1")
    def test_north_choice(self, _, __):
        self.assertEqual(get_player_movement_choice(), "north")

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="2")
    def test_south_choice(self, _, __):
        self.assertEqual(get_player_movement_choice(), "south")

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="3")
    def test_west_choice(self, _, __):
        self.assertEqual(get_player_movement_choice(), "west")

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="4")
    def test_east_choice(self, _, __y):
        self.assertEqual(get_player_movement_choice(), "east")

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="invalid")
    def test_invalid_choice_returns_none(self, _, __):
        self.assertIsNone(get_player_movement_choice())

