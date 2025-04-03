from unittest import TestCase
from player_manager import promote_player


class TestPromotePlayer(TestCase):
    def test_promote_from_pawn(self):
        player = {
            'piece': 'pawn',
            'position': [1, 1],
            'gold': 0,
            'knowledge': [],
            'completed_challenges': []
        }
        expected = {
            'piece': 'bishop',
            'position': [0, 0],
            'gold': 20,
            'knowledge': ['Master of Diagonal Warfare'],
            'completed_challenges': ['Level 1 Completed']
        }
        promote_player(player)
        self.assertEqual(player, expected)

    def test_promote_from_bishop(self):
        player = {
            'piece': 'bishop',
            'position': [2, 2],
            'gold': 10,
            'knowledge': ['Existing Skill'],
            'completed_challenges': ['Previous Challenge']
        }
        expected = {
            'piece': 'rook',
            'position': [2, 2],  # Position should remain unchanged
            'gold': 40,  # 10 + 30
            'knowledge': ['Existing Skill', 'Master of Straight-Line Power'],
            'completed_challenges': ['Previous Challenge', 'Level 2 Completed']
        }
        promote_player(player)
        self.assertEqual(player, expected)

    def test_promote_from_rook(self):
        player = {
            'piece': 'rook',
            'position': [3, 3],
            'gold': 20,
            'knowledge': ['Skill 1', 'Skill 2'],
            'completed_challenges': ['Challenge 1', 'Challenge 2']
        }
        expected = {
            'piece': 'overlord',
            'position': [3, 3],  # Position should remain unchanged
            'gold': 70,  # 20 + 50
            'knowledge': ['Skill 1', 'Skill 2', 'Overlord - Imposes dominance without being a King.'],
            'completed_challenges': ['Challenge 1', 'Challenge 2', 'Level 3 Completed']
        }
        promote_player(player)
        self.assertEqual(player, expected)

    def test_docstring_example(self):
        player = {
            'piece': 'pawn',
            'position': [2, 1],
            'gold': 0,
            'knowledge': [],
            'completed_challenges': []
        }
        expected = {
            'piece': 'bishop',
            'position': [0, 0],
            'gold': 20,
            'knowledge': ['Master of Diagonal Warfare'],
            'completed_challenges': ['Level 1 Completed']
        }
        promote_player(player)
        self.assertEqual(player, expected)