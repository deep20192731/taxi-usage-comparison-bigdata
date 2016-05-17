#!/usr/bin/env python

import sys

def monthUnderAnalysis(month):
    try:
        month = int(month)
        if((month == 3)):
            return True
    except:
        return False
    return False
    
def parseInput():
    for line in sys.stdin:
        values = line.strip('\n').strip('\t').strip('\r').split(',')
        if(len(values) > 1 and values[0] not in ['VendorID', 'Dispatching_base_num']):
            yield values
        
def mapper():
    for values in parseInput():
        day, time = values[1].split(" ")
        month = day.split("-")[1]
        hour = time.split(":")[0]
        if(monthUnderAnalysis(month)):
            print ("%s\t%s") % (hour, 1)
        
if __name__=='__main__':
    mapper()