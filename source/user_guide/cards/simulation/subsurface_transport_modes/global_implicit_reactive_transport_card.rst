Back to :ref:`card-index`

Back to :ref:`subsurface-transport-card`

Back to :ref:`subsurface-transport-mode-card`

.. _global-implicit-reactive-transport-card:

GIRT
====
 Indicates that the simulation will include the GIRT 
 (Global Implicit Reactive Transport) mode.
 A corresponding :ref:`chemistry-card` card must be included 
 in the SUBSURFACE block.

:ref:`reactive-transport-simulation-options`

:ref:`reactive-transport-newton-options`

.. _reactive-transport-simulation-options:

SIMULATION Options 
------------------
*(under SUBSURFACE_TRANSPORT in SIMULATION PROCESS_MODELS block)*

.. include:: sim_rt.tmp

.. _reactive-transport-newton-options:

NEWTON_SOLVER Options
---------------------

.. include:: newton_rt.tmp

Examples
--------
::

  SIMULATION
    SIMULATION_TYPE SUBSURFACE
    PROCESS_MODELS
      SUBSURFACE_TRANSPORT transport
        MODE GIRT
      /
    /
  END

