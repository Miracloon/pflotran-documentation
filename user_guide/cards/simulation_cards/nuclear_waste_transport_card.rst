Back to :ref:`card-index`

.. _nuclear-waste-transport-card:

NUCLEAR_WASTE_TRANSPORT
=======================

Optional Cards
--------------

GLOBAL_IMPLICIT
  Specifies fully implicit coupling of transport and reaction.

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
        GLOBAL_IMPLICIT
      /
    /
  END

