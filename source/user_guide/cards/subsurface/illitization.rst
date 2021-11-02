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

  * DEFAULT (HUANG)

    + SMECTITE_INITIAL
    + THRESHOLD_TEMPERATURE
    + SHIFT_PERM
    + SHIFT_KD
    + EA
    + FREQ
    + K_CONC
  
  * GENERAL (CUADROS_AND_LINARES)

    + SMECTITE_INITIAL
    + SMECTITE_EXPONENT
    + THRESHOLD_TEMPERATURE
    + SHIFT_PERM
    + SHIFT_KD
    + EA
    + FREQ
    + K_CONC
    + K_EXP


.. _ilt-parameter-definitions:

Illitization Parameter Definitions
---------------------------------------------------

In the DEFAULT model (ref. 1), for a given time step :math:`i+1`, the time rate of change of smectite :math:`\left(\frac{df_{S}}{dt}\right)` into illite is based on the smectite fraction :math:`f_{S,i}` and potassium cation concentration :math:`[K^{+}]`. It is defined as follows:

:math:`\left.-\frac{df_{S}}{dt}\right|^{i+1}=\left\{{\begin{array}{cc} [K^{+}]\cdot (f_{S}^{i})^{2}\cdot A\exp{\left(-\frac{E_{a}}{\mathcal{R}T^{i+1}}\right)} & T^{i+1}\geq T_{th} \\ 0 & T^{i+1}<T_{th} \\ \end{array} } \right.` [1/s]

where :math:`A` is the frequency term, :math:`E_{a}` is the activation energy, :math:`\mathcal{R}` is the ideal gas constant, :math:`T^{i+1}` is the temperature in Kelvin, and :math:`T_{th}` is the threshold temperature. The value of :math:`[K^{+}]` is currently implemented as a constant.

The time-integrated smectite fraction is evaluated as: 

:math:`f_{S}^{i+1} = \frac{f_{S}^{i}}{1-[K^{+}]\cdot A\exp{\left(-\frac{E_{a}}{\mathcal{R}T^{i+1}}\right)}\cdot (t^{i+1}-t^{i})\cdot f_{S}^{i}}`

The illite fraction is defined as the complement of the smectite fraction:

:math:`f_{I}^{i+1} = 1 - f_{S}^{i+1}`

A scale factor :math:`F` is defined that ranges from 0 to 1 and is based on the relative change in the fraction of illite:

:math:`F= \frac{f_{I}^{i+1}-f_{I}^{0}}{f_{S}^{0}}`

The change in a given permeability component :math:`k_{j}^{i+1}` at time step :math:`i+1` as a result of illitization is computed as:

:math:`k_{j}^{i+1}=k_{j}^{0}\left(1+F\cdot C_{k}\right)`

where :math:`k_{j}^{0}` is the original permeability tensor, :math:`C_{k}` is the permeability shift factor, and :math:`f_{S}^{0}` and :math:`f_{I}^{0}` are the initial fractions of smectite and illite, respectively. This suggests that when all of the original smectite is illitized, the permeability has been enhanced by a factor of :math:`1+ C_{k}`. 

In the GENERAL model (ref. 2), the time rate of change of smectite is defined with the potassium concentration raised to exponent :math:`m` and the smectite fraction raised to exponent :math:`n`, where the temperature-dependent Arrhenius term is simplified as :math:`k(T)`:

:math:`\left.-\frac{df_{S}}{dt}\right|^{i+1}=\left\{{\begin{array}{cc} [K^{+}]^{m}\cdot (f_{S}^{i})^{n}\cdot k(T) & T^{i+1}\geq T_{th} \\ 0 & T^{i+1}<T_{th} \\ \end{array} } \right.` [1/s]

The time-integrated smectite fraction is evaluated based on the choice of :math:`n`:

:math:`f_{S}^{i+1}=\left\{{\begin{array}{cc} \left\{[K^{+}]^{m}\cdot k(T)\cdot (n-1)(t^{i+1}-t^{i})+(f_{S}^{i})^{1-n}) \right\}^{\frac{1}{1-n}} & n>1 \\ f_{S}^{i}\cdot \exp{\left\{-k(T)\cdot[K^{+}]^{m}\cdot(t^{i+1}-t^{i})\right\}} & n=1 \\ \end{array} } \right.`

SMECTITE_INITIAL <float>
 The initial fraction of smectite in the material relative to illite, :math:`f_{S}^{0}` (default of 1.0).

SMECTITE_EXP <float>
 The exponent of the smectite fraction, :math:`n`.

THRESHOLD_TEMPERATURE <float>
 The temperature in Celsius at and above which the illitization process occurs, :math:`T_{th}` (default of 0°C).

SHIFT_PERM <float>
 The factor applied to the net change in illite fraction that is used to modify the permeability, :math:`C_{k}` (default of 1.0).

SHIFT_KD (optional)
 For specified elements, factors are provided to modify sorption distribution coefficients, :math:`K_{d}`, based on the net change in the illite fraction. One list entry consists of the element <string>, which must be present in the :ref:`ufd-decay-card` process model, the function type, and the functional parameters <float> (see below).
   
   DEFAULT - :math:`C_{1}` <float>
   
     :math:`K_{d}^{i+1} = K_{d}^{i}(1 + F\cdot C_{1})`

EA <float>
  The activation energy in the temperature-dependent Arrhenius term, :math:`E_{a}` [J/mol].

FREQ <float>
  The frequency term, or coefficient used to scale the temperature-dependent Arrhenius term, :math:`A` [L/mol-s].

K_CONC <float>
  The initial concentration of potassium cation in the material, :math:`[K^{+}]` [M].

K_EXP <float>
  The exponent of the potassium cation concentration, :math:`m`.


Optional Blocks and Cards:
**************************

.. _ilt-test:

Test Illitization Model
-----------------------
TEST
 Including this keyword will produce output (.dat file) for an illitization model that includes:
  (a) initial smectite fraction :math:`(f_{S}^{0})`,
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
      THRESHOLD_TEMPERATURE 2.50000d+1 C
      EA                    1.17152d+5 J/mol
      FREQ                  8.08000d+4 L/mol-s
      K_CONC                2.16000d-3 M
      SMECTITE_INITIAL      0.95000d+0
      SHIFT_PERM            1.00000d+3
      SHIFT_KD
        Cs  DEFAULT  1.05320d+0
      /
    END
    TEST
  END


.. _ilt-references:

References
**********
1. Huang, W.-L., J. M. Longo, and D. R. Pevear (1993). An experimentally derived kinetic model for smectite-to-illite conversion and its use as a geothermometer. Clays and Clay Minerals 41(2), 162-177. https://doi.org/10.1346/CCMN.1993.0410205

2. Cuadros, J., and Linares, J. (1996). Experimental kinetic study of the smectite-to-illite transformation. Geochimica et Cosmochimica Acta 60(3), 439-453. https://doi.org/10.1016/0016-7037(95)00407-6
