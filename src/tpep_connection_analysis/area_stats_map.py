#!/usr/bin/env python

import sys

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split('\t')
        if len(values) > 1 and values[0] != 'VendorID':
            yield values

def mapper():
    for key, values in parseInput():
        values_split = values.split(',')
        print "%s\t%s" % (key, values_split[2])
        
if __name__=='__main__':
    mapper()