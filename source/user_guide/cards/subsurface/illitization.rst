Back to :ref:`card-index`

.. _illitization-card:

ILLITIZATION
=============================
This option specifies the illitization model associated with a material property. This allows for a time- and temperature-dependent change from smectite to illite to be evaluated during the simulation, which in turn can be used to impart a commensurate change in permeability, etc.

This feature is currently available for :ref:`general-card` and :ref:`th-card` modes.

Required Blocks and Cards:
**************************
ILLITIZATION_FUNCTION <string>
  Opens an illitization block, where <string> indicates the type of illitization model to be employed.

  Supported ILLITIZATION_FUNCTIONs (along with their required cards):

  .. _ilt-default-input:

  * DEFAULT

    + SMECTITE_INITIAL
    + THRESHOLD
    + SHIFT_PERM
    + EA
    + FREQ
    + K_CONC


.. _ilt-parameter-definitions:

Illitization Parameter Definitions
---------------------------------------------------

In the DEFAULT model, the time rate of change of smectite :math:`\left(\frac{df_{S}}{dt}\right)` into illite based on an initial smectite fraction :math:`f_{S,0}>0` and potassium cation concentration :math:`[K^{+}]` is computed as follows:

:math:`\left.\frac{df_{S}}{dt}\right|_{i}=\left\{{\begin{array}{cc} [K^{+}]\cdot f_{S,0}^{2}\cdot A\exp{\left(-\frac{E_{a}}{RT_{i}}\right)} & T_{i}\geq T_{th} \\ 0 & T_{i}<T_{th} \\ \end{array} } \right.` [1/s]

where :math:`A` is the frequency term, :math:`E_{a}` is the activation energy, :math:`R` is the ideal gas constant, :math:`T_{i}` is the temperature in Kelvin at time step :math:`i`, and :math:`T_{th}` is the threshold temperature. [1] The value of :math:`[K^{+}]` is currently implemented as a constant.

The cumulative change in smectite at time step :math:`i+1` is evaluated as follows:

:math:`\Delta f_{S,i+1}\approx\Delta f_{S,i}+\left(\frac{df_{S}}{dt}\right)_{i+1}\cdot(t_{i+1}-t_{i})`

This cumulative change is used to evaluate the smectite and illite fractions: 

:math:`f_{S,i+1} = \frac{f_{S,0}}{1+\Delta f_{S,i+1}}`

:math:`f_{I,i+1} = 1 - f_{S,i+1}`

The change in a given permeability component :math:`k_{j}` at time step :math:`i` as a result of illitization is computed using the proportional change in the smectite fraction and a shift factor :math:`C_{k}`:

:math:`k_{j,i}=k_{j,0}\left[1+\left(\frac{f_{S,0}-f_{S,i}}{f_{S,0}}\right)\cdot C_{k}\right]`

This suggests that when all of the original smectite is illitized, the permeability has been enhanced by a factor of :math:`1+ C_{k}`. 

SMECTITE_INITIAL <float>
 The initial fraction of smectite in the material relative to illite, :math:`f_{S,0}` (default of 1.0).

THRESHOLD <float>
 The temperature in Celsius at and above which the illitization process occurs, :math:`T_{th}` (default of 0°C).

SHIFT_PERM <float>
 The factor applied to the net change in illite fraction that is used to modify the permeability, :math:`C_{k}` (default of 1.0).

EA <float>
  The activation energy in the temperature-dependent Arrhenius term, :math:`E_{a}` [J/mol].

FREQ <float>
  The frequency term, or coefficient used to scale the temperature-dependent Arrhenius term, :math:`A` [L/mol-s].

K_CONC <float>
  The initial concentration of potassium cation in the material, :math:`[K^{+}]` [M].


Optional Blocks and Cards:
**************************

.. _ilt-test:

Test Illitization Model
-----------------------
TEST
 Including this keyword will produce output (.dat file) for an illitization model that includes:
  (a) initial smectite fraction :math:`(f_{S,0})`,
  (b) temperature :math:`(T)`,
  (c) time :math:`(t)`,
  (d) illite fraction :math:`(f_{I})`,
  (e) :math:`\frac{df_{I}}{dT}`

Examples
********

.. _ilt-example-general:

Material with illitization model named "ilt_bentonite"
------------------------------------------------------
 ::

   MATERIAL_PROPERTY buffer
     ID 1
     CHARACTERISTIC_CURVES bentonite
     POROSITY 0.35
     TORTUOSITY_FUNCTION_OF_POROSITY 1.4
     SOIL_COMPRESSIBILITY 1.6d-8
     SOIL_COMPRESSIBILITY_FUNCTION LEIJNSE
     SOIL_REFERENCE_PRESSURE 101325.d0
     ROCK_DENSITY 2700.
     THERMAL_CHARACTERISTIC_CURVES cct_bentonite
     HEAT_CAPACITY 830.
     ILLITIZATION ilt_bentonite
     PERMEABILITY
       PERM_ISO  1.d-20
     /
   /

  ILLITIZATION ilt_bentonite
    ILLITIZATION_FUNCTION DEFAULT
      THRESHOLD         2.00000d+1 C
      EA                1.17152d+5 J/mol
      FREQ              8.08000d+4 L/mol-s
      K_CONC            2.16000d-3 M
      SMECTITE_INITIAL  0.95000d+0
      SHIFT_PERM        1.00000d+0
    END
    TEST
  END


.. _ilt-references:

References
**********
1. Huang, W.-L., J. M. Longo, and D. R. Pevear (1993). An experimentally derived kinetic model for smectite-to-illite conversion and its use as a geothermometer. Clays and Clay Minerals 41(2), 162-177. https://doi.org/10.1346/CCMN.1993.0410205
