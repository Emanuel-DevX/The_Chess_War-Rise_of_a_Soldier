import unittest
from map import generate_level_interior


class TestGenerateLevelInterior(unittest.TestCase):

    def test_total_tile_count(self):
        actual = len(generate_level_interior(10, 10))
        expected = 64  # 8x8
        self.assertEqual(actual, expected)

    def test_top_left_corner_included(self):
        actual = generate_level_interior(10, 10)
        expected = (10, 10)
        self.assertIn(expected, actual)

    def test_bottom_right_corner_included(self):
        actual = generate_level_interior(10, 10)
        expected = (17, 17)
        self.assertIn(expected, actual)

    def test_custom_size(self):
        actual = len(generate_level_interior(5, 5, size=4))
        expected = 16  # 4x4
        self.assertEqual(actual, expected)

    def test_all_positions_within_bounds(self):
        interior = generate_level_interior(2, 3, size=3)
        for row, col in interior:
            self.assertTrue(2 <= row <= 4 and 3 <= col <= 5)
