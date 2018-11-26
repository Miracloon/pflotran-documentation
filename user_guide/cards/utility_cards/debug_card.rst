Back to :ref:`card-index`

.. _debug-card:

DEBUG
===== 
Defines debugging options for writing data to the screen, output file and other 
external files.

Required Cards:
---------------
DEBUG
 Opens the DEBUG block.

Optional Cards:
---------------
PRINT_SOLUTION
 Prints current solution at each Newton iteration (filename = MODExx.dat).

PRINT_RESIDUAL
 Prints current residual at each Newton iteration (filename = MODEresidual.dat).

PRINT_JACOBIAN
 Prints current Jacobian at each Newton iteration (filename = MODEjacobian.dat).

PRINT_JACOBIAN_DETAILED
 Prints current detailed Jacobian at each Newton iteration, splitting out 
 individual contributions (e.g. accumulation, internal fluxes, bc fluxes, 
 src/sinks).  Not supported for all modes.

PRINT_JACOBIAN_NORM
 Prints norm of Jacobian at each Newton iteration.

PRINT_COUPLERS
 Prints each coupler to a file (for checking boundary connections).

PRINT_NUMERICAL_DERIVATIVES
 Not yet supported, but when finished, this will print the values of the 
 numerical derivative used to create the Jacobian matrix.

WAYPOINTS
 Prints a list of waypoints to the screen and to the pflotran.out file.

BINARY_FORMAT
  Saves the PETSc vectors and matrices in binary format. The default output 
  format for the PETSc vectors and matrices is ASCII.

Examples
--------
::

 DEBUG
   PRINT_SOLUTION
   PRINT_RESIDUAL
   PRINT_JACOBIAN
 END

