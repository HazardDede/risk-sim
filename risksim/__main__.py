"""Risk Simulator.

Usage:
  risksim <attacker> <defender> [-i <iter>] [--attacking-general] [--defending-general]
  risksim (-h | --help)
  risksim --version

Arguments:
  attacker      Number of attacking units (> 1)
  defender      Number of defending units (> 0)

Options:
  -h --help                      Show this screen.
  --version                      Show version.
  -i <iter> --iterations=<iter>  Number of iterations to simulate [default: 1000].
  --attacking-general            Enables the general when attacking (+1 to all pips) [default: False]
  --defending-general            Enables the general when defending (+1 to all pips) [default: False]
"""

from docopt import docopt
from schema import Schema, And, Use, SchemaError

from .model import Army, Context
from .simulator import simulate
from .stats import make_simulation_summary, terminal_result

validation_schema = Schema({
    '<attacker>': And(Use(int), lambda n: n > 1),
    '<defender>': And(Use(int), lambda n: n > 0),
    '--iterations': And(Use(int), lambda n: 1 <= n <= 100000),
    '--attacking-general': bool,
    '--defending-general': bool,
    '--help': bool,
    '--version': bool
})


def parse_args():
    args = docopt(__doc__, version='Risk Simulator 1.0')
    try:
        args = validation_schema.validate(args)
    except SchemaError as e:
        exit(e)

    return Context(
        iterations=args['--iterations'],
        attacker=Army(
            units=args['<attacker>'],
            dices=3,
            lead_by_general=args['--attacking-general']
        ),
        defender=Army(
            units=args['<defender>'],
            dices=2,
            lead_by_general=args['--defending-general']
        )
    )


def simulate_and_print(ctx):
    sim = simulate(ctx.attacker, ctx.defender, ctx.iterations)
    summary = make_simulation_summary(sim)
    print(terminal_result(summary))


if __name__ == '__main__':
    ctx = parse_args()
    simulate_and_print(ctx)
