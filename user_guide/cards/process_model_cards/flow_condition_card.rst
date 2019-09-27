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

.. leaving out heterogeneous conditions for now as they are mainly support
   by surface flow and more of an expert capability
  
TYPE specification in RICHARDS and TH flow modes
++++++++++++++++++++++++++++++++++++++++++++++++
 TYPE 
  [PRESSURE {DIRICHLET, HYDROSTATIC, SEEPAGE, CONDUCTANCE, DIRICHLET_SEEPAGE,
  DIRICHLET_CONDUCTANCE}, 
  RATE {MASS_RATE, VOLUMETRIC_RATE, SCALED_MASS_RATE, SCALED_VOLUMETRIC_RATE}, 
  FLUX {NEUMANN},
  TEMPERATURE {DIRICHLET},
  ENERGY_RATE {ENERGY_RATE, SCALED_ENERGY_RATE},
  ENERGY_FLUX {NEUMANN}]
         
  * PRESSURE DIRICHLET: specifies a fixed pressure across the entire condition.

  * PRESSURE HYDROSTATIC: specifies a hydrostatic condition where a 
    hydrostatic pressure profile is assigned based on the defined 
    DATUM (and GRADIENT, if applicable) and the function rho*g*h where 
    rho is water density, g is gravity and h is the distance from the 
    DATUM. Note that the water density is incrementally updated as the 
    algorithm moves above or below the DATUM at which the assigned 
    pressure and temperature are defined.

  * PRESSURE SEEPAGE: a seepage face condition is similar to a hydrostatic, 
    EXCEPT that flow may only come into the domain when the boundary face 
    pressure is above a user defined reference pressure. The flow out of the 
    domain is unmodified and is possible at all times. The default reference 
    pressure is atmospheric pressure (101325 Pa).

  * PRESSURE CONDUCTANCE: the conductance type condition is designed to mimic a 
    lower permeability soil layer at the boundary of a domain (e.g. a mud layer 
    at the bottom of a river).  A conductance condition is similar to a seepage 
    face, EXCEPT that a conductance term (permeability/distance) is specified 
    through a CONDUCTANCE keyword.  The permeability of the boundary 
    grid cell and its size (i.e. distance from cell center to boundary) no 
    longer matter. The conductance coefficient is a fit parameter.

  * PRESSURE DIRICHLET_SEEPAGE: a dirichlet-seepage condition is 
    similar to seepage, except a specified dirichlet pressure is applied
    at the boundary instead of sampling pressure from a hydrostatic profile.
    Inflow only occurs when the specified pressure is higher than the
    reference pressure.

  * PRESSURE DIRICHLET_CONDUCTANCE: a dirichlet-conductance condition is 
    similar to conductance, except a specified dirichlet pressure is applied
    at the boundary instead of sampling pressure from a hydrostatic profile.
    Inflow only occurs when the specified pressure is higher than the
    reference pressure.

  * FLUX NEUMANN: specifies a Darcy flux. 

  * RATE MASS_RATE: specifies a mass extraction/injection rate.

  * RATE VOLUMETRIC_RATE: specifies a volumetric extraction/injection rate.

  * RATE SCALED_MASS_RATE <string>: specifies an extraction/injection rate 
    scaled/distributed among grid cells in the coupled region, where <string>
    is one of the scaling options below.

  * RATE SCALED_VOLUMETRIC_RATE <string>: specifies a volumetric 
    extraction/injection rate scaled/distributed among grid cells in the 
    coupled region, where <string> is one of the scaling options below.

  * ENERGY_RATE ENERGY_RATE: specifies an energy extraction/injection rate.

  * ENERGY_RATE SCALED_ENERGY_RATE: specifies an energy extraction/injection 
    rate scaled/distributed among grid cells in the coupled region, 
    where <string> is one of the scaling options below. Note that in this
    case, the VOLUME scaling option makes the most sense.

