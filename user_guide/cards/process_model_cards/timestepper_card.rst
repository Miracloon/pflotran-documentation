Back to :ref:`card-index`

.. _timestepper-card:

TIMESTEPPER
===========
Specifies time step acceleration, maximum number of time steps, etc. 

Required Cards:
---------------
TIMESTEPPER <string>
 Specifies the type of timestepper, where <string> is FLOW or TRANSPORT.

Optional Cards:
---------------
NUM_STEPS_AFTER_TS CUT <int>
 Number of time steps after a time step cut that the time step size must be held 
 constant.  Use 0 to ramp up immediately.

MAX_STEPS <int>
 Maximum time step after which the simulation will be terminated

TS_ACCELERATION <int>
 Integer indexing time step acceleration ramp (**expert users only**). Use in 
 conjunction with DT_FACTOR.

MAX_TS_CUTS <int>
 Maximum number of consecutive time step cuts before the simulation is 
 terminated with plot of the current solution printed to a 
 ``XXX_cut_to_failure.tec`` file for debugging.

MAX_NUM_CONTIGUOUS_REVERTS <int>
 When a time step is cut to match a sync (e.g. waypoint), the previous time
 step size is stored and the time step is set back to that previous value 
 after the sync. This setting ensures that the previous time step size is 
 stored for up to MAX_NUM_CONTIGUOUS_REVERTS times before the previous 
 time step size is discarded.

DT_FACTOR <float array>
 Array of floating point numbers of tfac array (**expert users only**). Values 
 specify time step multiplier as a function of number of Newton iterations in
 consecutive order from 1 Newton iteration to TS_ACCELERATION Newton iterations.

TIMESTEP_REDUCTION_FACTOR <float>
 The factor by which the time step will be reduced when it is cut (default: 0.5).

TIMESTEP_MAXIMUM_GROWTH_FACTOR <float>
 The maximum factor by which the time step can be increased between time steps (default: 2.).

INITIALIZE_TO_STEADY_STATE
 Flag requesting that a steady state solution be computed based on boundary and 
 initial conditions at the beginning of the simulation (**Warning: not robust**)

RUN_AS_STEADY_STATE
 Flag indicating that the simulation is to be run as steady state 
 (**Warning: not robust**)

Examples
--------
 ::

  TIMESTEPPER FLOW
    TS_ACCELERATION 8
    MAX_STEPS 10000  ! terminates simulation after 10,000 time steps
    MAX_TS_CUTS 5    ! terminates simulation after 5 consecutive time step cuts
  END
