import attr


@attr.s
class Stats(object):
    minimum = attr.ib(validator=attr.validators.instance_of((int, float)))
    maximum = attr.ib(validator=attr.validators.instance_of((int, float)))
    average = attr.ib(validator=attr.validators.instance_of((int, float)))
    median = attr.ib(validator=attr.validators.instance_of((int, float)))

    selector = {
        'avg': lambda x: x.average,
        'median': lambda x: x.median,
        'min': lambda x: x.minimum,
        'max': lambda x: x.maximum,
    }


@attr.s
class Army(object):
    units = attr.ib(validator=attr.validators.instance_of(int))
    dices = attr.ib(validator=attr.validators.instance_of(int))
    lead_by_general = attr.ib(validator=attr.validators.instance_of(bool))


@attr.s
class Casualties(object):
    units = attr.ib(validator=attr.validators.instance_of((int, Stats)))
    ratio = attr.ib(validator=attr.validators.instance_of((float, Stats)))
    survivors = attr.ib(validator=attr.validators.instance_of((int, Stats)))


@attr.s
class Combat(object):
    victorious = attr.ib(validator=attr.validators.instance_of((bool, Stats)))
    attack_runs = attr.ib(validator=attr.validators.instance_of((int, Stats)))
    attacker_casualties = attr.ib(validator=attr.validators.instance_of((Casualties, Stats)))
    defender_casualties = attr.ib(validator=attr.validators.instance_of((Casualties, Stats)))


@attr.s
class Context(object):
    iterations = attr.ib(validator=attr.validators.instance_of(int))
    attacker = attr.ib(validator=attr.validators.instance_of(Army))
    defender = attr.ib(validator=attr.validators.instance_of(Army))
