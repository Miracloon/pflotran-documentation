Back to :ref:`card-index`

.. _thermal-characteristic-curves-card:

THERMAL_CHARACTERISTIC_CURVES
=============================
Specifies the thermal characteristic curves (e.g. thermal conductivity and associated parameters) to be associated with a material property. 
**This card is currently only supported for the GENERAL flow mode.** Thermal conductivity (only a function of liquid saturation, not of temperature) and specific heat should specified in the material property card for other flow modes.

Required Blocks and Cards:
**************************
THERMAL_CONDUCTIVITY_FUNCTION <string>
  Opens a thermal conductivity block, where <string> indicates the type of thermal conductivity function to be employed. 

  Supported THERMAL_CONDUCTIVITY_FUNCTIONs (along with their required cards):

  .. _tcc-default-card:

  * DEFAULT
    
    + THERMAL_CONDUCTIVITY_DRY
    + THERMAL_CONDUCTIVITY_WET

  * CONSTANT

    + CONSTANT_THERMAL_CONDUCTIVITY

  .. _tcc-power-card:      
      
  * POWER

    + THERMAL_CONDUCTIVITY_DRY
    + THERMAL_CONDUCTIVITY_WET
    + REFERENCE_TEMPERATURE
    + EXPONENT

  .. _tcc-cubic-polynomial-card:

  * CUBIC_POLYNOMIAL

    + THERMAL_CONDUCTIVITY_DRY
    + THERMAL_CONDUCTIVITY_WET
    + REFERENCE_TEMPERATURE
    + CUBIC_POLYNOMIAL_COEFFICIENTS

  .. _tcc-linear-resistivity-card:

  * LINEAR_RESISTIVITY

    + THERMAL_CONDUCTIVITY_DRY
    + THERMAL_CONDUCTIVITY_WET
    + REFERENCE_TEMPERATURE
    + LINEAR_RESISTIVITY_COEFFICIENTS

.. _parameter-definitions:

Parameter Definitions
---------------------

THERMAL_CONDUCTIVTY_WET <float>
 Thermal conductivity of the wet porous medium (:math:`s_l=1`) [W/m-K].

THERMAL_CONDUCTIVITY_DRY <float>
 Thermal conductivity of the dry porous medium (:math:`s_l=0`) [W/m-K].

 Effective thermal conductivity (:math:`\kappa_T`) at the given liquid saturation (Somerton et al., 1974) is computed as :math:`\kappa_T(s_l)=\kappa_T^{dry} + \sqrt{s_l}(\kappa_T^{wet} - \kappa_T^{dry})`
 
CONSTANT_THERMAL_CONDUCTIVITY <float>
 Thermal conductivity of porous medium that does not depend on temperature or saturation [W/m-K].

REFERENCE_TEMPERATURE <float>
 This temperature is subtracted from the actual temperature before the calcuation (useful for conversion from Cesius to Kelvin, or to shift the zero a polynomial) [C]

EXPONENT <float>
 In the POWER model, this is the exponent of temperature, called :math:`\gamma` [-].

 Thermal conductivity for the POWER model is computed as :math:`\kappa_T(s_l,T)=\kappa_T(s_l)[(T-T_{ref})/300]^\gamma`.

 The saturation dependence of the POWER model comes from the DEFAULT model, and when using the default :math:`T_{ref}=-273.15`, THERMAL_CONDUCTIVITY_WET and THERMAL_CONDUCTIVITY_DRY are at 26.85 Celsius.

CUBIC_POLYNOMIAL_COEFFICIENTS <float> <float> <float>
 Coefficients of a cubic polynomial expression for the temperature-dependence, called :math:`\beta_i`.

 Thermal conductivity for the CUBIC_POLYNOMIAL model is computed as :math:`\kappa_T(s_l,T)=\kappa_T(s_l)[1 + \beta_1 (T-T_{ref}) + \beta_2 (T-T_{ref})^2 + \beta_3 (T-T_{ref})^3]`.

 The saturation dependence of the CUBIC_POLYNOMIAL model comes from the DEFAULT model, and when using the default :math:`T_{ref}=0`, THERMAL_CONDUCTIVITY_WET and THERMAL_CONDUCTIVITY_DRY are at 0 Celsius. 
  
