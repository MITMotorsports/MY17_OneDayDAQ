class SegmentType:
    def __init__(self, name, position, range, line=None):
        self.name = ''
        self.position = (0, 2)
        self.range = (0, 2)

    def extract(self, msg):
        data = msg.data[slice(*self.position)]
