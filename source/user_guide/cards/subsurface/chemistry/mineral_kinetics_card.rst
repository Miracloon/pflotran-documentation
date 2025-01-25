Back to :ref:`card-index`

Back to :ref:`chemistry-card`

.. _mineral-kinetics-card:

MINERAL_KINETICS
================

Specifies coefficients for kinetic mineral precipitation-dissolution reactions. 
The rate law is defined through transition state theory, as detailed in section
:ref:`transition-state-theory` of the theory guide. The reaction rate :math:`I_m` for the :math:`m` th mineral is defined as

.. math::
   :label: tst_rate_law
   
   I_m = -a_m\Big(\sum_l k_{ml}(T) {\mathcal P}_{ml}\Big) \Big|1-\big(K_m Q_m\big)^{\left(\frac{1}{\lambda_m\sigma_m}\right)}\Big|^{\beta_m} {\rm sign}(1-K_mQ_m),


where a positive value corresponds to precipitation and a negative value to dissolution, and where
 
 :math:`a_m` = mineral specific surface area [m\ :math:`^{-1}`]

 :math:`{\mathcal P}_{ml}` = prefactor (a sum of prefactor rates; if activation energy is 
 provided the Arrhenius equation is applyied to each prefactor to calculate rates at different 
 temperatures)
 
 :math:`K_m` = equilibrium constant

 :math:`Q_m` = ion activity product

 :math:`\sigma_m` = Temkin number (default is 1)

 :math:`\lambda_m` = mineral scaling factor (default is 1)

 :math:`\beta_m` = affinity power (default is 1)
 
 :math:`k_{ml}` = rate constant 

..
 Note that prefactor calculations have not yet been verified.

Required Cards:
---------------

MINERAL_KINETICS
 Opens the block.

<string>
  Specifies mineral name.

RATE_CONSTANT <float> <optional units_string>
 Kinetic rate constant. 
 If negative, then raised to power 10 (e.g. -12.d0 is converted to :math:`10^{-12}`) 
 (default units [mol/m\ :sup:`2`\-sec])

Optional Cards:
---------------

ACTIVATION_ENERGY <float>
 If specified, used in the prefactor calculations for temperature dependent rates.
 (Arrhenius)
 [J/mol]

AFFINITY_THRESHOLD <float>
 If specified, rate is only calculated if :math:`K_m Q_m \geq` threshold 
 and :math:`{\rm sign}(1-K_mQ_m) < 0` corresponding to precipitation.

AFFINITY_POWER <flaot>
 :math:`\beta_m` in Eqn. :eq:`tst_rate_law` above.

..
 ARMOR_MINERAL
 ARMOR_PWR
 ARMOR_CRIT_VOL_FRAC

DISSOLUTION_RATE_CONSTANT <float> <optional units_string>
 Kinetic rate constant for dissolution that requires a complementary 
 precipitation rate constant. 
 If negative, then raised to power 10 (e.g. -12.d0 is converted to :math:`10^{-12}`) 
 (default units [mol/m\ :sup:`2`\-sec])

..
 IRREVERSIBLE
 Flag indicating the reaction is irreversible

MINERAL_SCALE_FACTOR <flaot>
 :math:`\lambda_m` in equation above.

NUCLEATION_KINETICS <string>
 Name of nucleations kinetics reaction to be applied to the mineral 
 (specified elsewhere in the NUCLEATION_KINETICS block).

PRECIPITATION_RATE_CONSTANT <float> <optional units_string>
 Kinetic rate constant for precipitation that requires a complementary 
 dissolution rate constant. 
 If negative, then raised to power 10 (e.g. -12.d0 is converted to :math:`10^{-12}`) 
 (default units [mol/m\ :sup:`2`\-sec])

:ref:`prefactor-card`
 Parameters for reaction rate prefactors

RATE_LIMITER <float>
 Limiting reaction rate factor (see Eqn. :eq:`dummy19` in Theory Guide, Mode: Reactive Transport for details).

SPECIFIC_SURFACE_AREA <float>
 The specific surface area of the reacting mineral.
 (default units [m\ :sup:`2`\/g])

SURFACE_AREA_FUNCTION <string>
 Specifies the function used to calculate the reacting surface area for a 
 mineral. $\left[\frac{m^2_\text{mnrl}}{m^3_\text{bulk}}\right]$ 

 Options: CONSTANT, POROSITY_RATIO, VOLUME_FRACTION_RATIO, 
 POROSITY_VOLUME_FRACTION_RATIO, MINERAL_MASS

 MINERAL_MASS
  
  :math:`a_m = \frac{\text{SSA}\cdot\overline{V_m}\cdot\porosity_m}{\text{FMW}}` 

 POROSITY_RATIO

  :math:`a_m = a_m^0 (\porosity/\porosity_0)^n`

 POROSITY_VOLUME_FRACTION_RATIO

  :math:`a_m = a_m^0 \left(\frac{\porosity_m}{\porosity_m^0}\right)^n  \left(\frac{1-\porosity}{1-\porosity_0}\right)^{n'}`

 VOLUME_FRACTION_RATIO

  :math:`a_m = a_m^0 (\porosity_m/\porosity_m^0)^n`

SURFACE_AREA_POROSITY_POWER <float>
 Exponent in equation for transient mineral surface area calculated as a 
 function of porosity, :math:`\porosity`:
 :math:`a_m = a_m^0 (\porosity/\porosity_0)^n`, :math:`n` = SURFACE_AREA_POROSITY_POWER.

SURFACE_AREA_VOL_FRAC_POWER <float>
 Exponent in equation for transient mineral surface area calculated as a function of the mineral volume fraction :math:`\porosity_m`:  
 :math:`a_m = a_m^0 (\porosity_m/\porosity_m^0)^n`, :math:`n` = SURFACE_AREA_VOL_FRAC_POWER. Note that the volume fraction power can be applied only if :math:`\porosity_m^0 > 0` corresponding to primary minerals.

TEMKIN_CONSTANT <flaot>
 Sigma in Eqn. :eq:`tst_rate_law` above.

VOLUME_FRACTION_EPSILON <float>
 Minimum volume fraction for a kinetic mineral.

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
