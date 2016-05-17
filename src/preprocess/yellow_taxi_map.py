#!/usr/bin/env python

import sys
import json
import datetime
from rtree import index as rtree
from matplotlib.path import Path
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
        print >> sys.stderr, ("Location Invalid", location)
        return False
  
def findNeighborhood(location, index, neighborhoods):
    try:
        if(location_valid(location)):
            point = Point(location[0], location[1])
            match = index.intersection((location[0], location[1], location[0], location[1]))
            for a in match:
                if neighborhoods[a][2].contains(point):
                    return a
        return -1
    except Exception,e:
        print >> sys.stderr, ("Niehbourhood Invalid", location, str(e))
        return -1
    
def readNeighborhood(shapeFile, index, neighborhoods):
    for sr in shapeFile:
        paths = map(Path, sr['geometry']['coordinates'])
        bbox = paths[0].get_extents()
        map(bbox.update_from_path, paths[1:])
        index.insert(len(neighborhoods), list(bbox.get_points()[0])+list(bbox.get_points()[1]))
        neighborhoods.append((sr['properties']['borough'], sr['properties']['neighborhood'], shape(sr['geometry'])))
    neighborhoods.append(('UNKNOWN', 'UNKNOWN', None))    
    
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
    
    neighborhoods = []
    index = rtree.Index()    
    readNeighborhood(js['features'], index, neighborhoods)
    
    for values in parseInput():
        if(compareTime(values[1], values[2])):
            # (Longitude, Latitude) in shape files are in same metric as geo-json files
            pickup_location = (float(values[5]), float(values[6]))
            dropoff_location = (float(values[9]), float(values[10]))
            
            pickup_index = findNeighborhood(pickup_location, index, neighborhoods)
            dropoff_index = findNeighborhood(dropoff_location, index, neighborhoods)
            
            print "%s\t%s,%s,%s,%s" % (','.join(values), neighborhoods[pickup_index][0], neighborhoods[pickup_index][1], neighborhoods[dropoff_index][0], neighborhoods[dropoff_index][1])


if __name__=='__main__':
    mapper()