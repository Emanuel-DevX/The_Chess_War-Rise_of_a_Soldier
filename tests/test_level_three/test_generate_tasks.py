import unittest
from level_three import generate_tasks


class TestGenerateTasks(unittest.TestCase):

    def test_task_sequence(self):
        expected = [
            "Find the hidden message",
            "Go to the market to find a translator",
            "Realize it was fake and seek the shrine",
            "Goto the oracle to find the shift key",
            "Decrypt the message at the church",
            "Locate the enemy king",
            "Lead the final strike️"
        ]

        task_gen = generate_tasks()
        for expected_task in expected:
            self.assertEqual(next(task_gen), expected_task)

        with self.assertRaises(StopIteration):
            next(task_gen)  # Make sure generator is exhausted after 7 yields
