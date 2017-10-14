class SegmentType:
    def __init__(self, name=None, c_type=None, position=None, range=None):
        self.name = name
        self.c_type = c_type
        self.position = position
        self.range = position

    def extract(self, msg):
        data = msg.data[slice(*self.position)]
