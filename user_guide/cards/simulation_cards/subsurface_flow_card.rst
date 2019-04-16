Back to :ref:`card-index`

.. _subsurface-flow-card:

SUBSURFACE_FLOW
===============

Required Cards
--------------

:ref:`mode-card` <string>
 Specifies the flow mode to be employed.  Follow the links below for a 
 description of each flow mode's options. The options for <string> include:
 TH, GENERAL, RICHARDS, MPHASE, IMMIS, MISCIBLE, FLASH2, TOIL_IMS.

Water Modes
+++++++++++

 :ref:`richards-card`: single-phase variably saturated flow

 :ref:`th-card`: variably saturated flow and energy (and optional ice phase)

 :ref:`wipp-flow-card`: two-phase immiscible air-water

 :ref:`general-card`: two-phase air-water-energy

Supercritical CO\ :sub:`2`\  Modes
++++++++++++++++++++++++++++++++++

 :ref:`mphase-card`: supercritical CO\ :sub:`2`\-water-energy

 IMMIS: immiscible two-phase CO\ :sub:`2`\-water-energy

 MISCIBLE: miscible H\ :sub:`2`\O-glycol

 FLASH2: supercritical CO\ :sub:`2`\-water-energy

Optional Cards
--------------

OPTIONS 
 MODE-dependent block for defining options for each flow process model. Click 
 on the MODEs above to see MODE-dependent options. Options for all MODEs are
 listed below:

  MAX_XXX_CHANGE 
   Attempts to govern the time step size based on the specified 
   value of the variable:

   MAX_PRESSURE_CHANGE <float>  (default = 5.d5 [Pa])

   MAX_TEMPERATURE_CHANGE <float>  (default = 5.d0)

   MAX_CONCENTRATION_CHANGE <float>  (default = 1.d0)

   MAX_SATURATION_CHANGE <float>  (default = 0.5d0)

  PRESSURE_DAMPENING_FACTOR <float>
    Dampens the update vector by this value.

  MAX_CFL <float>
    Restricts flow process model timestep size to <= <float> specified.

  SKIP_RESTART
    On a restarted simulation, employs the initial condition for process 
    model instead of the restarted solution.

Examples
--------
::

 SIMULATION
   SIMULATION_TYPE SUBSURFACE
   PROCESS_MODELS
     SUBSURFACE_FLOW flow
       MODE GENERAL
       OPTIONS
         ISOTHERMAL
         TWO_PHASE_ENERGY_DOF TEMPERATURE
         GAS_COMPONENT_FORMULA_WEIGHT 2.01588d0
         MAX_PRESSURE_CHANGE 1.0d6
         PRESSURE_DAMPENING_FACTOR 0.6d0
         MAX_CFL 1.d0
       /
     /
   /
 END
