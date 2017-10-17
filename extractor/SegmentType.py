import parse
from ValueType import ValueType

class SegmentType:
    attributes = ('name', 'c_type', 'position', 'values')
    def __init__(self, name, c_type, position, values=None):
        self.name = str(name)
        self.c_type = str(c_type)
        self.position = tuple(position)
        self.values = values if values else {}

        for valnm in self.values:
            self.values[valnm] = ValueType(valnm, self.values[valnm])

    def extract(self, msg):
        data = msg.data[slice(*self.position)]

    def __str__(self):
        '''
        A comma separated representation of a SegmentType's values.
        In the same order as SegmentType.attributes.
        '''
        return ', '.join(str(getattr(self, x)) for x in self.attributes)
