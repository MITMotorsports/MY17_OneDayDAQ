from CANSpec import CANSpec
from CANMessage import DAQMessage
from Log import Log

a = CANSpec('../fsae_can_spec.yml')
b = DAQMessage('99', '0x521', 0x000000000408)
print(a.interpret(b))
l = Log('./fakelog.log')
for msg in l:
    print(msg.time, hex(msg.can_id), msg.interpret(a))
