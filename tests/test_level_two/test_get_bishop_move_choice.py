from unittest import TestCase
from unittest.mock import patch
from level_two import get_bishop_move_choice


class TestGetBishopMoveChoice(TestCase):

    @patch('level_two.update_display')
    @patch('builtins.input')
    def test_invalid_then_valid_input(self, mock_input, _):
        mock_input.side_effect = ['5', '2']

        result = get_bishop_move_choice()

        self.assertIsNone(result)
        self.assertEqual(mock_input.call_count, 1)

    @patch('level_two.update_display')
    @patch('builtins.input')
    def test_multiple_invalid_then_valid(self, mock_input, _):
        mock_input.side_effect = ['0', 'idk', '']

        result = get_bishop_move_choice()

        self.assertIsNone(result)
        self.assertEqual(mock_input.call_count, 1)

    @patch('level_two.update_display')
    @patch('builtins.input')
    def test_valid_first_try(self, mock_input, _):
        mock_input.return_value = '1'

        result = get_bishop_move_choice()

        self.assertEqual(result, 'north_east')
        mock_input.assert_called_once()