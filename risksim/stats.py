from statistics import median

from terminaltables import DoubleTable

from .model import Stats, Combat, Casualties


def make_simulation_summary(simulation):
    def project(fun, iterable=None):
        if iterable is None:
            iterable = simulation
        return [fun(x) for x in iterable]

    def metric(fun, iterable=None):
        def m(values):
            return Stats(
                minimum=min(values),
                maximum=max(values),
                average=sum(values) / len(values),
                median=median(values)
            )
        return m(project(fun, iterable))

    def make_casualties_summary(casualties):
        return Casualties(
            units=metric(lambda c: c.units, casualties),
            ratio=metric(lambda c: c.ratio, casualties),
            survivors=metric(lambda c: c.survivors, casualties)
        )

    return Combat(
        victorious=metric(lambda sim: sim.victorious),
        attack_runs=metric(lambda sim: sim.attack_runs),
        attacker_casualties=make_casualties_summary(project(lambda sim: sim.attacker_casualties)),
        defender_casualties=make_casualties_summary(project(lambda sim: sim.defender_casualties)),
    )


def terminal_result(summary):
    def ident(value):
        return str(value)

    def pct_format(value):
        return str(round(value * 100, 2)) + ' %'

    projections = [
        ('Attacks', lambda s: s.attack_runs, ident),
        ('Attacker', None, ident),
        ('Casualties', lambda s: s.attacker_casualties.units, ident),
        ('Casualties %', lambda s: s.attacker_casualties.ratio, pct_format),
        ('Survivors', lambda s: s.attacker_casualties.survivors, ident),
        ('Defender', None, ident),
        ('Casualties', lambda s: s.defender_casualties.units, ident),
        ('Casualties %', lambda s: s.defender_casualties.ratio, pct_format),
        ('Survivors', lambda s: s.defender_casualties.survivors, ident),
    ]
    table_data = [
        ['Metric'] + [x for x in Stats.selector]
    ]
    for name, p, f in projections:
        table_data.append([name] + [f(m(p(summary))) if p is not None else '--' for m in Stats.selector.values()])

    return DoubleTable(table_data, 'Success Rate: {} %'.format(round(summary.victorious.average * 100, 2))).table
