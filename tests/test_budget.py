# Plain assert tests with explicit expected values.
# Run from the project folder:  python tests/test_budget.py
import sys

sys.path.insert(0, "src")

from budget_manager import services, storage


def test_normal_add_and_summary():
    transactions = []
    services.add_transaction(transactions, "2026-09-01", "income", "salary", "1800", "EUR")
    error = services.add_transaction(transactions, "2026-09-04", "expense", "food", "18.5", "EUR")
    assert error == ""
    assert transactions[1]["id"] == "T002"
    assert transactions[1]["amount"] == 18.5
    assert services.summarize(transactions) == {"EUR": {"income": 1800.0, "expense": 18.5}}


def test_boundary_bad_amounts():
    for bad in ["0", "-5", "abc"]:
        error = services.add_transaction([], "2026-09-04", "expense", "food", bad, "EUR")
        assert error == f"amount must be a number > 0, got '{bad}'."


def test_boundary_bad_category_and_date():
    error = services.add_transaction([], "2026-09-04", "expense", "gym", "5", "EUR")
    assert "category must be one of" in error
    error = services.add_transaction([], "04/09/2026", "expense", "food", "5", "EUR")
    assert error == "date must look like YYYY-MM-DD, got '04/09/2026'."


def test_save_and_load_round_trip():
    transactions = []
    services.add_transaction(transactions, "2026-09-04", "expense", "food", "18.5", "EUR")
    storage.save_transactions("test_round_trip.json", transactions)
    assert storage.load_transactions("test_round_trip.json") == transactions


test_normal_add_and_summary()
test_boundary_bad_amounts()
test_boundary_bad_category_and_date()
test_save_and_load_round_trip()
print("4 tests passed.")
