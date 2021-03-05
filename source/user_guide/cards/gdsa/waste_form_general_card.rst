Back to :ref:`card-index`

.. _waste-form-general-card:

WASTE_FORM_GENERAL
==================
The Waste Form Process Model is :ref:`formally documented here <pm_waste_form>`.

Specifies the waste form process model. 
Under the :ref:`simulation-card` block this process model is included by adding 
the ``WASTE_FORM`` block:

 ::
 
   SIMULATION
     SIMULATION_TYPE SUBSURFACE
     PROCESS_MODELS
       WASTE_FORM <name_string>
         TYPE GENERAL
       /
       SUBSURFACE_FLOW flow
         MODE GENERAL
       /
       SUBSURFACE_TRANSPORT transport
         MODE GIRT
       /
     /
   END
   
where <name_string> gives a user-defined name for the process model.

Required Cards:
---------------

WASTE_FORM_GENERAL
 Opens the WASTE_FORM_GENERAL block. Must have a matching END_WASTE_FORM_GENERAL.

MECHANISM <type_string>

 The mechanism block specifies a waste form mechanism. The mechanism includes the details of the radionuclide
 species, the waste form bulk material details, and the canister that contains the waste form. Several 
 different custom mechanisms can be defined, or chosen from pre-defined options. Each mechanism is given a 
 unique name, and later associated with specific listed waste forms. The following types are currently 
 supported: GLASS, DSNF, FMDM, FMDM_SURROGATE, FMDM_SURROGATE_KNNR, :ref:`WIPP<wipp_waste_form>`, and CUSTOM.

 ::

    MECHANISM GLASS
    /

 Within the MECHANISM block, the following sub-blocks and cards must be included
 for any MECHANISM type:
 
 NAME <name_string> (required for all mechanism types)

  Specifies a name for the mechanism. This name should be unique.

  ::

    NAME glass02

 SPECIES sub-block (required for all mechanism types)

  Specifies a list of waste form species, their formula weights (in units of g-species/mol-species), decay 
  constant (in units of 1/sec), initial mass fraction within the waste form matrix (g-species/g-bulk), 
  instant release fraction (a number between 0 and 1), and the name of the species daughter (if it exists).   
  The species listed here must also be listed in the CHEMISTRY block under Primary Species. Isotopes decay
  and ingrowth occurs following a 3-generation analytical solution derived for multiple parents and 
  grandparents and non-zero initial daughter concentrations, or by an implicit solution of the Bateman
  equation.
  
  ::

    SPECIES
     I-129   128.90d0 1.29d-15  2.18d-4  0.7d0
     Am-241  241.06d0 5.08d-11  8.70d-4  0.0d0  Np-237       
     Np-237  237.05d0 1.03d-14  8.59d-4  0.7d0  U-233
     U-233   233.04d0 1.38d-13  9.70d-9  0.0d0  Th-229   
     Th-229  229.03d0 2.78d-12  4.43d-12 0.0d0  
      ...      ...      ...        ...    ...     ...  
    /

 MATRIX_DENSITY <double> <unit_string> (required for all mechanism types)

  Specifies the density of the waste form bulk (or matrix).
  
  ::

    MATRIX_DENSITY 2.0d3 kg/m^3
    
 The following sub-block cards are now separated by MECHANISM type:
 
