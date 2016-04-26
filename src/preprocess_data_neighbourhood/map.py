#!/usr/bin/env python

import sys
sys.path.append('.')
import matplotlib
matplotlib.use('Agg')
from matplotlib.path import Path
from rtree import index as rtree
import numpy, shapefile


def findNeighborhood(location, index, neighborhoods):
    # get all the bounding boxes in which this point is in
    match = index.intersection((location[0], location[1], location[0], location[1]))
    
    # see if the point lies in any of the paths corresponding to shapes
    for a in match:
        if any(map(lambda x: x.contains_point(location), neighborhoods[a][1])):
            return a
    return -1

def readNeighborhood(shapeFilename, index, neighborhoods):
    sf = shapefile.Reader(shapeFilename)
    for sr in sf.shapeRecords():
        # each part is a line or a figure in itself, if a shape has multiple paths then all
        # those have to be joined, to form the figure
        paths = map(Path, numpy.split(sr.shape.points, sr.shape.parts[1:]))
        
        # gets a bounding box surrounding the shape
        bbox = paths[0].get_extents()
        map(bbox.update_from_path, paths[1:])

        # insert the bounding box of each shape in rtree.Index
        index.insert(len(neighborhoods), list(bbox.get_points()[0]) + list(bbox.get_points()[1]))
        
        # insert the BoroName, AreaName and Paths
        neighborhoods.append((sr.record[3], paths))
        
    neighborhoods.append(('UNKNOWN', None))


def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split(',')
        if len(values) > 1 and values[0] != 'VendorID': 
            # yield is usually used when we know we will iterate over something just once
            yield values

def mapper():
    index = rtree.Index()
    neighborhoods = []
    readNeighborhood('ZillowNeighborhoods-NY.shp', index, neighborhoods)

    for values in parseInput():
        # (Longitude, Latitude) in shape files are in same metric as trip files
        pickup_location = (float(values[5]), float(values[6]))
        dropoff_location = (float(values[9]), float(values[10]))
        pickup_neighborhood = findNeighborhood(pickup_location, index, neighborhoods)
        dropoff_neighborhood = findNeighborhood(dropoff_location, index, neighborhoods)
        
        print "%s\t%s,%s" % (','.join(values), neighborhoods[pickup_neighborhood][0],
                             neighborhoods[dropoff_neighborhood][0])


if __name__=='__main__':
    mapper()