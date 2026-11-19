import math
import unittest
from engine import (
    Sale, Expense, summarize, product_summary, validate_sale,
    validate_expense, break_even_estimate,
)


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

    def test_reject_zero_quantity(self):
        with self.assertRaises(ValueError):
            validate_sale(Sale("A", 0, 10, 5))

    def test_reject_blank_expense_name(self):
        with self.assertRaises(ValueError):
            validate_expense(Expense("  ", 10))

    def test_reject_negative_expense(self):
        with self.assertRaises(ValueError):
            validate_expense(Expense("Rent", -0.01))

    def test_reject_infinite_sale_price(self):
        with self.assertRaises(ValueError):
            validate_sale(Sale("A", 1, math.inf, 5))

    def test_product_aggregation_same_name(self):
        rows = product_summary([Sale("Tea", 2, 10, 4), Sale("Tea", 3, 12, 5)])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["quantity"], 5)
        self.assertEqual(rows[0]["revenue"], 56)
        self.assertEqual(rows[0]["cogs"], 23)

    def test_break_even_revenue(self):
        result = break_even_estimate([Sale("A", 10, 10, 4)], [Expense("Rent", 120)])
        self.assertEqual(result["break_even_revenue"], 200)
        self.assertEqual(result["additional_revenue_needed"], 100)
        self.assertFalse(result["is_at_or_above_break_even"])

    def test_break_even_already_reached(self):
        result = break_even_estimate([Sale("A", 10, 10, 4)], [Expense("Rent", 30)])
        self.assertEqual(result["additional_revenue_needed"], 0)
        self.assertTrue(result["is_at_or_above_break_even"])

    def test_break_even_not_calculable_without_positive_margin(self):
        result = break_even_estimate([Sale("A", 1, 5, 6)], [Expense("Rent", 10)])
        self.assertIsNone(result["break_even_revenue"])
        self.assertIsNone(result["additional_revenue_needed"])

    def test_break_even_zero_expenses(self):
        result = break_even_estimate([], [])
        self.assertEqual(result["break_even_revenue"], 0)
        self.assertTrue(result["is_at_or_above_break_even"])


if __name__ == "__main__":
    unittest.main()
