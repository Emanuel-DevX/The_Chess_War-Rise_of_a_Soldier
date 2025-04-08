import unittest
from unittest.mock import patch

from level_three import handle_tasks


class TestHandleTasks(unittest.TestCase):

    @patch("level_three.handle_market_task")
    @patch("level_three.update_display")
    def test_dispatches_to_market(self, _, mock_market):
        player = {"position": (5, 5)}
        adal_places = {(5, 5): {"name": "adal market"}}
        tasks = iter(["next task"])
        handle_tasks(player, adal_places, tasks)
        mock_market.assert_called_once_with(player, tasks)

    @patch("level_three.handle_trap")
    @patch("level_three.update_display")
    def test_dispatches_to_trap(self, _, mock_trap):
        player = {"position": (6, 6)}
        adal_places = {(6, 6): {"name": "scorpion trap"}}
        tasks = iter([])
        handle_tasks(player, adal_places, tasks)
        mock_trap.assert_called_once_with(player)

    @patch("level_three.update_display")
    def test_fallback_for_unknown_location(self, mock_display):
        player = {"position": (1, 1)}
        adal_places = {(1, 1): {"name": "ancient stone"}}
        tasks = iter([])
        handle_tasks(player, adal_places, tasks)
        mock_display.assert_called_once_with(["You're at ancient stone. There's nothing story-related here yet."])
