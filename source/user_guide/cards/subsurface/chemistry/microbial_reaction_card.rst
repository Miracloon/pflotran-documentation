Back to :ref:`card-index`

Back to :ref:`chemistry-card`

.. _microbial-reaction-card:

MICROBIAL_REACTION
==================
Specifies parameters for microbially-mediated reactions. 

By default, all aqueous concentrations are in molarity [mol/L].
The units of concentration in the RATE_CONSTANT, HALF_SATURATION, THRESHOLD_CONCENTRATION and INHIBITION_CONSTANT parameters must be consistent throughout all microbial reactions.

Required Cards:
---------------

REACTION <string>
 Reaction equation.  The rate constant is multiplied by the Monod expressions 
 for electron donor and acceptor for select species on the left side of the 
 equation.  The reaction may be inhibited by any species in the system.

RATE_CONSTANT <float>
 Rate constant for the reaction, where the units are [mol/L-sec] if no biomass, or [mol/(mol biomass-sec)] if biomass. Here, aqueous concentration units are the default [mol/L].

Optional Cards:
---------------

MONOD 
 Specifies the Monod equation for the electron donor or acceptor.

  SPECIES NAME <string>
   Name of species.
   
  HALF_SATURATION_CONSTANT <float>
   Half saturation constant for the Monod expression.
   
  THRESHOLD_CONCENTRATION <float>
   Threshold concentration below which the reaction stops.

INHIBITION
 Specifies inhibition based on species concentration and an inhibition 
 constant(s).  Three types of inhibition are currently supported:  MONOD, 
 INVERSE_MONOD, THRESHOLD.

  Monod Inhibition:
    INHIBITION
      SPECIES_NAME <string>

      TYPE MONOD
       Specifies the type of inhibition to be Monod.  The reaction proceeds as 
       long as the species concentration is well below the half saturation 
       constant: inhibition = C\ :sub:`th`\ / (C\ :sub:`th` \ + concentration) 

      INHIBITION_CONSTANT <float>
       Half saturation constant.


  Inverse Monod Inhibition:
    INHIBITION
      SPECIES_NAME <string>

      TYPE INVERSE_MONOD
       Specifies the type of inhibition to be inverse Monod.  The reaction 
       proceeds as long as the species concentration is well above the half 
       saturation constant: inhibition = concentration / (C\ :sub:`th` \ + 
       concentration) 

      INHIBITION_CONSTANT <float>
       Half saturation constant.


  Threshold Inhibition:
    INHIBITION
      SPECIES_NAME <string>

      TYPE THRESHOLD <float>
        Specifies the type of inhibition to be threshold and the scaling factor 
        to be applied.  Inhibition is calculated based on the following 
        equation: inhibition = 0.5 + arctan((concentration - C\ :sub:`th`\) * f) / PI.  
        Inhibition is above and below C\ :sub:`th` \ when the sign of 
        C\ :sub:`th` \ is negative or positive, respectively.

      INHIBITION_CONSTANT <float>
       Threshold concentration

BIOMASS 
 Specifies the immobile biomass species to be included in the rate expression.
 
  SPECIES_NAME <string>
   Name of the species
   
  YIELD <float>
   Fraction of energy going towared biomass synthesis.

CONCENTRATION_UNITS <string>
 Options include MOLARITY [mol/L], MOLALITY, [mol/kg water] and ACTIVITY. Default = MOLARITY.

Examples:
---------

 ::

  CHEMISTRY
    PRIMARY_SPECIES
      A(aq)
      B(aq)
      C(aq)
    /
    MICROBIAL_REACTION
      REACTION A(aq) + 2 B(aq) <-> 1.5 C(aq)
      RATE_CONSTANT 1.d-12
      MONOD
        SPECIES_NAME A(aq)     ! A is the donor
        HALF_SATURATION_CONSTANT 1.d-5
      /
      MONOD
        SPECIES_NAME B(aq)     ! B is the acceptor
        HALF_SATURATION_CONSTANT 1.d-4
      /
      INHIBITION
        SPECIES_NAME C(aq)
        TYPE MONOD
        INHIBITION_CONSTANT 6.d-4   ! C is the product and inhibits when too high
      /
    /
  ...

 ::

  CHEMISTRY
    PRIMARY_SPECIES
      A(aq)
      B(aq)
      C(aq)
    /
    IMMOBILE_SPECIES
      D(im)
    /
    MICROBIAL_REACTION
      CONCENTRATION_UNITS ACTIVITY
      REACTION A(aq) + 2 B(aq) <-> 1.5 C(aq)
      RATE_CONSTANT 1.d-6
      MONOD
        SPECIES_NAME A(aq)
        HALF_SATURATION_CONSTANT 1.d-5        ! A is the donor
        THRESHOLD_CONCENTRATION 1.d-20
      /
      MONOD
        SPECIES_NAME B(aq)
        HALF_SATURATION_CONSTANT 1.d-4        ! B is the acceptor
        THRESHOLD_CONCENTRATION 1.d-11
      /
      INHIBITION
        SPECIES_NAME C(aq)
        TYPE INVERSE_MONOD
        INHIBITION_CONSTANT 6.d-4   ! C is the product and inhibits when too high
      /
      BIOMASS
        SPECIES_NAME D(im)
        YIELD 0.01d0
      /
    /
    IMMOBILE_DECAY_REACTION
      SPECIES_NAME D(im)
      RATE_CONSTANT 1.d-9
    /
    ...
  /
