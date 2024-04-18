from typing import TypeVar, Callable, Sequence


Type = TypeVar
Predicate = TypeVar


class BasicTypesSystem:
    """Corresponds to Cooper (2023), A2.1"""
    def __init__(
            self,
            types: set[Type],
            a: Callable[[Type], set]
    ) -> None:
        self.types = frozenset(types)
        self.a = a

    def check(self, obj, type_):
        return obj in self.a(type_)


class PredicateSignature:
    """Corresponds to Cooper (2023), A3.1 (monophonic variant)"""
    def __init__(
            self,
            predicates: set[Predicate],
            arg_indices: set[Type],
            arity: Callable[[Type], Sequence[Type]]
    ) -> None:
        self.predicates = predicates
        self.arg_indices = arg_indices
        self.arity = arity


PType = dict  # See ComplexTypesSystem.create_ptype


class ComplexTypesSystem:
    """Corresponds to Cooper (2023), A3.1"""
    def __init__(
            self,
            basic_types_system: BasicTypesSystem,
            predicate_signature: PredicateSignature,
            f: Callable[[PType], set]
    ) -> None:
        self.basic_types_system = basic_types_system
        self.predicate_signature = predicate_signature
        self.f = f

    def create_ptype(self, predicate: Predicate, arguments: Sequence) -> PType:
        """Roughly corresponding to Cooper (2023, p.401), where P(a_1, ..., a_n) is represented as a labelled set,
        it is here represented as a dict with keys 'pred' and non-negative integers for arguments."""
        result = {'pred': predicate}
        for n, argument in enumerate(arguments):
            result[n] = argument
        return result
