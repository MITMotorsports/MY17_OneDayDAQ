import yaml
from pathlib import Path
from MessageType import MessageType

class CANSpec:
    def __init__(self, source):
        self._source = Path(source)
        self.messages = {}
        self.parse()

    def parse(self):
        with self._source.open('r') as f:
            self.messages = yaml.safe_load(f)

        for msgnm in self.messages:
            if isinstance(self.messages[msgnm], dict):
                self.messages[msgnm] = MessageType(msgnm, **self.messages[msgnm])
            elif not isinstance(self.messages[msgnm], MessageType):
                raise ValueError('segments can only be a dictionary of dictionaries or of MessageType.')

        return self.messages
