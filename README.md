# Budget Manager (Release 1)

A small command-line tool to add, list, summarise, import and back up personal budget transactions. Built for Python I (Practice 1: Interactive Personal Budget Manager), using the techniques from the course slides (Sessions 07 and 10).

## Setup
Python 3 only. No packages to install.

```
git clone <this repository>
cd budget-manager
```

## Run
Go into the `src` folder, then run the commands below. Data is saved in `transactions.json` in the folder you run from.

```
cd src
python -m budget_manager --help
python -m budget_manager add 18.5 --date 2026-09-04 --category food
python -m budget_manager add 1800 --date 2026-09-01 --kind income --category salary
python -m budget_manager list
python -m budget_manager summary
python -m budget_manager import ../data/sample_transactions.csv
python -m budget_manager backup backup-20260904.json
```

## Example
```
$ python -m budget_manager import ../data/sample_transactions.csv
Row 5: amount must be a number > 0, got '-5.00'.
Row 6: category must be one of ('food', 'rent', ...), got 'gym'.
Row 8: amount must be a number > 0, got 'abc'.
Row 9: date must look like YYYY-MM-DD, got '04/09/2026'.
Imported 5 transactions, rejected 4.

$ python -m budget_manager summary
Total entries: 5
EUR: income 1800.00, expense 680.90, net 1119.10
USD: income 0.00, expense 40.00, net -40.00
```
Note: the sample file has 4 deliberately invalid rows, so the import exits with code 1.

## Test
From the project folder (not `src`):
```
python tests/test_budget.py
```
Expected output: `4 tests passed.` (one normal case, bad amounts, bad category and date, save and load round trip).

## Exit codes
- 0: success
- 1: some CSV rows were rejected, or the backup did not match
- 2: invalid input to `add`

Errors are printed to stderr, normal output to stdout. Other problems (an unreadable data file, a backup name that already exists) stop the program with Python's own error message, like the starter cli.py.

## Scheduling a backup (draft, not installed)
A scheduler must give each backup a new dated name (backups never overwrite). Example entry, with absolute paths and the virtual-environment interpreter:
```
/project/.venv/bin/python -m budget_manager --data /project/src/transactions.json backup /project/backups/data-YYYYMMDD.json
```
Failure checklist: no retry (a second run with the same name fails and overwrites nothing); no lock file; the exit code and the log line are the alert signal.

## Known limitations
- No undo (stretch challenge not attempted).
- The CSV columns must be in this order: date,kind,category,amount,currency, with no commas inside values.
- Dates are checked for the YYYY-MM-DD shape only, not for real calendar dates.
- Backup file names are typed by the user (no automatic timestamp).
- Currencies are totalled separately and never converted.

## Files
`DESIGN.md` explains one design choice. `AI_DISCLOSURE.md` explains AI use.
