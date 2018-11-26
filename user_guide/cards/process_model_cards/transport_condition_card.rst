Back to :ref:`card-index`

.. _transport-condition-card:

TRANSPORT_CONDITION
===================
In setting up transport conditions, first create a list of self-consistent 
solute concentration constraints, and then associate them with various time 
points.

Required Cards:
---------------
TRANSPORT_CONDITION <name>
 Specifies the name of the transport condition.

TYPE <string>
  Specifies the type of the transport boundary condition (options for <string>
  include: DIRICHLET, DIRICHLET_ZERO_GRADIENT, NEUMANN, ZERO_GRADIENT, 
  EQUILIBRIUM):  

  DIRICHLET : Specified concentration

  DIRICHLET_ZERO_GRADIENT : Dirichlet (specified concentration) on inflow and 
  zero diffusive gradient on outflow (i.e. only advective transport is 
  considered on outflow).

  NEUMANN : Specified solute flux (**not currently implemented**)

  ZERO_GRADIENT : Zero diffusive gradient for inflow and outflow. Not 
  recommended for inflow boundaries.

  EQUILIBRIUM : Only applicable to the :ref:`source-sink-card` card. Attempts 
  to set the concentrations at cells within the associated region in equilibrium 
  with the constraint concentrations through a rather hardwired large rate 
  constant. The user should be careful to check that equilibrium is being 
  reached before trusting the code.

:ref:`constraint-card`
 Specifies a set of self-consistent solute concentrations. See the 
 :ref:`constraint-card` card for full details on how to use this card.

CONSTRAINT_LIST <a table of time and constraint>
 A list of solute concentration constraints that represent changes over time. 
 Step functions are used to interpolate. 

Optional Cards:
---------------
TIME_UNITS <string>
 Specifies the units for the times in the constraint list. If not specified, SI (seconds) is assumed.

Examples
--------

 ::


  TRANSPORT_CONDITION Initial
    TYPE dirichlet_zero_gradient
    CONSTRAINT_LIST
      0.d0 initial
    /
  /

  TRANSPORT_CONDITION U_source
    TYPE dirichlet
    TIME_UNITS s
    CONSTRAINT_LIST
      0.d0 U_source
      336000.d0 Initial
    /
  /

  : the units for time are seconds by default

  CONSTRAINT U_source
    CONCENTRATIONS
      H+       3.0              pH
      Ca++     1.20644e-3       T
      Cu++     1.e-8            T
      Mg++     5.09772e-4       M Dolomite
      UO2++    1E-6             T
      K+       1.54789e-4       T
      Na+      1.03498e-3       Z
      HCO3-    2.57305e-3       T
      Cl-      6.97741e-4       T
      F-       2.09491e-5       T
      HPO4--   1.e-8            M Fluorapatite
      NO3-     4.69979e-4       T
      SO4--    6.37961e-4       T
      Tracer   1.e-7            F
      Tracer2  1.e-7            F
    /
    MINERALS
    :mineral           vol. frac.  area
      Calcite          0.1         1.
      Metatorbernite   0.          1.
    / ! end of minerals
  / ! end of constraint

  CONSTRAINT initial
    CONCENTRATIONS
      H+       7.3              M Calcite
      Ca++     1.20644e-3       T
      Cu++     1.e-8            T
      Mg++     5.09772e-4       M Dolomite
      UO2++    2.4830E-11       T
      K+       1.54789e-4       T
      Na+      1.03498e-3       Z
      HCO3-    -3.5             G  CO2(g)
      Cl-      6.97741e-4       T
      F-       2.09491e-5       T
      HPO4--   1.e-8            M Fluorapatite
      NO3-     4.69979e-4       T
      SO4--    6.37961e-4       T
      Tracer   1.e-7            F
      Tracer2  1.e-7            F
    /
    MINERALS
    :mineral          vol. frac.  area
      Calcite         0.1         1.
      Metatorbernite  0.          1.
    / ! end of minerals
  / ! end of constraint