* **MECHANISM GLASS sub-block cards:**
  
   SPECIFIC_SURFACE_AREA <double> <unit_string> (required for types GLASS, FMDM, FMDM_SURROGATE, FMDM_SURROGATE_KNNR; semi-optional for type 
   CUSTOM; do not include for types DSNF and WIPP)

    Specifies the specific surface area of the waste form bulk (or matrix). 
  
    ::

      SPECIFIC_SURFACE_AREA 2.78d-3 cm^2/g
    
   KIENZLER_DISSOLUTION (optional for type GLASS only)
    
    If chosen, this option will implement the Kienzler (2012) glass dissolution equation. No other
    dissolution parameters are needed (i.e., no other sub-block cards other than SPECIFIC_SURFACE_AREA).
    
    ::
    
      KIENZLER_DISSOLUTION
    
   K0 <double> <unit_string> (optional for GLASS only)
    
    Specifies the intrinsic dissolution rate. If no units are provided, default units are kg/m^2-sec.
    If KIENZLER_DISSOLUTION is chosen, this card should not be given.
    
    ::
    
      K0 580.d0 kg/m^2-day
    
   K_LONG <double> <unit_string> (optional for GLASS only)
   
    Specifies the constant dissolution rate over the long term when the pore fluid solution is at
    saturation with respect to SiO2. If no units are provided, default units are kg/m^2-sec.
    If KIENZLER_DISSOLUTION is chosen, this card should not be given.
    
    ::
    
      K_LONG 46.d0 g/m^2-day
    
   NU <double> (optional for GLASS only)
   
    Specifies the pH dependence parameter. If KIENZLER_DISSOLUTION is chosen, this 
    card should not be given.
    
    ::
    
      NU 3.44d0
    
   EA <double> <unit_string> (optional for GLASS only)
    
    Specifies the effective activation energy. If no units are provided, default 
    units are J/mol. If KIENZLER_DISSOLUTION is chosen, this card should not be given.
    
    :: 
    
      EA 5.83d4 J/mol
    
   Q <double or string> (optional for GLASS only)
    
    Specifies the ion activity product of H4SiO4. If a constant value is desired,
    it should be entered following the Q keyword. Alternatively, Q can be calculated
    within the simulation by specifying the string AS_CALCULATED following the Q 
    keyword. If you specify AS_CALCULATED, then SiO2(aq) must be included as a primary
    or secondary species in the :ref:`chemistry-card` block, and USE_FULL_GEOCHEMISTRY should
    also be specified if full geochemistry is otherwise not being calculated. 
    If KIENZLER_DISSOLUTION is chosen, this card should not be given.
    
    ::
    
      Q 3.4d-8
      
      Q AS_CALCULATED
   
   K <double> (optional for GLASS only)
   
    Specifies the equilibrium constant for the rate limiting step, which is the activity of H4SiO4
    at saturation with the glass. If KIENZLER_DISSOLUTION is chosen, this card should not be given.
   
   V <double> (optional for GLASS only)
   
    Specifies the exponent in the affinity term, as in [1-(Q/K)**(1/V)].
    If KIENZLER_DISSOLUTION is chosen, this card should not be given.
   
   PH <double or string> (optional for GLASS only)
   
    Specifies the pH value at the glass surface. If a constant value is desired,
    it should be entered following the PH keyword. Alternatively, pH can be calculated
    within the simulation by specifying the string AS_CALCULATED following the PH 
    keyword. If you specify AS_CALCULATED, then H+ must be included as a primary
    or secondary species in the :ref:`chemistry-card` block, and USE_FULL_GEOCHEMISTRY should
    also be specified if full geochemistry is otherwise not being calculated. 
    If KIENZLER_DISSOLUTION is chosen, this card should not be given.
    
    ::
    
      PH 6.8d0
      
      PH AS_CALCULATED
    
* **MECHANISM DSNF sub-block cards:**
 
   No additional sub-block cards are required. 
 
* **MECHANISM FMDM sub-block cards:**

   For additional inputs required for this mechanism see
   :ref:`FMDM Mechanism`.

   If the FMDM mechanism is used, follow these instructions on how to link the external FMDM: 
   :ref:`running-pflotran-fmdm`.
 
   SPECIFIC_SURFACE_AREA <double> <unit_string> (required for types GLASS, FMDM, FMDM_SURROGATE, FMDM_SURROGATE_KNNR; semi-optional for type 
   CUSTOM; do not include for types DSNF and WIPP)

    Specifies the specific surface area of the waste form bulk (or matrix). 
  
    ::

      SPECIFIC_SURFACE_AREA 2.78d-3 cm^2/g

   BURNUP <double> (required for types FMDM, FMDM_SURROGATE, FMDM_SURROGATE_KNNR; semi-optional for type 
   CUSTOM; do not include for types DSNF and WIPP)

    Specifies the burnup of the waste form bulk (or matrix). 

    ::

      BURNUP 6.0d1 ! GWd/MTHM

* **MECHANISM FMDM_SURROGATE sub-block cards:**

   For additional inputs required for this mechanism see
   :ref:`FMDM Surrogate Mechanism`.
   
	 
   SPECIFIC_SURFACE_AREA <double> <unit_string> (required for types GLASS, FMDM, FMDM_SURROGATE, FMDM_SURROGATE_KNNR; semi-optional for type 
   CUSTOM; do not include for types DSNF and WIPP)

    Specifies the specific surface area of the waste form bulk (or matrix). 
  
    ::

      SPECIFIC_SURFACE_AREA 2.78d-3 cm^2/g

   BURNUP <double> (required for types FMDM, FMDM_SURROGATE, FMDM_SURROGATE_KNNR; semi-optional for type 
   CUSTOM; do not include for types DSNF and WIPP)

    Specifies the burnup of the waste form bulk (or matrix). 

    ::

      BURNUP 6.0d1 ! GWd/MTHM

   DECAY_TIME <double> <unit_string> (required for types FMDM_SURROGATE and FMDM_SURROGATE_KNNR; do not include for types CUSTOM, 
   DSNF, FMDM, and WIPP)

    Specifies the offset for the age of the fuel relative to the beginning of simulation time.

    ::

      DECAY_TIME 1.0d2 year

