import unittest
from unittest.mock import patch
from level_three import handle_shrine_task


class TestHandleShrineTask(unittest.TestCase):

    @patch("level_three.update_display")
    @patch("level_three.time.sleep")
    @patch("level_three.input", return_value="1")
    def test_choice_1_pray(self, _, __, mock_display):
        player = {"progress": {}}
        tasks = iter([])

        handle_shrine_task(player, tasks)

        mock_display.assert_any_call(["✝️ You enter the quiet church.",
                                      "A priest approaches: 'How may I help you, child?'",
                                      "1. To pray",
                                      "2. To speak with the priest"])
        mock_display.assert_any_call([unittest.mock.ANY], save_text=True)

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="2")
    def test_choice_2_translation_flow(self, _, __):
        player = {
            "next_task": "Realize it was fake and seek the shrine",
            "progress": {"found_message": True, "scammed": True}
        }
        tasks = iter(["Decrypt the message at the church"])

        handle_shrine_task(player, tasks)

        self.assertTrue(player["progress"]["message_saved"])
        self.assertTrue(player["progress"]["translated_but_encrypted"])
        self.assertEqual(player["next_task"], "Decrypt the message at the church")

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="2")
    def test_choice_2_decryption_flow(self, _, __):
        player = {
            "next_task": "Decrypt the message at the church",
            "progress": {"cipher_shift": 3, "message_saved": True}
        }
        tasks = iter(["Locate the enemy king"])

        handle_shrine_task(player, tasks)

        self.assertTrue(player["progress"]["king_location_known"])
        self.assertEqual(player["next_task"], "Locate the enemy king")

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="2")
    def test_choice_2_but_not_ready(self, _, mock_display):
        player = {
            "next_task": "Realize it was fake and seek the shrine",
            "progress": {"found_message": False, "scammed": False}
        }
        tasks = iter(["Anything next"])

        handle_shrine_task(player, tasks)

        mock_display.assert_any_call(["'Come back when you're ready.'"], save_text=True)

    @patch("level_three.update_display")
    @patch("level_three.input", return_value="random")
    def test_invalid_choice(self, _, mock_display):
        player = {"progress": {}}
        tasks = iter([])

        handle_shrine_task(player, tasks)

        mock_display.assert_any_call(["You leave the church."], save_text=True)

