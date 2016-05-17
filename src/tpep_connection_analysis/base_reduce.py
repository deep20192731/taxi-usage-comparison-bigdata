#!/usr/bin/env python

import sys

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        line = line.strip('\t')
        values = line.split('\t')
        yield values

def reducer():
    for values in parseInput():
        print '%s\t%s' % (values[0], values[1])
            
if __name__=='__main__':
    reducer()