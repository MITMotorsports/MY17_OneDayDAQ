import yaml
from pathlib import Path
from MessageType import MessageType
from CANMessage import CANMessage

class CANSpec:
    def __init__(self, source):
        self._source = Path(source)
        # A mapping of a message type's can_id to said message type.
        self.messages = {}
        self.parse()

    def parse(self):
        with self._source.open('r') as f:
            prem = yaml.safe_load(f)

        for msgnm in prem:
            msgtype = MessageType(msgnm, **prem[msgnm])
            self.messages[prem[msgnm]['can_id']] = msgtype

        return self.messages

    def interpret(self, message):
        '''
        Interprets a CANMessage instance based on self CAN specification.
        '''
        assert isinstance(message, CANMessage)
        return self.messages[message.can_id].interpret(message)
