import unittest
from map import generate_fire_tiles


class TestGenerateFireTiles(unittest.TestCase):

    def test_total_tile_count_without_exclusions(self):
        actual = len(generate_fire_tiles([]))
        expected = 42  # 7 rows * 6 columns
        self.assertEqual(actual, expected)

    def test_top_left_corner_exists(self):
        tiles = generate_fire_tiles([])
        expected = (23, 15)
        self.assertIn(expected, tiles)

    def test_bottom_right_corner_exists(self):
        tiles = generate_fire_tiles([])
        expected = (29, 20)
        self.assertIn(expected, tiles)

    def test_excluded_tiles_are_removed(self):
        excluded = [(23, 15), (29, 20)]
        tiles = generate_fire_tiles(excluded)
        for tile in excluded:
            self.assertNotIn(tile, tiles)
