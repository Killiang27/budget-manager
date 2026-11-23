# validation.py: boundary checks. Returns an error message, or "" if all is valid.
from budget_manager.models import CATEGORIES, CURRENCIES, KINDS


def check_transaction(date, kind, category, amount, currency):
    # amount arrives as text. Check it is a number before converting it.
    amount_parts = amount.split(".")  # "18.5" -> ["18", "5"]
    if len(amount_parts) > 2 or not amount_parts[0].isdigit() or not amount_parts[-1].isdigit() or float(amount) <= 0:
        return f"the amount must be a number > 0, got '{amount}'."
    # A valid date has dashes at positions 4 and 7, and digits everywhere else.
    if len(date) != 10 or date[4] != "-" or date[7] != "-":
        return f"the date must look like format YYYY-MM-DD, got '{date}'."
    if not date[:4].isdigit() or not date[5:7].isdigit() or not date[8:].isdigit():
        return f"the date must look like format YYYY-MM-DD, got '{date}'."
    if kind not in KINDS:
        return f"the kind must be one of {KINDS}, got '{kind}'."
    if category not in CATEGORIES:
        return f"the category must be one of the {CATEGORIES}, got '{category}'."
    if currency not in CURRENCIES:
        return f"the currency must be one of the {CURRENCIES}, got '{currency}'."
    return ""
