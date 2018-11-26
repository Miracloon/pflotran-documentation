Back to :ref:`card-index`

Back to :ref:`subsurface-flow-card`

Back to :ref:`mode-card`

.. _general-card:

GENERAL
=======
Defines options for the General subsurface flow mode.

Options
-------

WINDOW_EPSILON <float>
 Specifies the tolerance or window that must be exceeded before phase change 
 will occur.
 
GAS_COMPONENT_FORMULA_WEIGHT <float>
 Specifies the molecular weight of the gas component in grams per mole.
 
TWO_PHASE_ENERGY_DOF <string>
 Specifies the unknown solved for the energy degree of freedom.  
 Options are: AIR_PRESSURE, TEMPERATURE.

ISOTHERMAL
 Disables the energy calculation.
 
NO_AIR
 Disables the gas component calculation.
 
MAXIMUM_PRESSURE_CHANGE <float>
 Truncates maximum pressure change in a Newton iteration. (Not to be confused 
 with MAX_PRESSURE_CHANGE in OPTIONS of process model block.)

MAX_ITERATION_BEFORE_DAMPING <integer>
 Specifies the threshold number of Newton iterations before damping is imposed.

DAMPING_FACTOR <float>
 The scalar value by which the solution is damped once damping is imposed. 
  
Examples
--------
::

 ...
 PROCESS_MODELS
   SUBSURFACE_FLOW flow
     MODE GENERAL
     OPTIONS
       !WINDOW_EPSILON 1.d-4
       ISOTHERMAL
       TWO_PHASE_ENERGY_DOF TEMPERATURE
       GAS_COMPONENT_FORMULA_WEIGHT 2.01588D0 ! kg/kmol
       MAXIMUM_PRESSURE_CHANGE 1.0D6 ! truncates pressure change
     /
   /
 /
 ...
