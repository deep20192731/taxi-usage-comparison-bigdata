#!/bin/bash -xe

# Run this script as a bootstrap action in EMR. This will install all the
# python packages that are required by the map-reduce scripts
sudo pip install pyshp
sudo yum-config-manager --enable epel
sudo yum install -y spatialindex spatialindex-devel
sudo ln -sf /usr/bin/python2.7 /usr/bin/python
sudo pip install Rtree==0.7.0