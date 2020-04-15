Back to :ref:`card-index`

.. _subsurface-transport-card:

SUBSURFACE_TRANSPORT
====================

Required Cards
--------------

MODE <string>
  Specifies the transport modes. Options include: GIRT, OSRT, NWRT.
   * GIRT - global implicit reactive transport
   * OSRT - operator split reactive transport (experimental)
   * NWT - nuclear waste transport (experimental)

Optional Cards
--------------

OPTIONS
 MODE-dependent block for defining options for each transport process model. 

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
       MODE GIRT
       OPTIONS
         MAX_VOLUME_FRACTION_CHANGE 1.d-4
       /
     /
   /
 END

