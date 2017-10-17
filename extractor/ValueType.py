import parse

class ValueType:
    attributes = ['name', 'value']
    def __init__(self, name, value):
        assert isinstance(value, (tuple, list, int))
        self.name = name
        self.value = tuple(value) if isinstance(value, list) else value

    def __str__(self):
        '''
        A comma separated representation of a ValueType's values.
        In the same order as ValueType.attributes.
        '''
        return ', '.join(str(getattr(self, x)) for x in self.attributes)
