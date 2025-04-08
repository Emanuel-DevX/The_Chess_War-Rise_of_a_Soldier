import unittest
from map import initialize_game_map


class TestInitializeGameMap(unittest.TestCase):

    def test_map_has_correct_number_of_rows(self):
        size = 5
        actual = len(initialize_game_map(size))
        expected = 5
        self.assertEqual(actual, expected)

    def test_map_has_correct_number_of_columns(self):
        size = 5
        actual = len(initialize_game_map(size)[0])
        expected = 5
        self.assertEqual(actual, expected)

    def test_all_tiles_use_default_tile(self):
        size = 4
        default = "X"
        game_map = initialize_game_map(size, default_tile=default)
        for row in game_map:
            for tile in row:
                self.assertEqual(tile, default)

    def test_default_tile_is_applied_in_top_left(self):
        size = 3
        expected = "~"
        actual = initialize_game_map(size, default_tile="~")[0][0]
        self.assertEqual(actual, expected)

    def test_map_is_square(self):
        size = 6
        game_map = initialize_game_map(size)
        for row in game_map:
            self.assertEqual(len(row), size)
