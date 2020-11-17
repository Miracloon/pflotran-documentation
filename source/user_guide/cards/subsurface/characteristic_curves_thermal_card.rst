Back to :ref:`card-index`

.. _thermal-characteristic-curves-card:

THERMAL_CHARACTERISTIC_CURVES
=============================
This option specifies the thermal characteristic curves (e.g. thermal conductivity and associated parameters) associated with a material property. This expands thermal conductivity as a function of both temperature and saturation (with the exception of the CONSTANT and DEFAULT thermal conductivity functions). 

The legacy input method of specifying thermal conductivity by :ref:`material-property-card` (i.e. with THERMAL_CONDUCTIVITY_DRY and THERMAL_CONDUCTIVTY_WET) is backwards-compatible, where parameters are adapted to the DEFAULT thermal characteristic curve and functions are numbered in material sequence. However, THERMAL_CHARACTERISTIC_CURVES **cannot** be combined with the legacy convention in the same input file.

Required Blocks and Cards:
**************************
THERMAL_CONDUCTIVITY_FUNCTION <string>
  Opens a thermal conductivity block, where <string> indicates the type of thermal conductivity function to be employed. 

  Supported THERMAL_CONDUCTIVITY_FUNCTIONs (along with their required cards):
  
  .. _tcc-constant-card:
  
  * CONSTANT
    
    + CONSTANT_THERMAL_CONDUCTIVITY

  .. _tcc-default-card:

  * DEFAULT
    
    + THERMAL_CONDUCTIVITY_DRY
    + THERMAL_CONDUCTIVITY_WET

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

    .. _tcc-frozen-card:

  * FROZEN

    + THERMAL_CONDUCTIVITY_DRY
    + THERMAL_CONDUCTIVITY_WET
    + KERSTEN_EXPONENT
    + THERMAL_CONDUCTIVITY_FROZEN
    + KERSTEN_EXPONENT_FROZEN
    + ICE_MODEL

  .. _tcc-composite:
  
  * COMPOSITE
  
  .. _tcc_assembly:
  
  * ASM_AXIAL (Assembly Axial Model)
  
    + THERMAL_CONDUCTIVITY_WATER
    + THERMAL_CONDUCTIVITY_SOLID
    + POROSITY_ASSEMBLY
      
  * ASM_RADIAL (Assembly Radial Model)
  
    + THERMAL_CONDUCTIVITY_WATER
    + THERMAL_CONDUCTIVITY_SOLID
    + POROSITY_ASSEMBLY
    + THERMAL_CONDUCTIVITY_DRY
    + DRY_CONDITIONS_COEFFICIENT
    + DRY_CONDITIONS_EXPONENT
      
  * WATER_FILLED_CONDITIONS (Standalone model for water-filled assembly)
  
    + THERMAL_CONDUCTIVITY_WATER
    + THERMAL_CONDUCTIVITY_SOLID
    + POROSITY_ASSEMBLY
    + THERMAL_CONDUCTIVITY_DRY (optional)
    
  * DRY_CONDITIONS (Standalone model for dry assembly)
  
    + THERMAL_CONDUCTIVITY_DRY
    + DRY_CONDITIONS_COEFFICIENT
    + DRY_CONDITIONS_EXPONENT
    + THERMAL_CONDUCTIVITY_WET (optional)

.. _tcc-parameter-definitions:

Thermal Characteristic Curves Parameter Definitions
---------------------------------------------------

CONSTANT_THERMAL_CONDUCTIVITY <float>
 Thermal conductivity of porous medium that does not depend on temperature or saturation [W/m-K].

THERMAL_CONDUCTIVTY_WET <float>
 Thermal conductivity of the wet porous medium (:math:`s_l=1`) [W/m-K].

THERMAL_CONDUCTIVITY_DRY <float>
 Thermal conductivity of the dry porous medium (:math:`s_l=0`) [W/m-K].

 Effective thermal conductivity (:math:`\kappa_T`) at the given liquid saturation (Somerton et al., 1974) is computed as :math:`\kappa_T(s_l)=\kappa_T^{dry} + \sqrt{s_l}(\kappa_T^{wet} - \kappa_T^{dry})` [W/m-K]

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

KERSTEN_EXPONENT <float>
 In :ref:`th-card` mode, this is the exponent (:math:`\alpha_{u}` [-]) of liquid saturation used to derive the Kersten number for unfrozen soil: :math:`Ke_{u}=s^{\alpha_{u}}_{l}` (see :ref:`mode-th-ice-model`).
 
 Outside of :ref:`th-card` mode, only the dry and wet components of the ice model are utilized for FROZEN.

THERMAL_CONDUCTIVITY_FROZEN <float>
  In the FROZEN model, this is the thermal conductivity of frozen soil [W/m-K] (see :ref:`mode-th-ice-model`).

  When this parameter is specified in :ref:`th-card` mode, the FREEZING option (see :ref:`th-simulation-options`) automatically becomes active.
  
