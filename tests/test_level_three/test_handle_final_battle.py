import unittest
from unittest.mock import patch
from level_three import handle_final_battle


class TestHandleFinalBattle(unittest.TestCase):

    @patch("level_three.update_display")
    @patch("level_three.time.sleep")
    @patch("level_three.input", return_value="1")
    def test_solo_attack_results_in_defeat(self, _, __, ___):
        player = {"health": 80, "status": None}
        tasks = iter(["Aftermath"])

        handle_final_battle(player, tasks)

        self.assertEqual(player["status"], "defeated")
        self.assertEqual(player["health"], 0)
        self.assertEqual(player["next_task"], "Aftermath")

    @patch("level_three.update_display")
    @patch("level_three.time.sleep")
    @patch("level_three.input", return_value="2")
    def test_team_attack_results_in_victory(self, _, __, ___):
        player = {"health": 45, "status": None}
        tasks = iter(["Victory Parade"])

        handle_final_battle(player, tasks)

        self.assertEqual(player["status"], "victorious")
        self.assertEqual(player["next_task"], "Victory Parade")
        self.assertTrue(player["health"] >= 10)

    @patch("level_three.update_display")
    @patch("level_three.time.sleep")
    @patch("level_three.input", return_value="2")
    def test_health_falls_to_min_10(self, _, __, ___):
        player = {"health": 20, "status": None}
        tasks = iter(["End Credits"])

        handle_final_battle(player, tasks)

        self.assertEqual(player["health"], 10)

    @patch("level_three.update_display")
    @patch("level_three.time.sleep")
    @patch("level_three.input", return_value="2")
    def test_health_falls_with_current_health_100(self, _, __, ___):
        player = {"health": 100, "status": None}
        tasks = iter(["End Credits"])

        handle_final_battle(player, tasks)

        self.assertEqual(player["health"], 70)

