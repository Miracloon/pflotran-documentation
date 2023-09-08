Back to :ref:`card-index`

.. _subsurface-geophysics-card:

SUBSURFACE_GEOPHYSICS
=====================

Required Cards
--------------

:ref:`subsurface-geophysics-mode-card` <string>
 Specifies the geophysics mode to be employed.  Follow the links below for a 
 description of each geophysics mode's options. 

Flow Modes
++++++++++

 :ref:`ert-card`: electrical resistivity tomography

Optional Cards
--------------

OPTIONS 
 MODE-dependent block for defining options for each geophysics process model. 
 Click on the MODEs above to see MODE-dependent options.

Examples
--------
::

 SIMULATION
   SIMULATION_TYPE SUBSURFACE
   PROCESS_MODELS
     SUBSURFACE_GEOPHYSICS geophysics
       MODE ERT
       OPTIONS
         COMPUTE_JACOBIAN
         OUTPUT_ALL_SURVEYS
       /
     /
   /
 END

 SIMULATION
   SIMULATION_TYPE SUBSURFACE
   PROCESS_MODELS
     SUBSURFACE_FLOW flow
       MODE ZFLOW
       OPTIONS
         PROCESSES
           LIQUID_FLOW
           SOLUTE_TRANSPORT
         /
         LIQUID_DENSITY 998.32d0 kg/m^3
         LIQUID_VISCOSITY 8.9d-4
       /
     /
     SUBSURFACE_GEOPHYSICS geophysics
       MODE ERT
       OPTIONS
         COMPUTE_JACOBIAN
         MAX_TRACER_CONCENTRATION 1.d-3
         TRACER_CONDUCTIVITY 1.d-7
         SURVEY_TIMES h 2.7778d-4 6.d0 12.d0 24.d0 # 2.778d-4 ~= 1 second
         OUTPUT_ALL_SURVEYS
       /
     /
   /
 END