KERSTEN_EXPONENT_FROZEN <float>
  In the FROZEN model, this is the exponent (:math:`\alpha_{f}` [-]) of ice saturation used to derive the Kersten number for frozen soil: :math:`Ke_{f}=s^{\alpha_{f}}_{i}` (see :ref:`mode-th-ice-model`).
    
  This parameter must be specified with THERMAL_CONDUCTIVITY_FROZEN.
  
ICE_MODEL 
  Specifies the ice model for the FROZEN model. Options include:
    * PAINTER_EXPLICIT [1]
    * PAINTER_KARRA_IMPLICIT [2]
    * PAINTER_KARRA_EXPLICIT [2]
    * PAINTER_KARRA_EXPLICIT_NOCRYO [2]
    * DALL_AMICO [3,4]
    
  This parameter must be specified with THERMAL_CONDUCTIVITY_FROZEN.

Assembly Models
---------------
Models are available to describe thermal conduction in spent nuclear fuel assemblies along both radial and axial directions. The radial model takes the form of the DEFAULT curve, albeit with a temperature-dependent dry component and a special wet component: :math:`\kappa_{radial}(s_l,T)=\kappa_{d}(T)+[\kappa_{w}^{\prime}-\kappa_{d}(T)\sqrt{s_{l}}]` [W/m-K].

The dry thermal conductivity takes the form of a power law with temperature: :math:`\kappa_{d}(T)=\kappa_{d}^{0}+\alpha T^{\beta}` [W/m-K]. This model can be used on its own with the DRY_CONDITIONS function, where a constant :math:`\kappa_{w}` may be specified to impart the saturation dependence from the DEFAULT model.

The wet thermal conductivity takes into account the porosity of the assembly and thermal conductivities of its solid constituents and contained water: :math:`\kappa_{w}^{\prime}=\kappa_{l}\Bigg[1-\sqrt{1-\Phi}+\frac{\sqrt{1-\Phi}}{1+(\frac{\kappa_{l}}{\kappa_{s}}-1)\sqrt{1-\Phi}}\Bigg]` [W/m-K]. This model can be used on its own with the WATER_FILLED_CONDITIONS function, where a constant :math:`\kappa_{d}` may be specified to impart the saturation dependence from the DEFAULT model.

The axial model assumes parallel conduction between solid constituents in the assembly and the surrounding water. It differs from the DEFAULT curve by having linear saturation dependence and by using the thermal conductivities of solids and water as opposed to dry and wet components: :math:`\kappa_{axial}(s_{l})=(1-\Phi)\kappa_{s}+\Phi s_{l}\kappa_{l}` [W/m-K].

THERMAL_CONDUCTIVITY_WATER <float>
 The thermal conductivity of water (:math:`\kappa_{l}` [W/m-K]) saturating the assembly.
   
THERMAL_CONDUCTIVITY_SOLID <float>
 The thermal conductivity of the solid components in the assembly including rods and baskets (:math:`\kappa_{s}` [W/m-K]).
   
POROSITY_ASSEMBLY <float>
 The porosity of the assembly (:math:`\Phi`), or the ratio of the volume of void to the total volume. 
   
THERMAL_CONDUCTIVITY_DRY <float>
 For the radial assembly model, the dry thermal conductivity is applied as the zero-order term describing the baseline thermal conductivity of the dry assembly at 0 °C (:math:`\kappa_{d}^{0}` [W/m-K]).
   
DRY_CONDITIONS_COEFFICIENT <float>
 For the dry state of the radial assembly model, this is the coefficient for the temperature-dependent term (:math:`\alpha`).
   
DRY_CONDITIONS_EXPONENT <float>
 For the dry state of the radial assembly model, this is the exponent of temperature in the temperature-dependent term (:math:`\beta`). Both :math:`\alpha` and :math:`\beta` must be fitted to match the units of :math:`\kappa_{d}^{0}`. 

Optional Blocks and Cards:
**************************

.. _tcc-anisotropy-parameter-definitions:

Thermal Conductivity Anisotropy Parameter Definitions
-----------------------------------------------------

The following parameters are used to impart a direction-dependent treatment of thermal conductivity for thermal characteristic curves that employ :math:`\kappa_T(s_l)` from the DEFAULT function. The following inputs are ratios that determine what fraction of the user-input values (THERMAL_CONDUCTIVITY_DRY or THERMAL_CONDUCTIVITY_WET) comprise particular components of the thermal conductivity tensor. 

ANISOTROPY_RATIO_X <float>
 The ratio applied to user-input thermal conductivity to derive the :math:`\kappa_{xx}` component of the thermal conductivity tensor. Requires additional input of Y and Z ratios. 
 
ANISOTROPY_RATIO_Y <float>
 The ratio applied to user-input thermal conductivity to derive the :math:`\kappa_{yy}` component of the thermal conductivity tensor. Requires additional input of X and Z ratios. 
  
ANISOTROPY_RATIO_Z <float>
 The ratio applied to user-input thermal conductivity to derive the :math:`\kappa_{zz}` component of the thermal conductivity tensor. Requires additional input of X and Y ratios. 
 
In the COMPOSITE function, the following parameters are used to employ previously-defined thermal characteristic curves along certain principal axes. Anisotropy ratios can also be specified if needed. 
 
