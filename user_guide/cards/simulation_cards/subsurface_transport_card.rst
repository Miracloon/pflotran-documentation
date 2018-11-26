Back to :ref:`card-index`

.. _subsurface-transport-card:

SUBSURFACE_TRANSPORT
====================

Optional Cards
--------------

GLOBAL_IMPLICIT
  Specifies fully implicit coupling of transport and reaction.

MAX_VOLUME_FRACTION_CHANGE <float>    (default = 1.d0)
  Limits the time step based on the maximum desired change in mineral volume 
  fraction.

Examples
--------
::

 SIMULATION
   SIMULATION_TYPE SUBSURFACE
   PROCESS_MODELS
     SUBSURFACE_TRANSPORT transport
       GLOBAL_IMPLICIT
       MAX_VOLUME_FRACTION_CHANGE 1.d-4
     /
   /
 END

