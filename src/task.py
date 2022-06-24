from typing import Callable


class Task:
    def __init__(self, domain_functions: list, domain_objects: list, domain_goal: Callable) -> None:
        self.domain_functions = domain_functions
        self.domain_objects = domain_objects
        self.domain_goal = domain_goal