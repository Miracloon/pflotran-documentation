Back to :ref:`card-index`

Back to :ref:`subsurface-flow-card`

Back to :ref:`mode-card`

.. _general-card:

GENERAL
=======
Defines options for the General subsurface flow mode.

Options
-------

GAS_COMPONENT_FORMULA_WEIGHT <float>
 Specifies the molecular weight of the gas component in grams per mole.

ISOTHERMAL
 Disables the energy calculation.

IMMISCIBLE
 Disables solubility calculations.

NO_AIR
 Disables the gas component calculation.

MAX_ITERATION_BEFORE_DAMPING <integer>
 Specifies the threshold number of Newton iterations before damping is imposed.

DAMPING_FACTOR <float>
 The scalar value by which the solution is damped between each Newton-Raphson iteration. Acceptable values on (0,1].

ANALYTICAL_JACOBIAN
 Jacobian entries are calculated using analytical deriatives.

**State Change Options**

PHASE_CHANGE_EPSILON <float>
 Assign a fixed initial saturation of a new phase that is created upon a state change.

RESTRICT_STATE_CHANGE
 Restricts any changes of state to only occur once per Newton iteration.

WINDOW_EPSILON <float>
 Specifies the tolerance or window that must be exceeded before state change
 will occur.

**Newton Solver Options**

MAX_NEWTON_ITERATIONS <integer>
 Specify the maximum number of allowable Newton iterations. Default is 8.

LOGGING_VERBOSITY <integer>
 [1] Enables more verbose logging of Newton-Raphson convergence metrics.

USE_INFINITY_NORM_CONVERGENCE
 Newton iteration will converge on infinity norm convergence criteria for both the solution update and the residual.

**Scaled Residual (Residual / Accumulation term) Convergence Tolerances**

RESIDUAL_SCALED_INF_TOL or ITOL_SCALED_RESIDUAL <float>
 Specify a single infinity norm convergence tolerance on all scaled residuals. Default is 1e-5.

LIQUID_RESIDUAL_SCALED_INF_TOL <float>
 Specify the infinity norm convergence tolerance on the scaled residual of water mass (liquid phase).

GAS_RESIDUAL_SCALED_INF_TOL <float>
 Specify the infinity norm convergence tolerance on the scaled residual of solute mass (gas phase primary component).

ENERGY_RESIDUAL_SCALED_INF_TOL <float>
 Specify the infinit norm convergence tolerance on the scaled residual of energy.

**Solution Update Convergence Tolerances**

UPDATE_INF_TOL <float>
 Specify a single infinity norm convergence tolerance on the absolute value and relative updates of all solution updates at a given time step.

ABS_UPDATE_INF_TOL <float>
 Specify a single infinity norm convergence tolerance on the absolute value of all solution updates at a given time step.

REL_UPDATE_INF_TOL <float>
 Specify a single infinity norm convergence tolerance on the relative solution update at a given time step.

PRES_ABS_UPDATE_INF_TOL <float>
 Specify a single maximum absolute change in liquid phase, gas phase, and air partial pressure over a given time step.

LIQUID_PRES_ABS_UPDATE_INF_TOL <float>
 Specify a maximum absolute change in liquid phase pressure over a given time step.

GAS_PRES_ABS_UPDATE_INF_TOL <float>
 Specify a maximum absolute change in gas phase pressure over a given time step.

AIR_PRES_ABS_UPDATE_INF_TOL <float>
 Specify a maximum absolute change in air partial pressure in the gas phase over a given time step.

TEMP_ABS_UPDATE_INF_TOL <float>
 Specify a maximum absolute change in temperature over a given time step.

SAT_ABS_UPDATE_INF_TOL <float>
 Specify a maximum absolute change in phase saturation over a given time step.

XMOL_ABS_UPDATE_INF_TOL <float>
 Specity a maximum absolute change in solute mass fraction in the aqueous phase over a given time step.

PRES_REL_UPDATE_INF_TOL <float>
 Specify a single maximum relative change in liquid phase, gas phase, and air partial pressure over a given time step. 

LIQUID_PRES_REL_UPDATE_INF_TOL <float>
 Specify a maximum relative change in liquid phase pressure over a given time step.

GAS_PRES_REL_UPDATE_INF_TOL <float>
 Specify a maximum relative change in gas phase pressure over a given time step.

AIR_PRES_REL_UPDATE_INF_TOL <float>
 Specify a maximum relative change in air pressure over a given time step.

TEMP_REL_UPDATE_INF_TOL <float>
 Specify a maximum relative change in temperature over a given time step.

SAT_REL_UPDATE_INF_TOL <float>
 Specify a maximum relative change in phase saturation over a given time step.

XMOL_REL_UPDATE_INF_TOL <float>
 Specify a maximum relative change in mass fraction of solute in the aqueous phase over a given timestep.

NO_STATE_TRANSITION_OUTPUT
 Eliminates “State Transition” screen output. E.g. *State Transition: 2 Phase -> Gas at Cell 23331*

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

