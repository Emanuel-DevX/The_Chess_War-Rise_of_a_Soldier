import unittest
from map import generate_level_walls


class TestGenerateLevelWalls(unittest.TestCase):

    def test_total_tile_count(self):
        actual = len(generate_level_walls(10, 10))
        expected = 36  # Total boundary tiles for 10x10 - 8x8
        self.assertEqual(actual, expected)

    def test_top_left_corner_wall(self):
        walls = generate_level_walls(10, 10)
        expected = (9, 9)
        self.assertIn(expected, walls)

    def test_bottom_right_corner_wall(self):
        walls = generate_level_walls(10, 10)
        expected = (18, 18)
        self.assertIn(expected, walls)

    def test_interior_tile_not_included(self):
        walls = generate_level_walls(10, 10)
        unexpected = (10, 10)
        self.assertNotIn(unexpected, walls)

    def test_custom_size_boundary(self):
        walls = generate_level_walls(5, 5, size=4)
        actual = len(walls)
        expected = 20
        self.assertEqual(actual, expected)

    def test_all_wall_positions_are_on_edges(self):
        center_row, center_col, size = 7, 7, 4
        walls = generate_level_walls(center_row, center_col, size)
        for row, col in walls:
            is_edge_row = row == center_row - 1 or row == center_row + size
            is_edge_col = col == center_col - 1 or col == center_col + size
            self.assertTrue(is_edge_row or is_edge_col, f"Non-wall coordinate found: {(row, col)}")
