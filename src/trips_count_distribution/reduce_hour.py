#!/usr/bin/env python

import sys

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')

def reducer():
    current_hour = None
    current_hour_trips_count = 0
    
    for key, values in parseInput():
        if(key == current_hour):
            current_hour_trips_count += 1
        else:
            if(current_hour != None):
                # Try to make the file as csv file
                print ("%s,%s") % (current_hour, current_hour_trips_count)
            current_hour = key
            current_hour_trips_count = 1
    if(current_hour != None):
        print ("%s,%s") % (current_hour, current_hour_trips_count)

if __name__=='__main__':
    reducer()