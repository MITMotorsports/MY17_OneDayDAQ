class MessageType:
    def __init__(self, name, can_id, l_endian, freq):
        self.name = name
        self.can_id = can_id
        self.l_endian = l_endian
        self.freq = freq
        self.segments = {}

    def add_segment(self, segment):
        self.segments[segment.name] = segment

    def __str__(self):
        out = 'MESSAGE_NAME=' + str(self.name) + ' ID=' + str(self.can_id) + ' ENDIAN=' + 'LITTLE' if self.l_endian else 'BIG' + ' FREQ=' + str(self.freq) + '\n\t'
        out += '\n\t'.join([str(segment) for segment in self.segments])
        return out
