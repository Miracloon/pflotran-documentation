Back to :ref:`card-index`

Back to :ref:`subsurface-flow-card`

Back to :ref:`mode-card`

.. _wipp-flow-card:

WIPP_FLOW
=========
Defines options for the WIPP_FLOW subsurface flow mode.

Options
-------
LIQUID_RESIDUAL_INFINITY_TOL <float>
 Infinity norm tolerance for liquid residual equation. Units depend on the units of the residual: [kg/m\ :sup:`3` \] with BRAGFLO_RESIDUAL_UNITS and [kmol/sec] without. Default = 1.e-2

GAS_RESIDUAL_INFINITY_TOL <float>
 Infinity norm tolerance for gas residual equation. Units depend on the units of the residual: [kg/m\ :sup:`3`\] with BRAGFLO_RESIDUAL_UNITS and [kmol/sec] without. Default = 1.e-2

MAX_ALLOW_REL_LIQ_PRES_CHANG_NI <float>
 Maximum allowable relative change in liquid pressure between Newton iterations. Default = 1.e-2

MAX_ALLOW_REL_GAS_SAT_CHANGE_NI <float>
 Maximum allowable relative change in gas saturation between Newton iterations. Default = 1.e-3

MAX_ALLOW_LIQ_PRES_CHANGE_TS <float>
 Maximum absolute change in liquid pressure during a time step. Default = 1e7
 
MAX_ALLOW_GAS_SAT_CHANGE_TS <float>
 Maximum absolute change in gas saturation during a time step. Default = 1

GAS_COMPONENT_FORMULA_WEIGHT <float>
 Molecular weight of gas component gas phase. Default = 2.01588 for H\ :sub:`2(g)`\

BRAGFLO_RESIDUAL_UNITS
 Forces the residual calculation to be expressed in units of kg/m\ :sup:`3` \ instead of kmol/sec.

MATCH_BRAGFLO_OUTPUT
 Prints screen output in format more compatible with BRAGFLO for comparison purposes.

REL_LIQ_PRESSURE_PERTURBATION <float>
 Relative liquid pressure perturbation for derivatives.

MIN_LIQ_PRESSURE_PERTURBATION <float>
 Minimum liquid pressure perturbation for derivatives.

REL_GAS_SATURATION_PERTURBATION <float>
 Relative gas saturation perturbation for derivatives.

MIN_GAS_SATURATION_PERTURBATION <float>
 Minimum gas saturation perturbation for derivatives.

GAS_SAT_THRESH_FORCE_TS_CUT <float>
 Gas saturation threshold forcing a time step cut. If the gas saturation is outside the bounds of -GAS_SAT_THRESH_FORCE_TS_CUT and 1+GAS_SAT_THRESH_FORCE_TS_CUT, the time step will be cut immediately. Default = 0.2

GAS_SAT_THRESH_FORCE_EXTRA_NI <float>
 Gas saturation threshold forcing an extra Newton iteration. If the gas saturation is outside the bounds of -GAS_SAT_THRESH_FORCE_EXTRA_NI and 1+GAS_SAT_THRESH_FORCE_EXTRA_NI, an extra Newton iteration will be required. Default = 1.e-3

MIN_LIQ_PRES_FORCE_TS_CUT <float>
 The minimum liquid pressure below which Newton iteration will cease and the time step will be cut. Default = -1.e8

GAS_SAT_CHANGE_TS_GOVERNOR <float>
 Time step size will be reduced on the subsequent time step when the maximum change in gas saturation is above the governor value. Default = 0.3

LIQ_PRES_CHANGE_TS_GOVERNOR <float>
 Time step size will be reduced on the subsequent time step when the maximum change in liquid pressure is above the governor value. Default = 5.e5

GAS_SAT_GOV_SWITCH_ABS_TO_REL <float>
 When the gas saturation is greater than this value, a relative change in gas saturation will be used to calculate the new time step size based on the GAS_SAT_CHANGE_TS_GOVERNOR, while absolute change is used below the value. Default = 0.01

MINIMUM_TIMESTEP_SIZE <float>
 Value below which the time step size is truncated to MINIMUM_TIMESTEP_SIZE. Default = 8.64e-4 sec.
 
CONVERGENCE_TEST <string>
 BOTH - Both the residual infinity tolerance and absolute/relative change criteria must be met to declare convergence.
 EITHER - Either the residual infinity tolerance or absolute/relative change criter ia must be met to declare convergence.
 Defalt = BOTH

ALLOW_NEGATIVE_GAS_PRESSURE
 Allow gas pressure to drop below zero during Newton iteration and at the end of the time step. Default = TRUE

HARMONIC_PERMEABILITY_ONLY
 Perform harmonic averaging only on permeability for the flux calculation, instead of the full term. Default = FALSE

DEFAULT_ALPHA
 Allows one to bypass the reading of ALPHA. It is assumed that ALPHA does not factor into the interfacial areas between cells. Default = FALSE

ALPHA_DATASET <string>
 Specifies a cell-indexed dataset from which ALPHA values are read that define flaring in a 2D grid.

ELEVATION_DATASET <string>
 Specifies a cell-indexed dataset from which ELEVATION value (grid cell z coordinates) are read. Supercedes DIP_ROTATION_XXX cards.

DIP_ROTATION_ANGLE <float>
 Specifies the rotation angle (in degrees) from horizontal for dip (positive upward).

DIP_ROTATION_ORIGIN <float, float, float>
 Specifies the x,y,z origin for dip.

DIP_ROTATION_CEILING
 Specifies the ceiling for applying dip. Above this z coordinate (in the original grid), rotation will NOT be applied.

