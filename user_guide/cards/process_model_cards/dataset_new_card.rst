Back to :ref:`card-index`

.. _dataset-new-card:

DATASET(NEW)
============
**THIS IS A NEW EXPERIMENTAL IMPLEMENTATION OF THE OLDER** 
:ref:`dataset-card` **card.**
Specifies a data set to be associated with parameters sets in the model.  

Required Cards:
---------------
DATASET <optional string>
 Opens the DATASET block with the name of the data set in the string.  
 If the name is not provided, the NAME entry below must be included.

NAME <string>
 Name of the data set if not included with DATASET card.  
 **Note:** this string overwrites the name specified with the DATASET.

FILENAME <string>
 Name of file containing data.

HDF5_DATASET_NAME <string>
 Name of the group within an HDF5 file where the data resides.

For most any dataset where previously the FILE keyword could be applied, the 
user may now use DATASET followed by the name of the dataset entered under a 
DATASET block elsewhere in the input file.  However, the user must exercise 
vigilance to ensure that the dataset is properly organized in the HDF5 file and 
is aligned spatially with the domain.  Within the HDF5 file, the dataset takes 
the following form:

Names used in these steps refer to the example below:
 1. At the top of the file (i.e. outside of any lower level groups), the user 
    creates an HDF5 Group, in this case named *river_head*.  
 2. Within the Group, two separate HDF5 Datasets are created: one named 
    *Data* and the other *Time*, where *Time* is optional.

  a. The ''Times'' Dataset is one dimensional and holds the times associated 
     with the data in the *Data* dataset.  It's size corresponds to the right 
     most index in dataset (dim1,dim2,...,t).
  b. The ''Data'' Dataset is N dimensional array where the time dimension is 
     farthest to the right, again (dim1,dim2,...,t).

 3. Add the following HDF5 Attributes to the HDF5 Group

  a. Dimension <string>: where options are X, Y, Z, XY, XZ, YZ, XYZ
  b. Discretization <double array>: the grid spacing for the dimensions in *a*
  c. Origin <double array>: the origin of the dimensions in *a*
  d. Max Buffer Size <int>: size of internal buffer storing transient dataset
  e. Interpolation Method <string>: string = 'STEP' or 'LINEAR'
  f. Cell Centered <bool>: the dataset is cell centered.  Otherwise, it is node 
     centered and you need an additional entry for each dimension (e.g. nx+1 
     values for X).

The attached :download:`dataset.h5 <files/dataset.h5>` illustrates 
the usage.

Examples
--------

 ::

  DATASET river_boundary_head
    FILENAME data.h5
    HDF5_DATASET_NAME river_head
  END

  FLOW_CONDITION river
    TYPE
      PRESSURE HYDROSTATIC
    /
    DATUM DATASET y_river_boundary_head
    PRESSURE 101325.d0
  END
