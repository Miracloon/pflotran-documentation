Back to :ref:`card-index`

.. _flow-condition-card:

FLOW_CONDITION
==============
Sets flow parameters used in setting up flow boundary and initial conditions 
and source/sinks.

Required Cards:
---------------
FLOW_CONDITION <string>
 Opens the FLOW_CONDITION block, where <string> is the assigned name of the 
 condition so that it can be referred to in cards 
 :ref:`boundary-condition-card`, :ref:`initial-condition-card`, or 
 :ref:`source-sink-card`.

TYPE
 Opens the TYPE sub-block. Within this sub-block, the type of the flow 
 condition is specified. Options for TYPE are specific to which mode you 
 are running in. 
  
TYPE in ``RICHARDS Mode``  
+++++++++++++++++++++++++
 There are three main option types in ``RICHARDS Mode``: PRESSURE <string>, 
 FLUX <string>, RATE <string>, where <string> specifies further options for
 each:
  
 TYPE [PRESSURE {DIRICHLET, HYDROSTATIC, SEEPAGE, CONDUCTANCE}, 
   RATE {MASS_RATE, VOLUMETRIC_RATE, SCALED_MASS_RATE, SCALED_VOLUMETRIC_RATE}, 
   FLUX {NEUMANN}]
         
  * PRESSURE DIRICHLET: specified a fixed pressure across the entire condition.

  * PRESSURE HYDROSTATIC: specifies a hydrostatic condition.

  * PRESSURE SEEPAGE: a seepage face condition is similar to a hydrostatic, 
    EXCEPT that flow may only come into the domain when the boundary face 
    pressure is above a user defined reference pressure. The flow out of the 
    domain is unmodified and is possible at all times. The default reference 
    pressure is atmospheric pressure.

  * PRESSURE CONDUCTANCE: the conductance type condition is designed to mimic a 
    lower permeability soil layer at the boundary of a domain (e.g. a mud layer 
    at the bottom of a river).  A conductance condition is similar to a seepage 
    face, EXCEPT that a conductance term (permeability/distance) is specified 
    through a CONDUCTANCE keyword.  The permeability of the boundary 
    grid cell and its size (i.e. distance from cell center to boundary) no 
    longer matter. The conductance coefficient is a fit parameter.

  * RATE MASS_RATE: specifies a mass extraction/injection rate.

  * RATE ENERGY_RATE: specifies an energy extraction/injection rate.

  * RATE VOLUMETRIC_RATE: specifies a volumetric extraction/injection rate.

  * RATE SCALED_MASS_RATE <string>: specifies an extraction/injection rate 
    scaled/distributed among grid cells in the coupled region, where <string>
    is one of the scaling options below.

  * RATE SCALED_VOLUMETRIC_RATE <string>: specifies a volumetric 
    extraction/injection rate  scaled/distributed among grid cells in the 
    coupled region, where <string> is one of the scaling options below.

    Scaling options:
      * PERM: scaling weighted as a function of cell volume and X permeability

      * NEIGHBOR_PERM: scaling weighted as a function of the interfacial area 
        and permeability of neighboring cells (in x,y)

      * VOLUME: scaling weighted as a function of cell volume

  * FLUX NEUMANN: specifies a Darcy flux. 

    
TYPE in ``GENERAL Mode``
++++++++++++++++++++++++
 There are eleven main option types in ``GENERAL Mode``: 
  
 TYPE [LIQUID_PRESSURE {DIRICHLET, HYDROSTATIC, SEEPAGE, HETEROGENEOUS_SURFACE_SEEPAGE, CONDUCTANCE}, 
     GAS_PRESSURE {DIRICHLET}, 
     LIQUID_SATURATION {DIRICHLET}, 
     GAS_SATURATION {DIRICHLET}, 
     TEMPERATURE {DIRICHLET}, 
     MOLE_FRACTION {DIRICHLET}, 
     RELATIVE_HUMIDITY {DIRICHLET}, 
     LIQUID_FLUX {NEUMANN}, 
     GAS_FLUX {NEUMANN}, 
     ENERGY_FLUX {NEUMANN}, 
     RATE {MASS_RATE, VOLUMETRIC_RATE, SCALED_MASS_RATE, SCALED_VOLUMETRIC_RATE, HETEROGENEOUS_MASS_RATE, HETEROGENEOUS_VOLUMETRIC_RATE}]
          
  * RATE for ``GENERAL Mode`` is the same as RATE for ``RICHARDS Mode``, see 
    above.
  
  * LIQUID_PRESSURE options are the same as PRESSURE for ``RICHARDS Mode``, see 
    above, EXCEPT LIQUID_PRESSURE HETEROGENEOUS_SURFACE_SEEPAGE <string>: ?
    
  * GAS_PRESSURE DIRICHLET:
  
  * LIQUID_SATURATION DIRICHLET: specifies a liquid phase saturation.
  
  * GAS_SATURATION DIRICHLET: specifies a gas phase saturation.
  
  * TEMPERATURE DIRICHLET: specifies a temperature.
  
  * ENERGY_FLUX NEUMANN: specifies an energy flux.
  
  * LIQUID_FLUX NEUMANN: specifies a liquid phase Darcy flux.
  
  * GAS_FLUX NEUMANN: specifies a gas phase Darcy flux.
  
  * RELATIVE_HUMIDITY DIRICHLET: specifies a relative humidity.
  
  * MOLE_FRACTION DIRICHLET: specifies a gas/fluid? mole fraction.
       
  * ``GENERAL Mode`` flow conditions must include a TEMPERATURE and a 
    MOLE_FRACTION or GAS_SATURATION/LIQUID_SATURATION (but not both SATURATION 
    and a MOLE_FRACTION).
    
  * Initial thermodynamic states for combinations of dirichlet-based conditions: 
  
    * GAS_PRESSURE + GAS_SATURATION = two-phase state, 
    
    * LIQUID_PRESSURE + MOLE_FRACTION = single-phase liquid state,
    
    * GAS_PRESSURE + (MOLE_FRACTION | RELATIVE_HUMIDITY) = single-phase gas 
      state
      
  * ``GENERAL Mode`` dirichlet-based pressure or temperature must include 
    TEMPERATURE, LIQUID_PRESSURE or GAS_PRESSURE, and 
    MOLE_FRACTION/RELATIVE_HUMIDITY (gas state only) or 
    GAS_SATURATION/LIQUID_SATURATION.

  
