import parse
from ValueType import ValueType
from CANMessage import CANMessage

class SegmentType:
    attributes = ('name', 'c_type', 'position', 'values')
    def __init__(self, name, c_type, unit, position, values=None):
        self.name = str(name)
        self.c_type = str(c_type)
        self.unit = str(unit)
        self.position = tuple(position)
        self.values = values if values else {}

        for valnm in self.values:
            self.values[valnm] = ValueType(valnm, self.values[valnm])

    def interpret(self, message):
        assert isinstance(message, CANMessage)

        data = message[self.position[0]:self.position[1] + 1]
        return (self.data_name(data), data)

    def data_name(self, data):
        '''
        Returns the first contained ValueType in which data is contained.
        '''
        try:
            nm = next(value for value in self.values if data in self.values[value])
        except(StopIteration):
            nm = None
        return nm

    def __str__(self):
        '''
        A comma separated representation of a SegmentType's values.
        In the same order as SegmentType.attributes.
        '''
        return ', '.join(str(getattr(self, x)) for x in self.attributes)
