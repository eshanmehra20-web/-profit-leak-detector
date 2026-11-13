from dataclasses import dataclass
from math import isfinite
from typing import Iterable


@dataclass(frozen=True)
class Sale:
    product: str
    quantity: float
    unit_price: float
    unit_cost: float


@dataclass(frozen=True)
class Expense:
    name: str
    amount: float


def _number(value: float, field: str, *, allow_zero: bool = True) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{field} must be a number")
    if not isfinite(number):
        raise ValueError(f"{field} must be finite")
    if number < 0 or (not allow_zero and number == 0):
        raise ValueError(f"{field} must be {'greater than zero' if not allow_zero else 'zero or greater'}")
    return number


def validate_sale(sale: Sale) -> Sale:
    product = str(sale.product).strip()
    if not product:
        raise ValueError("product is required")
    quantity = _number(sale.quantity, "quantity", allow_zero=False)
    unit_price = _number(sale.unit_price, "unit_price")
    unit_cost = _number(sale.unit_cost, "unit_cost")
    return Sale(product, quantity, unit_price, unit_cost)


def validate_expense(expense: Expense) -> Expense:
    name = str(expense.name).strip()
    if not name:
        raise ValueError("expense name is required")
    amount = _number(expense.amount, "amount")
    return Expense(name, amount)


def summarize(sales: Iterable[Sale], expenses: Iterable[Expense]) -> dict:
    valid_sales = [validate_sale(s) for s in sales]
    valid_expenses = [validate_expense(e) for e in expenses]
    revenue = sum(s.quantity * s.unit_price for s in valid_sales)
    cogs = sum(s.quantity * s.unit_cost for s in valid_sales)
    operating_expenses = sum(e.amount for e in valid_expenses)
    gross_profit = revenue - cogs
    return {
        "revenue": round(revenue, 2),
        "cogs": round(cogs, 2),
        "gross_profit": round(gross_profit, 2),
        "expenses": round(operating_expenses, 2),
        "net_profit": round(gross_profit - operating_expenses, 2),
        "sales_count": len(valid_sales),
        "expense_count": len(valid_expenses),
    }


def product_summary(sales: Iterable[Sale]) -> list[dict]:
    totals = {}
    for raw in sales:
        sale = validate_sale(raw)
        row = totals.setdefault(sale.product, {"product": sale.product, "quantity": 0.0, "revenue": 0.0, "cogs": 0.0})
        row["quantity"] += sale.quantity
        row["revenue"] += sale.quantity * sale.unit_price
        row["cogs"] += sale.quantity * sale.unit_cost
    result = []
    for row in totals.values():
        profit = row["revenue"] - row["cogs"]
        result.append({
            "product": row["product"],
            "quantity": round(row["quantity"], 2),
            "revenue": round(row["revenue"], 2),
            "cogs": round(row["cogs"], 2),
            "contribution_profit": round(profit, 2),
            "is_loss_making": profit < 0,
        })
    return sorted(result, key=lambda item: item["contribution_profit"])
