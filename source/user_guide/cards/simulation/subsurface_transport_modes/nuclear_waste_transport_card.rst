Back to :ref:`card-index`

Back to :ref:`subsurface-transport-card`

Back to :ref:`subsurface-transport-mode-card`

.. _nuclear-waste-transport-card:

NWT
===
 Indicates that the simulation will include the NWT (Nuclear Waste Transport) 
 mode.
 A corresponding :ref:`nuclear-waste-chemistry-card` card must be included 
 in the SUBSURFACE block.

OPTIONS 
-------
*(under SUBSURFACE_TRANSPORT in SIMULATION PROCESS_MODELS block)*

.. include:: sim_nwt.tmp

NEWTON_SOLVER Options
---------------------

.. include:: newton_nwt.tmp


Examples
--------
::

  SIMULATION
    SIMULATION_TYPE SUBSURFACE
    PROCESS_MODELS
      SUBSURFACE_FLOW flow
        MODE WIPP_FLOW
      /
      SUBSURFACE_TRANSPORT transport
        MODE NWT
      /
    /
  END

