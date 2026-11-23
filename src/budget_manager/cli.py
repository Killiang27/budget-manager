# cli.py: command-line interaction only. Data goes to stdout, errors to stderr.
import argparse
import logging
import sys

from budget_manager import services, storage


def main():
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(prog="budget_manager")
    parser.add_argument("--data", default="transactions.json", help="JSON file that stores the transactions")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="add one transaction")
    add.add_argument("amount", help="number greater than 0, e.g. 18.5")
    add.add_argument("--date", required=True, help="YYYY-MM-DD")
    add.add_argument("--kind", default="expense", help="expense or income")
    add.add_argument("--category", required=True, help="e.g. food, rent, salary")
    add.add_argument("--currency", default="EUR", help="EUR, USD or GBP")

    commands.add_parser("list", help="list all transactions")
    commands.add_parser("summary", help="income, expense and net per currency")

    import_csv = commands.add_parser("import", help="import transactions from a CSV file")
    import_csv.add_argument("csv_file")

    backup = commands.add_parser("backup", help="copy the data file to a new file")
    backup.add_argument("destination")

    args = parser.parse_args()
    transactions = storage.load_transactions(args.data)

    if args.command == "add":
        error = services.add_transaction(
            transactions, args.date, args.kind, args.category, args.amount, args.currency
        )
        if error != "":
            print("error: " + error, file=sys.stderr)
            sys.exit(2)
        storage.save_transactions(args.data, transactions)
        tx = transactions[-1]
        print(f"Added {tx['id']}: {tx['kind']} {tx['amount']:.2f} {tx['currency']} ({tx['category']})")

    elif args.command == "list":
        for tx in transactions:
            print(f"{tx['id']} {tx['date']} {tx['kind']} {tx['category']} {tx['amount']:.2f} {tx['currency']}")

    elif args.command == "summary":
        print(f"Total entries: {len(transactions)}")
        totals = services.summarize(transactions)
        for currency in totals:
            income = totals[currency]["income"]
            expense = totals[currency]["expense"]
            print(f"{currency}: income {income:.2f}, expense {expense:.2f}, net {income - expense:.2f}")

    elif args.command == "import":
        added = 0
        rejected = 0
        row_number = 2  # line 1 of the file is the header
        for row in storage.read_csv_rows(args.csv_file):
            error = services.add_transaction(transactions, row[0], row[1], row[2], row[3], row[4])
            if error == "":
                added += 1
            else:
                rejected += 1
                print(f"Row {row_number}: {error}", file=sys.stderr)
            row_number += 1
        storage.save_transactions(args.data, transactions)
        print(f"Imported {added} transactions, rejected {rejected}.")
        logging.info("import_complete added=%s rejected=%s", added, rejected)
        if rejected > 0:
            sys.exit(1)

    elif args.command == "backup":
        if not storage.backup_file(args.data, args.destination):
            print("error: backup does not match the original.", file=sys.stderr)
            sys.exit(1)
        print(f"Backup written to {args.destination} and verified.")
        logging.info("backup_complete destination=%s", args.destination)
