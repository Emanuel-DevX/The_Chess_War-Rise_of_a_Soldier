import unittest
from unittest.mock import patch
from level_three import handle_message_task


class TestHandleMessageTask(unittest.TestCase):

    @patch("level_three.update_display")
    def test_message_discovery_and_task_progression(self, mock_display):
        player = {
            "progress": {},
            "next_task": "placeholder"
        }
        tasks = iter(["Go to the market to find a translator"])

        handle_message_task(player, tasks)

        self.assertTrue(player["progress"]["found_message"])
        self.assertEqual(player["next_task"], "Go to the market to find a translator")
        self.assertTrue(mock_display.called)
