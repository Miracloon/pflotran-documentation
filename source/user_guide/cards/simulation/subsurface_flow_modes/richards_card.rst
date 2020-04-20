Back to :ref:`card-index`

Back to :ref:`subsurface-flow-card`

Back to :ref:`subsurface-flow-mode-card`

.. _richards-card:

RICHARDS
========

Defines options for the Richards subsurface flow mode.

:ref:`richards-simulation-options`

:ref:`richards-newton-options`

.. _richards-simulation-options:

SIMULATION Options 
------------------
*(under SUBSURFACE_FLOW in SIMULATION PROCESS_MODELS block)*

.. include:: sim_richards.tmp

.. _richards-newton-options:
 
NEWTON Options 
--------------

.. include:: newton_richards.tmp

Examples
--------
::

 ...
 PROCESS_MODELS
   SUBSURFACE_FLOW flow
     MODE RICHARDS
   /
 /
 ...
