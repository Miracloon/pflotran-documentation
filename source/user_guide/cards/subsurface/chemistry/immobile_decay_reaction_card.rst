Back to :ref:`card-index`

Back to :ref:`chemistry-card`

.. _immobile-decay-reaction-card:

IMMOBILE_DECAY_REACTION
=======================
Specifies parameters for first-order decay of an immobile species.

Required Cards:
---------------

SPECIES_NAME <string>
 Name of immobile species to undergo first-order decay.

RATE_CONSTANT or HALF_LIFE (but not both)

  RATE_CONSTANT <float>
   First-order rate constant [1/sec].
  
  HALF_LIFE <float>
   Half life of species [sec].

*Note that rate constant or half life units other than sec or 1/sec may be specified.*

Examples:
---------

 ::

  CHEMISTRY
    PRIMARY_SPECIES
      ...
    /
    IMMOBILE_SPECIES
      D(im)
    /
    ...
    IMMOBILE_DECAY_REACTION
      SPECIES_NAME D(im)
      RATE_CONSTANT 1.d-9
    /
    ...
  /
    