import unittest
from level_three import update_player_visible_places


class TestUpdatePlayerVisiblePlaces(unittest.TestCase):

    def test_reveals_place_based_on_task(self):
        player = {
            "next_task": "Go to the market to find a translator",
            "visible places": {}
        }
        adal_map = {
            (5, 15): {"name": "adal market", "symbol": "🛍️ ", "description": "desc", "hidden": True},
            (6, 16): {"name": "oracle", "symbol": "🧙‍♂️ ", "description": "desc", "hidden": True},
        }

        update_player_visible_places(player, adal_map)

        # Should now be visible
        self.assertIn("adal market", player["visible places"])
        self.assertFalse(adal_map[(5, 15)]["hidden"])

    def test_filters_out_hidden_or_no_symbol_places(self):
        player = {
            "next_task": "Some unrelated task",
            "visible places": {}
        }
        adal_map = {
            (1, 1): {"name": "oracle", "symbol": None, "description": "desc", "hidden": False},
            (2, 2): {"name": "church", "symbol": "✝️ ", "description": "desc", "hidden": True},
            (3, 3): {"name": "drum circle", "symbol": "🪘 ", "description": "desc", "hidden": False}
        }

        update_player_visible_places(player, adal_map)

        # Only drum circle should remain
        self.assertEqual(len(player["visible places"]), 1)
        self.assertIn("drum circle", player["visible places"])

    def test_hides_oracle_and_message_if_conditions_match(self):
        player = {
            "next_task": "Go to shrine",
            "progress": {"translated_but_encrypted": False}
        }
        adal_map = {
            (5, 5): {"name": "oracle", "symbol": "🧙‍♂️ ", "description": "desc", "hidden": False},
            (6, 6): {"name": "hidden message", "symbol": "📜 ", "description": "desc", "hidden": False},
            (7, 7): {"name": "drum circle", "symbol": "🪘 ", "description": "desc", "hidden": False}
        }

        update_player_visible_places(player, adal_map)

        self.assertTrue(adal_map[(5, 5)]["hidden"])
        self.assertIsNone(adal_map[(5, 5)]["symbol"])
        self.assertTrue(adal_map[(6, 6)]["hidden"])
        self.assertIsNone(adal_map[(6, 6)]["symbol"])
        self.assertIn("drum circle", player["visible places"])

