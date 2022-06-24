from dataclasses import dataclass

from task import Task


@dataclass
class Bottle:
    volume: int
    fill: int


def fill_in(bottle: Bottle) -> None:
    bottle.fill += bottle.volume
    assert bottle.fill == bottle.volume


def pour_out(bottle_1: Bottle, bottle_2: Bottle) -> None:
    assert bottle_1 != bottle_2
    can_fit = bottle_2.volume - bottle_2.fill
    sf = bottle_1.fill
    bf = bottle_2.fill
    if bottle_1.fill <= can_fit:
        bottle_2.fill += bottle_1.fill
        bottle_1.fill = 0
        assert bottle_1.fill == 0
        assert bottle_2.fill == bf + sf
    else:
        bottle_2.fill += can_fit
        bottle_1.fill -= can_fit
        assert bottle_2.fill == bottle_2.volume
        assert bottle_1.fill == sf - can_fit


def empty(bottle):
    bottle.fill = 0
    assert bottle.fill == 0


bottle_1 = Bottle(3)
bottle_2 = Bottle(5)

def goal():
    assert bottle_2.fill == 4
    print("Goal found")

domain_actions = [fill_in, pour_out, empty]
domain_objects = [bottle_1, bottle_2]
domain_goal = goal

domain = Task(domain_actions, domain_objects, domain_goal)