Back to :ref:`card-index`

.. _region-card:

REGION
======

Defines a region (e.g. point, surface, volume) within the problem domain.

Required Cards:
---------------

REGION <string>
 Opens the REGION block, where <string> is the name of the region.

Within the REGION block, one of:

 COORDINATE <float float float>
  Defines the x, y, z location of a single point in space  (see note_ below)
   
   ::

    COORDINATE x y z

 COORDINATES
  Defines two coordinates which define a box (see note_ below)
  
   ::

    COORDINATES
      xmin ymin zmin
      xmax ymax zmax
    /

 BLOCK <int int int int int int> 
  Defines the i,j,k bounds of a region (structured grid only)

   ::

    BLOCK istart iend jstart jend kstart kend

 CARTESIAN_BOUNDARY <string>
  Maps a boundary region to a Cartesian domain (structured grid only).  
  The 'FACE' is implicit based on the *string*.

   ::

    CARTESIAN_BOUNDARY [WEST, EAST, SOUTH, NORTH, BOTTOM, TOP]

 FILE <string>
  Specifies a file (e.g. HDF5) from which cell ids and face directions (for 
  structured: 1=west, 2=east, 3=south, 4=north, 5=bottom, 6=top) can be read.

 LIST
  A generic list of cell ids (**not yet implemented**).  

Optional Card:
--------------

FACE <string>
 Required when defining a surface (structured grid only).

   ::

    FACE [WEST, EAST, SOUTH, NORTH, BOTTOM, TOP]


Examples
--------
 ::

  REGION source_zone
    FILE source_zone.h5
  /

  REGION all
    COORDINATES
      0.d0 0.d0 95.d0 
      120.d0 120.d0 110.d0
    /
  /

  REGION West
    COORDINATES
      0.d0 0.d0 95.d0 
      0.d0 120.d0 110.d0
    /
    FACE WEST
  /

  REGION East
    COORDINATES
      120.d0 0.d0 95.d0 
      120.d0 120.d0 110.d0
    /
    FACE EAST
  /

  REGION South
    COORDINATES
      0.d0 0.d0 95.d0 
      120.d0 0.d0 110.d0
    /
    FACE SOUTH
  /

  REGION South_Cartesian
    CARTESIAN_BOUNDARY SOUTH
  /

  REGION 2-9
    COORDINATE 60.07 88.75 102.5d0
  /

  REGION zone1
    BLOCK 45 90 32 40 1 100
  /

.. _note:

Note for COORDINATE/COORDINATES
-------------------------------
If a region (point, line, or plane) lies between cells within a structured grid (i.e. at a face or corner between cells), it will be assigned to the upwind cell (lower I,J,K index).  For instance, point X in

 ::

       |
    3  |  4
       |
  -----X-----
       |
    1  |  2
       |

is assigned to cell 1, in

 ::

       |
    3  X  4
       |
  -----|-----
       |
    1  |  2
       |

is assigned to cell 3, and in

 ::

       |
    3  |  4
       |
  --X--|-----
       |
    1  |  2
       |

is assigned to cell 1.

A line or a plane is similarly assigned to the adjacent upwind cells.  In the direction parallel to the line or plane, all cells INTERSECTED will be included (i.e. the region overlaps or crosses the boundary into the cell).  For instance, line X in

 ::

       |
    3  |  4
       X
  -----X-----
       X
    1  |  2
       |

will assign cells 1 and 3.

For 3D regions, the cells INTERSECTED by the volume will be included.  If the boundaries of the region coincide with cell boundaries, only the encompassed cells are included.  If there is ANY overlap of a 3D region with a cell (even femtometers into a cell), the cell is included. For instance, rectangle X in

 ::

       |
    3  |  4
     XXXX
  ---X-|X----
     XXXX
    1  |  2
       |

will assign cells 1, 2, 3 and 4, whereas

 ::

       |
    3  XXX4
       X X
  -----XXX---
       |
    1  |  2
       |

only assigns cell 4.

