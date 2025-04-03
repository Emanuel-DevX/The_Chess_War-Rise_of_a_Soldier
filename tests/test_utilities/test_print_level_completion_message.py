from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from utilities import print_level_completion_message


class TestPrintLevelCompletionMessage(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_level_1_message(self, mock_stdout):
        print_level_completion_message(1)
        expected = ("🎉 Congratulations! You have completed Level 1! Your journey as a Bishop begins."
                    "🔱 Your pawn has been promoted to a Bishop!\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_level_2_message(self, mock_stdout):
        print_level_completion_message(2)
        expected = ("🎉 Well done! Level 2 completed! The power of the Rook is now yours."
                    "🏰 Your Bishop has been promoted to a Rook!\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_level_3_message(self, mock_stdout):
        print_level_completion_message(3)
        expected = ("👑 Magnificent! You have reached the pinnacle as an Overlord! Rule wisely."
                    "👑 The Rook, now Overlord, enforces its rule from the Obsidian Tower!\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_default_message(self, mock_stdout):
        print_level_completion_message(99)  # Invalid level
        expected = "🎉 Congratulations on your achievement!\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
