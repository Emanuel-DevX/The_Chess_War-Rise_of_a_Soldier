import unittest
from unittest.mock import patch
from level_three import handle_villager_encounter


class TestHandleVillagerEncounter(unittest.TestCase):

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="1")  # "selam"
    @patch("level_three.random.choice", return_value=("selam", {"reply": "selam", "fail_penalty": 30}))
    def test_correct_response(self, _, __, ___):
        player = {"suspicion": 10}
        result = handle_villager_encounter(player)

        self.assertTrue(result)
        self.assertEqual(player["suspicion"], 10)  # no penalty

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="2")  # "dawit" (wrong)
    @patch("level_three.random.choice", return_value=("selam", {"reply": "selam", "fail_penalty": 20}))
    def test_incorrect_response_adds_suspicion(self, _, __, ___):
        player = {"suspicion": 50}
        result = handle_villager_encounter(player)

        self.assertTrue(result)
        self.assertEqual(player["suspicion"], 70)

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="3")  # "church" (wrong)
    @patch("level_three.random.choice", return_value=("selam", {"reply": "selam", "fail_penalty": 50}))
    def test_game_over_when_suspicion_hits_100(self, _, __, ___):
        player = {"suspicion": 60}
        result = handle_villager_encounter(player)

        self.assertFalse(result)
        self.assertEqual(player["suspicion"], 110)

