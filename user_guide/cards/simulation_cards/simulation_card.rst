Back to :ref:`card-index`

.. _simulation-card:

SIMULATION
==========
Defines the simulation type.

Required Cards:
---------------

SIMULATION
 Opens the SIMULATION block.

SIMULATION_TYPE <string>
 Specifies the type of simulation. Options for <string> include: SUBSURFACE,
 SURFACE_SUBSURFACE, HYDROGEOPHYSICS.

PROCESS_MODELS <string>
 Opens the PROCESS_MODELS block and lists the process models that are used in
 the simulation. Options for <string> include: :ref:`subsurface-flow-card`,
 :ref:`subsurface-transport-card`, SURFACE_FLOW. If 

 :ref:`mode-card` <string>
  Specifies the flow mode if SUBSURFACE_FLOW is chosen under PROCESS_MODELS. 
  Options for <string> are detailed in :ref:`mode-card`.
  
Optional Cards:
---------------

:ref:`checkpoint-card`
 Opens a block for specifying checkpointing parameters. Details can be found
 in :ref:`checkpoint-card`.
 
AUXILIARY <string>
 To be documented.
  
Examples
--------

::

  SIMULATION
    SIMULATION_TYPE SUBSURFACE
    PROCESS_MODELS
      SUBSURFACE_FLOW flow
	MODE GENERAL
      /
    /
  END
    
  SIMULATION
    SIMULATION_TYPE SUBSURFACE
    PROCESS_MODELS
      SUBSURFACE_TRANSPORT transport
	GLOBAL_IMPLICIT
      /
    /
  END
  
  SIMULATION
    SIMULATION_TYPE SUBSURFACE
    PROCESS_MODELS
      SUBSURFACE_FLOW flow
	MODE GENERAL
      /
      SUBSURFACE_TRANSPORT transport
	GLOBAL_IMPLICIT
      /
      AUXILIARY SALINITY
	SPECIES Tracer 58.442469d0
      /
    /
    CHECKPOINT
      PERIODIC TIMESTEP 10
    /
  END
  
  SIMULATION
    SIMULATION_TYPE SUBSURFACE
    PROCESS_MODELS
      SUBSURFACE_FLOW flow
	MODE TH
	OPTIONS
	  MAX_PRESSURE_CHANGE 1.e5
	  MAX_TEMPERATURE_CHANGE 5.
	/
      /
    /
  END

  SIMULATION
    SIMULATION_TYPE GEOMECHANICS_SUBSURFACE
    PROCESS_MODELS
      SUBSURFACE_FLOW flow
        MODE RICHARDS
      /
      GEOMECHANICS_SUBSURFACE geomech
    /
  END
