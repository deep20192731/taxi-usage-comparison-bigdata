#!/usr/bin/env python

import sys
import json
import datetime
from shapely.geometry import Point, shape

sys.path.append('.')

# Invalid pickup and drop-off time
def compareTime(pickup, dropoff):
    try:
        pickup_day, pickup_time = pickup.split(' ')
        p_year, p_month, p_day = pickup_day.split('-')
        p_hour, p_minute, p_sec = pickup_time.split(':')
        
        dropoff_day, dropoff_time = dropoff.split(' ')
        d_year, d_month, d_day = dropoff_day.split('-')
        d_hour, d_minute, d_sec = dropoff_time.split(':')
        return (datetime.datetime(int(p_year), int(p_month), int(p_day), int(p_hour), int(p_minute), int(p_sec))) < (datetime.datetime(int(d_year), int(d_month), int(d_day), int(d_hour), int(d_minute), int(d_sec)))
    except:
        #probably something wrong with input format
        print >> sys.stderr, (pickup, dropoff)
        return False

# Removing trips where location is invalid
def location_valid(location):
    try:
        if(location[0] != 0 and location[1] != 0):
            return True
        else:
            return False
    except:
        print >> sys.stderr, location
        return False

def point_in_polygon(location, shapes):
    try:
        if(location_valid(location)):
            point = Point(location[0], location[1])
            for shp in shapes:
                polygon = shape(shp['geometry'])
                if(polygon.contains(point)):
                    return (shp['properties']['borough'], shp['properties']['neighborhood'])
        else:
            return ('Unknown', 'Unknown')
        return ('Unknown', 'Unknown')
    except:
        print >> sys.stderr, location
        return ('Unknown', 'Unknown')
    
def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split(',')
        if len(values) > 1 and values[0] != 'VendorID': 
            # yield is usually used when we know we will iterate over something just once
            yield values

def mapper():
    # Import file as JSON
    with open('pediacitiesnycneighborhoods.geojson') as f:
        js = json.load(f)
        
    for values in parseInput():
        if(compareTime(values[1], values[2])):
            # (Longitude, Latitude) in shape files are in same metric as geo-json files
            pickup_location = (float(values[5]), float(values[6]))
            dropoff_location = (float(values[7]), float(values[8]))
            
            pickup_bou, pickup_nei = point_in_polygon(pickup_location, js['features'])
            dropoff_bou, dropoff_nei = point_in_polygon(dropoff_location, js['features'])
            
            print "%s\t%s,%s,%s,%s" % (','.join(values), pickup_bou, pickup_nei, dropoff_bou, dropoff_nei)


if __name__=='__main__':
    mapper()