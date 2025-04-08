import unittest
from unittest.mock import patch
from level_one import get_pawn_direction_choice


class TestGetPawnDirectionChoice(unittest.TestCase):

    @patch("level_one.update_display")
    @patch("level_one.input", return_value="1")
    def test_move_north(self, _, __):
        self.assertEqual(get_pawn_direction_choice(), "north")

    @patch("level_one.update_display")
    @patch("level_one.input", return_value="2")
    def test_capture_right(self, _, __):
        self.assertEqual(get_pawn_direction_choice(), "north_east")

    @patch("level_one.update_display")
    @patch("level_one.input", return_value="3")
    def test_capture_left(self, _, __):
        self.assertEqual(get_pawn_direction_choice(), "north_west")

    @patch("level_one.update_display")
    @patch("level_one.input", return_value="4")
    def test_invalid_input(self, _, __):
        self.assertIsNone(get_pawn_direction_choice())
