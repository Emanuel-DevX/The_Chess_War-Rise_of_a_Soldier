import unittest
from map import generate_forest_tiles


class TestGenerateForestTiles(unittest.TestCase):

    def test_first_few_tiles(self):
        actual = generate_forest_tiles([])[:3]
        expected = [(20, 0), (20, 1), (20, 2)]
        self.assertEqual(actual, expected)

    def test_total_tile_count_without_exclusions(self):
        actual = len(generate_forest_tiles([]))
        expected = 275
        self.assertEqual(actual, expected)

    def test_exclusion_reduces_count(self):
        actual = len(generate_forest_tiles([(20, 0), (21, 1)]))
        expected = 273  # 275 - 2
        self.assertEqual(actual, expected)
