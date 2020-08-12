Back to :ref:`card-index`

.. _thermal-characteristic-curves-card:

THERMAL_CHARACTERISTIC_CURVES
=============================
This option specifies the thermal characteristic curves (e.g. thermal conductivity and associated parameters) associated with a material property. This expands thermal conductivity as a function of both temperature and saturation (with the exception of the ``CONSTANT`` and ``DEFAULT`` thermal conductivity functions). 

The legacy input method of specifying thermal conductivity by :ref:`material-property-card` (i.e. with ``THERMAL_CONDUCTIVITY_DRY`` and ``THERMAL_CONDUCTIVTY_WET``) is backwards-compatible, where parameters are adapted to the ``DEFAULT`` thermal characteristic curve and functions are numbered with the material ``ID``. However, ``THERMAL_CHARACTERISTIC_CURVES`` **cannot** be combined with the legacy convention in the same input file.

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

.. _tcc-parameter-definitions:

Thermal Characteristic Curves Parameter Definitions
---------------------------------------------------

THERMAL_CONDUCTIVTY_WET <float>
 Thermal conductivity of the wet porous medium (:math:`s_l=1`) [W/m-K].

THERMAL_CONDUCTIVITY_DRY <float>
 Thermal conductivity of the dry porous medium (:math:`s_l=0`) [W/m-K].

 Effective thermal conductivity (:math:`\kappa_T`) at the given liquid saturation (Somerton et al., 1974) is computed as :math:`\kappa_T(s_l)=\kappa_T^{dry} + \sqrt{s_l}(\kappa_T^{wet} - \kappa_T^{dry})` [W/m-K]
 
CONSTANT_THERMAL_CONDUCTIVITY <float>
 Thermal conductivity of porous medium that does not depend on temperature or saturation [W/m-K].

REFERENCE_TEMPERATURE <float>
 This temperature is subtracted from the actual temperature before the calculation (useful for conversion from Celsius to Kelvin, or to shift the zero a polynomial) [°C]

EXPONENT <float>
 In the POWER model, this is the exponent of temperature, called :math:`\gamma` [-].

 Thermal conductivity for the POWER model is computed as :math:`\kappa_T(s_l,T)=\kappa_T(s_l)[(T-T_{ref})/300]^\gamma` [W/m-K].

 The saturation dependence of the POWER model comes from the DEFAULT model, and when using the default :math:`T_{ref}=-273.15` °C, THERMAL_CONDUCTIVITY_WET and THERMAL_CONDUCTIVITY_DRY are at 26.85 °C.

CUBIC_POLYNOMIAL_COEFFICIENTS <float> <float> <float>
 Coefficients of a cubic polynomial expression for the temperature-dependence, called :math:`\beta_i`.

 Thermal conductivity for the CUBIC_POLYNOMIAL model is computed as :math:`\kappa_T(s_l,T)=\kappa_T(s_l)[1 + \beta_1 (T-T_{ref}) + \beta_2 (T-T_{ref})^2 + \beta_3 (T-T_{ref})^3]` [W/m-K].

 The saturation dependence of the CUBIC_POLYNOMIAL model comes from the DEFAULT model, and when using the default :math:`T_{ref}=0` °C, THERMAL_CONDUCTIVITY_WET and THERMAL_CONDUCTIVITY_DRY are at 0 °C. 
  
LINEAR_RESISTIVITY_COEFFICIENTS <float> <float>
 Coefficients of a linear inverse conductivity (i.e., resistivity), called :math:`a_i`

 Thermal conductivity for the LINEAR_RESISTIVITY model is computed as :math:`\kappa_T(s_l,T)=\kappa_T(s_l)/[a_1 + a_2 (T - T_{ref})]` [W/m-K], with the default :math:`T_{ref}=0` °C

 The saturation dependence of the LINEAR_RESISTIVITY model comes from the DEFAULT model, and when using the default :math:`T_{ref}=0` °C, THERMAL_CONDUCTIVITY_WET and THERMAL_CONDUCTIVITY_DRY are at 0 °C. Typically :math:`a_1=1`. 

 .. _tcc-anisotropy-parameter-definitions:

Thermal Conductivity Anisotropy Parameter Definitions
-----------------------------------------------------

The following parameters are used to impart a direction-dependent treatment of thermal conductivity for thermal characteristic curves that employ :math:`\kappa_T(s_l)` from the DEFAULT function. The following inputs are ratios that determine what fraction of the user-input values (THERMAL_CONDUCTIVITY_DRY or THERMAL_CONDUCTIVITY_WET) comprise particular components of the thermal conductivity tensor. 

