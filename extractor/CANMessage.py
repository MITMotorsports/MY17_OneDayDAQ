import parse

class CANMessage:
    """
    Represents a logged CAN message with well defined time, ID, and data.
    """

    attributes = ['time', 'can_id', 'data']
    def __init__(self, time=None, can_id=None, data=None, line=None):
        '''
        Expects can_id, data in a string of capital hex format.
        '''
        if line:
            for key, val in parse.log(line).items():
                setattr(self, key + 'str', val)
        else:
            self.timestr = time
            self.can_idstr = can_id
            self.datastr = data

        # Store our attributes in the format we want them (numbers).
        for attr in self.attributes:
            setattr(self, attr, parse.number(getattr(self, attr + 'str')))

    def __json__(self):
        return {x: getattr(self, x + 'str') for x in self.attributes}

    def __str__(self):
        '''
        A comma separated representation of a CANMessage's values.
        In the same order as CANMessage.attributes.
        '''
        return ', '.join(getattr(self, x + 'str') for x in self.attributes)

    def __iter__(self):
        return (getattr(self, x + 'str') for x in self.attributes)