* **MECHANISM FMDM_SURROGATE_KNNR sub-block cards:**

   For additional inputs required for this mechanism see
   :ref:`FMDM Surrogate Mechanism`.
   
	 
   SPECIFIC_SURFACE_AREA <double> <unit_string> (required for types GLASS, FMDM, FMDM_SURROGATE, FMDM_SURROGATE_KNNR; semi-optional for type 
   CUSTOM; do not include for types DSNF and WIPP)

    Specifies the specific surface area of the waste form bulk (or matrix). 
  
    ::

      SPECIFIC_SURFACE_AREA 2.78d-3 cm^2/g

   BURNUP <double> (required for types FMDM, FMDM_SURROGATE, FMDM_SURROGATE_KNNR; semi-optional for type 
   CUSTOM; do not include for types DSNF and WIPP)

    Specifies the burnup of the waste form bulk (or matrix). 

    ::

      BURNUP 6.0d1 ! GWd/MTHM

   DECAY_TIME <double> <unit_string> (required for types FMDM_SURROGATE and FMDM_SURROGATE_KNNR; do not include for types CUSTOM, 
   DSNF, FMDM, and WIPP)

    Specifies the offset for the age of the fuel relative to the beginning of simulation time.

    ::

      DECAY_TIME 1.0d2 year
 
* **MECHANISM WIPP sub-block cards:**
 
   No additional sub-block cards are required.  **If the WIPP mechanism is used, the**
   **UFD_DECAY process model must also be used or the solubility limit functionality will not work properly.**
   Please read the :ref:`formal documentation here<wipp_waste_form>`.
 
* **MECHANISM CUSTOM sub-block cards:**

   DISSOLUTION_RATE <double> <unit_string> (semi-optional for type CUSTOM; do not include for type GLASS, 
   DSNF, FMDM, FMDM_SURROGATE, FMDM_SURROGATE_KNNR or WIPP)

    Specifies the dissolution rate for the waste form bulk (or matrix), in units of mass per surface area per 
    time. If dissolution rate is given for the CUSTOM mechanism type, the SPECIFIC_SURFACE_AREA must also be 
    specified (see below).

    ::

      DISSOLUTION_RATE 7.8d-8 kg/m^2-day

   FRACTIONAL_DISSOLUTION_RATE <double> <unit_string> (semi-optional for type CUSTOM; do not include for types 
   GLASS, DSNF, FMDM, FMDM_SURROGATE, FMDM_SURROGATE_KNNR or WIPP)

    Specifies the fractional dissolution rate for the waste form bulk (or matrix), in units of fractional 
    volume per time of the remaining volume. The unit string should resemble 1/time. 

    :: 

      FRACTIONAL_DISSOLUTION_RATE 3.4d-8 1/day
      
   FRACTIONAL_DISSOLUTION_RATE_VI <double> <unit_string> (semi-optional for type CUSTOM; do not include for types 
   GLASS, DSNF, FMDM, FMDM_SURROGATE, FMDM_SURROGATE_KNNR or WIPP)

    Specifies the fractional dissolution rate for the waste form bulk (or matrix), in units of fraction of 
    the initial volume per time. The unit string should resemble 1/time. 

    :: 

      FRACTIONAL_DISSOLUTION_RATE_VI 9.1d-5 1/day
    
   SPECIFIC_SURFACE_AREA <double> <unit_string> (required for types GLASS, FMDM, FMDM_SURROGATE, FMDM_SURROGATE_KNNR; semi-optional for type 
   CUSTOM; do not include for types DSNF and WIPP)

    Specifies the specific surface area of the waste form bulk (or matrix). If specific surface area is given 
    for the CUSTOM mechanism type, the DISSOLUTION_RATE keyword must also be specified (see above).
  
    ::

      SPECIFIC_SURFACE_AREA 2.78d-3 cm^2/g
      
