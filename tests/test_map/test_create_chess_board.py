import unittest
from map import create_chess_board


class TestCreateChessBoard(unittest.TestCase):

    def test_board_has_8_rows(self):
        board = create_chess_board()
        expected = 8
        actual = len(board)
        self.assertEqual(actual, expected)

    def test_each_row_has_8_columns(self):
        board = create_chess_board()
        for row in board:
            expected = 8
            actual = len(row)
            self.assertEqual(actual, expected)

    def test_top_left_corner_is_black(self):
        board = create_chess_board()
        expected = '⬛ '
        actual = board[0][0]
        self.assertEqual(actual, expected)

    def test_top_right_corner_is_white(self):
        board = create_chess_board()
        expected = '⬜ '
        actual = board[0][7]
        self.assertEqual(actual, expected)

    def test_bottom_right_corner_is_black(self):
        board = create_chess_board()
        expected = '⬛ '
        actual = board[7][7]
        self.assertEqual(actual, expected)

    def test_pattern_is_alternating(self):
        board = create_chess_board()
        for row_index, row in enumerate(board):
            for col_index, square in enumerate(row):
                expected = '⬜ ' if (row_index + col_index) % 2 else '⬛ '
                actual = square
                self.assertEqual(actual, expected)
