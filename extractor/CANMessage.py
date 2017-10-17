import parse

class CANMessage:
    attributes = ('can_id', 'data')
    def __init__(self, can_id, data):
        # Store our attributes in the format we want them (numbers).
        self.can_id = parse.number(can_id)
        self.data = parse.number(data)

    def __getitem__(self, index):
        '''
        Returns the bit or range of bits within data.
        '''
        return int('0b' + bin(self.data)[2:][index], 2)
        #TODO: Sue python for negative step not working for no reason.

    def __str__(self):
        '''
        A comma separated representation of a CANMessage's values.
        In the same order as CANMessage.attributes.
        '''
        return ', '.join(getattr(self, x) for x in self.attributes)

    def __iter__(self):
        return (getattr(self, x) for x in self.attributes)

class DAQMessage(CANMessage):
    '''
    Represents a logged CAN message with well defined time, ID, and data.
    '''
    attributes = ('time', 'can_id', 'data')
    def __init__(self, time, can_id, data):
        '''
        Expects can_id, data in a string of capital hex format.
        '''
        # Store our attributes in the format we want them (numbers).
        self.time = parse.number(time)
        self.can_id = parse.number(can_id)
        self.data = parse.number(data)
        print(hex(self.data))
