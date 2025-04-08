import unittest
from unittest.mock import patch
from level_three import handle_oracle_task


class TestHandleOracleTask(unittest.TestCase):

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="man")
    def test_correct_riddle_answer(self, _, __):
        player = {
            "progress": {},
            "next_task": "Goto the oracle to find the shift key"
        }
        tasks = iter(["Decrypt the message at the church"])

        handle_oracle_task(player, tasks)

        self.assertEqual(player["progress"]["cipher_shift"], 3)
        self.assertEqual(player["next_task"], "Decrypt the message at the church")

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="dog")
    def test_wrong_riddle_answer(self, _, __):
        player = {
            "progress": {},
            "next_task": "Solve the oracle's puzzle"
        }
        tasks = iter(["Next task placeholder"])

        handle_oracle_task(player, tasks)

        self.assertNotIn("cipher_shift", player["progress"])
        self.assertEqual(player["next_task"], "Solve the oracle's puzzle")  # unchanged

