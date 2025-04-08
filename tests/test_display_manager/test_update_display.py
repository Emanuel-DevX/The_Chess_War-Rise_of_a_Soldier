import unittest
from unittest.mock import patch
from display_manager import update_display


class TestUpdateDisplay(unittest.TestCase):

    @patch("builtins.print")
    @patch("display_manager.clean_ansi", side_effect=lambda x: x)
    @patch("display_manager.save_display_text", autospec=True)
    @patch("display_manager.make_status_box", return_value=[])
    @patch("display_manager.player_status")
    @patch("display_manager.load_player", return_value={"position": [0, 0], "piece": "pawn"})
    def test_minimal_2x2_display(self, _, __,___, ____,_____,mock_print):
        test_map = [["A", "B"], ["C", "D"]]
        display_text = ["Line 1", "Line 2"]

        update_display(display_text, save_text=False, status=False, game_map=test_map)

        actual_lines = [call.args[0] for call in mock_print.call_args_list if call.args]

        actual_lengths = {len(line) for line in actual_lines}
        expected_unique_lengths = 3
        actual_unique_lengths = len(actual_lengths)
        self.assertEqual(actual_unique_lengths, expected_unique_lengths)

        for row in test_map:
            expected_map_row = ''.join(row)
            match = any(expected_map_row in line for line in actual_lines)
            self.assertTrue(match)

        for expected_text in display_text:
            match = any(expected_text in line for line in actual_lines)
            self.assertTrue(match)
