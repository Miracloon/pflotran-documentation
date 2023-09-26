Back to :ref:`card-index`

Back to :ref:`subsurface-geophysics-card`

Back to :ref:`subsurface-geophysics-mode-card`

.. _ert-card:

ERT
===

Defines options for the ERT geophysics mode

:ref:`ert-simulation-options`

.. _ert-simulation-options:

SIMULATION Options 
------------------
*(under SUBSURFACE_GEOPHYSICS in SIMULATION PROCESS_MODELS block)*

**Basic Settings**

ARCHIE_CEMENTATION_EXPONENT
 Archie's cementation exponent.

ARCHIE_SATURATION_EXPONENT
 Archie's saturation exponent.

ARCHIE_TORTUOSITY_EXPONENT
 Archie's tortuosity exponent.

CALC_MAX_TRACER_CONCENTRATION
 Causes the maximum tracer concentration to be calculated based on the initial concentrations specified in the initial and boundary condition and source/sinks.

CLAY_VOLUME_FACTOR

COMPUTE_JACOBIAN
 Toggles on the calculation of the ERT Jacobian (derivatives of ERT measurements with respectd to bulk electrical conductivity).

CONDUCTIVITY_MAPPING_LAW
 Approach to calculating bulk electrical conductivity. Options: ARCHIE, WAXMAN_SMITS

MAX_TRACER_CONCENTRATION

MOBILITY_DATABASE

NO_ANALYTICAL POTENTIAL

OUTPUT_ALL_SURVEYS

SURFACE_ELECTRICAL_CONDUCTIVITY

SURVEY_TIMES

TRACER_CONDUCTIVITY

WATER_CONDUCTIVITY

WAXMAN_SMITS_CLAY_CONDUCTIVITY

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
