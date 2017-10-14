from pathlib import Path
import csv
from CANMessage import CANMessage

class Log:
    def __init__(self, src):
        self.src = Path(src)

    def __iter__(self):
        return (CANMessage(line=line) for line in open(self.src, 'r'))

    def csv(self, outpath):
        '''
        Outputs a csv representation of the log in outpath.
        '''
        csvfile = outpath.open('w', newline='')
        writer = csv.writer(csvfile)

        writer.writerow(CANMessage.attributes)
        for message in self:
            writer.writerow(message)
