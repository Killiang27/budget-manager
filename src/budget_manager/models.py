# models.py: the transaction schema. Every transaction is a dict with these six keys.

KINDS = ("expense", "income")
CATEGORIES = ("food", "rent", "transport", "leisure", "health", "salary", "other")
CURRENCIES = ("EUR", "USD", "GBP")


def make_transaction(tx_id, date, kind, category, amount, currency):
    return {
        "id": tx_id,
        "date": date,
        "kind": kind,
        "category": category,
        "amount": amount,
        "currency": currency,
    }
