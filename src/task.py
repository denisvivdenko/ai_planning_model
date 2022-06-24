from typing import Callable


class Task:
    def __init__(self, domain_functions: list, domain_objects: list, domain_goal: Callable) -> None:
        self.domain_functions = domain_functions
        self.domain_objects = [domain_objects]
        self.domain_goal = domain_goal


def unique_id(cls):
    class Wrapper:
        def __init__(self, x):
            self.wrap = cls(x)
            self.id = id(cls)

        def get_name(self):
            return self.wrap.name
                      
    return Wrapper