#!/usr/bin/env python

import sys

def compareEveningTime(dropoff):
    eveningTime=["19","20","21","22","23","00","01","02"]
    try:
        dropoff_day, dropoff_time = dropoff.split(' ')
        d_year, d_month, d_day = dropoff_day.split('-')
        d_hour, d_minute, d_sec = dropoff_time.split(':')
        if(d_hour in eveningTime):
            return True
        else:
            return False
    except:
        #probably something wrong with input format
        return False
    
def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split(',')
        if len(values) > 1 and values[0] != 'VendorID': 
            yield values
            
def mapper():
    for values in parseInput():
        if(compareEveningTime(values[2])):
            dropoff_borough=values[21]
            dropoff_neighbourhood=values[22]
            dropoff_time=values[2]
            print ("%s\t%s,%s") % (dropoff_neighbourhood,dropoff_borough,dropoff_time)
               
if __name__=='__main__':
    mapper()            