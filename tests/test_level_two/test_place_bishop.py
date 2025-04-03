from unittest import TestCase
from unittest.mock import patch
from level_two import place_bishop


class TestPlaceBishop(TestCase):
    @patch('level_two.update_display')
    @patch('level_two.save_player')
    @patch('builtins.input')
    def test_place_bishop_light_square(self, mock_input, mock_save, mock_display):
        mock_input.return_value = 'L'
        player = {
            "position": None,
            "health": 100,
            "bishop_color": None,
            "knowledge": []
        }
        board_start = (0, 0)

        place_bishop(player, board_start)

        mock_input.assert_called_once_with("Enter 'L' for light square ⬜ or 'D' for dark square ⬛: ")
        self.assertEqual(player["position"], (7, 2))  # c1 position
        self.assertEqual(player["bishop_color"], "light")
        self.assertEqual(player["health"], 110)
        self.assertIn("Light square bishop - strength on open positions", player["knowledge"])
        mock_save.assert_called_once_with(player)
        self.assertEqual(mock_display.call_count, 2)

    @patch('level_two.update_display')
    @patch('level_two.save_player')
    @patch('builtins.input')
    def test_place_bishop_dark_square(self, mock_input, mock_save, mock_display):
        mock_input.return_value = 'D'
        player = {
            "position": None,
            "health": 100,
            "bishop_color": None,
            "knowledge": []
        }
        board_start = (0, 0)

        place_bishop(player, board_start)

        mock_input.assert_called_once_with("Enter 'L' for light square ⬜ or 'D' for dark square ⬛: ")
        self.assertEqual(player["position"], (7, 5))  # f1 position
        self.assertEqual(player["bishop_color"], "dark")
        self.assertEqual(player["health"], 110)
        self.assertIn("Dark square bishop - strength in closed positions", player["knowledge"])
        mock_save.assert_called_once_with(player)
        self.assertEqual(mock_display.call_count, 2)

    @patch('level_two.update_display')
    @patch('builtins.print')
    @patch('builtins.input')
    def test_place_bishop_invalid_then_valid(self, mock_input, mock_print, _):
        mock_input.side_effect = ['X', 'L']
        player = {
            "position": None,
            "health": 100,
            "bishop_color": None,
            "knowledge": []
        }
        board_start = (0, 0)

        place_bishop(player, board_start)

        self.assertEqual(mock_input.call_count, 2)
        mock_print.assert_called_once_with("Invalid choice. Please enter 'L' or 'D'.")
        self.assertEqual(player["position"], (7, 2))  # Should still get light square position