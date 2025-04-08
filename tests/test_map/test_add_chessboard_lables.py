import unittest
from map import add_chess_board_labels


class TestAddChessBoardLabels(unittest.TestCase):

    def test_rank_labels_are_correct(self):
        game_map = [["." for _ in range(10)] for _ in range(10)]
        add_chess_board_labels(game_map, 1, 1)

        expected = [" 8 ", " 7 ", " 6 ", " 5 ", " 4 ", " 3 ", " 2 ", " 1 "]
        actual = [game_map[1 + i][0] for i in range(8)]
        self.assertEqual(actual, expected)

    def test_file_labels_are_correct(self):
        game_map = [["." for _ in range(10)] for _ in range(10)]
        add_chess_board_labels(game_map, 1, 1)

        expected = [" A ", " B ", " C ", " D ", " E ", " F ", " G ", " H "]
        actual = [game_map[9][1 + i] for i in range(8)]
        self.assertEqual(actual, expected)

    def test_unaffected_tiles_remain_unchanged(self):
        game_map = [["⬜" for _ in range(10)] for _ in range(10)]
        original_tile = game_map[2][2]
        add_chess_board_labels(game_map, 1, 1)
        self.assertEqual(game_map[2][2], original_tile)
