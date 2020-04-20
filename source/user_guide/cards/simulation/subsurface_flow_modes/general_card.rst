Back to :ref:`card-index`

Back to :ref:`subsurface-flow-card`

Back to :ref:`subsurface-flow-mode-card`

.. _general-card:

GENERAL
=======
Defines options for the General subsurface flow mode.

:ref:`general-simulation-options`

:ref:`general-newton-options`

.. _general-simulation-options:

SIMULATION Options 
------------------
*(under SUBSURFACE_FLOW in SIMULATION PROCESS_MODELS block)*

.. include:: sim_general.tmp

.. _general-newton-options:

NEWTON_SOLVER Options
---------------------

.. include:: newton_general.tmp

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

 ...
 PROCESS_MODELS
    SUBSURFACE_FLOW flow
      MODE GENERAL
      OPTIONS
        LOGGING_VERBOSITY 1
        ANALYTICAL_JACOBIAN
        RESTRICT_STATE_CHANGE
        USE_INFINITY_NORM_CONVERGENCE
        DAMPING_FACTOR 0.8
        PHASE_CHANGE_EPSILON 1.d-6
        REL_UPDATE_INF_TOL 1.d-4
        RESIDUAL_INF_TOL 1.d-6
        IMMISCIBLE
        MAX_NEWTON_ITERATIONS 8
      /
    /
  /

 ...

