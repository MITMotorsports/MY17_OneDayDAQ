import parse

class ValueType:
    attributes = ['name', 'value']
    def __init__(self, name, value):
        assert isinstance(value, (tuple, list, int))
        self.name = name
        self.value = tuple(value) if isinstance(value, list) else value
