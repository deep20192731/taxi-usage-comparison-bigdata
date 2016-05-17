#!/usr/bin/env python

import sys

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')

def reducer():
    current_month = None
    current_month_trips_count = 0
    
    for key, values in parseInput():
        if(key == current_month):
            current_month_trips_count += 1
        else:
            if(current_month != None):
                # Try to make the file as csv file
                print ("%s,%s") % (current_month, current_month_trips_count)
            current_month = key
            current_month_trips_count = 1
    if(current_month != None):
        print ("%s,%s") % (current_month, current_month_trips_count)

if __name__=='__main__':
    reducer()