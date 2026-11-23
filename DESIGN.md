# Design

I split the project into layers so each file has one job. `cli.py` talks to the user, `services.py` holds budget rules, `storage.py` reads and writes files, and `validation.py` checks input where it enters the `add` command and the CSV import. Since `services.py` never prints anything or asks for input or touches files, I can test the rules directly with simple `assert` statements. The trade-off that had to be accepted is more files and passing the list of transactions between layers in exchange for the code that can be tested one part at a time. 