COMPOSITE_X <string>
  Name of the thermal characteristic curve governing conduction in the X direction.

COMPOSITE_Y <string>
  Name of the thermal characteristic curve governing conduction in the Y direction.

COMPOSITE_Z <string>
  Name of the thermal characteristic curve governing conduction in the Z direction.

.. _tcc-test:

Test Thermal Characteristic Curve
---------------------------------
TEST
 Including this keyword will produce output (.dat file) for a thermal characteristic curve that includes: 
  (a) temperature [:math:`T`],
  (b) liquid saturation [:math:`s_l`],
  (c) thermal conductivity [:math:`\kappa_T`],
  (d) :math:`\frac{\partial \kappa_T}{\partial s_l}`,
  (e) :math:`\frac{\partial \kappa_T}{\partial T}`,
  (f) numerical approximation to (d.), and
  (g) numerical approximation to (e.). 
  
 When the FROZEN model is in use with FREEZING active, there are additional parameters in the output:
   * ice saturation [:math:`s_i`]
   * :math:`\frac{\partial \kappa_T}{\partial s_i}`
   * numerical approximation to :math:`\frac{\partial \kappa_T}{\partial s_i}`
 
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

  THERMAL_CHARACTERISTIC_CURVES cct_constant
    THERMAL_CONDUCTIVITY_FUNCTION CONSTANT
      CONSTANT_THERMAL_CONDUCTIVITY 5.5000D+0 W/m-C
    END
    TEST
  END

  THERMAL_CHARACTERISTIC_CURVES cct_default
    THERMAL_CONDUCTIVITY_FUNCTION DEFAULT
      THERMAL_CONDUCTIVITY_DRY 5.5000D+0 W/m-C
      THERMAL_CONDUCTIVITY_WET 7.0000D+0 W/m-C
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

  THERMAL_CHARACTERISTIC_CURVES cct_frozen
    THERMAL_CONDUCTIVITY_FUNCTION FROZEN
      THERMAL_CONDUCTIVITY_DRY 0.2500D+0 W/m-C
      THERMAL_CONDUCTIVITY_WET 1.3000D+0 W/m-C
      KERSTEN_EXPONENT 0.45
      #THERMAL_CONDUCTIVITY_FROZEN 2.3500D+0 W/m-C
      #KERSTEN_EXPONENT_FROZEN 0.95
      #ICE_MODEL PAINTER_EXPLICIT
    END
    TEST
  END

  THERMAL_CHARACTERISTIC_CURVES cct_axial
    THERMAL_CONDUCTIVITY_FUNCTION ASM_AXIAL
      THERMAL_CONDUCTIVITY_WATER 1.7200D+0 W/m-C
      THERMAL_CONDUCTIVITY_SOLID 1.6700D+1 W/m-C
      POROSITY_ASSEMBLY          5.0000D-1
    END
  END
  
  THERMAL_CHARACTERISTIC_CURVES cct_radial
    THERMAL_CONDUCTIVITY_FUNCTION ASM_RADIAL
      THERMAL_CONDUCTIVITY_DRY   0.1430D+0 W/m-C
      THERMAL_CONDUCTIVITY_WATER 1.7200D+0 W/m-C
      THERMAL_CONDUCTIVITY_SOLID 1.6700D+1 W/m-C
      DRY_CONDITIONS_COEFFICIENT 1.6700D+0
      DRY_CONDITIONS_EXPONENT    3.8300D-5
      POROSITY_ASSEMBLY          5.0000D-1
    END
  END
  
  THERMAL_CHARACTERISTIC_CURVES cct_composite
    THERMAL_CONDUCTIVITY_FUNCTION COMPOSITE
      COMPOSITE_X cct_radial
      COMPOSITE_Y cct_radial
      COMPOSITE_Z cct_axial
    END
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
      ANISOTROPY_RATIO_X  1.0000D+0
      ANISOTROPY_RATIO_Y  0.8000D+0
      ANISOTROPY_RATIO_Z  0.5000D+0
    END
    TEST
  END

References
**********
1. Painter, S.L. (2011). Three-phase numerical model of water migration in partially frozen geological media: model formulation, validation, and applications. Computational Geosciences 15, 69–85. https://doi.org/10.1007/s10596-010-9197-z
2. Painter, S.L., and S. Karra (2014). Constitutive model for unfrozen water content in subfreezing unsaturated soils. Vadose Zone 13(4), 1-8. https://doi.org/10.2136/vzj2013.04.0071
3. Dall'Amico, M. (2010). Coupled  water  and  heat  transfer  in  permafrost modeling. Ph.D. thesis, Institute of Civil and Environmental Engineering, Universita’ degli Studi di Trento, Trento, Italy. http://eprints-phd.biblio.unitn.it/335/
4. Dall'Amico, M., S. Endrizzi, S. Gruber, and R. Rigon (2011). A robust and energy-conserving model of freezing variably-saturated soil. The Cryosphere 5(2), 469-484. https://doi.org/10.5194/tc-5-469-2011
