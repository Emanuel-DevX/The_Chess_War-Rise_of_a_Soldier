from unittest import TestCase
from unittest.mock import patch
from level_two import generate_clues


class TestGenerateClues(TestCase):
    @patch('random.randint')
    @patch('random.choice')
    @patch('random.shuffle')
    def test_generate_clues_structure(self, mock_shuffle, mock_choice, mock_randint):
        mock_randint.return_value = 2  # Spy will be "The Queen"
        mock_choice.side_effect = [
            "meeting with enemies",
            "Royal Chambers",
            "carrying secret messages",
            "Eastern Gardens",
            "avoiding certain areas"
        ]

        clues, spy = generate_clues()

        self.assertEqual(spy, "The Queen")
        self.assertEqual(len(clues), 7)  # 4 suspects + 3 general clues

        mock_shuffle.assert_called_once()

    def test_generate_clues_always_has_spy_clue(self):
        for _ in range(100):
            clues, spy = generate_clues()

            # Verify at least one genuine clue references the actual spy
            spy_clues = [
                clue for clue, is_genuine in clues
                if is_genuine and spy in clue
            ]
            self.assertGreaterEqual(len(spy_clues), 1)