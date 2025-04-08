import unittest
from unittest.mock import patch
from map import get_adal_map


class TestGetAdalMap(unittest.TestCase):

    @patch("map.setup_game_environment")
    @patch("map.load_player")
    def test_adal_map_includes_player_and_visible_places(self, mock_load_player, mock_setup_env):
        # Arrange mock data
        mock_player = {
            "position": [1, 1],
            "visible places": {
                "oracle": {"position": [2, 2], "symbol": "🧙‍♂️ "},
                "market": {"position": [3, 3], "symbol": "🛍️ "}
            }
        }
        base_map = [["⬜" for _ in range(5)] for _ in range(5)]

        mock_load_player.return_value = mock_player
        mock_setup_env.return_value = base_map

        result_map = get_adal_map()

        self.assertEqual(result_map[1][1], "🟡 ")
        self.assertEqual(result_map[2][2], "🧙‍♂️ ")
        self.assertEqual(result_map[3][3], "🛍️ ")
