import parse
from SegmentType import SegmentType

class MessageType:
    attributes = ('name', 'can_id', 'is_big_endian', 'frequency', 'segments')
    def __init__(self, name, can_id, is_big_endian, frequency, segments=None):
        self.name = str(name)
        self.can_id = parse.number(can_id)
        self.is_big_endian = bool(is_big_endian)
        self.frequency = parse.frequency(frequency)
        self.segments = segments if segments else {}

        for segnm in self.segments:
            if isinstance(self.segments[segnm], dict):
                self.segments[segnm] = SegmentType(segnm, **self.segments[segnm])
            elif not isinstance(self.segments[segnm], SegmentType):
                raise ValueError('segments can only be a dictionary of dictionaries or of SegmentType.')

    def upsert_segment(self, segment):
        self.segments[segment.name] = segment

    def __str__(self):
        '''
        A comma separated representation of a MessageTypes's values.
        In the same order as MessageTypes.attributes.
        '''
        return ', '.join(str(getattr(self, x)) for x in self.attributes)
