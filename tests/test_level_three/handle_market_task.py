import unittest
from unittest.mock import patch
from level_three import handle_market_task


class TestHandleMarketTask(unittest.TestCase):

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="1")
    def test_buy_medicine_with_enough_gold(self, _, __):
        player = {"gold": 50, "health": 60}
        tasks = iter([])

        handle_market_task(player, tasks)

        self.assertEqual(player["gold"], 30)
        self.assertEqual(player["health"], 90)

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="1")
    def test_buy_medicine_not_enough_gold(self, _, __):
        player = {"gold": 10, "health": 50}
        tasks = iter([])

        handle_market_task(player, tasks)

        self.assertEqual(player["gold"], 10)  # No change
        self.assertEqual(player["health"], 50)

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="2")
    def test_first_time_translator_scam(self, _, __):
        player = {
            "gold": 40,
            "health": 70,
            "progress": {},
            "next_task": "Fake translator hunt"
        }
        tasks = iter(["Realize it was fake and seek the shrine"])

        handle_market_task(player, tasks)

        self.assertTrue(player["progress"]["scammed"])
        self.assertEqual(player["next_task"], "Realize it was fake and seek the shrine")
        self.assertEqual(player["position"], [12, 22])

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="2")
    def test_second_time_real_translator(self, _, __):
        player = {
            "gold": 40,
            "health": 70,
            "progress": {"scammed": True}
        }
        tasks = iter([])

        handle_market_task(player, tasks)

        self.assertTrue(player["progress"]["true_translation"])

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="2")
    def test_already_found_translator(self, _, mock_display):
        player = {
            "gold": 40,
            "health": 70,
            "progress": {"scammed": True, "true_translation": True}
        }
        tasks = iter([])

        handle_market_task(player, tasks)

        mock_display.assert_any_call(["You've already found the true translator."], save_text=True)
