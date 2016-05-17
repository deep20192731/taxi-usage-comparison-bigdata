#!/bin/bash -xe

# Run this script as a bootstrap action in EMR. This will install all the
# python packages that are required by the map-reduce scripts
sudo yum-config-manager --enable epel
sudo yum install -y spatialindex spatialindex-devel
sudo pip install Rtree==0.7.0
sudo ln -sf /usr/bin/python2.7 /usr/bin/python
sudo yum install geos geos-devel
sudo pip install shapely
