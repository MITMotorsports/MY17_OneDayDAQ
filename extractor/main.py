from CANSpec import CANSpec
from CANMessage import DAQMessage
from Log import Log

a = CANSpec('../fsae_can_spec.yml')
l = Log('./fakelog.log')
for msg in l:
    print(msg.time, msg.can_id, a.interpret(msg))
