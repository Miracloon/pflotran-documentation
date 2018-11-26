Back to :ref:`card-index`

Back to :ref:`transport-condition-card`

.. _constraint-card:

CONSTRAINT
==========
Creates a set of solute concentration constraints. This card must be included 
with the :ref:`transport-condition-card` card.

Required Cards: 
---------------
CONSTRAINT <name>
 Specifies the name of the constraint.

CONCENTRATIONS
 Solute concentrations are provided for the species using the following list
 structure,

  <string> <float> <char> <optional string>

  species_name concentration constraint_type constraint_species

 Constraint type options:
  * F = free ion concentration
  * P = pH
  * T = total aqueous component concentration
  * M = concentration based on equilibrium with specified mineral
  * G = concentration based on equilibrium with a gas (partial pressure in bars)
  * S = total aqueous + sorbed component concentration (sorbed concentration 
    [mol/m\ :sub:`bulk`\] must be converted to molarity [mol/L\ :sub:`water`\] 
    by dividing by porosity * saturation * 1000).
  * Z = charge balance

FREE_ION_GUESS
 Provides an initial guess for the free ion concentrations of the aqueous 
 species and improves convergence of initial speciation calculations, using the
 following list structure,

  <string> <float>

  species_name guess

MINERALS
 Provides mineral concentrations for the minerals using the following list 
 structure,

  <string> <float> <float>
  
  mineral_name volume_fraction specific_surface_area 
  [m\ :sup:`2` \ mineral/m\ :sup:`3` \ bulk]

  Note that specific surface area supports units of area mineral per mass mineral (e.g. [cm\ :sup:`2` \ mineral/g mineral]) where the specific surface area is based on the initial mass of mineral in a cell based on initial volume fraction.

Examples
--------

 ::

  CONSTRAINT initial
    CONCENTRATIONS
      H+       7.3              M  Calcite
      Ca++     1.20644e-3       T
      Cu++     1.e-8            T
      Mg++     5.09772e-4       T  Dolomite
      UO2++    2.4830E-11       T
      K+       1.54789e-4       T
      Na+      1.03498e-3       Z
      HCO3-    2.57305e-3       T
      Cl-      6.97741e-4       T
      F-       2.09491e-5       T
      HPO4--   1.e-8            M  Fluorapatite
      NO3-     4.69979e-4       T
      SO4--    6.37961e-4       T
      Tracer   1.e-7            F
      Tracer2  1.e-7            F
    /
    MINERALS
      Calcite        0.1   1.  cm^2/cm^3
      Metatorbernite 0.    1.  m^2/m^3
    /
  /

  CONSTRAINT U_source
    CONCENTRATIONS
      H+       7.3              M  Calcite
      Ca++     1.20644e-3       T
      Cu++     1.e-6            T
      Mg++     5.09772e-4       T  Dolomite
      UO2++    2.34845e-7       T      
      K+       1.54789e-4       T
      Na+      1.03498e-3       Z
      HCO3-    2.57305e-3       T
      Cl-      6.97741e-4       T
      F-       2.09491e-5       T
      HPO4--   1.e-6            M  Fluorapatite
      NO3-     4.69979e-4       T
      SO4--    6.37961e-4       T
      Tracer   1.e-7            F
      Tracer2  1.e-7            F
    /
    FREE_ION_GUESS
      H+                    2.7340E-08
      Ca++                  1.1344E-03
      Cu++                  3.4195E-10
      Mg++                  4.6508E-04
      UO2++                 1.0165E-19
      K+                    1.5433E-04
      Na+                   1.3344E-03
      HCO3-                 2.4015E-03
      Cl-                   6.9732E-04
      F-                    2.0709E-05
      HPO4--                8.9094E-10
      NO3-                  4.6803E-04
      SO4--                 5.5862E-04
      Tracer                1.0000E-07
      Tracer2               1.0000E-03 
    /
    MINERALS
      Calcite        0.1    0.18 cm^2/g
      Metatorbernite 0.0    1.
    /
  /

