import unittest
from level_one import assign_position_attributes


class TestAssignPositionAttributes(unittest.TestCase):

    def test_safe_zone_col_4(self):
        actual = assign_position_attributes(4)
        expected = ("Safe Zone", 5, 10)
        self.assertEqual(actual, expected)

    def test_safe_zone_col_11(self):
        actual = assign_position_attributes(11)
        expected = ("Safe Zone", 5, 10)
        self.assertEqual(actual, expected)

    def test_moderate_risk_col_5(self):
        actual = assign_position_attributes(5)
        expected = ("Moderate Risk", 10, 5)
        self.assertEqual(actual, expected)

    def test_moderate_risk_col_10(self):
        actual = assign_position_attributes(10)
        expected = ("Moderate Risk", 10, 5)
        self.assertEqual(actual, expected)

    def test_risky_col_6(self):
        actual = assign_position_attributes(6)
        expected = ("Risky", 15, 0)
        self.assertEqual(actual, expected)

    def test_risky_col_9(self):
        actual = assign_position_attributes(9)
        expected = ("Risky", 15, 0)
        self.assertEqual(actual, expected)

    def test_high_risk_col_3(self):
        actual = assign_position_attributes(3)
        expected = ("High Risk", 20, -5)
        self.assertEqual(actual, expected)

    def test_high_risk_col_7(self):
        actual = assign_position_attributes(7)
        expected = ("High Risk", 20, -5)
        self.assertEqual(actual, expected)