For each TYPE option specified in the TYPE sub-block described above, a
corresponding type-value card must be included that specifies the
value of the TYPE. The possible type-value cards include:

PRESSURE <float>
 The pressure [Pa] applied at the boundary.

LIQUID_PRESSURE <float>
 The liquid pressure [Pa] applied at the boundary.

GAS_PRESSURE <float>
 The gas pressure [Pa] applied at the boundary.

FLUX <float>
 The Darcy flux [m/s] applied to the boundary. Positive flux is inward, 
 negative outward, regardless of the direction of the boundary connection.

LIQUID_FLUX <float>
 The liquid Darcy flux [m/s] applied to the boundary. Positive flux is inward, 
 negative outward, regardless of the direction of the boundary connection.

GAS_FLUX <float>
 The gas Darcy flux [m/s] applied to the boundary. Positive flux is inward, 
 negative outward, regardless of the direction of the boundary connection.

TEMPERATURE <float>
 The temperature [C] applied at the boundary.

ENERGY_FLUX <float>
 The energy flux [MW/\ :sup:`2`\/s] applied to the boundary. Positive flux is 
 inward, negative outward, regardless of the direction of the boundary 
 connection.

RELATIVE_HUMIDITY <float>
 The relative humidity [-] applied at the boundary.

RATE <float> [<float> float>]
 Injection/extraction rate in kg/s (mass) or m\ :sup:`3`\/s (volumetric).  
 Positive in, negative out. For multiphase flow, the rate is by component and 
 energy (i.e. water component [kg/s], air component [kg/s], energy [MW]).

LIQUID_SATURATION <float>
 The liquid saturation [-] applied at the boundary.

GAS_SATURATION <float>
 The gas saturation [-] applied at the boundary.

MOLE_FRACTION <float>
 The gas mole fraction [-] applied at the boundary.

**A list or external file may be used instead of specifying a float using** 
**the keywords: LIST or FILE <string>.  To do so, one must provide an** 
**external file with a** :ref:`rank-one`.

Optional Cards:
---------------

DATUM <float float float>
 X,Y,Z coordinate of where the flow condition is applied.  I.e. If type is 
 PRESSURE HYDROSTATIC, the datum coordinate is where the PRESSURE value is set, 
 and other pressures in the vertical hydrostatic condition are calculated from 
 that reference point.

GRADIENT
 Gradient for the datum coordinate.  Gradient in X and Y is a unitless gradient 
 plane <dh/dx, dh/dy> based on change in elevation with change in direction.  
 Gradient in Z is in dp/dz, change in pressure [Pa] with respect to elevation.

 PRESSURE <float float float>
  Specifies the gradient in the x y z directions.

  **An external file may be used instead of specifying floats using the** 
  **keywords: FILE <string>.  To do so, one must provide an external file** 
  **with a** :ref:`rank-three`.

INTERPOLATION <string>
 Interpolation scheme used to calculate transient update, where the options
 for <string> include: [linear, step (default)].

CYCLIC
 Cycles a transient data set back to initial value when maximum data set time 
 is exceeded.

SYNC_TIMESTEP_WITH_UPDATE
 Forces waypoints to be set for each time in a timeseries. 

CONDUCTANCE <float>
 Conductance coefficient used when a conductance condition is specified.
 

