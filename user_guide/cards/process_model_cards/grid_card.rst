Back to :ref:`card-index`

.. _grid-card:

GRID
====

Specifies the discretization scheme to be employed in the simulation.

Required Cards:
---------------

TYPE <type>
 Grid type.  Options: STRUCTURED, UNSTRUCTURED, UNSTRUCTURED_EXPLICIT

 * STRUCTURED

   - CARTESIAN (default)
   - CYLINDRICAL
   - SPHERICAL

 * :ref:`unstructured-implicit-grid-card` <filename>

   Standard finite element format where cells (elements) are defined by lists of vertices and vertices are defined by coordinates. We often refer to these as *implicit* unstructured grids. See :download:`PFLOTRAN_cell_numbering_schemes.pdf <files/PFLOTRAN_cell_numbering_schemes.pdf>` for cell face and vertex numbering schemes.
   
 * :ref:`unstructured-explicit-grid-card` <filename>

   The grid is defined by a list of cells and connectivity. Cells are defined by an id, coordinate and volume while connections are composed of two cell ids, an area and a face-center coordinate.

NXYZ <int int int>
 # of cells in x, y, z dimensions (structured only)

BOUNDS (may not be used with DXYZ)
 Specifies bounds of structured Cartesian grid (see examples below) 
  ::

   BOUNDS
     x_min y_min z_min   
     x_max y_max z_max  
   /
  
 Notes: 
  1. The origin is automatically calculated based on the lower bound.
  2. Cylindrical grids include only x and z coordinates.

DXYZ (may not be used with BOUNDS)
 Specifies grid spacing of structured Cartesian grid (see examples below).  
  ::
 
   DXYZ
     dx
     dy
     dz
   /

Use line continuation through a backslash '\' when lines exceed ~80 characters 
(see DXYZ examples below). PFLOTRAN input can handle lines of 512 characters, 
but that may change.

FILE <filename>
  Name of file containing grid information (unstructured only)

Optional Cards:
---------------

GRAVITY <float float float>
 Specifies gravity vector (default: 0. 0. -9.8068)

ORIGIN <float float float>
 Coordinate of grid origin (default: 0. 0. 0.)

INVERT_Z
 Inverts the z axis (positive Z is down instead of default up)

PERM_TENSOR_TO_SCALAR_MODEL <string>
 Specifies the algorithm for converting the diagonal permeability tensor
 to a scalar at a face for a flux calculation. Options include [LINEAR,
 FLOW, POTENTIAL]. Defaults: LINEAR for structured grids, and POTENTIAL for
 unstructured grids. 

Examples
--------

 ::

  GRID
    TYPE structured
    NXYZ 5 4 2
    DXYZ 
      2@1. 3@1.5 
      1@1. 3@0.5 
      2@0.25
    /
  END

 ::

  GRID
    TYPE structured
    NXYZ 5 4 2
    BOUNDS 
      0. 0. 0.
      100. 50. 25.
    /
  END


BOUNDS card with GRID
.....................

 ::

  BOUNDS
   0. 0. 0.
   100. 50. 25.
  /


DXYZ card with GRID
...................

 ::

  DXYZ 
    1. 
    1. 
    0.25
  /
 
 ::

  DXYZ 
    2@1. 3@1.5 
    1@1. 3@0.5 
    2@0.25
  /

DXYZ with continuation:
+++++++++++++++++++++++

 ::

  NXYZ 130 1 9
  DXYZ
    0.08 0.09 0.10 0.10 0.12 0.13 0.14 0.15 0.17 0.19 \
    0.20 0.22 0.25 0.27 0.30 0.33 0.36 0.40 0.44 0.48 \
    0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 \
    0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 \
    0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 \
    0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 \
    0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 \
    0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 \
    0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 \
    0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.53 \
    0.53 0.53 0.53 0.53 0.53 0.53 0.53 0.64 0.76 0.92 \
    1.10 1.32 1.58 1.90 2.28 2.73 3.28 3.94 4.73 5.67 \
    6.80 8.17 9.80 11.76 14.11 16.93 20.32 24.38 29.26 35.11
    1
    1.666666666666666666667 ! note that all 9 cells in z will be assign 1.666...7.
  /
 
Cylindrical Coordinates
.......................
Note: For cylindrical coordinates, the X dimension corresponds to the radius of the cylinder while the Z dimension represents the height.  It is assumed that the Y dimension is variable with NY = 1, and no Y grid spacing is specified.  PFLOTRAN will calculate the distance in the Y direction automatically based on the cylindrical coordinate system.

 ::

  GRID
    TYPE structured cylindrical
    NXYZ 100 1 10
    BOUNDS
      0.d0 0. 
      100.d0 10.d0
    /
  END


But all REGIONs must include Y coordinates of 0 and 1.  E.g.

 ::

  REGION all
    COORDINATES
      0.d0 0.d0 0.d0
      100.d0 1.d0 10.d0
    /
  END

  REGION top
    FACE top
    COORDINATES
      0.d0 0.d0 10.d0
      100.d0 1.d0 10.d0
    /
  END

Unstructured Mesh Examples
..........................

Format


Example implicit unstructured mesh (see `mixed.ugi`_)

.. _mixed.ugi: https://bitbucket.org/pflotran/pflotran/src/master/regression_tests/default/discretization/mixed.ugi

 ::

  15 24
  P 4 5 6 2 1
  T 4 3 5 1
  W 2 7 6 4 9 5
  W 8 7 2 10 9 4
  W 10 9 4 21 14 11
  H 19 9 5 12 17 7 6 16
  T 5 13 14 15
  T 5 14 9 15
  P 5 9 19 12 15
  P 13 5 12 22 15
  H 20 10 9 19 18 8 7 17
  H 24 21 14 23 20 10 9 19
  P 23 19 9 14 15
  P 22 12 19 23 15
  P 22 23 14 13 15
  5.000000e+00 5.000000e+00 5.000000e+00
  5.000000e+00 2.500000e+00 5.000000e+00
  5.000000e+00 5.000000e+00 2.500000e+00
  5.000000e+00 2.500000e+00 2.500000e+00
  2.500000e+00 5.000000e+00 2.500000e+00
  2.500000e+00 5.000000e+00 5.000000e+00
  2.500000e+00 2.500000e+00 5.000000e+00
  2.500000e+00 0.000000e+00 5.000000e+00
  2.500000e+00 2.500000e+00 2.500000e+00
  2.500000e+00 0.000000e+00 2.500000e+00
  5.000000e+00 2.500000e+00 0.000000e+00
  0.000000e+00 5.000000e+00 2.500000e+00
  2.500000e+00 5.000000e+00 0.000000e+00
  2.500000e+00 2.500000e+00 0.000000e+00
  1.250000e+00 3.750000e+00 1.250000e+00
  0.000000e+00 5.000000e+00 5.000000e+00
  0.000000e+00 2.500000e+00 5.000000e+00
  0.000000e+00 0.000000e+00 5.000000e+00
  0.000000e+00 2.500000e+00 2.500000e+00
  0.000000e+00 0.000000e+00 2.500000e+00
  2.500000e+00 0.000000e+00 0.000000e+00
  0.000000e+00 5.000000e+00 0.000000e+00
  0.000000e+00 2.500000e+00 0.000000e+00
  0.000000e+00 0.000000e+00 0.000000e+00
