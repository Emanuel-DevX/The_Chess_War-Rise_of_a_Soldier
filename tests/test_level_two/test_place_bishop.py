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

        place_bishop(player, (0, 0))

        mock_save.assert_called_once_with(player)
        self.assertIs(mock_save.call_args[0][0], player)

    @patch('level_two.update_display')
    @patch('level_two.save_player')
    @patch('builtins.input')
    def test_place_bishop_dark_square(self, mock_input, mock_save, _):
        mock_input.return_value = 'D'
        player = {
            "position": None,
            "health": 100,
            "bishop_color": None,
            "knowledge": []
        }

        place_bishop(player, (0, 0))

        mock_save.assert_called_once_with(player)
