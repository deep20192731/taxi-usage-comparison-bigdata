#!/usr/bin/env python
import sys

def parseInput():
    for line in sys.stdin:
        line = line.strip()
        values = line.split('\t')
        yield values

def reducer():
    for values in parseInput():
        key= values[0]
        
        if(len(values)>2):
            value=values[2]
        else:
            value= values[1]
        print "%s,%s" % (key, value)

 
if __name__=='__main__':
    reducer()