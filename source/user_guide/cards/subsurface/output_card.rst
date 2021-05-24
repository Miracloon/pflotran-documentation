Back to :ref:`card-index`

.. _output-card:

OUTPUT
====== 
Defines the type and frequency of output.

Required Cards:
---------------
OUTPUT
 Opens output block. 

Optional Sub-blocks and Cards:
-------------------------------

SNAPSHOT_FILE
 Opens the snapshot output file block. A snapshot file gives the value of 
 specified variables over the entire domain at a single moment in time.

OBSERVATION_FILE
 Opens the observation output file block. An observation file gives the values 
 of specified variables at a point at several moments in time.

MASS_BALANCE_FILE
 Opens the mass balance output file block. Mass balance output will be 
 generated, which includes global mass balance as well as fluxes at all 
 boundaries for water and chemical species specified for output in the 
 :ref:`chemistry-card`.

Within the SNAPSHOT_FILE, OBSERVATION_FILE, and MASS_BALANCE_FILE blocks, the 
following cards can be specified:

 TIMES <string> <float> ... <float>
  Specifies a list of times when output will be generated. <string> indicates 
  the time unit applied to the following <float>s that indicate the times.

 PERIODIC TIMESTEP <int> 
  Generates output every <int> number of timesteps.

 PERIODIC TIME <int or float> <string>
  Generates output at every <int or float> units of time, where <string> defines 
  the units of time.

 NO_PRINT_INITIAL
  If included, the initial state of the system will not be printed to the output 
  file.

 NO_PRINT_FINAL
  If included, the final state of the system will not be printed to the output 
  file.

 EXTEND_HDF5_TIME_FORMAT
  Extends the time format in group names to 13 digits of precision (default = 6   digits of precision).  This better enables the printing of small time step.'

Within the SNAPSHOT_FILE and OBSERVATION_FILE blocks (but not 
MASS_BALANCE_FILE), the variables to be saved can be specified:

.. _output-variables:

 VARIABLES
  Opens a block which lists variables to be included in the output file. Options include: PERMEABILITY, PERMEABILITY_X, PERMEABILITY_Y, PERMEABILITY_Z, PERMEABILITY_XY, PERMEABILITY_XZ, PERMEABILITY_YZ, LIQUID_PRESSURE, LIQUID_SATURATION, LIQUID_DENSITY, LIQUID_HEAD, LIQUID_MOBILITY, LIQUID_ENERGY, LIQUID_MOLE_FRACTIONS, LIQUID_MASS_FRACTIONS, GAS_PRESSURE, GAS_SATURATION, GAS_DENSITY, GAS_MOBILITY, GAS_ENERGY, GAS_MOLE_FRACTIONS, GAS_MASS_FRACTIONS, AIR_PRESSURE, CAPILLARY_PRESSURE, VAPOR_PRESSURE, SATURATION_PRESSURE, THERMODYNAMIC_STATE, TEMPERATURE, RESIDUAL, POROSITY, EFFECTIVE_POROSITY, TORTUOSITY, MINERAL_POROSITY, MAXIMUM_PRESSURE, OIL_PRESSURE, OIL_SATURATION, OIL_DENSITY, OIL_MOBILITY, OIL_ENERGY, SOIL_COMPRESSIBILITY, SOIL_REFERENCE_PRESSURE, PROCESS_ID, VOLUME, MATERIAL_ID, K_ORTHOGONALITY_ERROR.  To obtain the most up to date list, look in output.F90:OutputVariableRead().
  If you do not include the ``VARIABLES`` block, then a default list of variables
  will be populated dependent on the flow mode. However, if you prefer no
  default output, you can turn defaults off by including ``NO_FLOW_VARIABLES`` 
  or ``NO_ENERGY_VARIABLES``.
  
Within the SNAPSHOT_FILE block only, the output file format can be specified:

 FORMAT <string>
  Specifies the output file type for snapshots in time. Options available include TECPLOT BLOCK, TECPLOT POINT, VTK, HDF5, HDF5 SINGLE_FILE, or HDF5 MULTIPLE_FILES.  The default for HDF5 is SINGLE_FILE. For HDF5 MULTIPLE_FILES, each snapshot will be printed into a new HDF5 file. The optional keyword TIMES_PER_FILE <int> can be included, which will limit the number of snapshots printed to each HDF5 file to <int> number of snapshots.  **The POINT format is not supported in parallel. PFLOTRAN will switch from POINT to BLOCK if the number of cores employed is greater than one.**

Within the MASS_BALANCE_FILE block only, you can specify the sub-block NO_PRINT_SOURCE_SINK which will not print out source and sinks to the mass ballance file and the sub-block TOTAL_MASS_REGIONS which specifies a list of regions where the total component mass is calculated within the region. The total component mass includes all species in the aqueous, sorbed, and precipitated states is outputted in [mols] (see examples below).

Optional Cards
--------------
The following cards are placed within the OUTPUT block, but outside of the
SNAPSHOT_FILE, OBSERVATION_FILE, or MASS_BALANCE_FILE blocks. 

PERIODIC_OBSERVATION TIME <float> <string>
  Generates output for observation points and mass balance at every <float> units of time, where <string> defines the units of time.

PERIODIC_OBSERVATION TIMESTEP <int>
  Generates output for observation points and mass balance at every <int> number of timesteps.

TIME_UNITS <string>
 Specifies the time units printed in screen and file output (e.g. s, day, yr)

SCREEN PERIODIC <int>
 Prints output to the screen every <int> time steps.

VARIABLES
 Opens the variables block. Variables listed outside of the ?_FILE blocks will applied to each ?_FILE block that did not specify its own variable list. If no variable list is specified within the ?_FILE blocks or within the OUTPUT block, defaults will be used.
 However, if you prefer no default output, you can turn defaults off by 
 including ``NO_FLOW_VARIABLES`` or ``NO_ENERGY_VARIABLES``.
 
VELOCITY_AT_CENTER / VELOCITY_AT_FACE


Examples
--------
 ::

  OUTPUT
    TIME_UNITS yr
    SNAPSHOT_FILE
      FORMAT HDF5 MULTIPLE_FILES TIMES_PER_FILE 10 
      NO_PRINT_INITIAL
      PERIODIC TIME 100 day
      VARIABLES
        LIQUID_PRESSURE
        GAS_PRESSURE
        CAPILLARY_PRESSURE
        TEMPERATURE
      /
    /
    OBSERVATION_FILE
      NO_PRINT_INITIAL
      NO_PRINT_FINAL
      TIMES y 0.23d0 9.712d0
      VARIABLES
        TEMPERATURE
        POROSITY
        PERMEABILITY
      /
    /
    MASS_BALANCE_FILE
      PERIODIC TIME 1 w between 1 y and 2 y
      PERIODIC TIMESTEP 5
      TOTAL_MASS_REGIONS
        all
        top
      /
    /
    SCREEN PERIODIC 15
  /

 ::

  OUTPUT
    VARIABLES
      LIQUID_PRESSURE
      POROSITY
      TORTUOSITY
    /
    SNAPSHOT_FILE
      FORMAT TECPLOT BLOCK
      PERIODIC TIME 1 y
    /
    OBSERVATION_FILE
      TIMES day 10 20 30
      NO_PRINT_FINAL
    /
  /

 ::

  OUTPUT
    VARIABLES
      NO_FLOW_VARIABLES
      NO_ENERGY_VARIABLES
    /
    SNAPSHOT_FILE
      FORMAT TECPLOT BLOCK
      PERIODIC TIME 1 y
    /
    OBSERVATION_FILE
      TIMES day 10 20 30
      NO_PRINT_FINAL
    /
  /