LINEAR_RESISTIVITY_COEFFICIENTS <float> <float>
 Coefficients of a linear inverse conductivity (i.e., resistivity), called :math:`a_i`

 Thermal conductivity for the LINEAR_RESISTIVITY model is computed as :math:`\kappa_T(s_l,T)=\kappa_T(s_l)/[a_1 + a_2 (T - T_{ref})]`, with the default :math:`T_{ref}=0`

 The saturation dependence of the LINEAR_RESISTIVITY model comes from the DEFAULT model, and when using the default :math:`T_{ref}=0`, THERMAL_CONDUCTIVITY_WET and THERMAL_CONDUCTIVITY_DRY are at 0 Celsius. Typically :math:`a_1=1`. 
  
Optional Card under the THERMAL_CHARACTERISTIC_CURVES block:
************************************************************
TEST
 Including this keyword will produce output (.dat file) which provides (a) temperature [:math:`T`], (b) liquid saturation [:math:`s_l`], (c) thermal conductivity [:math:`\kappa_T`], (d) :math:`\frac{\partial \kappa_T}{\partial s_l}`, (e) :math:`\frac{\partial \kappa_T}{\partial T}`, (f) numerical approximation to d, and (g) numerical approximation to e. 

Examples
********

GENERAL mode
------------
 ::

  MATERIAL_PROPERTY soil
    ID 1
    CHARACTERISTIC_CURVES cc1
    POROSITY 0.000001
    TORTUOSITY 1.0
    ROCK_DENSITY 2650.0 kg/m^3
    THERMAL_CHARACTERISTIC_CURVES cct_power
    HEAT_CAPACITY 830.0 J/kg-C
    PERMEABILITY
      PERM_ISO 1.d-12
    /
  /

  THERMAL_CHARACTERISTIC_CURVES cct_default
    THERMAL_CONDUCTIVITY_FUNCTION DEFAULT
      THERMAL_CONDUCTIVITY_DRY 5.5D+0 W/m-C
      THERMAL_CONDUCTIVITY_WET 5.5D+0 W/m-C
    END
    TEST
  END

  THERMAL_CHARACTERISTIC_CURVES cct_constant
    THERMAL_CONDUCTIVITY_FUNCTION CONSTANT
      CONSTANT_THERMAL_CONDUCTIVITY 5.5D+0 W/m-C
    END
    TEST
  END

  THERMAL_CHARACTERISTIC_CURVES cct_power
    THERMAL_CONDUCTIVITY_FUNCTION POWER
      THERMAL_CONDUCTIVITY_DRY 5.9676D+0 W/m-C
      THERMAL_CONDUCTIVITY_WET 5.9676D+0 W/m-C
      #REFERENCE_TEMPERATURE -273.15 ! default value
      EXPONENT -1.18D+0 
    END
    TEST
  END

  THERMAL_CHARACTERISTIC_CURVES cct_cubic_polynomial
    THERMAL_CONDUCTIVITY_FUNCTION CUBIC_POLYNOMIAL
      THERMAL_CONDUCTIVITY_DRY 6.8077D+0 W/m-C
      THERMAL_CONDUCTIVITY_WET 6.8077D+0 W/m-C
      #REFERENCE_TEMPERATURE 0.d0 ! default value
      CUBIC_POLYNOMIAL_COEFFICIENTS -4.53398D-3 1.41580D-5 -1.94840D-8
    END
    TEST
  END

  THERMAL_CHARACTERISTIC_CURVES cct_linear_resistivity
    THERMAL_CONDUCTIVITY_FUNCTION LINEAR_RESISTIVITY
      THERMAL_CONDUCTIVITY_DRY 6.8077D+0 W/m-C
      THERMAL_CONDUCTIVITY_WET 6.8077D+0 W/m-C
      #REFERENCE_TEMPERATURE 0.d0 ! default value
      LINEAR_RESISTIVITY_COEFFICIENTS 1.0d0 5.038D-3
    END
    TEST
  END

