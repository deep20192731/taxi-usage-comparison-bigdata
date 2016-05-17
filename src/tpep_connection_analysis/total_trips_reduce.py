#!/usr/bin/env python

import sys

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        line = line.strip('\t')
        values = line.split('\t')
        yield values

def reducer():
    current_value = None
    current_count = 0
    for values in parseInput():
        if(values[0] == current_value):
            current_count += 1
        else:
            if(current_value != None):
                print '%s\t%s' % (current_value, current_count)
            current_value = values[0]
            current_count = 1
                
    if(current_value != None):
        print '%s\t%s' % (current_value, current_count)
            
if __name__=='__main__':
    reducer()