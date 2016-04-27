#!/usr/bin/env python

import sys

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')

def reducer():
    for key, values in parseInput():
        print '%s,%s' % (key, values)

if __name__=='__main__':
    reducer()