TYPE specification in GENERAL flow mode
+++++++++++++++++++++++++++++++++++++++
 TYPE 
  [LIQUID_PRESSURE {DIRICHLET, HYDROSTATIC, SEEPAGE, CONDUCTANCE}, 
  GAS_PRESSURE {DIRICHLET}, 
  LIQUID_SATURATION {DIRICHLET}, 
  GAS_SATURATION {DIRICHLET}, 
  TEMPERATURE {DIRICHLET}, 
  MOLE_FRACTION {DIRICHLET}, 
  RELATIVE_HUMIDITY {DIRICHLET}, 
  LIQUID_FLUX {NEUMANN}, 
  GAS_FLUX {NEUMANN}, 
  ENERGY_FLUX {NEUMANN}, 
  RATE {MASS_RATE, SCALED_MASS_RATE}]
          
  * LIQUID_PRESSURE DIRICHLET: specified a fixed pressure.
    Note that HYDROSTATIC can be used, but only within the saturated zone
    (liquid phase state only).
     
  * GAS_PRESSURE DIRICHLET: specifies a fixed gas pressure
    (two-phase and gas state only).
  
  * LIQUID_SATURATION DIRICHLET: specifies a liquid phase saturation
    (two phase state only).
  
  * GAS_SATURATION DIRICHLET: specifies a gas phase saturation
    (two phase state only).
  
  * TEMPERATURE DIRICHLET: specifies a temperature.
  
  * ENERGY_FLUX NEUMANN: specifies an energy flux.
  
  * LIQUID_FLUX NEUMANN: specifies a liquid phase Darcy flux.
  
  * GAS_FLUX NEUMANN: specifies a gas phase Darcy flux.
  
  * RELATIVE_HUMIDITY DIRICHLET: specifies a relative humidity from which
    an air partial pressure will be calculated 
    (gas phase state only).
  
  * MOLE_FRACTION DIRICHLET: specifies the air mole fraction in the 
    gas or liquid phase 
    (liquid and gas phase states only).
       
  * RATE MASS_RATE: specifies a mass extraction/injection rate. **Note that
    this actually applies to energy too.**

  * RATE SCALED_MASS_RATE <string>: specifies an extraction/injection rate 
    scaled/distributed among grid cells in the coupled region, where <string>
    is one of the scaling options below. **Note that
    this actually applies to energy too.**

 Initial thermodynamic states for combinations of Dirichlet-based conditions: 

  * GAS_PRESSURE + GAS_SATURATION = two-phase state, 
    
  * LIQUID_PRESSURE + MOLE_FRACTION = single-phase liquid state,
    
  * GAS_PRESSURE + (MOLE_FRACTION | RELATIVE_HUMIDITY) = single-phase gas 
    state
      
 GENERAL mode flow conditions must include a TEMPERATURE and a 
 MOLE_FRACTION/RELATIVE_HUMIDITY or GAS_SATURATION/LIQUID_SATURATION 
 (but not both SATURATION and a MOLE_FRACTION/RELATIVE_HUMIDITY).
    
