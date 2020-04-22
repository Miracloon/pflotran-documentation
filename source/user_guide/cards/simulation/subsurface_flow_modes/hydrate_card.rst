Back to :ref:`card-index`

Back to :ref:`subsurface-flow-card`

Back to :ref:`subsurface-flow-mode-card`

.. _hydrate-card:

HYDRATE
=======
Defines options for the Hydrate subsurface flow mode.

:ref:`hydrate-simulation-options`

:ref:`hydrate-timestepper-options`

:ref:`hydrate-newton-options`

:ref:`hydrate-block-options`

:ref:`hydrate-examples`

.. _hydrate-simulation-options:

SIMULATION Options 
------------------
*(under SUBSURFACE_FLOW in SIMULATION PROCESS_MODELS block)*

.. include:: sim_hydrate.tmp

.. _hydrate-timestepper-options:

TIMESTEPPER Options
-------------------

.. include:: timestepper_hydrate.tmp

.. _hydrate-newton-options:

NEWTON_SOLVER Options
---------------------

.. include:: newton_hydrate.tmp

.. _hydrate-block-options:

HYDRATE Block
-------------
*(within SUBSURFACE block)*

METHANOGENESIS
 Invokes a methanogenesis source term. Current source implementation (following Malinverno, 2010) requires:
  NAME <string>
    Arbitrary name of the methanogenesis source
  ALPHA <float>
    Seafloor labile organic carbon [wt%]
  LAMBDA <float>
    Methanogenesis reaction rate [1/s]
  V_SED <float>
    Sedimentation rate [m/s]
  SMT_DEPTH <float>
    Depth to the sulfate-methane transition [m]
  K_ALPHA <float>
    Conversion factor from organic carbon to methane (typically 2241)
  
WITH_SEDIMENTATION 
 Turns on sedimentation. Moves immobile pore species at the sedimentation rate specified in the METHANOGENESIS block and in the direction of gravity.

WITH_GIBBS_THOMSON
  Turns on the Gibbs-Thomson effect. Shifts the gas hydrate phase boundary as a function of required subcooling to precipitate hydrate.

GT_3PHASE
  Applies the Gibbs-Thomson effect in the 3-phase zone. Currently this works by partitioning the pore space occupied by hydrate and gas 50/50

ADJUST_SOLUBILITY_WITHIN_GHSZ
  Applies a correction to methane solubility within the hydrate stability zone as a function of distance from the phase boundary.

NO_PC
  Turns off capillary pressure.

EFFECTIVE_SAT_SCALING
 Scale saturations of mobile pore species by the total amount of mobile pore fluids. 

HYDRATE_PHASE_BOUNDARY <string>
 Sets the gas hydrate phase boundary equation. Default is Kamath, 1984. Current options: MORIDIS

SCALE_PERM_BY_HYD_SAT
 Scales the absolute permeability of the sediment matrix by hydrate saturation.

PERM_SCALING_FUNCTION <string>
 Selects the specific function used for absolute permeability scaling as a function of hydrate saturation. Current options: DAI_AND_SEOL

HENRYS_CONSTANT <string>
 Set function for Henry's constant for methane. Current default: Carroll and Mather, 1997. Current options: CRAMER

.. _hydrate-examples:

Examples
--------
::

 SUBSURFACE

 ...

 SIMULATION
   SIMULATION_TYPE SUBSURFACE
   PROCESS_MODELS
     SUBSURFACE_FLOW flow
       MODE HYDRATE
       OPTIONS
         RESTRICT_STATE_CHANGE
       /
     /
   /
 END
 ...
 SUBSURFACE
   NUMERICAL_METHODS FLOW
     NEWTON_SOLVER
       USE_INFINITY_NORM_CONVERGENCE
     /
   /
   ...
   HYDRATE
     SCALE_PERM_BY_HYD_SAT
     PERM_SCALING_FUNCTION DAI_AND_SEOL
     HYDRATE_PHASE_BOUNDARY MORIDIS
     EFFECTIVE_SAT_SCALING
     WITH_GIBBS_THOMSON
     GT_3PHASE
     ADJUST_SOLUBILITY_WITHIN_GHSZ
     NO_PC
     WITH_SEDIMENTATION
     METHANOGENESIS
      NAME ss_methanogenesis
      ALPHA 0.005
      K_ALPHA 2241
      LAMBDA 1.d-14
      V_SED 3.17d-11
      SMT_DEPTH 10.d0
     /
   /
 END
