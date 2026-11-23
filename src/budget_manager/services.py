# services.py: budget rules only. No print, no input, no files.
from budget_manager.models import make_transaction
from budget_manager.validation import check_transaction


def next_id(transactions):
    number = len(transactions) + 1
    if number < 10:
        return "T00" + str(number)
    if number < 100:
        return "T0" + str(number)
    return "T" + str(number)


def add_transaction(transactions, date, kind, category, amount, currency):
    """Add transaction(s). Returns "" on success, or an error message."""
    error = check_transaction(date, kind, category, amount, currency)
    if error != "":
        return error
    tx = make_transaction(next_id(transactions), date, kind, category, float(amount), currency)
    transactions.append(tx)
    return ""


def summarize(transactions):
    """Income and expense totals per currency, e.g. {"EUR": {"income": 5, "expense": 2}}."""
    totals = {}
    for tx in transactions:
        if tx["currency"] not in totals:
            totals[tx["currency"]] = {"income": 0, "expense": 0}
        totals[tx["currency"]][tx["kind"]] += tx["amount"]
    return totals
