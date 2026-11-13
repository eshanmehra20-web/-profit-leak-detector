import math
import unittest
from engine import Sale, Expense, summarize, product_summary, validate_sale, validate_expense


class EngineTests(unittest.TestCase):
    def test_basic_profit(self):
        result = summarize([Sale("Pen", 10, 10, 4)], [Expense("Rent", 20)])
        self.assertEqual(result["revenue"], 100)
        self.assertEqual(result["cogs"], 40)
        self.assertEqual(result["net_profit"], 40)

    def test_product_loss_flag(self):
        row = product_summary([Sale("Item", 2, 5, 8)])[0]
        self.assertTrue(row["is_loss_making"])
        self.assertEqual(row["contribution_profit"], -6)

    def test_multiple_expenses(self):
        result = summarize([], [Expense("Rent", 100), Expense("Power", 25)])
        self.assertEqual(result["expenses"], 125)
        self.assertEqual(result["net_profit"], -125)

    def test_multiple_products(self):
        rows = product_summary([Sale("A", 1, 10, 3), Sale("B", 2, 5, 4)])
        self.assertEqual({r["product"] for r in rows}, {"A", "B"})

    def test_reject_negative_quantity(self):
        with self.assertRaises(ValueError):
            validate_sale(Sale("A", -1, 10, 5))

    def test_reject_negative_cost(self):
        with self.assertRaises(ValueError):
            validate_sale(Sale("A", 1, 10, -5))

    def test_reject_nan(self):
        with self.assertRaises(ValueError):
            validate_sale(Sale("A", math.nan, 10, 5))

    def test_reject_infinite_expense(self):
        with self.assertRaises(ValueError):
            validate_expense(Expense("Rent", math.inf))

    def test_reject_blank_product(self):
        with self.assertRaises(ValueError):
            validate_sale(Sale(" ", 1, 10, 5))

    def test_zero_sales(self):
        result = summarize([], [])
        self.assertEqual(result["net_profit"], 0)
        self.assertEqual(result["sales_count"], 0)


if __name__ == "__main__":
    unittest.main()
