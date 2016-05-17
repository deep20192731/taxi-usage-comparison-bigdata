#!/usr/bin/env python

import sys

def parseInput():
    for line in sys.stdin:
        values = line.strip('\n').strip('\t').strip('\r').split(',')
        if(len(values) > 1 and values[0] not in ['VendorID', 'Dispatching_base_num']):
            yield values
        
def mapper():
    for values in parseInput():
        day, time = values[1].split(" ")
        month = day.split("-")[1]
        print ("%s\t%s") % (month, 1)
        
if __name__=='__main__':
    mapper()