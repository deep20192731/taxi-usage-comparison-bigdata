#!/usr/bin/env python

import sys
  
# Just checking total_amount for now (But actually if amount < 0 then it is just a possibility that
# data entry was wrong, trip can still hold. So not using this)
def checkCorrectFare(amount):
    try:
        return float(amount) >= 0
    except:
        print >> sys.stderr, amount
        return False
          
          
def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        line = line.strip('\t')
        values = line.split(',')
        if len(values) > 1 and values[0] != 'VendorID':
            yield values

def mapper():
    for values in parseInput():
        # See if the trip is a store-and-fwd flag. This index is different for Green and Yellow Taxis
        if(values[8] == 'Y'):
            # Key = Area AND Value = Borough, VendorId, time, longi, lati
            print "%s\t%s,%s,%s,%s,%s" % (values[22], values[21], values[0], values[2], values[9], values[10])
        

if __name__=='__main__':
    mapper()