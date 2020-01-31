import unittest
from app.tip_calculator import bill_amount, tip_percentage


class Test_Tip_Calculations(unittest.TestCase):
    def test_bill_amount_in_float(self):
        self.assertEqual(type(bill_amount(10)), float)

    def test_tip_percentage_is_float(self):
        self.assertEqual(type(tip_percentage(10)), float)
