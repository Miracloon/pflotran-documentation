Back to :ref:`card-index`

.. _restart-card:

RESTART
=======
Specifies restart options so you can continue running a simulation where it 
left off.

Required Cards:
---------------
RESTART <string> <optional RESET>
 Specifies the name of the restart file and, optionally, the keyword RESET
 that forces the simulation to revert back to the initial simulation time
 (0. unless otherwise specified in the input file).

Examples
--------
Restart the program running from where it left off when the file 
``pflotran.chk3000`` was printed:
 
::

  RESTART pflotran.chk3000

Restart the simulation from the end of the previous simulation, but set the 
time back to the initial simulation time:

::

 RESTART restart.chk RESET
