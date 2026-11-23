# AI disclosure

**Tool used:** Claude (Anthropic)

**What the AI did:** It wrote the first draft of this README, structure and this file. The `cli.py` in `src/budget_manager/` is an extended and restructured version of the starter from blackboard. The AI also ran the tests and example commands to check they work. It also trouble-shooted some functions since the code didn't run a couple of times. 

**Why I used it:** To get a working and well-structured first look and working code and to see the layered design to match my original structure vision. I also wanted a legible structure to make the structure look clean and neat so the AI cleaned it up to look more organised

**What I did myself:** Coded the general structure and functions with some mistakes, read and triple checked each file, ran the tests, edited the design/readme rationale in my own words, tried my own inputs as well. Edited functions and code. 

**Troubleshooting:** While building, the AI's tests found a mistake in count of valid CSV rows, which was fixed after counting the sample rows by hand. It troubleshooted most of the code through thorough testing after much coding. 

**Beyond the slides:** A few things are not shown in the slides: the number-formatting in f-strings (`:.2f`) but is necessary for money, two basic string tools (`split` for date formatting and `isdigit`).
