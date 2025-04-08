import unittest
from map import place_tiles_on_map


class TestPlaceTilesOnMap(unittest.TestCase):

    def test_tiles_are_placed_correctly(self):
        test_map = [["⬜" for _ in range(3)] for _ in range(3)]
        place_tiles_on_map(test_map, [(0, 1), (2, 2)], "🔥")
        expected = "🔥"
        actual1 = test_map[0][1]
        actual2 = test_map[2][2]
        self.assertEqual(actual1, expected)
        self.assertEqual(actual2, expected)

    def test_unaffected_tile_remains_same(self):
        test_map = [["⬜" for _ in range(3)] for _ in range(3)]
        place_tiles_on_map(test_map, [(1, 1)], "🌲")
        expected = "⬜"
        actual = test_map[0][0]
        self.assertEqual(actual, expected)

    def test_full_map_patch(self):
        test_map = [["." for _ in range(2)] for _ in range(2)]
        tiles = [(0, 0), (0, 1), (1, 0), (1, 1)]
        place_tiles_on_map(test_map, tiles, "⛰️")
        for row in range(2):
            for col in range(2):
                self.assertEqual(test_map[row][col], "⛰️")

    def test_empty_tiles_does_nothing(self):
        test_map = [["." for _ in range(2)] for _ in range(2)]
        place_tiles_on_map(test_map, [], "🌳")
        expected = [["." for _ in range(2)] for _ in range(2)]
        self.assertEqual(test_map, expected)