* **Optional keywords for ALL MECHANISM types:**      

  SEED <integer>
  
   Specifies a seed number (must be an integer) which seeds the random number 
   generator that selects waste package degradation rates from the truncated
   normal distribution. If this keyword is omitted, the default seed value is 1.
      
* **Optional sub-block for ALL MECHANISM types:**

  CANISTER_DEGRADATION_MODEL sub-block (optional for all mechanism types)

   If this optional block is included, the canister degradation model will be turned on. Currently, this 
   model will keep track of canister vitality, a parameter which controls the time of waste form breach. At 
   the beginning of the simulation, vitality = 1. Waste form breach occurs when the canister vitality falls 
   to zero. The reference vitality degradation rate (Rv0) is either (a) chosen at the beginning of the 
   simulation, for each waste form, based on a normal distribution of degradation rates, (b) specified for 
   each waste form by the user, or (c) ignored if the user specifies a canister breach time for each waste 
   form instead of a rate. The effective vitality degradation rate (Rv) is calculated as an Arrhenius 
   function of temperature, canister material constant (C), and the reference vitality degradation rate: 

   log10(Rv) = log10(Rv0) + C * (1/333.15[K] - 1/T[K])

   If option "a" is desired, the normal distribution for the reference rate is formed by providing the 
   following block keywords (all required):

    VITALITY_LOG10_MEAN

     Specifies the Log(base10) mean vitality degradation rate (in units of log10-1/yr). If this distribution 
     parameter is omitted, then CANISTER_VITALITY_RATE must be included for all waste forms associated with 
     this mechanism.

    VITALITY_LOG10_STDEV

     Specifies the Log(base10) standard deviation of the vitality degradation rate (in units of log10-1/yr). 
     If this distribution parameter is omitted, then CANISTER_VITALITY_RATE must be included for all waste 
     forms associated with this mechanism.

    VITALITY_UPPER_TRUNCATION

     Specifies the Log(base10) upper truncation of the mean vitality degradation rate (in units of 
     log10-1/yr). If this distribution parameter is omitted, then CANISTER_VITALITY_RATE must be included for 
     all waste forms associated with this mechanism.

    CANISTER_MATERIAL_CONSTANT

     Specifies the canister material constant (ex: 1500 for 316L stainless steel).

    ::

     CANISTER_DEGRADATION_MODEL
       VITALITY_LOG10_MEAN -4.5
       VITALITY_LOG10_STDEV 0.5
       VITALITY_UPPER_TRUNCATION -3.0
       CANISTER_MATERIAL_CONSTANT 1500
     /
  
  SPACER_DEGRADATION_MODEL sub-block (optional for all mechanism types involving spent nuclear fuel)
  
    If this optional block is included, a time- and temperature-dependent spacer grid corrosion model will be evaluated as a means of terminating criticality events associated with the waste form. The model becomes active after the canister is breached. When the spacer grids have degraded below 0.5% of the original total mass, they are assumed to fail, which implies a loss of critical configuration.
    
    The spacer grid vitality :math:`V_{s}` is determined using the corrosion rate :math:`R` and total initial mass :math:`M_{0}` over time steps :math:`t_{i}` to :math:`t_{i+1}`, where at canister breach :math:`V_{s,0}=1`:
    
    :math:`V_{s,i+1}=V_{s,i}-\frac{R_{i+1}\cdot(t_{i+1}-t_{i})}{M_{0}}`
    
    The corrosion rate is governed by an Arrhenius term using the average temperature of the waste form :math:`\bar{T}`, the total spacer grid surface area :math:`A_{0}`, and a saturation-dependent term :math:`f_{S}(S_{l})`, where :math:`\mathcal{R}` is the ideal gas constant:
    
    :math:`R_{i+1}=f_{S}(S_{l,i+1})\cdot A_{0}\cdot\mathcal{C}\exp{\left(-\frac{Q}{\mathcal{R}\bar{T}_{i+1}}\right)}`
    
    The saturation-dependent term modifies the corrosion rate depending on an exposure level :math:`S_{l}^{exp}`, which is the saturation for which the spacer grids are considered fully-inundated with water. When the saturation of the waste form is at or above this limit, the corrosion rate is unaffected. Otherwise, the rate is reduced proportionally based on the saturation.  
    
    :math:`f_{S}(S_{l})=\left\{{\begin{array}{cc}
    \frac{S_{l}}{S_{l}^{exp}} & S_{l}<S_{l}^{exp} \\
    1 & S_{l}\geq S_{l}^{exp} \\
    \end{array} }\right.`
  
    MASS <double> <unit_string>
     
     Total mass of spacer grids, :math:`M_{0}` [kg].
     
    SURFACE_AREA <double> <unit_string>
     
     Total surface area of spacer grids, :math:`A_{0}\,[m^{2}]` .
     
    EXPOSURE_LEVEL <double> (optional)
     
     Threshold saturation :math:`S_{l}^{exp}` for spacer grids to be considered fully-inundated with water. Saturation-dependence can be turned off by setting :math:`S_{l}^{exp}=0` or by not including this entry. 
     
    C <double> <unit_string>
     
     Empirical coefficient of the Arrhenius term governing corrosion, :math:`\mathcal{C}\,\,\left[\frac{kg}{m^{2}s}\right]`.
     
    Q <double> <unit_string>
     
     Activation energy operating on the reciprocal of temperature within the Arrhenius term governing corrosion, :math:`Q` [J/mol]. 
    
    ::

     SPACER_DEGRADATION_MODEL
       MASS           1.67040D+05 g
       SURFACE_AREA   2.37309D+04 dm^2
       EXPOSURE_LEVEL 9.93317D-01
       C              3.4700D+07  mg/s-dm^2
       Q              2.2675D+04  cal/mol
     /

