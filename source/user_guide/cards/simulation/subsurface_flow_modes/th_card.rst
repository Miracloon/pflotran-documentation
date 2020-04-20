Back to :ref:`card-index`

Back to :ref:`subsurface-flow-card`

Back to :ref:`subsurface-flow-mode-card`

.. _th-card:

TH
==

Defines options for the TH subsurface flow mode.

:ref:`th-simulation-options`

:ref:`th-newton-options`

.. _th-simulation-options:

SIMULATION Options 
------------------
*(under SUBSURFACE_FLOW in SIMULATION PROCESS_MODELS block)*

.. include:: sim_th.tmp

.. _th-newton-options:

NEWTON Options
--------------
 
.. include:: newton_th.tmp

Examples
--------
::

 ...
 PROCESS_MODELS
   SUBSURFACE_FLOW flow
     MODE TH
     OPTIONS
       FREEZING
       ICE_MODEL PAINTER_EXPLICIT    
     /
   /
 /
 ...