THERMAL_CONDUCTIVITY_X <float>
 The ratio applied to user-input thermal conductivity to derive the :math:`\kappa_{xx}` component of the thermal conductivity tensor. Requires additional input of Y and Z ratios. 
 
THERMAL_CONDUCTIVITY_Y <float>
 The ratio applied to user-input thermal conductivity to derive the :math:`\kappa_{yy}` component of the thermal conductivity tensor. Requires additional input of X and Z ratios. 
  
THERMAL_CONDUCTIVITY_Z <float>
 The ratio applied to user-input thermal conductivity to derive the :math:`\kappa_{zz}` component of the thermal conductivity tensor. Requires additional input of X and Y ratios. 
  
Optional Card under the THERMAL_CHARACTERISTIC_CURVES block:
************************************************************
TEST
 Including this keyword will produce output (.dat file) which provides 
  (a) temperature [:math:`T`],
  (b) liquid saturation [:math:`s_l`],
  (c) thermal conductivity [:math:`\kappa_T`],
  (d) :math:`\frac{\partial \kappa_T}{\partial s_l}`,
  (e) :math:`\frac{\partial \kappa_T}{\partial T}`,
  (f) numerical approximation to (d.), and
  (g) numerical approximation to (e.). 

Examples
********

Material with thermal characteristic curve named "cct_power"
------------------------------------------------------------
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
      THERMAL_CONDUCTIVITY_DRY 5.5000D+0 W/m-C
      THERMAL_CONDUCTIVITY_WET 7.0000D+0 W/m-C
    END
    TEST
  END

  THERMAL_CHARACTERISTIC_CURVES cct_constant
    THERMAL_CONDUCTIVITY_FUNCTION CONSTANT
      CONSTANT_THERMAL_CONDUCTIVITY 5.5000D+0 W/m-C
    END
    TEST
  END

  THERMAL_CHARACTERISTIC_CURVES cct_power
    THERMAL_CONDUCTIVITY_FUNCTION POWER
      THERMAL_CONDUCTIVITY_DRY 5.5000D+0 W/m-C
      THERMAL_CONDUCTIVITY_WET 7.0000D+0 W/m-C
      #REFERENCE_TEMPERATURE -273.15 ! default value
      EXPONENT -1.18D+0 
    END
    TEST
  END

  THERMAL_CHARACTERISTIC_CURVES cct_cubic_polynomial
    THERMAL_CONDUCTIVITY_FUNCTION CUBIC_POLYNOMIAL
      THERMAL_CONDUCTIVITY_DRY 5.5000D+0 W/m-C
      THERMAL_CONDUCTIVITY_WET 7.0000D+0 W/m-C
      #REFERENCE_TEMPERATURE 0.d0 ! default value
      CUBIC_POLYNOMIAL_COEFFICIENTS -4.53398D-3 1.41580D-5 -1.94840D-8
    END
    TEST
  END

  THERMAL_CHARACTERISTIC_CURVES cct_linear_resistivity
    THERMAL_CONDUCTIVITY_FUNCTION LINEAR_RESISTIVITY
      THERMAL_CONDUCTIVITY_DRY 5.5000D+0 W/m-C
      THERMAL_CONDUCTIVITY_WET 7.0000D+0 W/m-C
      #REFERENCE_TEMPERATURE 0.d0 ! default value
      LINEAR_RESISTIVITY_COEFFICIENTS 1.0d0 5.038D-3
    END
    TEST
  END

Material with anisotropic thermal conductivity
----------------------------------------------
 ::

  MATERIAL_PROPERTY soil
    ID 1
    CHARACTERISTIC_CURVES cc1
    POROSITY 0.25
    TORTUOSITY 0.5
    ROCK_DENSITY 2650.0 kg/m^3
    THERMAL_CHARACTERISTIC_CURVES cct_linear_resistivity
    HEAT_CAPACITY 830.0 J/kg-C
    PERMEABILITY
      PERM_ISO 1.d-12
    /
  /

  THERMAL_CHARACTERISTIC_CURVES cct_linear_resistivity
    THERMAL_CONDUCTIVITY_FUNCTION LINEAR_RESISTIVITY
      THERMAL_CONDUCTIVITY_DRY 5.5000D+0 W/m-C
      THERMAL_CONDUCTIVITY_WET 7.0000D+0 W/m-C
      #REFERENCE_TEMPERATURE 0.d0 ! default value
      LINEAR_RESISTIVITY_COEFFICIENTS 1.0d0 5.038D-3
      THERMAL_CONDUCTIVITY_X  1.0000D+0
      THERMAL_CONDUCTIVITY_Y  0.8000D+0
      THERMAL_CONDUCTIVITY_Z  0.5000D+0
    END
    TEST
  END