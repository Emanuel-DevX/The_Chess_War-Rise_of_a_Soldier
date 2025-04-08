import unittest
from unittest.mock import patch
from itertools import product
from level_three import generate_adal_places


class TestGenerateAdalPlaces(unittest.TestCase):

    @patch("level_three.random.sample")
    def test_returns_25_unique_places(self, mock_sample):
        # Prepare 25 fake places
        fake_places = [
            (f"place_{i}", f"emoji_{i}", f"description_{i}", bool(i % 2))
            for i in range(25)
        ]
        # Prepare 25 fake positions within 8x8 grid starting at (5,15)
        positions = list(product(range(5, 13), range(15, 23)))
        positions.pop()
        fake_positions = positions[:25]

        mock_sample.side_effect = [fake_places, fake_positions]

        result = generate_adal_places()

        self.assertEqual(len(result), 25)
        self.assertEqual(len(set(result.keys())), 25)

    @patch("level_three.random.sample")
    def test_structure_of_place_data(self, mock_sample):
        fake_places = [
            (f"place_{i}", f"emoji_{i}", f"description_{i}", bool(i % 2))
            for i in range(25)
        ]
        positions = list(product(range(5, 13), range(15, 23)))
        positions.pop()
        fake_positions = positions[:25]

        mock_sample.side_effect = [fake_places, fake_positions]

        result = generate_adal_places()

        for data in result.values():
            self.assertIn("name", data)
            self.assertIn("symbol", data)
            self.assertIn("description", data)
            self.assertIn("hidden", data)