Full examples of the MECHANISM sub-block (note some values may be unrealistic, these are just examples
for form, not parameter values):

::

    MECHANISM GLASS
      NAME glass02
      SPECIFIC_SURFACE_AREA 2.78d-3 m^2/kg
      MATRIX_DENSITY 2.0d3 kg/m^3
      KIENZLER_DISSOLUTION
      SPECIES 
       #name,   MW[g/mol],dcy[1/s], initMF, inst_rel_frac,daughter
        I-129   128.90d0  1.29d-15  2.18d-4   0.2d0
        Am-241  241.06d0  5.08d-11  8.70d-4   0.0d0         
        Np-237  237.05d0  1.03d-14  8.59d-4   0.2d0  Am-241
        U-233   233.04d0  1.38d-13  9.70d-9   0.0d0  Np-237   
        Th-229  229.03d0  2.78d-12  4.43d-12  0.0d0  U-233
      /
      CANISTER_DEGRADATION_MODEL
        VITALITY_LOG10_MEAN -3.5
        VITALITY_LOG10_STDEV 1.5
        VITALITY_UPPER_TRUNCATION -2.75
        CANISTER_MATERIAL_CONSTANT 1500.0
      /
    /
    
    MECHANISM GLASS 
    NAME glass05
      SPECIFIC_SURFACE_AREA 2.78d-3 m^2/kg
      MATRIX_DENSITY 2.46d3 kg/m^3
      K0 560.d0 kg/m^2-day           #
      K_LONG 400.d0 kg/m^2-day       #
      NU 5.d-2                       #
      EA 60211.58 J/mol              #
      Q 1.d0                         #  Dissolution model parameters
      K 1.d0                         #
      V 1.d0                         #
      PH AS_CALCULATED               #
      SPECIES
       #name,   MW[g/mol],dcy[1/s], initMF, inst_rel_frac, daughter               
        I-129   128.90d0  1.29d-15  2.18d-4   0.2d0
        Am-241  241.06d0  5.08d-11  8.70d-4   0.0d0  Np-237
        Np-237  237.05d0  1.03d-14  8.59d-4   0.2d0  U-233
        U-233   233.04d0  1.38d-13  9.70d-9   0.0d0  Th-229
        Th-229  229.03d0  2.78d-12  4.43d-12  0.0d0  
      /  
      CANISTER_DEGRADATION_MODEL
        CANISTER_MATERIAL_CONSTANT 1500
      /
    /

    MECHANISM DSNF
      NAME dsnf01
      MATRIX_DENSITY 3.56d3 kg/m^3
      SPECIES 
       #name,   MW[g/mol],dcy[1/s], initMF, inst_rel_frac,daughter
        Am-243  243.06d0  2.98d-12  1.12d-5  0.0d0 
        Th-230  230.03d0  2.75d-13  2.45d-8  0.0d0 
      /
      CANISTER_DEGRADATION_MODEL
        VITALITY_LOG10_MEAN -3.2
        VITALITY_LOG10_STDEV 0.75
        VITALITY_UPPER_TRUNCATION -2.0
        CANISTER_MATERIAL_CONSTANT 1200.0
      /
    /
    
    MECHANISM WIPP
      NAME wipp3
      MATRIX_DENSITY 1.d0 g/m^3
      SPECIES 
       #name,    MW[g/mol],dcy[1/s], initMF, inst_rel_frac,daughter
        tracer   100.d0    2.d-15    1.12d0  0.0d0 
        tracer2  200.d0    2.d-15    1.12d0  0.0d0 
      /
    /

    MECHANISM CUSTOM
      NAME custom05
      FRACTIONAL_DISSOLUTION_RATE 2.0d-9 1/day
      MATRIX_DENSITY 2.44d3 kg/m^3
      SPECIES 
       #name,   MW[g/mol],dcy[1/s], initMF, inst_rel_frac,daughter
        Pu-240  240.05d0  3.34d-12  2.84d-3  0.2d0 
        U-236   236.05d0  9.20d-16  4.33d-3  0.0d0  Pu-240
        Tc-99   98.91d0   1.04d-13  8.87d-4  0.0d0
      /
      CANISTER_DEGRADATION_MODEL
        CANISTER_MATERIAL_CONSTANT 1500.0
      /
    /

    MECHANISM CUSTOM
      NAME custom03
      DISSOLUTION_RATE 4.1d-8 kg/m^2-day
      SPECIFIC_SURFACE_AREA 2.11d-3 m^2/kg
      MATRIX_DENSITY 2.44d3 kg/m^3
      SPECIES 
       #name,   MW[g/mol],dcy[1/s], initMF, inst_rel_frac,daughter
        Pu-240  240.05d0  3.34d-12  2.84d-3  0.2d0 
        U-236   236.05d0  9.20d-16  4.33d-3  0.0d0  Pu-240
        Tc-99   98.91d0   1.04d-13  8.87d-4  0.0d0
      /
      CANISTER_DEGRADATION_MODEL
        VITALITY_LOG10_MEAN -3.5
        VITALITY_LOG10_STDEV 0.5
        VITALITY_UPPER_TRUNCATION -2.75
        CANISTER_MATERIAL_CONSTANT 1500.0
      /
      SPACER_DEGRADATION_MODEL
        MASS           1.00000D+05 g
        SURFACE_AREA   2.50000D+04 dm^2
        EXPOSURE_LEVEL 9.00000D-01
        C              3.50000D+07 mg/s-dm^2
        Q              8.50000D+04 J/mol
      /
    /

      MECHANISM FMDM
        NAME fmdm02
        MATRIX_DENSITY 10.97d3 kg/m^3
        BURNUP 60 #GWd/MTHM
        SPECIFIC_SURFACE_AREA 0.001 m^2/g
        SPECIES 
         #name,   MW[g/mol],dcy[1/s], initMF, inst_rel_frac,daughter
          Uranium 238.02d0  1.00d-90  0.50d0  0.0d0 
        /
        CANISTER_DEGRADATION_MODEL
          CANISTER_MATERIAL_CONSTANT 1500.0
        /
      /

      MECHANISM FMDM_SURROGATE
        NAME fmdm_surrogate01
        MATRIX_DENSITY 10.97d3 kg/m^3
        BURNUP 60 #GWd/MTHM
        SPECIFIC_SURFACE_AREA 0.001 m^2/g
        DECAY_TIME 100 year
        SPECIES 
         #name,   MW[g/mol],dcy[1/s], initMF, inst_rel_frac,daughter
          Uranium 238.02d0  1.00d-90  0.50d0  0.0d0 
        /
        CANISTER_DEGRADATION_MODEL
          CANISTER_MATERIAL_CONSTANT 1400.0
        /
      /

