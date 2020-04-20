Back to :ref:`card-index`

Back to :ref:`subsurface-transport-card`

Back to :ref:`subsurface-transport-mode-card`

.. _operator-split-reactive-transport-card:

OSRT
====
 Indicates that the simulation will include the OSRT 
 (Operator-Split Reactive Transport) mode.
 A corresponding :ref:`chemistry-card` card must be included 
 in the SUBSURFACE block.

:ref:`osrt-simulation-options`

.. _osrt-simulation-options:

SIMULATION Options 
------------------

OPTIONS 
-------
*(under SUBSURFACE_TRANSPORT in SIMULATION PROCESS_MODELS block)*

.. include:: sim_rt.tmp

Examples
--------
::

  SIMULATION
    SIMULATION_TYPE SUBSURFACE
    PROCESS_MODELS
      SUBSURFACE_TRANSPORT transport
        MODE OSRT
      /
    /
  END

