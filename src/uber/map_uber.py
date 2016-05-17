#!/usr/bin/env python

import sys

def createLocIndex(uber_dict):
    lines = open("taxi-zone-lookup.csv").readlines()[0].split('\r')
    lines = lines[1:]
    for line in lines:
        id, bo, ar = line.split(',')
        uber_dict[int(id)] = (bo, ar)

# Lets analyze data for July
def rightPickupDay(pickup):
    year, month, day = pickup.split("-")
    try:
        if(int(month) == 7):
            return True
    except:
        return False
    return False
    
def parseInput():
    for line in sys.stdin:
        values = line.strip('\n').strip('\t').strip('\r').split(',')
        if(len(values) > 1 and values[0] != 'Dispatching_base_num'):
            yield values 
    
def mapper():
    uber_loc_index = {}
    createLocIndex(uber_loc_index)
    
    for values in parseInput():
        pickup_day, pickup_time = values[1].split(" ")
        if(rightPickupDay(pickup_day)):
            bo, ar = uber_loc_index[int(values[3])]
            print "%s\t%s,%s,%s" % (ar, pickup_time, bo, ar)

if __name__=='__main__':
    mapper()