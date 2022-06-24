import numpy as np
from copy import deepcopy
from inspect import signature

from task import Task


def solve_attempt(task: Task, max_plan_length: int = 250) -> list:
    actions = task.domain_functions
    objects = deepcopy(task.domain_objects)
    goal = task.domain_goal
    plan = []
    while len(plan) < max_plan_length:
        try:
            current_action = np.random.choice(actions)
            arguments_count = len(signature(current_action).parameters)
            arguments = np.random.choice(objects, size=arguments_count)
            current_action(arguments)
            plan.append((current_action, [argument if isinstance(argument, (str, int, float, bool)) else argument.id for argument in arguments]))
            goal()
        except:
            break
    return plan
        
            

