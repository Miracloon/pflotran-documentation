Back to :ref:`card-index`

Back to :ref:`subsurface-flow-card`

Back to :ref:`mode-card`

.. _mphase-card:

MPHASE
======

Defines options for the MPHASE supercritical CO\ :sub:`2`\ subsurface flow mode.

Options
-------

  MAX_PRESSURE_CHANGE <float>
   Controls time step to not exceed maximum pressure change

  MAX_TEMPERATURE_CHANGE <float>
   Controls time step to not exceed maximum temperature change

  MAX_CONCENTRATION_CHANGE <float>
   Controls time step to not exceed maximum concentration change

  MAX_SATURATION_CHANGE <float>
   Controls time step to not exceed maximum saturation change

 
Examples
--------
::

 ...
 PROCESS_MODELS
   SUBSURFACE_FLOW flow
     MODE MPHASE
     OPTIONS
       MAX_PRESSURE_CHANGE 5.e4
       MAX_TEMPERATURE_CHANGE 5.d0
       MAX_CONCENTRATION_CHANGE 1.e-2
       MAX_SATURATION_CHANGE 0.025
     /
   /
 /
 ...
