from unittest import TestCase
from utilities import move


class TestMove(TestCase):
    # Cardinal directions
    def test_move_north(self):
        actual = move(5, 5, 'north')
        expected = (4, 5)
        self.assertEqual(actual, expected)

    def test_move_south(self):
        actual = move(5, 5, 'south')
        expected = (6, 5)
        self.assertEqual(actual, expected)

    def test_move_east(self):
        actual = move(5, 5, 'east')
        expected = (5, 6)
        self.assertEqual(actual, expected)

    def test_move_west(self):
        actual = move(5, 5, 'west')
        expected = (5, 4)
        self.assertEqual(actual, expected)

    # Diagonal directions
    def test_move_north_east(self):
        actual = move(5, 5, 'north_east')
        expected = (4, 6)
        self.assertEqual(actual, expected)

    def test_move_north_west(self):
        actual = move(5, 5, 'north_west')
        expected = (4, 4)
        self.assertEqual(actual, expected)

    def test_move_south_east(self):
        actual = move(5, 5, 'south_east')
        expected = (6, 6)
        self.assertEqual(actual, expected)

    def test_move_south_west(self):
        actual = move(5, 5, 'south_west')
        expected = (6, 4)
        self.assertEqual(actual, expected)

    # Edge cases (assuming board boundaries are handled elsewhere)
    def test_move_from_origin_north(self):
        actual = move(0, 0, 'north')
        expected = (-1, 0)
        self.assertEqual(actual, expected)

    def test_move_from_origin_east(self):
        actual = move(0, 0, 'east')
        expected = (0, 1)
        self.assertEqual(actual, expected)

    def test_move_from_origin_south_west(self):
        actual = move(0, 0, 'south_west')
        expected = (1, -1)
        self.assertEqual(actual, expected)

    # Test cases from docstring examples
    def test_docstring_example1(self):
        actual = move(7, 3, 'north')
        expected = (6, 3)
        self.assertEqual(actual, expected)

    def test_docstring_example2(self):
        actual = move(0, 0, 'east')
        expected = (0, 1)
        self.assertEqual(actual, expected)

    def test_docstring_example3(self):
        actual = move(4, 4, 'north_east')
        expected = (3, 5)
        self.assertEqual(actual, expected)

    def test_docstring_example4(self):
        actual = move(1, 1, 'south_west')
        expected = (2, 0)
        self.assertEqual(actual, expected)

