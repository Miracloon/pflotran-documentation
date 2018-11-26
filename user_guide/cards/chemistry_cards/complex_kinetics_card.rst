Back to :ref:`card-index`

Back to :ref:`chemistry-card`

Back to :ref:`sorption-card`

Back to :ref:`surface-complexation-rxn-card`

.. _complex-kinetics-card:

COMPLEX_KINETICS
================
Specifies kinetic parameters for a kinetic surface complexation reaction.

Required Cards:
---------------
COMPLEX_KINETICS
 Opens the block.

<string>
 Names the surface complex to which the kinetics are assigned.

Optional Cards: 
---------------
FORWARD_RATE_CONSTANT
 Indicates the forward rate constant [1/sec].

BACKWARD_RATE_CONSTANT
 Indicates the backward rate constant [1/sec].

Examples
--------
 :: 

  SORPTION
    SURFACE_COMPLEXATION_RXN
      KINETIC
      MINERAL Kaolinite
      SITE >AlOH 0.00636
      COMPLEXES
        >AlOUO2+
      /
      COMPLEX_KINETICS
        FORWARD_RATE_CONSTANT 1.d-6
        BACKWARD_RATE_CONSTANT 1.d-5
      /
    /
  END

