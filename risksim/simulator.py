import random

from .model import Combat, Casualties

DICE_MIN = 1
DICE_MAX = 6

random.seed()


def roll_dice(n=1, offset=0):
    rolls = [random.randint(DICE_MIN, DICE_MAX) + offset for _ in range(n)]
    rolls.sort(reverse=True)
    return rolls


def fight(attack_rolls, defend_rolls):
    relevant_dices = min(len(attack_rolls), len(defend_rolls))
    cmp = zip(attack_rolls, defend_rolls)
    loses = sum([a > d for a, d in cmp])
    return relevant_dices - loses, loses


def combat(attacker, defender):
    current_attack_units = attacker.units
    current_defend_units = defender.units

    runs = 0
    while True:
        max_attack_dices = min(current_attack_units - 1, attacker.dices)
        max_defend_dices = min(current_defend_units, defender.dices)
        if max_attack_dices <= 0 or max_defend_dices <= 0:
            break;

        runs += 1
        attack_rolls = roll_dice(max_attack_dices, int(attacker.lead_by_general))
        defend_rolls = roll_dice(max_defend_dices, int(defender.lead_by_general))
        l1, l2 = fight(attack_rolls, defend_rolls)
        current_attack_units -= l1
        current_defend_units -= l2

    return Combat(
        victorious=current_defend_units <= 0,
        attack_runs=runs,
        attacker_casualties=Casualties(
            units=attacker.units - current_attack_units,
            ratio=(attacker.units - current_attack_units) / attacker.units,
            survivors=current_attack_units
        ),
        defender_casualties=Casualties(
            units=defender.units - current_defend_units,
            ratio=(defender.units - current_defend_units) / defender.units,
            survivors=current_defend_units
        )
    )


def simulate(attacker, defender, iterations=1000):
    return [combat(attacker, defender) for _ in range(iterations)]
