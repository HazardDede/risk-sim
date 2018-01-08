import random

from sim.simulator import roll_dice, fight


def test_roll_dice():
    random.seed(42)

    assert roll_dice(1) == [6]
    assert roll_dice(3) == [6, 1, 1]

    random.seed(42)
    assert roll_dice(3, 1) == [7, 2, 2]


def test_fight():
    assert fight([6, 1, 1], [1, 1]) == (1, 1)
    assert fight([1, 1], [1, 1]) == (2, 0)
    assert fight([6, 6], [1, 1]) == (0, 2)