WASTE_FORM sub-block

 Specifies the details of each waste form. This block should be repeated for each waste form, and can include 
 the following cards:

  COORDINATE <double> <double> <double> -or- REGION <string>

   If COORDINATE, <double> <double> <double> gives the location of each waste form in x, y, z. Waste forms can
   be co-located (i.e., there can be multiple waste forms located at the same coordinate point. If REGION, 
   <string> gives the name of a defined region that the waste form occupies. The source term will be released
   over the cells of the REGION, or the single cell of the COORDINATE. Note that REGION and COORDINATE can't
   be given, only one is allowed.

  EXPOSURE_FACTOR <double> (optional)

   Gives the exposure factor of each waste form, which is a multiplier to the waste form dissolution rate. If 
   this keyword is not specified, the default value is 1.

  VOLUME <double> <unit_string>

   Gives the volume of each waste form.

  MECHANISM_NAME <string>

   Specifies the name of the mechanism associated with the waste form. The mechanism name given here must 
   match one of the mechanisms defined in the MECHANISM sub-block(s).

  CANISTER_VITALITY_RATE <double> <unit_string> (optional)

   Specifies the waste form canister's vitality degradation rate in units of 1/time. If this parameter is 
   specified, the mechanism associated to this waste form must include the CANISTER_DEGRADATION_BLOCK, but 
   *without* the distribution parameters (e.g. VITALITY_LOG10_MEAN, VITALITY_LOG10_STDEV, and  
   VITALITY_UPPER_TRUNCATION). This option cannot be combined with CANISTER_BREACH_TIME for a single waste 
   form, but both CANISTER_BREACH_TIME and CANISTER_VITALITY_RATE can be combined for different waste forms 
   under the same mechanism which omits the distribution parameters.

  CANISTER_BREACH_TIME <double> <unit_string> (optional)

   Specifies the waste form canister's breach time in units of time. The canister will breach during the next 
   timestep where time > CANISTER_BREACH_TIME. If this parameter is specified, the mechanism associated to 
   this waste form must include the CANISTER_DEGRADATION_BLOCK, but *without* the distribution parameters 
   (e.g. VITALITY_LOG10_MEAN, VITALITY_LOG10_STDEV, and VITALITY_UPPER_TRUNCATION). This option cannot be 
   combined with CANISTER_VITALITY_RATE for a single waste form, but both CANISTER_BREACH_TIME and 
   CANISTER_VITALITY_RATE can be combined for different waste forms under the same mechanism which omits the 
   distribution parameters.
  
  DECAY_START_TIME <double> <unit_string> (optional)
  
   Specifies the time that the waste within the waste form will begin to decay.
   If this card is not specified, the default decay start time is 0 seconds
   (e.g. at the first time step of the simulation). This card is useful if you
   have an inventory that is specific to a certain time in the simulation, and
   you don't want to back-calculate what the inventory should have been at
   the beginning of the simulation.

  CRITICALITY sub-block (optional)
   
   If this optional block is included, the heat source terms from decay and/or criticality can be evaluated for the waste form along with the time-dependent inventory table. Multiple sub-blocks may be named if criticality events occur at different time periods.
   
   MECH_NAME <string>
    Name of the criticality mechanism sub-block governing the criticality event.
   
   CRIT_START <double> <unit_string>
    Start time of criticality event.
   
   CRIT_END <double> <unit_string>
    End time of criticality event.

  ::

    WASTE_FORM
      COORDINATE 0.5d0 4.5d0 0.5d0
      EXPOSURE_FACTOR 4.d0
      VOLUME 1.14d0 m^3
      MECHANISM_NAME glass02
    /

    WASTE_FORM
      REGION WF-a1
      VOLUME 2.1d0 m^3
      CANISTER_BREACH_TIME 250 yr
      MECHANISM_NAME custom01
      
      CRITICALITY
        MECH_NAME crit_1
        CRIT_START 3.00d+2 y
        CRIT_END   2.00d+3 y
      /
    /

    WASTE_FORM
      REGION WF-3b
      VOLUME 0.55d0 m^3
      CANISTER_VITALITY_RATE 1.0d-7 1/yr
      MECHANISM_NAME custom01
    /

Optional Cards: 
---------------

PRINT_MASS_BALANCE

 If this option is included, output will be generated at each timestep that the waste form process model is 
 called. The output includes the cumulative mass and instantaneous mass rate for each species in each waste 
 form, the volume, dissolution rate, and the canister vitality of each waste form.
 
IMPLICIT_SOLUTION

 Including this card will solve the decay and ingrowth of the radionuclide
 inventory within the waste form using an implicit approach based on solving
 the Bateman equation using Newton's method. This option should be used if the
 3-generation analytical solution is not appropriate.

CRITICALITY_MECH
 
 Including this card will define the mechanism for associated criticality events in a waste form.
 
 NAME <name_string>
  
  Specifies a unique name for the criticality mechanism.
 
 CRITICAL_SATURATION <double>
  
  This is the liquid saturation below which the criticality event cannot be sustained. There is no heat emission from criticality until the waste form saturation is at or above this level. This is meant to be used for canisters in unsaturated systems.
 
 CRITICAL_WATER_DENSITY <double> <unit_string>
  
  This the liquid density below which the criticality event cannot be sustained. There is no heat emission from criticality until the waste form liquid density is at or above this level. This is meant to be used for canisters in saturated systems where moderator voiding is a key reactivity feedback mechanism.
 
 HEAT_OF_CRITICALITY
  
  This sub-block defines the heat source term from criticality either as a constant or as a value that can obtained from a temperature-based lookup table. The average temperature of the waste form is used for linear interpolation of this table.
  
  CONSTANT_HEAT <double> <unit_string>
  
  DATASET <file_string>
  
 DECAY_HEAT <type_string>
  
  This sub-block defines the heat source term from radioactive decay, which is obtained from a time-dependent lookup table. The types of decay heat treatment include TOTAL, ADDITIONAL, and CYCLIC. When a criticality event is active, the criticality source term is assumed to account for decay heat and this data is ignored.
  
  DATASET <file_string>
  
 INVENTORY
  
  This sub-block defines the fractional change (g/g) in nuclide inventory during criticality, which is obtained from a time-dependent lookup table. The number of data entries in this table must equal the number of species specified in the waste form process model.
  
  DATASET <file_string>
 
 ::
 
   WASTE_FORM
     REGION wf
     EXPOSURE_FACTOR 1.d0
     VOLUME 1.5d0 m^3
     MECHANISM_NAME csnf
     CANISTER_BREACH_TIME 2.50d+2 y
     
     CRITICALITY
       MECH_NAME crit_1
       CRIT_START 3.00d+2 y
       CRIT_END   2.00d+3 y
     /
   /
   
   CRITICALITY_MECH
     NAME crit_1
     CRITICAL_SATURATION    0.700d+0
     CRITICAL_WATER_DENSITY 9.200d+2 kg/m^3
     HEAT_OF_CRITICALITY
       CONSTANT_HEAT 4.0d+0 kW
       # DATASET criticality_heat.txt
     /
     DECAY_HEAT TOTAL
       DATASET ./decay_heat.txt
     /
     INVENTORY
       DATASET ./inventory_crit.txt
     /
   /


Full Example:
-------------

The following example specifies several waste forms, each associated with one of two particular mechanisms. Output will be generated for each waste form.

::

    WASTE_FORM_GENERAL

      PRINT_MASS_BALANCE
      MECHANISM FMDM
        NAME fmdm01
        MATRIX_DENSITY 10.97d3 kg/m^3
        BURNUP 60 #GWd/MTHM
        SPECIFIC_SURFACE_AREA 0.001 m^2/g
        SPECIES 
         #name,   MW[g/mol],dcy[1/s], initMF, inst_rel_frac,daughter
          Uranium 238.02d0  1.00d-90  0.50d0  0.0d0 
        /
        CANISTER_DEGRADATION_MODEL
          VITALITY_LOG10_MEAN -3.2
          VITALITY_LOG10_STDEV 0.75
          VITALITY_UPPER_TRUNCATION -2.0
          CANISTER_MATERIAL_CONSTANT 1200.0
        /
      /
      MECHANISM CUSTOM
        NAME custom05
        FRACTIONAL_DISSOLUTION_RATE 2.0d-9 1/day
        MATRIX_DENSITY 2.44d3 kg/m^3
        SPECIES 
         #name,   MW[g/mol],dcy[1/s], initMF, inst_rel_frac,daughter
          Pu-240  240.05d0  3.34d-12  2.84d-3  0.2d0 
          U-236   236.05d0  9.20d-16  4.33d-3  0.0d0  Pu-240
          Tc-99   98.91d0   1.04d-13  8.87d-4  0.0d0
        /
        CANISTER_DEGRADATION_MODEL
          CANISTER_MATERIAL_CONSTANT 1500.0
        /
      /
      WASTE_FORM
        REGION WF-custom-1
        EXPOSURE_FACTOR 3.d0
        VOLUME 1.14d0 m^3
        MECHANISM_NAME custom05
        CANISTER_BREACH_TIME 375 yr
      /
      WASTE_FORM
        REGION WF-custom-2
        EXPOSURE_FACTOR 4.d0
        VOLUME 1.14d0 m^3
        MECHANISM_NAME custom05
        CANISTER_VITALITY_RATE 3.d-6 1/day
      /
      WASTE_FORM
        COORDINATE 12.5d0 55.5d0 0.5d0
        VOLUME 1.55d0 m^3
        MECHANISM_NAME fmdm01
      /
      WASTE_FORM
        COORDINATE 5.5d0 4.5d0 0.5d0
        VOLUME 1.55d0 m^3
        MECHANISM_NAME fmdm01
      /

    END_WASTE_FORM_GENERAL
   
