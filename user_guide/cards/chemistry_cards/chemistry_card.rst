Back to :ref:`card-index`

.. _chemistry-card:

CHEMISTRY
=========
Specifies geochemistry details for multicomponent transport.

Required Cards:
---------------

PRIMARY_SPECIES
 List of primary aqueous or basis species for which concentrations will be 
 solved.

Optional Cards:
---------------
SECONDARY_SPECIES
 List of secondary aqueous species or complexes.

:ref:`radioactive-decay-reaction-card`
 Parameters for kinetic radioactive decay reactions.

:ref:`general-reaction-card`
 Parameters for general forward/reverse kinetic reactions.

:ref:`immobile-decay-reaction-card`
 Parameters for decay of immobile species (e.g. biomass).

:ref:`microbial-reaction-card`
 Parameters for microbially-mediated reactions.

MINERALS
 List of minerals. 

:ref:`mineral-kinetics-card`
 Parameters for kinetic mineral precipitation/dissolution reactions.

:ref:`sorption-card`
 Sorption reactions.

:ref:`reaction-sandbox-card`
  Reaction sandbox for custom, user-defined reactions.

DATABASE <string>
 Path/filename for reaction database.  Description of 
 :ref:`geochemical-database`.

LOG_FORMULATION
 Flag for solving Newton-Raphson equations with derivatives computed with 
 respect to the logarithm  (base 10) of the concentrations.

ACTIVITY_COEFFICIENTS <string> <string>
 Specifies algorithms for calculating activity coefficients

 - Algorithms:

  - LAG: 
     Single pass update to activity coefficients
  - NEWTON
     Iterative Newton-based updated (iterates until convergence tolerance is 
     satisfied)

 - Update Frequency:

  - TIMESTEP
     Update after every time step
  - NEWTON_ITERATION
     Update after every newton iteration

NO_CHECKPOINT_ACT_COEFS
 Do not store activity coefficients when checkpointing simulations.

NO_BDOT
 Do not use bdot form of activity coefficient equation.

UPDATE_POROSITY <optional float>
 Update porosity after every time step.  Optional float specifies minimum 
 porosity to which porosity is truncated if below that value (default = 0.).

UPDATE_PERMEABILITY
 Update permeabilty after every time step.

UPDATE_TORTUOSITY
 Update tortuosity after every time step.

UPDATE_MINERAL_SURFACE_AREA
 Update mineral surface area after every time step.

MOLAL, MOLALITY
 Print concentrations as molalities.

ACTIVITY_H2O, ACTIVITY_WATER
 Calculate activity of water.

:ref:`chemistry-output-card`
 Specifies parameters for output.

MAX_DLNC <float>
 Specifies maximum change in log concentration for a Newton Raphson iteration.  
 Changes in concentration larger than this value will be truncated to this 
 value.  Default = 5.

MAX_RELATIVE_CHANGE_TOLERANCE <float>
 Specifies the maximum relative change in free ion concentration allowed for 
 convergence (i.e. ||(c^k+1-c^k)/c^k||_inf).  Default = 1.e-12.

MAX_RESIDUAL_TOLERANCE <float>
 Specified the maximum residual allowed for a primary species for convergence 
 (i.e. ||f(c^k+1)||_inf).  Default = 1.e-12.

TRUNCATE_CONCENTRATION <float>
 Specify a minimum concentration below which free-ion concentration may not 
 fall.  (Due to the molality/molarity conversion, the concentration may fall 
 slightly below the prescribed value when the water density is less than 1000 
 kg/m\ :sup:`3`\)
 
USE_FULL_GEOCHEMISTRY
 Forces full geochemistry calculation even if only tracers are specified. 

Examples
--------

 ::

  CHEMISTRY
    PRIMARY_SPECIES
      H+
      HCO3-
      Ca++
    /
    SECONDARY_SPECIES
      OH-
      CO3--
      CO2(aq)
      CaOH+
      CaHCO3+
      CaCO3(aq)
    /
    MINERALS
      Calcite
    /
    MINERAL_KINETICS
      Calcite
        RATE_CONSTANT 1.d-13
      /
    /
    DATABASE ./calcite.dat
    LOG_FORMULATION
    ACTIVITY_COEFFICIENTS TIMESTEP
  END

 ::

  CHEMISTRY
    PRIMARY_SPECIES
      H+
      Ca++
      Cu++
      Mg++
      UO2++
      K+
      Na+
      HCO3-
      Cl-
      F-
      HPO4--
      NO3-
      SO4--
      Tracer
      Tracer2
    /
    SECONDARY_SPECIES
      OH-
      CO3--
      CO2(aq)
      CaCO3(aq)
      CaHCO3+
      CaSO4(aq)
      CaCl+
      CaCl2(aq)
      CaF+
      CaH2PO4+
      CaHPO4(aq)
      CaNO3+
      CaPO4-
      MgCO3(aq)
      MgHCO3+
      MgSO4(aq)
      MgCl+
      MgF+
      UO2(H2PO4)(H3PO4)+
      UO2(H2PO4)2(aq)
      UO2HPO4(aq)
      UO2H2PO4+
      UO2H3PO4++
      UO2PO4-
    /
    GAS_SPECIES
      CO2(g)
    /
    MINERALS
      Calcite
      Magnesite
      Dolomite
      Dolomite-dis
      Dolomite-ord
      Brucite
      Nesquehonite
      Gypsum
      Schoepite
      UO2CO3
      UO2(PO3)2
      (UO2)3(PO4)2
      (UO2)3(PO4)2.4H2O
      CaUO4
      UO2SO4
      UOF4
      UO3.2H2O
      UO3.0.9H2O(alpha)
      Saleeite
      Sylvite
      Metatorbernite
      Whitlockite
      Chalcanthite
      Brochantite
      Tenorite
      Malachite
      Fluorapatite
      Fluorite
      Hydroxylapatite
      Torbernite
    /
  :
    MINERAL_KINETICS
      Calcite 
        RATE_CONSTANT 1.e-12 mol/cm^2-sec
      /
      Metatorbernite 
        RATE_CONSTANT 2.e-17 mol/cm^2-sec
      /
    /
    SORPTION
      JUMPSTART_KINETIC_SORPTION
      SURFACE_COMPLEXATION_RXN
        MINERAL Calcite
        SITE >SOH 15.264 ! 20 m^2/g, por = 0.25
        COMPLEXES
          >SOUO2OH
          >SOHUO2CO3
        /
      /
    /
    DATABASE ../../../hanford.dat
    LOG_FORMULATION
    MAX_RELATIVE_CHANGE_TOLERANCE 1.d-10
    ACTIVITY_COEFFICIENTS NEWTON_ITERATION
    OUTPUT
      UO2++
      Tracer
    /
  END