DIP_ROTATION_BASEMENT
 Specifies the basement for applying dip. Below this z coordinate (in the original grid), rotation will NOT be applied.

DIP_ROTATION_REGIONS
 Specifies names of regions where dip rotation will be applied. This useful for cells above the ceiling or below the basement (e.g. a shaft).

JACOBIAN_PRESSURE_DERIV_SCALE
 Scalign factor for the liquid pressure derivative. Default = 1.e7

SCALE_JACOBIAN
 Toggles on scaling of the linear system. The Jacobian pressure derivatives are first right-hand scaled by JACOBIAN_PRESSURE_DERIV_SCALE, and then the Jacobian is left-hand scaled by the reciprocal of the maximum absolute value in each row. Default = TRUE

DO_NOT_SCALE_JACOBIAN
 Turns off Jacobian scaling.

2D_FLARED_DIRICHLET_BCS <string>
 Enables Dirichlet boundary conditions to be specified at cell centers through a list of cells ids and the initial condition. The entries are read from the file named by *string*, with each entry providing the cell ID and flags for whether the *pressure* and *saturation* are held constant.

Debugging Options
-----------------
RESIDUAL_TEST
 Toggle on printing of residual information at a specific cell. RESIDUAL_TEST_CELL must be defined.

RESIDUAL_TEST_CELL
 Cell at which residual information will be printed when RESIDUAL_TEST is present.

JACOBIAN_TEST
 Toggles on testing of numerical Jacobian usign full residual evaluation.

JACOBIAN_TEST_RDOF
 Residual equation that will be printed for JACOBIAN_TEST (X in dR/dX).

JACOBIAN_TEST_XDOF
 Unknown that will be printed for JACOBIAN_TEST (R in dR/dX).

NO_ACCUMULATION
 Skip accumulation term calculation.

NO_FLUX
 Skip internal flux calculation.

NO_BCFLUX
 Skip boundary flux calculation.

NO_FRACTURE
 Skip fracture.

NO_CREEP_CLOSURE
 Skip creep closure.

NO_GAS_GENERATION
 Skip gas generation.

PRINT_RESIDUAL
 Print the residual to a file *pf_residual.txt* at each Newton iteration.

PRINT_SOLUTION
 Print the solution to a file *pf_solution.txt* at each Newton iteration.

PRINT_UPDATE
 Print the update to a file *pf_update.txt* at each Newton iteration.

DEBUG
 Toggles on increasing verbose output for debugging.

DEBUG_GAS_GENERATION
 Increasingly verbose information for gas generation from pm_wipp_srcsink.

DEBUG_FIRST_ITERATION
 Stops the simulation after the first Newton iteration when debugging is toggled on.
 
DEBUG_OSCILLATORY_BEHAVIOR
 Turns on increasingly verbose information for a cell where the residual is oscilating.

DEBUG_TS_UPDATE
 Prints dtime(1:2) ramping factors used in updating the time step size.

USE_BRAGFLO_CC
 Toggles the use of characteristic curves exactly as coded in BRAGFLO. The code was lifted from BRAGFLO and wrapped for use in PFLOTRAN for debugging purposes.

Examples
--------
::

 ...
 PROCESS_MODELS
   SUBSURFACE_FLOW flow
     MODE WIPP_FLOW
     OPTIONS
       GAS_COMPONENT_FORMULA_WEIGHT 2.01588d0 #hardwired
       2D_FLARED_DIRICHLET_BCS
         EXTERNAL_FILE ../dirichlet_bcs.txt
       /
       ALLOW_NEGATIVE_GAS_PRESSURE
       ALPHA_DATASET alpha
       BRAGFLO_RESIDUAL_UNITS
       CONVERGENCE_TEST BOTH                  ! ICONVTEST 1
       DIP_ROTATION_ANGLE 1.d0
       DIP_ROTATION_ORIGIN 23495.7d0 0.d0 378.685d0
       DIP_ROTATION_CEILING 779.69d0
       DIP_ROTATION_BASEMENT 178.07d0
       DIP_ROTATION_REGIONS rSHFTU
       GAS_RESIDUAL_INFINITY_TOL 1.d-2        ! FTOL_PRES
       GAS_SAT_CHANGE_TS_GOVERNOR 0.3d0       ! SATNORM
       GAS_SAT_GOV_SWITCH_ABS_TO_REL 1.d0     ! TSWITCH
       GAS_SAT_THRESH_FORCE_EXTRA_NI 1.d-3    ! SATLIMIT
       GAS_SAT_THRESH_FORCE_TS_CUT 0.2d0      ! DSATLIM
       LIQUID_RESIDUAL_INFINITY_TOL 1.d-2     ! FTOL_SAT
       LIQ_PRES_CHANGE_TS_GOVERNOR 5.d5       ! PRESNORM
       MAX_ALLOW_GAS_SAT_CHANGE_TS 1.d0       ! DSAT_MAX
       MAX_ALLOW_LIQ_PRES_CHANGE_TS 1.d7      ! DPRES_MAX
       MAX_ALLOW_REL_GAS_SAT_CHANGE_NI 1.d-3  ! EPS_SAT
       MAX_ALLOW_REL_LIQ_PRES_CHANG_NI 1.d-2  ! EPS_PRES
       MINIMUM_TIMESTEP_SIZE 8.64d-4          ! DELTMIN
       MIN_LIQ_PRES_FORCE_TS_CUT -1.d8        ! DPRELIM
       SCALE_JACOBIAN                         ! LSCALE
     /
   /
 /
 ...

