# storage.py: reading and writing files. No budget rules here.
import json
from pathlib import Path


def load_transactions(path):
    file = Path(path)
    return json.loads(file.read_text()) if file.exists() else []


def save_transactions(path, transactions):
    Path(path).write_text(json.dumps(transactions))


def read_csv_rows(path):
    """Columns must be such that date,kind,category,amount,currency. The first line is the header."""
    lines = Path(path).read_text().splitlines()
    rows = []
    for line in lines[1:]:
        rows.append(line.split(","))
    return rows


def backup_file(source, destination):
    """Copy the source to the destination ("x" mode never overwrites). Returns True if the copy matches."""
    text = Path(source).read_text()
    with open(destination, "x") as output:
        output.write(text)
    return Path(destination).read_text() == text
