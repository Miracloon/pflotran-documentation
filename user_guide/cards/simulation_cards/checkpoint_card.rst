Back to :ref:`card-index`

.. _checkpoint-card:

CHECKPOINT
==========
Defines checkpointing options for restart capability.

Required Cards:
---------------

CHECKPOINT
 Opens the CHECKPOINT block, although block form is not required if only one 
 option is specified. The checkpoint card block must be located within the 
 :ref:`simulation-card` block.

At least one of the following must be used:

TIMES <time_unit> <double> <double> . . . <double>
 Specifies the points in time when checkpoint file output is desired, where 
 <time_unit> indicates the units of the points in time, and <double> is each 
 point in time. 
 Any number of specific time points can be listed.

PERIODIC TIME <double> <time_unit>
 Specifies a time interval for checkpoint file output, where <double> is the 
 length of the time interval, and <time_unit> indicates the units of the time
 interval.

PERIODIC TIMESTEP <int>
 Outputs checkpoint files every <int> number of timesteps. 
 This option is identical to CHECKPOINT <int>.

Optional Cards:
---------------

FORMAT <string>
 Indicates the checkpoint file format. Only <string> = BINARY or HDF5 supported.
 If FORMAT is not specified, the default format is BINARY.

**If a periodic timestep is chosen, checkpoint files will be named** 
**"pflotran-ts<int>.chk", where "ts" stands for timestep, and <int> is the** 
**time step number when the file was printed. If a periodic time, or specific** 
**times were chosen, checkpoint files will be named** 
**"pflotran-<double><time_unit>.chk", where <double> is the simulation time,** 
**and <time_unit> is the unit of time specified in the CHECKPOINT card block.** 
**If the simulation completes (i.e. it reaches the final time), an additional** 
**checkpoint file appended with "-restart.chk" will also be written, where one**
**can increase the final time and pick up from where the simulation stopped.**

Examples
--------
 ::

  SIMULATION
    SIMULATION_TYPE SUBSURFACE
    PROCESS_MODELS
      SUBSURFACE_FLOW flow
        ...
      /
      SUBSURFACE_TRANSPORT transport
        ...
      /
    /
    CHECKPOINT
      PERIODIC TIMESTEP 5
      TIMES y 10. 20. 25. 50. 55.
      FORMAT HDF5
    /
    RESTART restart.chk 0.
  END

