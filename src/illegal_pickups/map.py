#!/usr/bin/env python

import sys

def validNeighbourhood(dispatch_type, nei, area):
    neighbourhoods= ["East Harlem","Harlem","Washington Heights","Inwood","Randall's Island","Roosevelt Island",
                    "Morningside Heights", "Marble Hill"]
    airports = ["LaGuardia Airport", "JFK Airport", "John F. Kennedy International Airport"]
    
    # Both Street Hail and Pre arranged are allowed
    if(area == "Manhattan"):
        if((nei in neighbourhoods)):
            return True
        else:
            return False
    elif(area == "Queens" or area == "Queen"):
        if((nei in airports) and int(dispatch_type) != 2):
            return False
    return True

def parseInput():
    for line in sys.stdin:
        line = line.strip('\t').strip('\n').strip('\r')
        values = line.split(',')
        if(len(values) == 25):
            values.insert(21, '')
            values.insert(21, '')
            print >> sys.stderr, values
        yield values

def mapper():
    for values in parseInput():
        nei = values[24]
        area = values[23]
        dispatch_type = values[20]
        if(not validNeighbourhood(dispatch_type, nei, area)):
            # output= area, nei + pickup_time, pickup_lati, longi, dispatch_type, payment_type
            print ("%s,%s\t%s,%s,%s,%s,%s") % (values[23], values[24], values[1], values[6],
                                               values[5], values[20], values[19])
             
        

if __name__=='__main__':
    mapper()