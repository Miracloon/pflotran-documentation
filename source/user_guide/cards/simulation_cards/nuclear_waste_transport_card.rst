Back to :ref:`card-index`

.. _nuclear-waste-transport-card:

NUCLEAR_WASTE_TRANSPORT
=======================
 Indicates that the simulation will include the NUCLEAR_WASTE_TRANSPORT mode.
 A corresponding :ref:`nuclear-waste-chemistry-card` card must be included 
 in the SUBSURFACE block.

Examples
--------
::

  SIMULATION
    SIMULATION_TYPE SUBSURFACE
    PROCESS_MODELS
      SUBSURFACE_FLOW flow
        MODE WIPP_FLOW
        OPTIONS
          EXTERNAL_FILE ../../block_options.txt
        /
      /
      NUCLEAR_WASTE_TRANSPORT  nw_trans
      /
    /
  END

