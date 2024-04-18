from typing import TypeVar, Callable


Type = TypeVar


class BasicTypesSystem:
    def __init__(self, types: set[Type], a: Callable[[Type], set]) -> None:
        self.types = frozenset(types)
        self.a = a

    def check(self, obj, type_):
        return obj in self.a(type_)
