from unittest import TestCase
from unittest.mock import patch
from utilities import set_traps


class TestSetTraps(TestCase):

    @patch('random.randint')
    def test_set_5_traps(self, mock_randint):
        mock_randint.side_effect = [1, 1, 1, 2, 2, 1, 2, 2, 3, 3]
        game_map = [["" for _ in range(10)] for _ in range(10)]

        traps = set_traps(game_map, (0, 0), 5)
        self.assertEqual(traps, [(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)])

    @patch('random.randint')
    def test_set_3_traps(self, mock_randint):
        mock_randint.side_effect = [5, 5, 6, 6, 7, 7]
        game_map = [["" for _ in range(10)] for _ in range(10)]

        traps = set_traps(game_map, (0, 0), 3)
        self.assertEqual(traps, [(5, 5), (6, 6), (7, 7)])

    @patch('random.randint')
    def test_default_5_traps(self, mock_randint):
        mock_randint.side_effect = [1, 1, 1, 2, 2, 1, 2, 2, 3, 3]
        game_map = [["" for _ in range(10)] for _ in range(10)]

        traps = set_traps(game_map, (0, 0))
        self.assertEqual(len(traps), 5)

    @patch('random.randint')
    def test_only_two_empty_spots(self, mock_randint):
        game_map = [['filled' for _ in range(10)] for _ in range(10)]
        game_map[1][2] = ''
        game_map[2][1] = ''

        mock_randint.side_effect = [1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2]

        traps = set_traps(game_map, (0, 0), 2)
        self.assertEqual(sorted(traps), [(1, 2), (2, 1)])

    @patch('random.randint')
    def test_different_start_position(self, mock_randint):
        mock_randint.side_effect = [5, 5, 5, 6, 6, 5, 6, 6]
        game_map = [["" for _ in range(20)] for _ in range(20)]

        traps = set_traps(game_map, (5, 5), 4)
        self.assertEqual(traps, [(5, 5), (5, 6), (6, 5), (6, 6)])
