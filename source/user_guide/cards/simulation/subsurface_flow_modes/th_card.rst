Back to :ref:`card-index`

Back to :ref:`subsurface-flow-card`

Back to :ref:`subsurface-flow-mode-card`

.. _th-card:

TH
==

Defines options for the TH subsurface flow mode.

OPTIONS 
-------
*(under SUBSURFACE_FLOW in SIMULATION PROCESS_MODELS block)*

FREEZING
 Enables freezing.

ICE_MODEL <string>
 Specifies the ice model.  Options include: PAINTER_EXPLICIT, 
 PAINTER_KARRA_IMPLICIT, PAINTER_KARRA_EXPLICIT, PAINTER_KARRA_EXPLICIT_NOCRYO,
 CALL_AMICO.
 
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
