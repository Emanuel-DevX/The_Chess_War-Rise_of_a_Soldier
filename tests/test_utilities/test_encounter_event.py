from unittest import TestCase
from unittest.mock import patch
from utilities import encounter_event


class TestEncounterEvent(TestCase):

    @patch('random.choice')
    def test_movement_points_event(self, mock_choice):
        mock_choice.return_value = "You found a hidden passage! +5 movement points."
        player = {"movement_points": 10}

        result = encounter_event(player)

        self.assertEqual(result, "You found a hidden passage! +5 movement points.")
        self.assertEqual(player["movement_points"], 15)

    @patch('random.choice')
    def test_regular_event(self, mock_choice):
        mock_choice.return_value = "The path ahead looks clear."
        player = {"movement_points": 10}

        result = encounter_event(player)

        self.assertEqual(result, "The path ahead looks clear.")
        self.assertEqual(player["movement_points"], 10)  # Unchanged

    def test_all_possible_events(self):
        player = {}
        possible_events = {
            "You found a hidden passage! +5 movement points.",
            "You sense a trap nearby. Proceed with caution.",
            "You spot enemy movement in the distance.",
            "You find signs of recent activity.",
            "The path ahead looks clear."
        }

        for _ in range(20):
            event = encounter_event(player)
            self.assertIn(event, possible_events)


