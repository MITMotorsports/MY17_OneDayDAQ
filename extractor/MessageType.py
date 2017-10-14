class MessageType:
    def __init__(self, name, can_id, big_endian, frequency):
        self.name = name
        self.can_id = can_id
        self.big_endian = big_endian
        self.frequency = frequency
        self.segments = {}

    def upsert_segment(self, segment):
        self.segments[segment.name] = segment
