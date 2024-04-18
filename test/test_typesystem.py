from typesystem import Type, BasicTypesSystem


class TestBasicTypesSystem:
    def test_check(self):
        dog = Type('dog')
        sally = object()
        sam = object()

        def extension_function(x):
            if x == dog:
                return {sally}

        system = BasicTypesSystem({dog}, extension_function)
        assert system.check(sally, dog)
        assert not system.check(sam, dog)
