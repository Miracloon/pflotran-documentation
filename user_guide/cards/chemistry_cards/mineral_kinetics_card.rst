Back to :ref:`card-index`

Back to :ref:`chemistry-card`

.. _mineral-kinetics-card:

MINERAL_KINETICS
================

Specifies coefficients for kinetic mineral precipitation-dissolution reactions. 
The rate law is defined through transition state theory, as detailed in section
:ref:`transition-state-theory` of the theory guide. The reaction rate :math:`I_m` for the :math:`m` th mineral is defined as

.. math::
   
   I_m = -a_m\Big(\sum_l k_{ml}(T) {\mathcal P}_{ml}\Big) \Big|1-\big(K_m Q_m\big)^{1/\sigma_m}\Big|^{\beta_m} {\rm sign}(1-K_mQ_m),


where a positive value corresponds to precipitation and a negative value to dissolution, and where
 
 :math:`a_m` = mineral specific surface area [1/m]

 :math:`{\mathcal P}_{ml}` = prefactor (a sum of prefactor rates; if activation energy is 
 provided the Arrhenius equation is applyied to each prefactor to calculate rates at different 
 temperatures)
 
 :math:`K_m` = equilibrium constant

 :math:`Q_m` = ion activity product

 :math:`\sigma_m` = Temkin number (default is 1)

 :math:`\beta_m` = affinity power (default is 1)
 
 :math:`k_{ml}` = rate constant 

Note that prefactor calculations have not yet been verified.

Required Cards:
---------------

MINERAL_KINETICS
 Opens the block.

Optional Cards:
---------------

<string>
  Specifies mineral name.

RATE_CONSTANT <float>
 Kinetic rate constant [mol/m\ :sup:`2`\-sec]. If negative, then raised to power 10 (e.g. -12.d0 is converted to :math:`10^{-12}`)

ACTIVATION_ENERGY <float>
 If specified, used in the prefactor calculations for temperature specific rates 
 (Arrhenius)

AFFINITY_THRESHOLD <float>
 If specified, rate is only calculated if :math:`K_m Q_m \geq` threshold and sign < 0 corresponding to dissolution.

RATE_LIMITER <float>
 Limiting reaction rate factor (see Eqn. :eq:`dummy19` in Theory Guide, Mode: Reactive Transport for details).

IRREVERSIBLE
 Flag indicating the reaction is irreversible

SURFACE_AREA_POROSITY_POWER <float>
 Exponent in equation for transient mineral surface area calculated as a 
 function of porosity, :math:`\phi`:
 :math:`A_m = A_m^0 (\phi/\phi_0)^n`, :math:`n` = SURFACE_AREA_POROSITY_POWER.

SURFACE_AREA_VOL_FRAC_POWER <float>
 Exponent in equation for transient mineral surface area calculated as a function of the mineral volume fraction :math:`\phi_m`:  
 :math:`A_m = A_m^0 (\phi_m/\phi_m^0)^n`, :math:`n` = SURFACE_AREA_VOL_FRAC_POWER. Note that the volume fraction power can be applied only if :math:`\phi_m^0 > 0` corresponding to primary minerals.

:ref:`prefactor-card`
 Parameters for reaction rate prefactors

Examples
--------

 ::
 
  CHEMISTRY
    ...
    MINERAL_KINETICS
      Calcite
        RATE_CONSTANT 1.d-13 mol/cm^2-sec
      /
    /
    ...
  END

.. _Back to Quick Guide: ../QuickGuide
.. _Back to CHEMISTRY: ../Chemistry
.. _PREFACTOR: ./MineralKinetics/Prefactor