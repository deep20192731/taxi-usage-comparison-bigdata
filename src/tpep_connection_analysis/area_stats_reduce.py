#!/usr/bin/env python

import sys

def getMonth(time_str):
    date, time = time_str.split(" ")
    return date.split('-')[1]

def resetMonthStatArray(arr):
    try:
        for i in range(0, 12):
            arr[i] = 0;
    except IndexError:
        for i in range(0, 12):
            arr.append(0);

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').strip('\t').split('\t')
        
def reducer():
    current_area = None
    connection_month = []
    current_area_conn_count = 0
    
    for key, value in parseInput():
        if(current_area == key):
            current_area_conn_count += 1
            connection_month[int(getMonth(value)) - 1] += 1
        else:
            if(current_area != None):
                print "%s\t%s\t%s" % (current_area, current_area_conn_count, ' '.join(map(str, connection_month)))
            current_area = key
            current_area_conn_count = 1 
            resetMonthStatArray(connection_month)
            try:
                connection_month[int(getMonth(value))-1] += 1
            except:
                print >> sys.stderr, value, ' '.join(map(str, connection_month)), int(getMonth(value))-1
    
    if(current_area != None):
        print "%s\t%s\t%s" % (current_area, current_area_conn_count, ' '.join(map(str, connection_month)))

if __name__=='__main__':
    reducer()