TYPE specification in WIPP_FLOW flow mode
+++++++++++++++++++++++++++++++++++++++++
 TYPE 
  [LIQUID_PRESSURE {DIRICHLET}, 
  LIQUID_SATURATION {DIRICHLET}, 
  GAS_SATURATION {DIRICHLET}, 
  LIQUID_FLUX {NEUMANN}, 
  GAS_FLUX {NEUMANN}, 
  RATE {MASS_RATE, SCALED_MASS_RATE
          
  * LIQUID_PRESSURE DIRICHLET: specified a fixed pressure.
     
  * LIQUID_SATURATION DIRICHLET: specifies a liquid phase saturation
  
  * GAS_SATURATION DIRICHLET: specifies a gas phase saturation
  
  * LIQUID_FLUX NEUMANN: specifies a liquid phase Darcy flux.
  
  * GAS_FLUX NEUMANN: specifies a gas phase Darcy flux.

  * RATE MASS_RATE: specifies a mass extraction/injection rate.

  * RATE SCALED_MASS_RATE <string>: specifies an extraction/injection rate 
    scaled/distributed among grid cells in the coupled region, where <string>
    is one of the scaling options below.

RATE Scaling Options:
+++++++++++++++++++++
 * PERM: scaling weighted as a function of cell volume and X permeability

 * NEIGHBOR_PERM: scaling weighted as a function of the interfacial area 
   and permeability of neighboring cells (in x,y)

 * VOLUME: scaling weighted as a function of cell volume
    
Value specification for all flow modes:
+++++++++++++++++++++++++++++++++++++++
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
 The energy flux [MW/m\ :sup:`2`\] applied to the boundary. Positive flux is 
 inward, negative outward, regardless of the direction of the boundary 
 connection.

RELATIVE_HUMIDITY <float>
 The relative humidity in percent [-] applied at the boundary.

RATE <float> [<float> [<float>]]
 Injection/extraction rate in kg/s (mass) or m\ :sup:`3`\/s (volumetric).  
 Positive in, negative out. 
 For WIPP_FLOW mode, the rate is by component (i.e. water component [kg/s], 
 air component [kg/s])
 For GENERAL mode, the rate is by component and 
 energy (i.e. water component [kg/s], air component [kg/s], energy [MW]).

 **A list or external file may be used instead of specifying a float using** 
 **the keywords: LIST or FILE <string>.  To do so, one must provide an** 
 **external file with a** :ref:`rank-one` **or a** :ref:`rank-three`. 

LIQUID_SATURATION <float>
 The liquid saturation [-] applied at the boundary.

GAS_SATURATION <float>
 The gas saturation [-] applied at the boundary.

MOLE_FRACTION <float>
 The gas mole fraction [-] applied at the boundary.

**A list or external file may be used instead of specifying a float using** 
**the keywords: LIST or FILE <string>.  To do so, one must provide an** 
**external file with a** :ref:`rank-one`

Optional Cards:
---------------

DATUM <float float float>
 Reference X,Y, Z coordinate for defining the flow condition.  
 E.g. If type is PRESSURE HYDROSTATIC, the datum coordinate is 
 where the PRESSURE value is set, and other pressures in the 
 hydrostatic condition are calculated in the vertical and horizontal 
 (if a GRADIENT is defined) based on that reference point.

 **An external file may be used instead of specifying floats using the** 
 **keywords: FILE <string>.  To do so, one must provide an external file** 
 **with a** :ref:`rank-three`.

GRADIENT
 Opens a block defining a pressure or temperature gradient based on the 
 datum coordinate.  

 **An external file may be used instead of specifying floats using the** 
 **keywords: FILE <string>.  To do so, one must provide an external file** 
 **with a** :ref:`rank-three`.

 PRESSURE <float float float>
  When the Z value is zero (0.),
   Specifies the unitless head gradient in the x and y directions through
   the gradient plane <dh/dx, dh/dy> [m/m]
  When the Z value is nonzero,
   Specifies a pressure gradient in x y z <dp/dx, dp/dy, dp/dz> [Pa/m].

 TEMPERATURE <float float float>
  Specifies the temperature gradient in the x y z <dT/dx, dT/dy, dT/dz> 
  [C/m].

INTERPOLATION <string>
 Interpolation scheme used to calculate transient update, where the options
 for <string> include: [LINEAR, STEP (default)].

CYCLIC
 Cycles a transient data set back to initial value when maximum data set time 
 is exceeded, repeatedly cycling through the data.

SYNC_TIMESTEP_WITH_UPDATE
 Forces waypoints to be set for each time in a timeseries forcing 
 time stepping to match the waypoints. 

CONDUCTANCE <float>
 Conductance coefficient used when a conductance condition is specified.
 
Examples
--------

RICHARDS Mode Examples
++++++++++++++++++++++
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

TH Mode Examples
++++++++++++++++
 ::

  FLOW_CONDITION initial
    TYPE
      PRESSURE DIRICHLET
      TEMPERATURE DIRICHLET
    /
    PRESSURE 1.D5
    TEMPERATURE DATASET Temperature
  END

  FLOW_CONDITION recharge
    TYPE
      FLUX NEUMANN
      TEMPERATURE DIRICHLET
    /
    FLUX 10 cm/y
    TEMPERATURE 25.D0
  END

GENERAL Mode Examples
+++++++++++++++++++++
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
      TEMPERATURE DIRICHLET
      LIQUID_PRESSURE DIRICHLET
      MOLE_FRACTION DIRICHLET
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
      ENERGY_FLUX NEUMANN
      LIQUID_FLUX NEUMANN
      GAS_FLUX NEUMANN
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
      TEMPERATURE DIRICHLET
      LIQUID_PRESSURE DIRICHLET
      MOLE_FRACTION DIRICHLET
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

WIPP_FLOW Mode Examples
+++++++++++++++++++++++
 ::

  FLOW_CONDITION INITIAL
    TYPE
      LIQUID_PRESSURE DIRICHLET
      LIQUID_SATURATION DIRICHLET
    END
    LIQUID_PRESSURE 1.280390d5
    LIQUID_SATURATION 6.5d-1
  END
