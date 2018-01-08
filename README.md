# risk-sim - Risk Combat Simulator

This python program is a combat simulator for the famous `Risk` strategy board game.

The idea was born during an exciting game of `Risk: Halo Legendary Edition` with my family and friends.
Back then I was curious about the odds when attacking an enemy army, which inspired my to write this little program to perform some hacker statistics in the `Risk` campaign setting.

I will not take a deeper look at the rules - so if you are interested do it yourself:
[https://www.wikihow.com/Play-Risk](https://www.wikihow.com/Play-Risk)

The `Risk: Halo Legendary Edition` introduced so called leaders (generals), which grants units in the same territory a +1 to the value of their rolled dices.

Besides implementing some hacker statistics about `Risk` I also pursued the following goals:

* Use `attrs` to model my container classes
* Use `docopt` for parsing console arguments
* Use `schema` for adapting additional validation

## Installation

Cause I will not publish this repo via pypi you have to install it manually without pip support

    # Clone this repo
    https://github.com/HazardDede/risk-sim.git && cd risk-sim

    # Make a python3 virtualenv
    virtualenv -p python3 venv && source venv/bin/activate

    # Install the dependencies
    pip install -r requirements.txt

    # Run the test to see if everything worked fine
    pytest

## Running the simulator

    $ python risk_sim.py -h
    Risk Simulator.

    Usage:
      risk_sim.py <attacker> <defender> [-i <iter>] [--attacking-general] [--defending-general]
      risk_sim.py (-h | --help)
      risk_sim.py --version

    Arguments:
      attacker      Number of attacking units (> 1)
      defender      Number of defending units (> 0)

    Options:
      -h --help                      Show this screen.
      --version                      Show version.
      -i <iter> --iterations=<iter>  Number of iterations to simulate [default: 1000].
      --attacking-general            Enables the general when attacking (+1 to all pips) [default: False]
      --defending-general            Enables the general when defending (+1 to all pips) [default: False]

Following these help page you have to

    python risk-sim.py 100 50 --defending-general --iterations=1000

to simulate a battle between 100 attacking and 50 defending units, while the defending army is lead by a general (+1 to all rolled dice values).
The same battle between those units will be repeated and recorded for a 1.000 times, leading to a summary statistic like below:

    ╔Success Rate: 63.8 %════╦═════════╦════════╦═════════╗
    ║ Metric       ║ avg     ║ median  ║ min    ║ max     ║
    ╠══════════════╬═════════╬═════════╬════════╬═════════╣
    ║ Attacks      ║ 68.174  ║ 69.0    ║ 49     ║ 77      ║
    ║ Attacker     ║ --      ║ --      ║ --     ║ --      ║
    ║ Casualties   ║ 87.872  ║ 92.0    ║ 45     ║ 99      ║
    ║ Casualties % ║ 87.87 % ║ 92.0 %  ║ 45.0 % ║ 99.0 %  ║
    ║ Survivor     ║ 12.128  ║ 8.0     ║ 1      ║ 55      ║
    ║ Defender     ║ --      ║ --      ║ --     ║ --      ║
    ║ Casualties   ║ 47.308  ║ 50.0    ║ 25     ║ 50      ║
    ║ Casualties % ║ 94.62 % ║ 100.0 % ║ 50.0 % ║ 100.0 % ║
    ║ Survivor     ║ 2.692   ║ 0.0     ║ 0      ║ 25      ║
    ╚══════════════╩═════════╩═════════╩════════╩═════════╝

Cause the odds are highest when rolling three (attacker) or two (defender) dices the algorithm will always (if possible) maximize the number of rolled dices.
