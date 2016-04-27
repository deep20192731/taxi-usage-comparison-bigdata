#!/bin/bash -xe

# Run this script as a bootstrap action in EMR. This will install all the
# python packages that are required by the map-reduce scripts
sudo yum install geos geos-devel
sudo pip install shapely
