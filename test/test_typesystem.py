from typesystem import Type, BasicTypesSystem, Predicate, PredicateSignature, ComplexTypesSystem


class TestBasicTypesSystem:
    def test_check(self):
        dog = Type('dog')
        sally = object()
        sam = object()

        def extension_function(x):
            if x == dog:
                return {sally}
            return {}

        system = BasicTypesSystem({dog}, extension_function)
        assert system.check(sally, dog)
        assert not system.check(sam, dog)


class TestComplexTypesSystem:
    def test_create_ptype(self):
        """Corresponds to Cooper (2023, p.16)"""
        ind = Type('ind')

        def extension_function(x):
            return {}

        basic_types_system = BasicTypesSystem({ind}, extension_function)
        boy = Predicate('boy')
        dog = Predicate('dog')
        hug = Predicate('hug')

        def arity(x):
            if x in [boy, dog]:
                return (ind,)
            elif x == hug:
                return (ind, ind)

        predicate_signature = PredicateSignature(predicates={boy, dog, hug}, arg_indices={ind}, arity=arity)
        system = ComplexTypesSystem(basic_types_system, predicate_signature, extension_function)
        assert system.create_ptype(hug, (boy, dog)) == LabelledSet({'pred': hug, 0: boy, 1: dog})

    def test_create_rectype(self):
        """Corresponds to listing 22a in Cooper (2023, p.24)"""
        ind = Type('ind')

        def extension_function(x):
            return {}

        basic_types_system = BasicTypesSystem({ind}, extension_function)
        boy = Predicate('boy')
        dog = Predicate('dog')
        hug = Predicate('hug')

        def arity(x):
            if x in [boy, dog]:
                return (ind,)
            elif x == hug:
                return (ind, ind)

        predicate_signature = PredicateSignature(predicates={boy, dog, hug}, arg_indices={ind}, arity=arity)
        system = ComplexTypesSystem(basic_types_system, predicate_signature, extension_function)
        hug_x_y = system.create_ptype(hug, (x, y))
        assert system.create_rectype({
            'x': ind,
            'y': ind,
            'c': DependentField(lambda x, y: system.create_ptype(hug, (x, y)), ['x', 'y'])}
        ) == LabelledSet({...}, flavour=RT)
