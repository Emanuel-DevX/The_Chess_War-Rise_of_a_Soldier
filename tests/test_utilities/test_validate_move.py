from unittest import TestCase
from utilities import validate_move

class TestValidateMove(TestCase):

    # Cardinal direction tests
    def test_north_valid(self):
        actual = validate_move((0, 0), 5, 3, 'north')
        expected = True
        self.assertEqual(actual, expected)

    def test_north_invalid_at_top_edge(self):
        actual = validate_move((0, 0), 0, 3, 'north')
        expected = False
        self.assertEqual(actual, expected)

    def test_south_valid(self):
        actual = validate_move((0, 0), 5, 3, 'south')
        expected = True
        self.assertEqual(actual, expected)

    def test_south_invalid_at_bottom_edge(self):
        actual = validate_move((0, 0), 7, 3, 'south')
        expected = False
        self.assertEqual(actual, expected)

    def test_east_valid(self):
        actual = validate_move((0, 0), 3, 5, 'east')
        expected = True
        self.assertEqual(actual, expected)

    def test_east_invalid_at_right_edge(self):
        actual = validate_move((0, 0), 3, 7, 'east')
        expected = False
        self.assertEqual(actual, expected)

    def test_west_valid(self):
        actual = validate_move((0, 0), 3, 5, 'west')
        expected = True
        self.assertEqual(actual, expected)

    def test_west_invalid_at_left_edge(self):
        actual = validate_move((0, 0), 3, 0, 'west')
        expected = False
        self.assertEqual(actual, expected)

    # Diagonal direction tests
    def test_north_east_valid(self):
        actual = validate_move((0, 0), 5, 5, 'north_east')
        expected = True
        self.assertEqual(actual, expected)

    def test_north_east_invalid_at_top_edge(self):
        actual = validate_move((0, 0), 0, 5, 'north_east')
        expected = False
        self.assertEqual(actual, expected)

    def test_north_east_invalid_at_right_edge(self):
        actual = validate_move((0, 0), 5, 7, 'north_east')
        expected = False
        self.assertEqual(actual, expected)

    def test_north_west_valid(self):
        actual = validate_move((0, 0), 5, 5, 'north_west')
        expected = True
        self.assertEqual(actual, expected)

    def test_north_west_invalid_at_top_edge(self):
        actual = validate_move((0, 0), 0, 5, 'north_west')
        expected = False
        self.assertEqual(actual, expected)

    def test_north_west_invalid_at_left_edge(self):
        actual = validate_move((0, 0), 5, 0, 'north_west')
        expected = False
        self.assertEqual(actual, expected)

    def test_south_east_valid(self):
        actual = validate_move((0, 0), 5, 5, 'south_east')
        expected = True
        self.assertEqual(actual, expected)

    def test_south_east_invalid_at_bottom_edge(self):
        actual = validate_move((0, 0), 7, 5, 'south_east')
        expected = False
        self.assertEqual(actual, expected)

    def test_south_east_invalid_at_right_edge(self):
        actual = validate_move((0, 0), 5, 7, 'south_east')
        expected = False
        self.assertEqual(actual, expected)

    def test_south_west_valid(self):
        actual = validate_move((0, 0), 5, 5, 'south_west')
        expected = True
        self.assertEqual(actual, expected)

    def test_south_west_invalid_at_bottom_edge(self):
        actual = validate_move((0, 0), 7, 5, 'south_west')
        expected = False
        self.assertEqual(actual, expected)

    def test_south_west_invalid_at_left_edge(self):
        actual = validate_move((0, 0), 5, 0, 'south_west')
        expected = False
        self.assertEqual(actual, expected)

    # Corner cases
    def test_top_left_corner_north(self):
        actual = validate_move((0, 0), 0, 0, 'north')
        expected = False
        self.assertEqual(actual, expected)

    def test_top_left_corner_west(self):
        actual = validate_move((0, 0), 0, 0, 'west')
        expected = False
        self.assertEqual(actual, expected)

    def test_bottom_right_corner_south(self):
        actual = validate_move((0, 0), 7, 7, 'south')
        expected = False
        self.assertEqual(actual, expected)

    def test_bottom_right_corner_east(self):
        actual = validate_move((0, 0), 7, 7, 'east')
        expected = False
        self.assertEqual(actual, expected)

    # Docstring examples
    def test_docstring_example1(self):
        actual = validate_move((0, 0), 7, 3, 'north')
        expected = True
        self.assertEqual(actual, expected)

    def test_docstring_example2(self):
        actual = validate_move((0, 0), 7, 3, 'south')
        expected = False
        self.assertEqual(actual, expected)

    def test_docstring_example3(self):
        actual = validate_move((0, 0), 0, 0, 'north')
        expected = False
        self.assertEqual(actual, expected)

    def test_docstring_example4(self):
        actual = validate_move((0, 0), 4, 4, 'north_east')
        expected = True
        self.assertEqual(actual, expected)

    def test_docstring_example5(self):
        actual = validate_move((0, 0), 0, 7, 'north_west')
        expected = False
        self.assertEqual(actual, expected)

    def test_docstring_example6(self):
        actual = validate_move((0, 0), 6, 6, 'south_east')
        expected = True
        self.assertEqual(actual, expected)

    def test_docstring_example7(self):
        actual = validate_move((0, 0), 1, 1, 'south_west')
        expected = True
        self.assertEqual(actual, expected)
