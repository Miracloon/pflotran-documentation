import sys
import math
from h5py import *
import numpy
import random

filename = 'hdvz_material_ids.h5'
h5file = File(filename,mode='w')

nx = 432
ny = 1
nz = 256
nxXny = nx*ny
n = nx*ny*nz

iarray = numpy.zeros((n),'=i4')

# add cell ids to file
for i in range(n):
  iarray[i] = i+1
dataset_name = 'Materials/Cell Ids'
h5dset = h5file.create_dataset(dataset_name, data=iarray)
print 'done with ', dataset_name

filename = 'geology_resamp.dat'
fin = open(filename,'r')
for i in range(n):
  s = fin.readline()
  iarray[i] = int(s)
dataset_name = 'Materials/Material Ids'
h5dset = h5file.create_dataset(dataset_name, data=iarray)
print 'done with ', dataset_name
      
h5file.close()
print 'done with everything'
  