Examples
--------

 ::

  FLOW_CONDITION Initial
    TYPE
      PRESSURE HYDROSTATIC
    /
    DATUM 0.d0 0.d0 105.016d0
    GRADIENT
      PRESSURE -1.9542d-4 1.4240d-4 0.d0
    /
    PRESSURE 101325.d0
  /

  FLOW_CONDITION Piezometric_Surface
    TYPE
      PRESSURE HYDROSTATIC
    /
    CYCLIC
    DATUM FILE ./A_datum_2008.txt
    GRADIENT
      PRESSURE FILE ./A_gradient_2008.txt
    /
    PRESSURE 101325.d0
  /

  FLOW_CONDITION Recharge
    TYPE
      FLUX NEUMANN
    /
    FLUX 1.757d-9 ! [m/s]
  /

  FLOW_CONDITION injection
    TYPE
      RATE SCALED_VOLUMETRIC_RATE NEIGHBOR_PERM
    /
    RATE 1 m^3/day
  /

  FLOW_CONDITION injection
    TYPE
      RATE SCALED_VOLUMETRIC_RATE 
    /
    RATE FILE transient_rate.txt 
  /

  FLOW_CONDITION injection
    TYPE
      RATE SCALED_VOLUMETRIC_RATE 
    /
    : to inject at 2 m^3/day between days 10-15.
    SYNC_TIMESTEP_WITH_UPDATE
    RATE LIST
      TIME_UNITS day
      DATA_UNITS m^3/day
      0. 0.
      10. 2.
      15. 0.
    /
  /

  ! Distributes a mass rate of 0.02 kg/day across all grid cells in region, scaled
  ! by fraction cell volume / total volume
  FLOW_CONDITION injection
    TYPE
      RATE SCALED_MASS_RATE VOLUME
    /
    RATE 2.d-2 kg/day
  END  

``GENERAL Mode`` Examples
+++++++++++++++++++++++++

 ::

  FLOW_CONDITION Liquid
    TYPE
      LIQUID_PRESSURE DIRICHLET
      MOLE_FRACTION DIRICHLET
      TEMPERATURE DIRICHLET
    /
    LIQUID_PRESSURE 2.d5
    MOLE_FRACTION 1.d-8
    TEMPERATURE 25.d0
  /

  FLOW_CONDITION Two_Phase
    TYPE
      GAS_PRESSURE DIRICHLET
      GAS_SATURATION DIRICHLET
      TEMPERATURE DIRICHLET
    /
    GAS_PRESSURE 2.d5
    GAS_SATURATION 0.25d0
    TEMPERATURE 25.d0
  /
  
  FLOW_CONDITION east_face
    TYPE
      TEMPERATURE dirichlet
      LIQUID_PRESSURE dirichlet
      MOLE_FRACTION dirichlet
    /
    TEMPERATURE DATASET temperature_bc_east
    LIQUID_PRESSURE 101325 Pa
    MOLE_FRACTION 1.d-20
  END

  FLOW_CONDITION Two_Phase ! alternate
    TYPE
      GAS_PRESSURE DIRICHLET
      LIQUID_SATURATION DIRICHLET
      TEMPERATURE DIRICHLET
    /
    GAS_PRESSURE 2.d5
    LIQUID_SATURATION 0.75d0
    TEMPERATURE 25.d0
  /
  
  FLOW_CONDITION west_face
    TYPE
      ENERGY_FLUX neumann
      LIQUID_FLUX neumann
      GAS_FLUX neumann
    /
    ENERGY_FLUX -1.0d0 W/m^2
    LIQUID_FLUX 0.d0 m/yr
    GAS_FLUX 0.d0 m/yr
  END

  FLOW_CONDITION Gas
    TYPE
      GAS_PRESSURE DIRICHLET
      MOLE_FRACTION DIRICHLET
      TEMPERATURE DIRICHLET
    /
    GAS_PRESSURE 2.d5
    MOLE_FRACTION 0.01d0
    TEMPERATURE 25.d0
  /

  FLOW_CONDITION Gas2
    TYPE
      GAS_PRESSURE DIRICHLET
      RELATIVE_HUMIDITY DIRICHLET
      TEMPERATURE DIRICHLET
    /
    GAS_PRESSURE 2.d5
    RELATIVE_HUMIDITY 50 ! in percent
    TEMPERATURE 25.d0
  /

  ! example for an source/sink injection well
  FLOW_CONDITION well
    TYPE
      RATE mass_rate
    /
       ! liquid gas   energy
    RATE 0.d0   1.d-5 0.d0 kg/s kg/s MW
  /
  
  FLOW_CONDITION left_end
    TYPE
      TEMPERATURE dirichlet
      LIQUID_PRESSURE dirichlet
      MOLE_FRACTION dirichlet
    /
    TEMPERATURE LIST
      # T = Tb*t; Tb=2C
      TIME_UNITS day
      DATA_UNITS C
      INTERPOLATION LINEAR
      #time  #temperature
      0.00d0 0.0d0
      0.25d0 0.5d0
      0.50d0 1.0d0
      1.00d0 2.0d0
    /
    LIQUID_PRESSURE 101325 Pa
    MOLE_FRACTION 1.d-10
  END

